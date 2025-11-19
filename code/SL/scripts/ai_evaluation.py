import json
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from config import DATASET_PATH, AI_APIS
import openai
import re

class AIEvaluator:
    def __init__(self):
        self.dataset = None
        # evaluation_results 现在只在内存中作为临时存储
        self.evaluation_results = {}
    
    def load_dataset(self):
        """加载数据集"""
        with open(DATASET_PATH, 'r', encoding='utf-8') as f:
            self.dataset = json.load(f)
    
    def call_api(self, prompt, ai_name):
        """调用指定的API"""
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
Analyze this code step by step and determine the final output value. Provide only the number. """ 
        return prompt
    
    def evaluate_task_with_ai(self, task_data, ai_name):
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

    def evaluate_all_tasks(self):
        """评估所有任务并根据结果更新难度"""
        self.load_dataset()
        self.evaluation_results.clear() # 清空旧结果
        
        ai_names = list(AI_APIS.keys())
        
        for i in range(1, len(self.dataset)):
            task = self.dataset[i]
            if "task" not in task:
                continue
            
            if task.get("metadata", {}).get("language") != "python":
                print(f"Skipping evaluation for task {task['id']} (Not Python)")
                continue
                
            task_id = task["id"]
            expected_answer = task["task"]["answer"]
            original_difficulty = task["metadata"].get("difficulty", 3) # 增加 .get 提高稳健性
            
            print(f"Evaluating task {task_id} (original difficulty: {original_difficulty})...")
            
            ai_correctness = []
            
            for ai_name in ai_names:
                print(f"  Testing with {ai_name}...")
                predicted_answer = self.evaluate_task_with_ai(task, ai_name)
                
                if predicted_answer is not None and predicted_answer == expected_answer:
                    ai_correctness.append(1)
                    print(f"    ✓ Correct: {predicted_answer}")
                else:
                    ai_correctness.append(0)
                    print(f"    ✗ Wrong: {predicted_answer} (expected: {expected_answer})")
            
            new_difficulty = self.calculate_difficulty_from_errors(ai_correctness)
            self.dataset[i]["metadata"]["difficulty"] = new_difficulty
            
            correctness_str = " ".join(map(str, ai_correctness))
            result_line = f"{task_id}：难度：{new_difficulty} ai评估记录：{correctness_str}"
            
            self.evaluation_results[task_id] = {
                "original_difficulty": original_difficulty,
                "new_difficulty": new_difficulty,
                "ai_correctness": ai_correctness,
                "error_count": ai_correctness.count(0),
                "result_line": result_line
            }
            
            if new_difficulty != original_difficulty:
                print(f"  难度更新：{original_difficulty} → {new_difficulty}")
            
            print(f"  结果：{result_line}")
        
        # (已修改) 保存更新后的数据集
        with open(DATASET_PATH, 'w', encoding='utf-8') as f:
            json.dump(self.dataset, f, indent=2, ensure_ascii=False)
        print(f"\nDataset difficulty updated at {DATASET_PATH}")
        
        # (已修改) 生成统计数据
        print("\nGenerating AI evaluation statistics...")
        summary_stats = self.generate_difficulty_statistics() 
        
        # (已修改) 创建简洁的任务详情
        task_details = {}
        # 按 task_id 排序，使报告更整洁
        for task_id, results in sorted(self.evaluation_results.items()):
            task_details[task_id] = results["result_line"]
        
        # (已修改) 组合成最终报告
        final_report = {
            "evaluation_summary": summary_stats,
            "task_details": task_details
        }
        
        # (已修改) 保存新的报告结构
        report_path = "data/ai_evaluation_with_difficulty.json"
        with open(report_path, 'w', encoding='utf-8') as f:
            json.dump(final_report, f, indent=2, ensure_ascii=False)
        
        print(f"Summarized evaluation report saved to {report_path}")
        print("AI evaluation completed!")

    def generate_difficulty_statistics(self):
        """
        生成难度统计报告 (已修改)
        现在此方法会打印报告到控制台，并返回一个包含统计数据的字典。
        """
        ai_names = list(AI_APIS.keys())
        
        # (已修改) 这是将要返回的字典
        statistics_summary = {}

        print("\n=== AI评估统计报告 ===")
        
        # (已修改) 1. 任务详情 (仅打印到控制台)
        print(f"\n=== 任务详情 ===")
        for task_id, results in sorted(self.evaluation_results.items()):
            print(results["result_line"])
        
        # (已修改) 2. 难度分布统计
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
        
        # (已修改) 存入摘要
        statistics_summary["difficulty_distribution"] = difficulty_stats_dict
        statistics_summary["difficulty_changes"] = f"{difficulty_changes} tasks"
        
        # (已修改) 3. 整体正确率统计
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
        
        # (已修改) 存入摘要
        statistics_summary["overall_ai_accuracy"] = accuracy_stats_dict
        statistics_summary["total_tasks_evaluated"] = total_tasks
        
        return statistics_summary
    
if __name__ == "__main__": 
    evaluator = AIEvaluator() 
    evaluator.evaluate_all_tasks()