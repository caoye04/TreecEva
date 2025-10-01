import json
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from config import DATASET_PATH, AI_APIS
import openai

class CoTGenerator:
    def __init__(self):
        self.dataset = None
        
    def load_data(self):
        """加载数据集"""
        with open(DATASET_PATH, 'r', encoding='utf-8') as f:
            self.dataset = json.load(f)
    
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
                        "content": "You are an expert code analyst. Provide a concise chain of thought in exactly 3 sentences, each sentence no more than 25 words."
                    },
                    {
                        "role": "user", 
                        "content": prompt
                    }
                ],
                temperature=0.3,
                max_tokens=200
            )
            
            return response.choices[0].message.content
                
        except Exception as e:
            return f"API Error: {str(e)}"
    
    def has_valid_cot(self, task_data):
        """检查任务是否已有有效的CoT"""
        if "task" not in task_data:
            return False
            
        cot = task_data["task"].get("cot", "")
        
        # 检查CoT是否为空、空字符串或仅包含空白字符
        if not cot or not cot.strip():
            return False
            
        # 检查是否包含API错误信息
        if "API Error:" in cot:
            return False
            
        # 检查CoT长度是否合理（至少应该有一些实际内容）
        if len(cot.strip()) < 10:
            return False
            
        return True
    
    def generate_cot_prompt(self, task_data):
        """生成CoT提示"""
        task_id = task_data["id"]
        description = task_data["task"]["description"]
        code = task_data["task"]["code"]
        answer = task_data["task"]["answer"]
        
        prompt = f"""
Analyze the following code and provide a concise chain of thought in exactly 3 sentences:

Task ID: {task_id}
Problem: {description}
Answer: {answer}

Code:
```
{code}
```
Requirements:
1. Use exactly 3 sentences
2. Each sentence maximum 25 words
3. Structure: Sentence 1 - data initialization, Sentence 2 - core computation process, Sentence 3 - final result output
4. Provide only the 3 sentences, no other explanation

Format:
First: ...
Second: ...
Third: ...
"""
        return prompt
    
    def generate_cot_for_task(self, task_data):
        """为单个任务生成CoT"""
        task_id = task_data["id"]
        
        # 生成提示
        prompt = self.generate_cot_prompt(task_data)
        
        # 调用API生成CoT
        print(f"Generating CoT for task {task_id}...")
        cot = self.call_api(prompt)
        
        return cot
    
    def update_dataset_with_cot(self):
        """更新数据集，添加CoT（跳过已有有效CoT的任务）"""
        self.load_data()
        
        generated_count = 0
        skipped_count = 0
        
        # 跳过第一个元素（背景信息）
        for i in range(1, len(self.dataset)):
            task = self.dataset[i]
            
            if "task" not in task:
                continue
                
            task_id = task["id"]
            
            # 检查是否已有有效的CoT
            if self.has_valid_cot(task):
                print(f"⏭ Task {task_id}: CoT already exists, skipping")
                skipped_count += 1
                continue
            
            # 生成新的CoT
            cot = self.generate_cot_for_task(task)
            self.dataset[i]["task"]["cot"] = cot
            print(f"✓ Task {task_id}: CoT generated")
            generated_count += 1
        
        # 保存更新后的数据集
        with open(DATASET_PATH, 'w', encoding='utf-8') as f:
            json.dump(self.dataset, f, indent=2, ensure_ascii=False)
        
        print(f"\nCoT generation completed:")
        print(f"  Generated: {generated_count}")
        print(f"  Skipped: {skipped_count}")
        print(f"  Dataset updated at {DATASET_PATH}")

if __name__ == "__main__":
    generator = CoTGenerator()
    generator.update_dataset_with_cot()