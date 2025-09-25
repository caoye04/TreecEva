import json
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from config import DATASET_PATH, AI_APIS
import openai

class TaskGenerator:
    def __init__(self):
        self.dataset = None
    
    def load_dataset(self):
        """加载数据集"""
        with open(DATASET_PATH, 'r', encoding='utf-8') as f:
            self.dataset = json.load(f)
    
    def call_api(self, prompt, api_name="qwen3_coder"):
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
                        "content": "You are an expert in creating challenging programming problems. Generate complex code samples that require multi-step reasoning to solve."
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                temperature=0.7,
                max_tokens=3000
            )
            
            return response.choices[0].message.content
                
        except Exception as e:
            return f"API Error: {str(e)}"
    
    def generate_task_prompt(self):
        """生成新任务的提示"""
        # 分析现有任务模式
        background = self.dataset[0] if self.dataset else {}
        existing_tasks = self.dataset[1:] if len(self.dataset) > 1 else []
        
        # 获取已使用的ID
        used_ids = [task.get("id", "") for task in existing_tasks]
        next_id_num = len(used_ids) + 1
        next_id = f"SL-MIX-S{next_id_num:03d}"
        
        # 选择语言（循环使用）
        languages = ["python", "cpp", "java", "c"]
        selected_language = languages[len(used_ids) % len(languages)]
        
        prompt = f"""
                Based on the following background and requirements, generate a new complex programming task:

                Background: {background.get('background', '')}

                Requirements: {background.get('requirements', '')}

                Please generate a new task with the following specifications:

                1. ID: {next_id}
                2. Language: {selected_language}
                3. Difficulty: 8-10 (very challenging)
                4. Intervention: 6-10 (requires deep reasoning)

                The task should include:
                - Complex nested data structures
                - Multiple calculation steps
                - Advanced programming constructs
                - Mathematical operations
                - String/data manipulations

                Please provide the response in this exact JSON format:
                ```json
                {{
                    "id": "{next_id}",
                    "metadata": {{
                        "category": "Statement-Level",
                        "language": "{selected_language}",
                        "difficulty": <number_8_to_10>,
                        "intervention": <number_6_to_10>
                    }},
                    "task": {{
                        "description": "<detailed_description>",
                        "code": "<complex_code>",
                        "answer": <correct_numerical_answer>,
                        "cot": ""
                    }}
                }}```
                Make sure the code is syntactically correct, executable, and produces a deterministic numerical result.
                The complexity should match or exceed the existing examples.
                """
        return prompt

    def generate_new_task(self):
        """生成新任务"""
        self.load_dataset()
        
        print("Generating new task...")
        prompt = self.generate_task_prompt()
        response = self.call_api(prompt)
        
        # 解析JSON响应
        try:
            # 提取JSON部分
            import re
            json_match = re.search(r'```json\s*(.*?)\s*```', response, re.DOTALL)
            if json_match:
                json_str = json_match.group(1)
            else:
                # 如果没有代码块，尝试直接解析
                json_str = response
            
            new_task = json.loads(json_str)
            
            # 验证任务格式
            required_fields = ["id", "metadata", "task"]
            if all(field in new_task for field in required_fields):
                # 添加到数据集
                self.dataset.append(new_task)
                
                # 保存更新后的数据集
                with open(DATASET_PATH, 'w', encoding='utf-8') as f:
                    json.dump(self.dataset, f, indent=2, ensure_ascii=False)
                
                print(f"New task {new_task['id']} generated and added to dataset!")
                return new_task
            else:
                print("Generated task missing required fields")
                return None
                
        except json.JSONDecodeError as e:
            print(f"Failed to parse generated task JSON: {e}")
            print(f"Raw response: {response}")
            return None

    def generate_and_validate_task(self):
        """生成并验证新任务"""
        new_task = self.generate_new_task()
        
        if new_task:
            print("Task generation completed successfully!")
            return new_task
        else:
            print("Task generation failed!")
            return None
        
if __name__ == "__main__":
    generator = TaskGenerator()
    generator.generate_and_validate_task()