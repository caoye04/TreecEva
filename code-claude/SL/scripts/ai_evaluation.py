import json
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from config import DATASET_PATH, AI_APIS
import openai
import re
from concurrent.futures import ThreadPoolExecutor, as_completed
from threading import Lock
import time

class AIEvaluator:
    def __init__(self, max_workers=5):
        """
        初始化AI评估器
        
        Args:
            max_workers: 并行处理的最大线程数 (建议3-10,根据API限流调整)
        """
        self.dataset = None
        self.max_workers = max_workers
        self.save_lock = Lock()
        self.progress_lock = Lock()
        
        # evaluation_results 现在只在内存中作为临时存储
        self.evaluation_results = {}
        
        # 统计信息
        self.stats = {
            "total_tasks": 0,
            "evaluated_tasks": 0,
            "skipped_tasks": 0,
            "processed": 0
        }
    
    def load_dataset(self):
        """加载数据集"""
        with open(DATASET_PATH, 'r', encoding='utf-8') as f:
            self.dataset = json.load(f)
    
    def call_api(self, prompt, ai_name):
        """调用指定的API (线程安全)"""
        api_config = AI_APIS[ai_name]
        
        client = openai.OpenAI(
            api_key=api_config['api_key'],
            base_url=api_config['base_url']
        )
        
        try:
            response = client.chat.completions.create(
                model=api_config['model'],
                messages=[
                    {
                        "role": "system",
                        "content": "You are an expert programmer. Analyze the given code and predict the final output value. Provide only the numerical answer, no explanation."
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                temperature=0.1,
                max_tokens=50
            )
            
            return response.choices[0].message.content
                
        except Exception as e:
            return f"API Error: {str(e)}"
    
    def extract_number_from_response(self, response):
        """从响应中提取数字"""
        if "Error:" in response:
            return None
            
        patterns = [
            r'^(\d+)$',
            r'(\d+)',
        ]
        
        for pattern in patterns:
            match = re.search(pattern, response.strip(), re.MULTILINE)
            if match:
                return int(match.group(1))
        
        return None
    
    def generate_evaluation_prompt(self, task_data):
        """生成评估提示 (仅限Python)"""
        description = task_data["task"]["description"]
        code = task_data["task"]["code"]
        
        prompt = f"""
{description}

Code:
```python
{code}
```
Analyze this code step by step and determine the final output value. Provide only the number."""
        return prompt
    
    def evaluate_task_with_single_ai(self, task_data, ai_name):
        """使用指定AI评估任务"""
        prompt = self.generate_evaluation_prompt(task_data)
        response = self.call_api(prompt, ai_name)
        predicted_answer = self.extract_number_from_response(response)
        
        return predicted_answer

    def calculate_difficulty_from_errors(self, ai_correctness):
        """根据AI错误数计算难度（0-5）"""
        error_count = ai_correctness.count(0)
        difficulty = min(error_count, 5)
        return difficulty

    def should_evaluate_task(self, task, evaluate_mode="unrated"):
        """
        判断任务是否需要评估
        
        Args:
            task: 任务数据
            evaluate_mode: 评估模式
                - "all": 评估所有任务
                - "unrated": 只评估难度为-1的未评估任务（默认）
                - "difficulty_-1": 只评估难度为-1的任务（别名）
        
        Returns:
            bool: 是否需要评估
        """
        if task.get("metadata", {}).get("language") != "python":
            return False
        
        if evaluate_mode == "all":
            return True
        elif evaluate_mode in ["unrated", "difficulty_-1"]:
            difficulty = task.get("metadata", {}).get("difficulty", -1)
            return difficulty == -1
        else:
            # 可扩展：支持其他筛选模式
            return False

    def evaluate_single_task(self, task_index, task, ai_names):
        """
        评估单个任务 (由线程池调用)
        
        Args:
            task_index: 任务在数据集中的索引
            task: 任务数据
            ai_names: 所有AI模型名称列表
            
        Returns:
            包含评估结果的字典
        """
        task_id = task["id"]
        expected_answer = task["task"]["answer"]
        original_difficulty = task["metadata"].get("difficulty", -1)
        
        ai_correctness = []
        ai_predictions = {}
        
        # 依次测试每个AI
        for ai_name in ai_names:
            predicted_answer = self.evaluate_task_with_single_ai(task, ai_name)
            ai_predictions[ai_name] = predicted_answer
            
            if predicted_answer is not None and predicted_answer == expected_answer:
                ai_correctness.append(1)
            else:
                ai_correctness.append(0)
        
        # 计算新难度
        new_difficulty = self.calculate_difficulty_from_errors(ai_correctness)
        
        # 生成结果行
        correctness_str = " ".join(map(str, ai_correctness))
        result_line = f"{task_id}：难度：{new_difficulty} ai评估记录：{correctness_str}"
        
        return {
            "task_index": task_index,
            "task_id": task_id,
            "original_difficulty": original_difficulty,
            "new_difficulty": new_difficulty,
            "ai_correctness": ai_correctness,
            "ai_predictions": ai_predictions,
            "expected_answer": expected_answer,
            "error_count": ai_correctness.count(0),
            "result_line": result_line
        }

    def update_stats(self, status):
        """线程安全的统计更新"""
        with self.progress_lock:
            self.stats[status] += 1
            self.stats["processed"] += 1

    def print_progress(self):
        """打印进度信息"""
        with self.progress_lock:
            processed = self.stats["processed"]
            total = self.stats["total_tasks"]
            evaluated = self.stats["evaluated_tasks"]
            skipped = self.stats["skipped_tasks"]
            
            if total > 0:
                percentage = (processed / total) * 100
                print(f"Progress: [{processed}/{total}] {percentage:.1f}% "
                    f"(✓{evaluated} ⊘{skipped})")

    def save_task_difficulty(self, task_index, new_difficulty):
        """线程安全的保存单个任务难度"""
        with self.save_lock:
            self.dataset[task_index]["metadata"]["difficulty"] = new_difficulty

    def save_dataset(self):
        """线程安全的保存整个数据集"""
        with self.save_lock:
            with open(DATASET_PATH, 'w', encoding='utf-8') as f:
                json.dump(self.dataset, f, indent=2, ensure_ascii=False)

    def evaluate_all_tasks(self, evaluate_mode="unrated"):
        """
        并行评估任务并根据结果更新难度
        
        Args:
            evaluate_mode: 评估模式
                - "all": 评估所有任务
                - "unrated": 只评估难度为-1的未评估任务（默认）
        """
        self.load_dataset()
        self.evaluation_results.clear()
        
        ai_names = list(AI_APIS.keys())
        
        # 重置统计信息
        self.stats = {
            "total_tasks": 0,
            "evaluated_tasks": 0,
            "skipped_tasks": 0,
            "processed": 0
        }
        
        print(f"\n{'='*70}")
        print(f"AI EVALUATION MODE: {evaluate_mode.upper()} (PARALLEL)")
        print(f"{'='*70}")
        print(f"Max parallel workers: {self.max_workers}")
        print(f"AI models: {', '.join(ai_names)}")
        print(f"{'='*70}\n")
        
        # 预处理：收集需要评估的任务
        tasks_to_evaluate = []
        for i in range(1, len(self.dataset)):
            task = self.dataset[i]
            if "task" not in task:
                continue
            
            self.stats["total_tasks"] += 1
            task_id = task["id"]
            
            # 检查是否需要评估
            if not self.should_evaluate_task(task, evaluate_mode):
                difficulty = task.get("metadata", {}).get("difficulty", "N/A")
                language = task.get("metadata", {}).get("language", "N/A")
                
                if language != "python":
                    reason = "Not Python"
                else:
                    reason = f"Difficulty={difficulty} (skip in '{evaluate_mode}' mode)"
                
                print(f"Skipping task {task_id} ({reason})")
                self.stats["skipped_tasks"] += 1
                self.stats["processed"] += 1
                continue
            
            tasks_to_evaluate.append((i, task))
        
        if not tasks_to_evaluate:
            print("\nNo tasks to evaluate.")
            return
        
        print(f"\nFound {len(tasks_to_evaluate)} tasks to evaluate\n")
        
        start_time = time.time()
        
        # 使用线程池并行处理
        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            # 提交所有评估任务
            future_to_task = {
                executor.submit(
                    self.evaluate_single_task,
                    task_index,
                    task,
                    ai_names
                ): (task_index, task["id"])
                for task_index, task in tasks_to_evaluate
            }
            
            # 处理完成的任务
            for future in as_completed(future_to_task):
                task_index, task_id = future_to_task[future]
                
                try:
                    result = future.result()
                    
                    # 保存结果
                    self.evaluation_results[result["task_id"]] = {
                        "original_difficulty": result["original_difficulty"],
                        "new_difficulty": result["new_difficulty"],
                        "ai_correctness": result["ai_correctness"],
                        "error_count": result["error_count"],
                        "result_line": result["result_line"]
                    }
                    
                    # 更新数据集中的难度
                    self.save_task_difficulty(result["task_index"], result["new_difficulty"])
                    
                    # 更新统计
                    self.update_stats("evaluated_tasks")
                    
                    # 打印详细结果
                    print(f"✓ [{result['task_id']}] Evaluated:")
                    for i, ai_name in enumerate(ai_names):
                        pred = result["ai_predictions"][ai_name]
                        expected = result["expected_answer"]
                        status = "✓" if result["ai_correctness"][i] == 1 else "✗"
                        print(f"    {status} {ai_name}: {pred} (expected: {expected})")
                    
                    if result["new_difficulty"] != result["original_difficulty"]:
                        print(f"  难度更新：{result['original_difficulty']} → {result['new_difficulty']}")
                    
                    print(f"  {result['result_line']}")
                    
                    # 打印进度
                    self.print_progress()
                    
                    # 定期保存(每5个任务)
                    if self.stats["evaluated_tasks"] % 5 == 0:
                        self.save_dataset()
                        print(f"  💾 Progress saved\n")
                    
                except Exception as e:
                    print(f"✗ [{task_id}] Evaluation failed: {str(e)}")
                    self.update_stats("processed")
        
        # 最终保存
        self.save_dataset()
        
        elapsed_time = time.time() - start_time
        
        # 打印统计信息
        print(f"\n{'='*70}")
        print(f"EVALUATION SUMMARY")
        print(f"{'='*70}")
        print(f"Total tasks in dataset: {self.stats['total_tasks']}")
        print(f"Tasks evaluated: {self.stats['evaluated_tasks']}")
        print(f"Tasks skipped: {self.stats['skipped_tasks']}")
        print(f"Evaluation mode: {evaluate_mode}")
        print(f"⏱ Total time: {elapsed_time:.1f}s")
        if self.stats['evaluated_tasks'] > 0:
            print(f"⚡ Average: {elapsed_time/self.stats['evaluated_tasks']:.2f}s per task")
        print(f"{'='*70}\n")
        
        print(f"Dataset difficulty updated at {DATASET_PATH}")
        
        # 生成统计数据
        if self.stats['evaluated_tasks'] > 0:
            print("\nGenerating AI evaluation statistics...")
            summary_stats = self.generate_difficulty_statistics()
            
            # 创建简洁的任务详情
            task_details = {}
            for task_id, results in sorted(self.evaluation_results.items()):
                task_details[task_id] = results["result_line"]
            
            # 组合成最终报告
            final_report = {
                "evaluation_mode": evaluate_mode,
                "statistics": {
                    "total_tasks": self.stats["total_tasks"],
                    "evaluated_tasks": self.stats["evaluated_tasks"],
                    "skipped_tasks": self.stats["skipped_tasks"],
                    "elapsed_time": f"{elapsed_time:.1f}s",
                    "average_time_per_task": f"{elapsed_time/self.stats['evaluated_tasks']:.2f}s"
                },
                "evaluation_summary": summary_stats,
                "task_details": task_details
            }
            
            # 保存报告
            report_path = "data/ai_evaluation_with_difficulty.json"
            with open(report_path, 'w', encoding='utf-8') as f:
                json.dump(final_report, f, indent=2, ensure_ascii=False)
            
            print(f"Summarized evaluation report saved to {report_path}")
        else:
            print("\nNo tasks were evaluated - skipping report generation")
        
        print("AI evaluation completed!")

    def generate_difficulty_statistics(self):
        """
        生成难度统计报告
        现在此方法会打印报告到控制台，并返回一个包含统计数据的字典。
        """
        ai_names = list(AI_APIS.keys())
        
        statistics_summary = {}

        print("\n=== AI评估统计报告 ===")
        
        # 1. 任务详情 (仅打印到控制台)
        print(f"\n=== 任务详情 ===")
        for task_id, results in sorted(self.evaluation_results.items()):
            print(results["result_line"])
        
        # 2. 难度分布统计
        print(f"\n=== 难度分布统计 ===")
        difficulty_distribution = {}
        difficulty_changes = 0
        
        for results in self.evaluation_results.values():
            new_diff = results["new_difficulty"]
            difficulty_distribution[new_diff] = difficulty_distribution.get(new_diff, 0) + 1
            
            if results["original_difficulty"] != results["new_difficulty"]:
                difficulty_changes += 1
        
        difficulty_stats_dict = {}
        for difficulty in range(6):  # 0-5
            count = difficulty_distribution.get(difficulty, 0)
            difficulty_stats_dict[f"difficulty_{difficulty}_(errors)"] = f"{count} tasks"
            print(f"难度 {difficulty}: {count} 个任务")
        
        print(f"\n难度发生变化的任务数: {difficulty_changes}")
        
        statistics_summary["difficulty_distribution"] = difficulty_stats_dict
        statistics_summary["difficulty_changes"] = f"{difficulty_changes} tasks"
        
        # 3. 整体正确率统计
        total_tasks = len(self.evaluation_results)
        ai_total_correct = [0] * len(ai_names)
        
        for results in self.evaluation_results.values():
            for i, correct in enumerate(results["ai_correctness"]):
                ai_total_correct[i] += correct
        
        print(f"\n=== 整体正确率 (共 {total_tasks} 个任务) ===")
        accuracy_stats_dict = {}
        for i, ai_name in enumerate(ai_names):
            accuracy = ai_total_correct[i] / total_tasks * 100 if total_tasks > 0 else 0
            result_str = f"{ai_total_correct[i]}/{total_tasks} ({accuracy:.1f}%)"
            accuracy_stats_dict[ai_name] = result_str
            print(f"{ai_name}: {result_str}")
        
        statistics_summary["overall_ai_accuracy"] = accuracy_stats_dict
        statistics_summary["total_tasks_evaluated"] = total_tasks
        
        return statistics_summary
    
if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(
    description="Evaluate tasks with multiple AI models (with parallel processing)"
    )
    parser.add_argument("--mode", default="unrated",
    choices=["all", "unrated"],
    help="Evaluation mode: 'all' or 'unrated' (default: unrated)")
    parser.add_argument("--workers", type=int, default=5,
    help="Number of parallel workers (default: 5, recommended: 3-10)")
    args = parser.parse_args()
    evaluator = AIEvaluator(max_workers=args.workers)
    evaluator.evaluate_all_tasks(evaluate_mode=args.mode)

    # python ai_evaluation.py --mode all --workers 8
    # python ai_evaluation.py(5个并发)