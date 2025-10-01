import json
import sys
import re
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from config import DATASET_PATH, AI_APIS
import openai

class TaskGenerator:
    def __init__(self):
        self.dataset = None
    
    def load_dataset(self):
        """Load dataset"""
        with open(DATASET_PATH, 'r', encoding='utf-8') as f:
            self.dataset = json.load(f)
    
    def call_api(self, prompt, api_name="qwen3_coder"):
        """Call API to generate content"""
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
    
    def fix_case_with_api(self, task_data, error_info, max_attempts=5):
        """Fix problematic case using API"""
        current_task = task_data.copy()
        
        for attempt in range(max_attempts):
            print(f"  Attempting to fix case, attempt {attempt + 1}/{max_attempts}")
            
            fix_prompt = f"""
            Please help me fix this code task so it can execute correctly and produce a unique numerical output.

            Task Background: This is a dataset for testing AI code reasoning capabilities.

            Requirements:
            1. The code must compile and execute successfully
            2. The code must have a unique, deterministic numerical output
            3. Ask for the value of a specific variable at some point in the code execution
            4. Code complexity should remain at level 8-10

            Current Task Information:
            ID: {current_task['id']}
            Language: {current_task['metadata']['language']}
            Description: {current_task['task']['description']}

            Current Code:
            ```{current_task['metadata']['language']}
            {current_task['task']['code']}
            ```

            Problem Encountered: {error_info}

            Please generate the fixed complete task, ensuring:
            1. Fix all compilation/runtime errors
            2. The code has a clear variable value that can be queried at a key execution point
            3. This variable value should be a unique, deterministic number
            4. The code should print this variable value at the end, format: "Target result: {{variable_value}}"

            Please return the fixed task in JSON format:
            ```json
            {{
                "id": "{current_task['id']}",
                "metadata": {{
                    "category": "Statement-Level",
                    "language": "{current_task['metadata']['language']}",
                    "difficulty": {current_task['metadata']['difficulty']},
                    "intervention": {current_task['metadata']['intervention']}
                }},
                "task": {{
                    "description": "<Fixed description asking for a variable value at some execution point>",
                    "code": "<Fixed executable code>",
                    "answer": <Correct numerical answer>,
                    "cot": ""
                }}
            }}```
            """
            
            response = self.call_api(fix_prompt)
            
            # Parse the fixed task
            try:
                json_match = re.search(r'```json\s*(.*?)\s*```', response, re.DOTALL)
                if json_match:
                    json_str = json_match.group(1)
                else:
                    json_str = response
                
                fixed_task = json.loads(json_str)
                
                # Validate the fixed task format
                required_fields = ["id", "metadata", "task"]
                if all(field in fixed_task for field in required_fields):
                    return fixed_task
                
            except json.JSONDecodeError:
                continue
        
        return None

    def generate_task_prompt(self):
        """Generate prompt for new task"""
        background = self.dataset[0] if self.dataset else {}
        existing_tasks = self.dataset[1:] if len(self.dataset) > 1 else []
        
        used_ids = [task.get("id", "") for task in existing_tasks]
        next_id_num = len(used_ids) + 1
        next_id = f"SL-MIX-S{next_id_num:03d}"
        
        # 只使用三种语言
        languages = ["python", "cpp", "c"]
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

        Special Requirements:
        1. The code must be syntactically correct and directly compilable/executable
        2. The code must produce a unique, deterministic numerical result
        3. At some critical point in code execution, there should be an important variable whose value is the answer we seek
        4. The problem description should ask "what is the value of variable X at execution point Y"
        5. The code must print this variable value at the end, format: "Result: {{variable_value}}" or "Target result: {{variable_value}}"

        Ensure the code:
        - Has no syntax errors
        - Has no undefined constants (e.g., M_PI needs to be defined or include math.h)
        - Has no missing library files
        - Produces deterministic output

        Please respond in this JSON format:
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
                "description": "<Detailed description asking for a variable value at some execution point>",
                "code": "<Complex executable code>",
                "answer": <correct_numerical_answer>,
                "cot": ""
            }}
        }}```
        
        Ensure the code complexity matches or exceeds existing examples while guaranteeing executability.
        """
        return prompt

    def generate_new_task(self):
        """Generate new task"""
        self.load_dataset()
        
        print("Generating new task...")
        prompt = self.generate_task_prompt()
        response = self.call_api(prompt)
        
        # Parse JSON response
        try:
            json_match = re.search(r'```json\s*(.*?)\s*```', response, re.DOTALL)
            if json_match:
                json_str = json_match.group(1)
            else:
                json_str = response
            
            new_task = json.loads(json_str)
            
            # Validate task format
            required_fields = ["id", "metadata", "task"]
            if all(field in new_task for field in required_fields):
                self.dataset.append(new_task)
                
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
        """Generate and validate new task"""
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