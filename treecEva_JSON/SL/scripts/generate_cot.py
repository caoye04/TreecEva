import json
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from config import DATASET_PATH, ANSWER_PATH, AI_APIS
import openai

class CoTGenerator:
    def __init__(self):
        self.dataset = None
        self.answers = None
        
    def load_data(self):
        """加载数据集和答案"""
        with open(DATASET_PATH, 'r', encoding='utf-8') as f:
            self.dataset = json.load(f)
        
        with open(ANSWER_PATH, 'r', encoding='utf-8') as f:
            self.answers = json.load(f)
    
    def call_api(self, prompt, api_name="qwen3_235b"):
        """调用API生成内容"""
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
                        "content": "You are an expert programmer and code analyst. Generate a clear, step-by-step chain of thought for code execution."
                    },
                    {
                        "role": "user", 
                        "content": prompt
                    }
                ],
                temperature=0.3,
                max_tokens=1500
            )
            
            return response.choices[0].message.content
                
        except Exception as e:
            return f"API Error: {str(e)}"
    
    def generate_cot_prompt(self, task_data, execution_result):
        """生成CoT提示"""
        task_id = task_data["id"]
        description = task_data["task"]["description"]
        code = task_data["task"]["code"]
        expected_answer = task_data["task"]["answer"]
        
        actual_result = execution_result.get("result") if execution_result.get("success") else "execution failed"
        
        prompt = f"""
                Please analyze the following code and generate a clear, step-by-step chain of thought explaining how to arrive at the final answer.

                Task ID: {task_id}
                Description: {description}

                Code:
                '''
                {code}
                '''
                Expected Answer: {expected_answer}
                Actual Execution Result: {actual_result}

                Please provide a detailed step-by-step reasoning process that explains:
                1. How the code initializes variables and data structures
                2. The logical flow of execution
                3. Key calculations and transformations
                4. How intermediate results lead to the final answer

                Format your response as a clear, logical chain of thought that could help someone understand the code execution process.
                """
        return prompt
    
    def generate_cot_for_task(self, task_data):
        """为单个任务生成CoT"""
        task_id = task_data["id"]
        
        # 获取执行结果
        execution_result = self.answers.get(task_id, {})
        
        # 生成提示
        prompt = self.generate_cot_prompt(task_data, execution_result)
        
        # 调用API生成CoT
        print(f"Generating CoT for task {task_id}...")
        cot = self.call_api(prompt)
        
        return cot
    
    def update_dataset_with_cot(self):
        """更新数据集，添加CoT"""
        self.load_data()
        
        # 跳过第一个元素（背景信息）
        for i in range(1, len(self.dataset)):
            task = self.dataset[i]
            
            if "task" in task and task["task"].get("cot", "") == "":
                cot = self.generate_cot_for_task(task)
                self.dataset[i]["task"]["cot"] = cot
        
        # 保存更新后的数据集
        with open(DATASET_PATH, 'w', encoding='utf-8') as f:
            json.dump(self.dataset, f, indent=2, ensure_ascii=False)
        
        print(f"CoT generation completed. Dataset updated at {DATASET_PATH}")

if __name__ == "__main__":
    generator = CoTGenerator()
    generator.update_dataset_with_cot()