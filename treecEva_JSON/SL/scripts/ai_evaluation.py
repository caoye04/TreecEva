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
    
    def call_api(self, prompt, api_name):
        """调用指定的API"""
        api_config = AI_APIS[api_name]
        
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
                        "content": "You are an expert programmer. Analyze the given code and predict the final output value. Provide only the numerical answer."
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                temperature=0.1,
                max_tokens=100
            )
            
            return response.choices[0].message.content
                
        except Exception as e:
            return f"API Error: {str(e)}"
    
    def extract_number_from_response(self, response):
        """从响应中提取数字"""
        # 移除错误信息
        if "Error:" in response:
            return None
            
        # 寻找数字模式
        patterns = [
            r'(?:answer|result|output|value).*?(\d+)',
            r'^(\d+)$',
            r'(\d+)(?:\s*$|\s*\.)',
        ]
        
        for pattern in patterns:
            match = re.search(pattern, response, re.IGNORECASE | re.MULTILINE)
            if match:
                return int(match.group(1))
        
        # 尝试提取最后一个数字
        numbers = re.findall(r'\d+', response)
        if numbers:
            return int(numbers[-1])
        
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
                Please analyze this code step by step and determine the final output value. Provide only the numerical answer.
                """
        return prompt
    
    def evaluate_task_with_ai(self, task_data, ai_name):
        """使用指定AI评估任务"""
        prompt = self.generate_evaluation_prompt(task_data)
        response = self.call_api(prompt, ai_name)
        predicted_answer = self.extract_number_from_response(response)
        
        return {
            "raw_response": response,
            "predicted_answer": predicted_answer
        }
    
    def evaluate_all_tasks(self):
        """评估所有任务"""
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
            
            print(f"Evaluating task {task_id}...")
            
            task_results = {
                "expected_answer": expected_answer,
                "ai_predictions": {},
                "correct_ais": [],
                "incorrect_ais": []
            }
            
            # 对每个AI进行评估
            for ai_name in ai_names:
                print(f"  Testing with {ai_name}...")
                ai_result = self.evaluate_task_with_ai(task, ai_name)
                
                if ai_result and ai_result["predicted_answer"] is not None:
                    task_results["ai_predictions"][ai_name] = ai_result
                    
                    # 检查答案是否正确
                    if ai_result["predicted_answer"] == expected_answer:
                        task_results["correct_ais"].append(ai_name)
                    else:
                        task_results["incorrect_ais"].append(ai_name)
                else:
                    task_results["ai_predictions"][ai_name] = {
                        "raw_response": ai_result["raw_response"] if ai_result else "Failed to get response",
                        "predicted_answer": None
                    }
                    task_results["incorrect_ais"].append(ai_name)
        
            self.evaluation_results[task_id] = task_results
        
        # 保存评估结果
        with open("data/ai_evaluation_results.json", 'w', encoding='utf-8') as f:
            json.dump(self.evaluation_results, f, indent=2, ensure_ascii=False)
        
        # 生成统计报告
        self.generate_statistics_report()
        
        print("AI evaluation completed!")

    def generate_statistics_report(self):
        """生成统计报告"""
        ai_names = list(AI_APIS.keys())
        stats = {ai_name: {"correct": 0, "total": 0} for ai_name in ai_names}
        
        for task_id, results in self.evaluation_results.items():
            for ai_name in ai_names:
                stats[ai_name]["total"] += 1
                if ai_name in results["correct_ais"]:
                    stats[ai_name]["correct"] += 1
        
        print("\n=== AI Evaluation Statistics ===")
        for ai_name, stat in stats.items():
            accuracy = stat["correct"] / stat["total"] * 100 if stat["total"] > 0 else 0
            print(f"{ai_name}: {stat['correct']}/{stat['total']} ({accuracy:.1f}%)")

if __name__ == "__main__":
    evaluator = AIEvaluator()
    evaluator.evaluate_all_tasks()