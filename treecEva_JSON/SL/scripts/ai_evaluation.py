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
            
        # 寻找数字模式
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
        """生成评估提示"""
        description = task_data["task"]["description"]
        code = task_data["task"]["code"]
        
        prompt = f"""
{description}

Code:
```{task_data["metadata"]["language"]}
{code}
```
Analyze this code step by step and determine the final output value. Provide only the number.
"""
        return prompt
    
    def evaluate_task_with_ai(self, task_data, ai_name):
        """使用指定AI评估任务"""
        prompt = self.generate_evaluation_prompt(task_data)
        response = self.call_api(prompt, ai_name)
        predicted_answer = self.extract_number_from_response(response)
        
        return predicted_answer

    def calculate_difficulty_from_errors(self, ai_correctness):
        """根据AI错误数计算难度（0-5）"""
        # ai_correctness 中 0 表示错误，1 表示正确
        error_count = ai_correctness.count(0)
        
        # 难度 = AI错误的数目，范围 0-5
        # 如果所有AI都答对了，难度为0
        # 如果所有5个AI都答错了，难度为5
        difficulty = min(error_count, 5)
        
        return difficulty

    def evaluate_all_tasks(self):
        """评估所有任务并根据结果更新难度"""
        self.load_dataset()
        
        # 获取所有AI名称
        ai_names = list(AI_APIS.keys())
        
        # 跳过第一个元素（背景信息）
        for i in range(1, len(self.dataset)):
            task = self.dataset[i]
            if "task" not in task:
                continue
                
            task_id = task["id"]
            expected_answer = task["task"]["answer"]
            original_difficulty = task["metadata"]["difficulty"]
            
            print(f"Evaluating task {task_id} (original difficulty: {original_difficulty})...")
            
            # 存储每个AI的评估结果（1表示正确，0表示错误）
            ai_correctness = []
            
            # 对每个AI进行评估
            for ai_name in ai_names:
                print(f"  Testing with {ai_name}...")
                predicted_answer = self.evaluate_task_with_ai(task, ai_name)
                
                if predicted_answer is not None and predicted_answer == expected_answer:
                    ai_correctness.append(1)
                    print(f"    ✓ Correct: {predicted_answer}")
                else:
                    ai_correctness.append(0)
                    print(f"    ✗ Wrong: {predicted_answer} (expected: {expected_answer})")
            
            # 根据AI错误数计算新难度
            new_difficulty = self.calculate_difficulty_from_errors(ai_correctness)
            
            # 更新数据集中的难度
            self.dataset[i]["metadata"]["difficulty"] = new_difficulty
            
            # 记录格式：case2：难度：3 ai评估记录：0 0 0 1 1
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
        
        # 保存更新后的数据集（含新难度）
        with open(DATASET_PATH, 'w', encoding='utf-8') as f:
            json.dump(self.dataset, f, indent=2, ensure_ascii=False)
        
        # 保存评估结果
        with open("data/ai_evaluation_with_difficulty.json", 'w', encoding='utf-8') as f:
            json.dump(self.evaluation_results, f, indent=2, ensure_ascii=False)
        
        # 生成统计报告
        self.generate_difficulty_statistics()
        
        print("AI evaluation completed and difficulties updated!")

    def generate_difficulty_statistics(self):
        """生成难度统计报告"""
        ai_names = list(AI_APIS.keys())
        
        print("\n=== AI评估统计报告 ===")
        
        # 按任务显示结果
        for task_id, results in self.evaluation_results.items():
            print(results["result_line"])
        
        # 难度分布统计
        print(f"\n=== 难度分布统计 ===")
        difficulty_distribution = {}
        difficulty_changes = 0
        
        for results in self.evaluation_results.values():
            new_diff = results["new_difficulty"]
            if new_diff not in difficulty_distribution:
                difficulty_distribution[new_diff] = 0
            difficulty_distribution[new_diff] += 1
            
            if results["original_difficulty"] != results["new_difficulty"]:
                difficulty_changes += 1
        
        for difficulty in range(6):  # 0-5
            count = difficulty_distribution.get(difficulty, 0)
            print(f"难度 {difficulty}: {count} 个任务")
        
        print(f"\n难度发生变化的任务数: {difficulty_changes}")
        
        # 整体正确率统计
        total_tasks = len(self.evaluation_results)
        ai_total_correct = [0] * len(ai_names)
        
        for results in self.evaluation_results.values():
            for i, correct in enumerate(results["ai_correctness"]):
                ai_total_correct[i] += correct
        
        print(f"\n=== 整体正确率 ===")
        for i, ai_name in enumerate(ai_names):
            accuracy = ai_total_correct[i] / total_tasks * 100 if total_tasks > 0 else 0
            print(f"{ai_name}: {ai_total_correct[i]}/{total_tasks} ({accuracy:.1f}%)")

if __name__ == "__main__":
    evaluator = AIEvaluator()
    evaluator.evaluate_all_tasks()