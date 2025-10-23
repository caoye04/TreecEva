# 代码记录

## 任务需求

我在做一个数据集，想用AI来进行辅助。我需要写四个AI的API调用程序和脚本来完成以下四项任务：

1. 基于已有的任务，将其task/code用脚本转换为真实code文件，并且运行并记录返回值。这个会单独存储在一个answer.json里，如果输出返回值有值，则在json里记录该任务的值，不对的话则在json中标注，无法运行成功，且简要记录运行错误原因
2. 基于已有的任务+记录的answer生成思维链，并在数据集文件中更新
3. 调用五个不同的AI的API，不看answer和cot，直接预测任务答案，与真实答案对比，并记录每个问题回答正确的AI和错误的AI
4. 基于目前的内容，再生成一个task，并再数据集文件中更新，并且再重复上面的三步

## 工作结构

```cmd
工作目录/
├── scripts/
│   ├── data/
│   │   ├── Statement-Level-MIX.json
│ 	│   └── answer.json 
│ 	│   └── ai_evaluation_with_difficulty.json
│   ├── temp_code/
│   ├── execute_tasks.py
│   ├── generate_cot.py
│   ├── ai_evaluation.py
│   ├── generate_new_task.py
│   └── main_loop.py
├── requirements.txt
├── test_api.py
└── config.py
```

## scripts

### execute_tasks.py

```py
import json
import subprocess
import os
import tempfile
import sys
import re
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from config import DATASET_PATH, ANSWER_PATH, TEMP_CODE_DIR

class TaskExecutor:
    def __init__(self):
        self.results = {}
        
    def execute_python_code(self, code, task_id):
        """执行Python代码"""
        try:
            os.makedirs(TEMP_CODE_DIR, exist_ok=True)
            temp_file = os.path.join(TEMP_CODE_DIR, f"{task_id}.py")
            
            with open(temp_file, 'w', encoding='utf-8') as f:
                f.write(code)
            
            result = subprocess.run(
                [sys.executable, temp_file],
                capture_output=True,
                text=True,
                timeout=30
            )
            
            if result.returncode == 0:
                output = result.stdout.strip()
                return self.extract_result_from_output(output)
            else:
                return {
                    "success": False,
                    "error": f"Runtime error: {result.stderr}"
                }
                
        except subprocess.TimeoutExpired:
            return {
                "success": False,
                "error": "Execution timeout (30s)"
            }
        except Exception as e:
            return {
                "success": False,
                "error": f"Execution error: {str(e)}"
            }
    
    def execute_cpp_code(self, code, task_id):
        """执行C++代码"""
        try:
            os.makedirs(TEMP_CODE_DIR, exist_ok=True)
            temp_cpp = os.path.join(TEMP_CODE_DIR, f"{task_id}.cpp")
            temp_exe = os.path.join(TEMP_CODE_DIR, f"{task_id}.exe")
            
            # 为C++代码添加必要的数学常数定义
            if "#define _USE_MATH_DEFINES" not in code:
                code = "#define _USE_MATH_DEFINES\n" + code
            if "#define M_PI" not in code and "M_PI" in code:
                code = "#define M_PI 3.14159265358979323846\n" + code
            
            with open(temp_cpp, 'w', encoding='utf-8') as f:
                f.write(code)
            
            # 编译
            compile_result = subprocess.run(
                ["g++", "-o", temp_exe, temp_cpp, "-std=c++17"],
                capture_output=True,
                text=True,
                timeout=30
            )
            
            if compile_result.returncode != 0:
                return {
                    "success": False,
                    "error": f"Compilation error: {compile_result.stderr}"
                }
            
            # 运行
            run_result = subprocess.run(
                [temp_exe],
                capture_output=True,
                text=True,
                timeout=30
            )
            
            if run_result.stdout.strip():
                output = run_result.stdout.strip()
                return self.extract_result_from_output(output)
            else:
                return {
                    "success": False,
                    "error": f"Runtime error: {run_result.stderr}"
                }
                
        except Exception as e:
            return {
                "success": False,
                "error": f"Execution error: {str(e)}"
            }
    
    def execute_c_code(self, code, task_id):
        """执行C代码"""
        try:
            os.makedirs(TEMP_CODE_DIR, exist_ok=True)
            temp_c = os.path.join(TEMP_CODE_DIR, f"{task_id}.c")
            temp_exe = os.path.join(TEMP_CODE_DIR, f"{task_id}.exe")
            
            # 为C代码添加必要的数学常数定义
            if "#define _USE_MATH_DEFINES" not in code:
                code = "#define _USE_MATH_DEFINES\n" + code
            if "#define M_PI" not in code and "M_PI" in code:
                code = "#define M_PI 3.14159265358979323846\n" + code
            
            with open(temp_c, 'w', encoding='utf-8') as f:
                f.write(code)
            
            # 编译
            compile_result = subprocess.run(
                ["gcc", "-o", temp_exe, temp_c, "-lm", "-std=c99"],
                capture_output=True,
                text=True,
                timeout=30
            )
            
            if compile_result.returncode != 0:
                return {
                    "success": False,
                    "error": f"Compilation error: {compile_result.stderr}"
                }
            
            # 运行
            run_result = subprocess.run(
                [temp_exe],
                capture_output=True,
                text=True,
                timeout=30
            )
            
            if run_result.stdout.strip():
                output = run_result.stdout.strip()
                return self.extract_result_from_output(output)
            else:
                return {
                    "success": False,
                    "error": f"Runtime error: {run_result.stderr}"
                }
                
        except Exception as e:
            return {
                "success": False,
                "error": f"Execution error: {str(e)}"
            }
    
    def extract_result_from_output(self, output):
        """从输出中提取结果"""
        patterns = [
            r'Final result:\s*(\d+(?:\.\d+)?)',
            r'Target result:\s*(\d+(?:\.\d+)?)', 
            r'Master result:\s*(\d+(?:\.\d+)?)',
            r'Final output:\s*(\d+(?:\.\d+)?)',
            r'Result:\s*(\d+(?:\.\d+)?)',
            r'Answer:\s*(\d+(?:\.\d+)?)',
        ]
        
        for pattern in patterns:
            match = re.search(pattern, output, re.MULTILINE | re.IGNORECASE)
            if match:
                value_str = match.group(1)
                if '.' in value_str:
                    result = int(round(float(value_str)))
                else:
                    result = int(value_str)
                
                return {
                    "success": True,
                    "result": result
                }
        
        # 提取最后一个数字
        numbers = re.findall(r'\d+(?:\.\d+)?', output)
        if numbers:
            value_str = numbers[-1]
            if '.' in value_str:
                result = int(round(float(value_str)))
            else:
                result = int(value_str)
                
            return {
                "success": True,
                "result": result
            }
        
        return {
            "success": False,
            "error": f"Could not extract result from output: {output}"
        }
    
    def execute_task(self, task_data):
        """执行单个任务"""
        task_id = task_data["id"]
        language = task_data["metadata"]["language"]
        code = task_data["task"]["code"]
        
        print(f"Executing task {task_id} ({language})...")
        
        if language == "python":
            result = self.execute_python_code(code, task_id)
        elif language in ["cpp", "c++"]:
            result = self.execute_cpp_code(code, task_id)
        elif language == "c":
            result = self.execute_c_code(code, task_id)
        else:
            result = {
                "success": False,
                "error": f"Unsupported language: {language}"
            }
        
        return result
    
    def execute_all_tasks(self):
        """执行所有任务，保存到answer.json，并覆写数据集的answer字段"""
        # 加载数据集
        with open(DATASET_PATH, 'r', encoding='utf-8') as f:
            dataset = json.load(f)
        
        tasks = dataset[1:] if len(dataset) > 1 else []
        
        for i, task in enumerate(tasks):
            if "task" in task and "code" in task["task"]:
                result = self.execute_task(task)
                self.results[task["id"]] = result
                
                # 如果执行成功，覆写数据集中的answer字段
                if result["success"]:
                    dataset[i + 1]["task"]["answer"] = result["result"]
                    print(f"✓ Task {task['id']}: Answer updated to {result['result']}")
                else:
                    print(f"✗ Task {task['id']}: Execution failed - {result.get('error', 'Unknown error')}")
        
        # 保存执行结果到answer.json
        with open(ANSWER_PATH, 'w', encoding='utf-8') as f:
            json.dump(self.results, f, indent=2, ensure_ascii=False)
        
        # 保存更新后的数据集（覆写answer字段）
        with open(DATASET_PATH, 'w', encoding='utf-8') as f:
            json.dump(dataset, f, indent=2, ensure_ascii=False)
        
        print(f"Execution completed. Results saved to {ANSWER_PATH}")
        print(f"Dataset answers updated at {DATASET_PATH}")
        return self.results

if __name__ == "__main__":
    executor = TaskExecutor()
    executor.execute_all_tasks()
```

### generate_cot.py

````py
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
````

### ai_evaluation.py

~~~py
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
~~~

### generate_new_task.py

~~~py
import json
import sys
import re
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from config import DATASET_PATH, AI_APIS
import openai
import random

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
                temperature=0.8,  # 提高温度以增加多样性
                max_tokens=3000
            )
            
            return response.choices[0].message.content
                
        except Exception as e:
            return f"API Error: {str(e)}"
    
    def analyze_dataset_distribution(self):
        """分析数据集的难度和语言分布"""
        existing_tasks = self.dataset[1:] if len(self.dataset) > 1 else []
        
        # 统计难度分布（0-5，基于AI错误数）
        difficulty_counts = {i: 0 for i in range(6)}
        language_counts = {}
        intervention_counts = {i: 0 for i in range(11)}
        
        for task in existing_tasks:
            if "metadata" in task:
                # 难度是AI评估后确定的（0-5）
                diff = task["metadata"].get("difficulty", 3)
                difficulty_counts[diff] = difficulty_counts.get(diff, 0) + 1
                
                # 语言分布
                lang = task["metadata"].get("language", "python")
                language_counts[lang] = language_counts.get(lang, 0) + 1
                
                # Intervention分布
                interv = task["metadata"].get("intervention", 5)
                intervention_counts[interv] = intervention_counts.get(interv, 0) + 1
        
        return {
            "difficulty_distribution": difficulty_counts,
            "language_distribution": language_counts,
            "intervention_distribution": intervention_counts,
            "total_tasks": len(existing_tasks)
        }
    
    def identify_missing_difficulty_range(self, distribution):
        """识别缺失的难度范围（基于AI错误数）"""
        difficulty_counts = distribution["difficulty_distribution"]
        total = distribution["total_tasks"]
        
        if total == 0:
            # 第一个任务，生成中等难度
            return "medium"
        
        # 目标分布：基于AI错误数的难度分布
        # 0-1错误（容易）：30% - AI基本都对
        # 2-3错误（中等）：40% - 部分AI错
        # 4-5错误（困难）：30% - 多数/全部AI错
        target_ranges = {
            "easy": {
                "errors": (0, 1),
                "target_ratio": 0.30,
                "description": "Most AIs get it right"
            },
            "medium": {
                "errors": (2, 3),
                "target_ratio": 0.40,
                "description": "Some AIs struggle"
            },
            "hard": {
                "errors": (4, 5),
                "target_ratio": 0.30,
                "description": "Most/All AIs fail"
            }
        }
        
        # 计算每个范围的缺失度
        deficits = {}
        for range_name, range_info in target_ranges.items():
            min_err, max_err = range_info["errors"]
            count = sum(difficulty_counts.get(d, 0) for d in range(min_err, max_err + 1))
            actual_ratio = count / total
            deficit = range_info["target_ratio"] - actual_ratio
            deficits[range_name] = deficit
        
        # 70%选择最缺失的，30%随机选择
        if random.random() < 0.7:
            target_range = max(deficits, key=deficits.get)
        else:
            # 从缺失度>0的范围中随机选
            positive_deficits = {k: v for k, v in deficits.items() if v > 0}
            if positive_deficits:
                target_range = random.choice(list(positive_deficits.keys()))
            else:
                target_range = "medium"
        
        return target_range
    
    def map_difficulty_range_to_complexity(self, target_range):
        """将目标难度范围映射为代码复杂度描述"""
        complexity_mapping = {
            "easy": {
                "description": "Simple and straightforward",
                "logic_steps": "1-3 sequential logic steps",
                "nesting": "Minimal or no nesting",
                "concepts": "1-2 basic programming concepts",
                "expected_errors": "0-1 AI errors (most AIs should solve it)",
                "examples": "simple loops, basic arithmetic, direct array operations"
            },
            "medium": {
                "description": "Moderate complexity",
                "logic_steps": "4-7 logic steps with some interdependencies",
                "nesting": "2-3 levels of nesting",
                "concepts": "3-4 programming concepts combined",
                "expected_errors": "2-3 AI errors (challenging for some AIs)",
                "examples": "nested loops, hash tables, recursive logic, bit manipulation"
            },
            "hard": {
                "description": "High complexity",
                "logic_steps": "8-15 logic steps with complex interdependencies",
                "nesting": "4+ levels of nesting or multiple abstraction layers",
                "concepts": "5+ advanced programming concepts",
                "expected_errors": "4-5 AI errors (very challenging, most AIs will fail)",
                "examples": "advanced algorithms, complex state machines, multiple data structures, intricate bit operations, meta-programming"
            }
        }
        
        return complexity_mapping.get(target_range, complexity_mapping["medium"])
    
    def select_language_and_features(self, distribution):
        """智能选择语言和特征组合"""
        language_counts = distribution["language_distribution"]
        total = distribution["total_tasks"]
        
        # 三种语言的目标比例
        target_ratios = {"python": 0.40, "cpp": 0.35, "c": 0.25}
        
        # 计算缺失度
        language_deficits = {}
        for lang, target_ratio in target_ratios.items():
            actual_ratio = language_counts.get(lang, 0) / total if total > 0 else 0
            language_deficits[lang] = target_ratio - actual_ratio
        
        # 70%选择最缺的语言，30%随机
        if random.random() < 0.7 and total > 0:
            selected_language = max(language_deficits, key=language_deficits.get)
        else:
            selected_language = random.choice(list(target_ratios.keys()))
        
        # 为不同语言定义特征池
        language_features = {
            "python": [
                "decorators and metaclasses",
                "list comprehensions and generator expressions",
                "context managers",
                "functional programming (map, filter, reduce)",
                "collections (defaultdict, Counter, deque)",
                "itertools and combinatorics",
                "dataclasses and named tuples",
                "lambda functions and closures",
                "set operations and frozenset",
                "dictionary comprehensions and merging"
            ],
            "cpp": [
                "templates and template specialization",
                "smart pointers (unique_ptr, shared_ptr)",
                "STL containers and algorithms",
                "move semantics",
                "operator overloading",
                "constexpr functions",
                "variadic templates",
                "RAII pattern",
                "lambda expressions and captures",
                "std::optional and std::variant"
            ],
            "c": [
                "function pointers and callbacks",
                "struct bit fields and unions",
                "pointer arithmetic and array manipulation",
                "preprocessor macros",
                "volatile variables",
                "custom memory management",
                "linked data structures (lists, trees)",
                "bitwise operations and masks",
                "type punning with unions",
                "flexible array members"
            ]
        }
        
        # 随机选择2-4个特征
        num_features = random.randint(2, 4)
        selected_features = random.sample(
            language_features[selected_language], 
            min(num_features, len(language_features[selected_language]))
        )
        
        return selected_language, selected_features
    
    def select_computational_paradigms(self, complexity_level):
        """根据复杂度级别选择计算范式组合"""
        all_paradigms = {
            "arithmetic": [
                "basic arithmetic operations",
                "bitwise operations (XOR, AND, OR, shifts)",
                "modular arithmetic",
                "logarithms and exponents",
                "floating point operations"
            ],
            "boolean": [
                "comparison operations",
                "logical operations (AND, OR, NOT)",
                "short-circuit evaluation",
                "ternary operators"
            ],
            "control_flow": [
                "nested loops",
                "conditional branches",
                "early returns and break",
                "state machines",
                "switch/case statements"
            ],
            "data_structures": [
                "arrays and matrices",
                "hash tables and maps",
                "trees (binary, n-ary)",
                "linked lists",
                "queues and stacks",
                "heaps"
            ],
            "algorithms": [
                "sorting algorithms",
                "searching (binary search, etc.)",
                "dynamic programming",
                "recursion and backtracking",
                "greedy algorithms",
                "divide and conquer"
            ],
            "string_ops": [
                "pattern matching and regex",
                "encoding/decoding",
                "string hashing",
                "parsing and tokenization",
                "string transformations"
            ],
            "mathematical": [
                "combinatorics (permutations, combinations)",
                "number theory (primes, GCD, LCM)",
                "geometry and spatial calculations",
                "statistics (mean, variance, etc.)",
                "mathematical sequences (fibonacci, etc.)"
            ]
        }
        
        # 根据复杂度决定选择多少个范式
        if complexity_level == "easy":
            num_categories = random.randint(1, 2)
            num_paradigms_per_category = 1
        elif complexity_level == "medium":
            num_categories = random.randint(2, 3)
            num_paradigms_per_category = random.randint(1, 2)
        else:  # hard
            num_categories = random.randint(3, 5)
            num_paradigms_per_category = random.randint(1, 2)
        
        selected_categories = random.sample(list(all_paradigms.keys()), 
                                           min(num_categories, len(all_paradigms)))
        selected_paradigms = []
        
        for category in selected_categories:
            num_items = min(num_paradigms_per_category, len(all_paradigms[category]))
            selected_paradigms.extend(random.sample(all_paradigms[category], num_items))
        
        return selected_paradigms
    
    def generate_diversity_constraints(self, existing_tasks, selected_language):
        """生成多样性约束"""
        if not existing_tasks:
            return "- This is the first task, create something creative and interesting!"
        
        # 分析最近的任务
        recent_tasks = existing_tasks[-5:] if len(existing_tasks) >= 5 else existing_tasks
        
        # 提取已使用的主题词
        used_themes = set()
        theme_keywords = [
            "matrix", "hash", "quantum", "crypto", "fibonacci", "prime", 
            "tree", "graph", "sort", "search", "encryption", "compression",
            "calendar", "game", "sensor", "network", "database", "parser"
        ]
        
        for task in recent_tasks:
            if "task" in task and "description" in task["task"]:
                desc = task["task"]["description"].lower()
                for keyword in theme_keywords:
                    if keyword in desc:
                        used_themes.add(keyword)
        
        # 提取常用的变量名模式
        used_var_patterns = set()
        var_patterns = ["data", "result", "value", "node", "state", "buffer", "config"]
        
        for task in recent_tasks:
            if "task" in task and "code" in task["task"]:
                code = task["task"]["code"].lower()
                for pattern in var_patterns:
                    if pattern in code:
                        used_var_patterns.add(pattern)
        
        constraints = []
        
        if used_themes:
            constraints.append(f"- AVOID these recently used themes: {', '.join(sorted(used_themes))}")
        
        constraints.append("- CREATE a unique problem scenario NOT similar to recent tasks")
        constraints.append("- USE creative and domain-specific variable names (avoid generic names like 'data', 'result')")
        constraints.append(f"- FOCUS on {selected_language}-specific idioms and best practices")
        constraints.append("- ENSURE the problem context is realistic and interesting")
        
        return "\n".join(constraints)
    
    def estimate_initial_intervention(self, complexity_level):
        """根据复杂度估算初始intervention值（实际值会在AI评估后更新）"""
        intervention_ranges = {
            "easy": (4, 6),
            "medium": (6, 8),
            "hard": (8, 10)
        }
        
        min_val, max_val = intervention_ranges.get(complexity_level, (6, 8))
        return random.randint(min_val, max_val)

    def generate_task_prompt(self):
        """生成优化的任务生成提示"""
        background = self.dataset[0] if self.dataset else {}
        existing_tasks = self.dataset[1:] if len(self.dataset) > 1 else []
        
        used_ids = [task.get("id", "") for task in existing_tasks]
        next_id_num = len(used_ids) + 1
        next_id = f"SL-MIX-S{next_id_num:03d}"
        
        # 分析当前数据集分布
        distribution = self.analyze_dataset_distribution()
        
        # 识别缺失的难度范围
        target_range = self.identify_missing_difficulty_range(distribution)
        complexity_info = self.map_difficulty_range_to_complexity(target_range)
        
        # 智能选择语言和特征
        selected_language, selected_features = self.select_language_and_features(distribution)
        
        # 选择计算范式
        selected_paradigms = self.select_computational_paradigms(target_range)
        
        # 估算初始intervention值
        initial_intervention = self.estimate_initial_intervention(target_range)
        
        # 生成多样性约束
        diversity_constraints = self.generate_diversity_constraints(existing_tasks, selected_language)
        
        prompt = f"""
Based on the following background and requirements, generate a new programming task:

Background: {background.get('background', '')}

Requirements: {background.get('requirements', '')}

═══════════════════════════════════════════════════════════════════
TASK SPECIFICATIONS
═══════════════════════════════════════════════════════════════════

1. Task ID: {next_id}
2. Language: {selected_language}
3. Target Complexity Level: {target_range.upper()}

COMPLEXITY REQUIREMENTS FOR "{target_range.upper()}" LEVEL:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
• Description: {complexity_info["description"]}
• Logic Steps: {complexity_info["logic_steps"]}
• Nesting Depth: {complexity_info["nesting"]}
• Concepts: {complexity_info["concepts"]}
• Expected AI Performance: {complexity_info["expected_errors"]}
• Examples: {complexity_info["examples"]}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

IMPORTANT: The final difficulty (0-5) will be determined by AI evaluation:
  - Difficulty = Number of AIs that answer incorrectly (out of 5 AIs)
  - Your task is to generate code matching the {target_range.upper()} complexity level
  - This should naturally result in {complexity_info["expected_errors"]}

4. Initial Intervention Estimate: {initial_intervention}
   (This represents the expected reasoning steps. Actual value will be updated after evaluation.)

═══════════════════════════════════════════════════════════════════
MANDATORY LANGUAGE-SPECIFIC FEATURES
═══════════════════════════════════════════════════════════════════
You MUST incorporate at least 2 of these {selected_language} features:

{chr(10).join(f'  • {feature}' for feature in selected_features)}

═══════════════════════════════════════════════════════════════════
REQUIRED COMPUTATIONAL PARADIGMS
═══════════════════════════════════════════════════════════════════
You MUST incorporate these computational elements:

{chr(10).join(f'  • {paradigm}' for paradigm in selected_paradigms)}

═══════════════════════════════════════════════════════════════════
DIVERSITY CONSTRAINTS (CRITICAL!)
═══════════════════════════════════════════════════════════════════
{diversity_constraints}

═══════════════════════════════════════════════════════════════════
CODE REQUIREMENTS
═══════════════════════════════════════════════════════════════════
1. The code MUST be syntactically correct and directly compilable/executable
2. The code MUST produce a unique, deterministic numerical result
3. At some critical execution point, there should be a key variable whose value is the answer
4. The problem description should ask: "what is the value of variable X at execution point Y"
5. The code MUST print this variable value at the end
   Format: "Result: {{variable_value}}" or "Target result: {{variable_value}}"

ENSURE THE CODE:
✓ Has no syntax errors
✓ Has no undefined constants (e.g., for C/C++: define M_PI or include math.h)
✓ Has no missing library files
✓ Produces deterministic output (no randomness unless seeded)
✓ Matches the {target_range.upper()} complexity level precisely

═══════════════════════════════════════════════════════════════════
RESPONSE FORMAT
═══════════════════════════════════════════════════════════════════
Please respond with ONLY the JSON (no additional text):

```json
{{
    "id": "{next_id}",
    "metadata": {{
        "category": "Statement-Level",
        "language": "{selected_language}",
        "difficulty": 5,
        "intervention": {initial_intervention}
    }},
    "task": {{
        "description": "<Creative problem description asking for a specific variable value>",
        "code": "<Executable code matching {target_range.upper()} complexity>",
        "answer": <correct_numerical_answer>,
        "cot": ""
    }}
}}```

NOTE: Set difficulty to 5 initially (it will be updated to 0-5 after AI evaluation based on how many AIs fail).

CRITICAL REMINDERS:
🎯 Match {target_range.upper()} complexity exactly - not too simple, not too complex
🎯 Use creative, domain-specific variable names and problem context
🎯 Avoid patterns similar to recent tasks
🎯 Ensure code is executable and produces deterministic output
"""
        return prompt
    
    def fix_case_with_api(self, task_data, error_info, max_attempts=5):
        """使用API修复有问题的case"""
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
4. Maintain the original complexity level

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

Fix all compilation/runtime errors
The code has a clear variable value that can be queried at a key execution point
This variable value should be a unique, deterministic number
The code should print this variable value at the end, format: "Target result: {{variable_value}}"
Maintain similar complexity level
Please return the fixed task in JSON format:
```
{{
    "id": "{current_task['id']}",
    "metadata": {{
        "category": "Statement-Level",
        "language": "{current_task['metadata']['language']}",
        "difficulty": 5,
        "intervention": {current_task['metadata']['intervention']}
    }},
    "task": {{
        "description": "<Fixed description asking for a variable value at some execution point>",
        "code": "<Fixed executable code>",
        "answer": <Correct numerical answer>,
        "cot": ""
    }}
}}
```
"""
            
            response = self.call_api(fix_prompt)
            
            # 解析修复后的任务
            try:
                json_match = re.search(r'```json\s*(.*?)\s*```', response, re.DOTALL)
                if json_match:
                    json_str = json_match.group(1)
                else:
                    json_str = response
                
                fixed_task = json.loads(json_str)
                
                # 验证修复后的任务格式
                required_fields = ["id", "metadata", "task"]
                if all(field in fixed_task for field in required_fields):
                    return fixed_task
                
            except json.JSONDecodeError:
                continue
        
        return None

    def generate_new_task(self):
        """生成新任务（带难度均衡和多样性优化）"""
        self.load_dataset()
        
        print("\n" + "="*70)
        print("ANALYZING CURRENT DATASET DISTRIBUTION")
        print("="*70)
        
        distribution = self.analyze_dataset_distribution()
        
        print(f"📊 Total tasks: {distribution['total_tasks']}")
        
        print(f"\n📈 Difficulty Distribution (0=easy, 5=hard, based on AI errors):")
        for diff in range(6):
            count = distribution['difficulty_distribution'].get(diff, 0)
            percentage = (count / distribution['total_tasks'] * 100) if distribution['total_tasks'] > 0 else 0
            bar = "█" * int(percentage / 2)
            print(f"   {diff} errors: {count:2d} tasks ({percentage:5.1f}%) {bar}")
        
        print(f"\n🌐 Language Distribution:")
        for lang, count in sorted(distribution['language_distribution'].items()):
            percentage = (count / distribution['total_tasks'] * 100) if distribution['total_tasks'] > 0 else 0
            bar = "█" * int(percentage / 2)
            print(f"   {lang:8s}: {count:2d} tasks ({percentage:5.1f}%) {bar}")
        
        print(f"\n🎯 Intervention Distribution:")
        for interv in range(4, 11):
            count = distribution['intervention_distribution'].get(interv, 0)
            if count > 0:
                percentage = (count / distribution['total_tasks'] * 100)
                bar = "█" * int(percentage / 2)
                print(f"   Level {interv}: {count:2d} tasks ({percentage:5.1f}%) {bar}")
        
        print("\n" + "="*70)
        print("GENERATING NEW TASK")
        print("="*70)
        
        prompt = self.generate_task_prompt()
        response = self.call_api(prompt)
        
        # 解析JSON响应
        try:
            json_match = re.search(r'```json\s*(.*?)\s*```', response, re.DOTALL)
            if json_match:
                json_str = json_match.group(1)
            else:
                json_str = response
            
            new_task = json.loads(json_str)
            
            # 验证任务格式
            required_fields = ["id", "metadata", "task"]
            if all(field in new_task for field in required_fields):
                self.dataset.append(new_task)
                
                with open(DATASET_PATH, 'w', encoding='utf-8') as f:
                    json.dump(self.dataset, f, indent=2, ensure_ascii=False)
                
                print(f"\n✅ NEW TASK GENERATED SUCCESSFULLY!")
                print(f"   ID: {new_task['id']}")
                print(f"   Language: {new_task['metadata']['language']}")
                print(f"   Initial Difficulty: {new_task['metadata']['difficulty']} (will be updated after AI evaluation)")
                print(f"   Intervention: {new_task['metadata']['intervention']}")
                print(f"   Description: {new_task['task']['description'][:100]}...")
                print("\n" + "="*70)
                
                return new_task
            else:
                print("❌ Generated task missing required fields")
                return None
                
        except json.JSONDecodeError as e:
            print(f"❌ Failed to parse generated task JSON: {e}")
            print(f"Raw response preview: {response[:500]}...")
            return None

    def generate_and_validate_task(self):
        """生成并验证新任务"""
        new_task = self.generate_new_task()
        
        if new_task:
            print("\n🎉 Task generation completed successfully!")
            return new_task
        else:
            print("\n⚠️ Task generation failed!")
            return None
        
if __name__ == "__main__":
    generator = TaskGenerator()
    generator.generate_and_validate_task()
~~~

### main_loop.py

```py
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

from scripts.execute_tasks import TaskExecutor
from scripts.generate_cot import CoTGenerator
from scripts.ai_evaluation import AIEvaluator
from scripts.generate_new_task import TaskGenerator

def run_execute_only():
    """只执行任务代码并生成答案"""
    print("=== Executing tasks only ===")
    executor = TaskExecutor()
    executor.execute_all_tasks()
    print("✓ Task execution completed")

def run_cot_only():
    """只生成思维链(CoT)"""
    print("=== Generating chain of thought only ===")
    cot_generator = CoTGenerator()
    cot_generator.update_dataset_with_cot()
    print("✓ CoT generation completed")

def run_evaluation_only():
    """只评估AI模型正确性"""
    print("=== Running AI evaluation only ===")
    evaluator = AIEvaluator()
    evaluator.evaluate_all_tasks()
    print("✓ AI evaluation completed")

def run_generate_task_only(num_tasks=1):
    """只生成新任务"""
    print(f"=== Generating {num_tasks} new task(s) only ===")
    
    successful_generations = 0
    task_generator = TaskGenerator()
    
    for i in range(num_tasks):
        print(f"\nGenerating task {i+1}/{num_tasks}...")
        try:
            new_task = task_generator.generate_and_validate_task()
            if new_task:
                successful_generations += 1
                print(f"✓ Task {i+1} generated successfully (ID: {new_task['id']})")
            else:
                print(f"✗ Task {i+1} generation failed")
        except Exception as e:
            print(f"✗ Task {i+1} generation failed with error: {e}")
    
    print(f"\n=== Generation Summary ===")
    print(f"Successfully generated: {successful_generations}/{num_tasks} tasks")
    return successful_generations > 0

def run_single_cycle():
    """运行一个完整的循环"""
    print("=== Starting new cycle ===")
    
    # 1. 执行任务
    print("\n1. Executing tasks...")
    executor = TaskExecutor()
    executor.execute_all_tasks()
    
    # 2. 生成思维链
    print("\n2. Generating chain of thought...")
    cot_generator = CoTGenerator()
    cot_generator.update_dataset_with_cot()
    
    # 3. AI评估
    print("\n3. Running AI evaluation...")
    evaluator = AIEvaluator()
    evaluator.evaluate_all_tasks()
    
    # 4. 生成新任务
    print("\n4. Generating new task...")
    task_generator = TaskGenerator()
    new_task = task_generator.generate_and_validate_task()
    
    print("\n=== Cycle completed ===")
    return new_task is not None

def run_multiple_cycles(num_cycles=5):
    """运行多个循环"""
    print(f"Starting {num_cycles} cycles of task generation and evaluation...")
    
    successful_cycles = 0
    for i in range(num_cycles):
        print(f"\n{'='*50}")
        print(f"CYCLE {i+1}/{num_cycles}")
        print(f"{'='*50}")
        
        try:
            success = run_single_cycle()
            if success:
                successful_cycles += 1
                print(f"✓ Cycle {i+1} completed successfully")
            else:
                print(f"✗ Cycle {i+1} failed")
        except Exception as e:
            print(f"✗ Cycle {i+1} failed with error: {e}")
    
    print(f"\n{'='*50}")
    print(f"SUMMARY: {successful_cycles}/{num_cycles} cycles completed successfully")
    print(f"{'='*50}")

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Run the complete task generation and evaluation pipeline")
    
    # 单独执行选项
    parser.add_argument("--execute", action="store_true", help="Only execute tasks and generate answers")
    parser.add_argument("--cot", action="store_true", help="Only generate chain of thought")
    parser.add_argument("--evaluate", action="store_true", help="Only run AI evaluation")
    parser.add_argument("--generate", type=int, nargs='?', const=1, help="Only generate new tasks (specify number, default=1)")
    
    # 完整流程选项
    parser.add_argument("--single", action="store_true", help="Run a single complete cycle")
    parser.add_argument("--cycles", type=int, default=1, help="Number of cycles to run")
    
    args = parser.parse_args()
    
    try:
        # 单独执行选项（互斥）
        if args.execute:
            run_execute_only()
        elif args.cot:
            run_cot_only()
        elif args.evaluate:
            run_evaluation_only()
        elif args.generate is not None:
            run_generate_task_only(args.generate)
        elif args.single:
            run_single_cycle()
        else:
            # 默认行为：运行指定数量的完整循环
            run_multiple_cycles(args.cycles)
            
    except KeyboardInterrupt:
        print("\n\n⚠️  Process interrupted by user")
    except Exception as e:
        print(f"\n\n❌ Error occurred: {e}")
        sys.exit(1)
```

## data

### answer.json

```json
{
  "SL-MIX-S001": {
    "success": true,
    "result": 2147
  },
  "SL-MIX-S002": {
    "success": true,
    "result": 2861
  },
  "SL-MIX-S003": {
    "success": true,
    "result": 56556
  },
  "SL-MIX-S004": {
    "success": true,
    "result": 181202
  },
  "SL-MIX-S005": {
    "success": true,
    "result": 52
  },
  "SL-MIX-S006": {
    "success": true,
    "result": 203
  },
```

### Statement-Level-MIX.json

```json
[
  {
    "background": "I am developing a comprehensive evaluation benchmark for large language models in the code reasoning domain. This benchmark specifically focuses on assessing statement-level reasoning capabilities of LLMs across multiple computational paradigms: (1) Arithmetic Operations - including basic arithmetic (addition, subtraction, multiplication, division), advanced mathematical operations (exponentiation, logarithms, trigonometric functions), bitwise operations (AND, OR, XOR, shift operations), and composite calculations combining multiple operation types; (2) Boolean Logic - encompassing comparison operations (equality, inequality, relational comparisons), logical operations (AND, OR, NOT), and short-circuit evaluation patterns; (3) API/Function Calls - covering built-in function invocations, mathematical library usage, string manipulation functions, and container/data structure operations; (4) Variable Assignment - including simple assignments, multiple simultaneous assignments, tuple unpacking, and destructuring assignments; (5) Complex Mixed Scenarios - integrating multiple reasoning types in sophisticated logical chains.",
    "requirements": "Generate additional examples following the provided template format with these specific criteria: (1) Create significantly more complex code samples with extended logical reasoning chains requiring multiple inference steps; (2) Ensure each example has a unique, deterministic answer that can be computed through step-by-step execution; (3) Maintain strict format consistency across all generated examples, matching the exact structure and field organization of the provided samples; (4) Incorporate diverse programming languages and paradigms while maintaining code complexity at an advanced level suitable for challenging LLM reasoning capabilities."
  },
  {
    "id": "SL-MIX-S001",
    "metadata": {
      "category": "Statement-Level",
      "language": "python",
      "difficulty": 5,
      "intervention": 7
    },
    "task": {
      "description": "Given the following complex Python code involving nested data structures, recursive calculations, bit operations, and string manipulations, what is the final value of variable target_result?",
      "code": "import hashlib\nimport itertools\nfrom functools import reduce\n\n# Constants and initial data structures\nBASE_MULTIPLIER = 17\nMOD_VALUE = 1000007\nSECRET_KEY = 0xABCDEF\ndata_matrix = [\n    [3, 7, 11, 15],\n    [19, 23, 27, 31], \n    [35, 39, 43, 47],\n    [51, 55, 59, 63]\n]\nweight_vector = [0.25, 0.35, 0.15, 0.25]\nconfiguration = {\n    'active': True,\n    'threshold': 42.5,\n    'iterations': 8,\n    'precision': 3\n}\n\n# String processing and hash calculations\ninput_string = \"DataProcessing2024\"\nhash_object = hashlib.md5(input_string.encode())\nhex_hash = hash_object.hexdigest()\nhash_numeric = int(hex_hash[:8], 16)\nreduced_hash = hash_numeric % 10000\n\n# Matrix operations with conditional logic\nflattened_data = [item for row in data_matrix for item in row]\nfiltered_data = [x for x in flattened_data if x % 4 == 3]\nsorted_filtered = sorted(filtered_data, reverse=True)\n\n# Weighted calculations\nweighted_sum = sum(w * sorted_filtered[i] for i, w in enumerate(weight_vector) if i < len(sorted_filtered))\nnormalized_weight = weighted_sum / sum(weight_vector)\n\n# Bitwise operations sequence\nbit_pattern = SECRET_KEY\nfor i in range(4):\n    bit_pattern ^= (sorted_filtered[i] << (i * 2))\n    bit_pattern &= 0xFFFFFF\n    bit_pattern |= (1 << (7 + i))\n\n# Recursive-style calculation using reduce\nrecursive_product = reduce(lambda x, y: (x * y) % MOD_VALUE, sorted_filtered[:4], 1)\npower_result = pow(recursive_product, 3, MOD_VALUE)\n\n# String manipulation and encoding\nreversed_string = input_string[::-1]\nchar_codes = [ord(c) for c in reversed_string[:8]]\nchar_sum = sum(char_codes)\nencoded_value = char_sum ^ reduced_hash\n\n# Complex conditional assignments\nis_threshold_met = normalized_weight > configuration['threshold']\nis_pattern_valid = (bit_pattern & 0xFF) > 128\nis_power_significant = power_result > 50000\n\n# Multi-level calculations\nif is_threshold_met and is_pattern_valid:\n    level_1 = encoded_value * BASE_MULTIPLIER\nelif is_power_significant:\n    level_1 = encoded_value + power_result\nelse:\n    level_1 = encoded_value // 2\n\n# Nested list comprehension with filtering\nnested_result = [\n    sum(row[i] * weight_vector[i] for i in range(len(row)))\n    for row in data_matrix\n    if sum(row) % 3 == 0\n]\n\n# Itertools operations\ncombination_sum = sum(\n    reduce(lambda x, y: x + y, combo)\n    for combo in itertools.combinations(sorted_filtered, 2)\n    if sum(combo) % 7 == 0\n)\n\n# Final aggregation with modular arithmetic\ntemp_result = (\n    level_1 +\n    (bit_pattern % 1000) +\n    (power_result % 500) +\n    len(nested_result) * 100 +\n    (combination_sum % 200) +\n    configuration['iterations'] * 15\n)\n\n# Ultimate calculation with multiple transformations\ntarget_result = (\n    (temp_result * 3) % 8192 +\n    (reduced_hash % 256) +\n    (len(char_codes) * 7) +\n    (1 if all([is_threshold_met, is_pattern_valid, is_power_significant]) else 0)\n) % 10000\n\nprint(f\"Target result: {target_result}\")",
      "answer": 2147,
      "cot": "First: Constants, matrix data, weights, and configuration are initialized alongside string input and hash-derived values.  \nSecond: Core computations involve filtering, weighted sums, bitwise operations, recursive products, and conditional logic to derive intermediate values.  \nThird: Final aggregation combines all intermediate results with modular arithmetic to produce target_result, which equals 2147."
    }
  },
  {
    "id": "SL-MIX-S002",
    "metadata": {
      "category": "Statement-Level",
      "language": "cpp",
      "difficulty": 5,
      "intervention": 8
    },
    "task": {
      "description": "Given the following comprehensive C++ code involving complex pointer arithmetic, struct manipulations, memory operations, and mathematical calculations, what is the final value of computation_result->final_output?",
      "code": "#include <iostream>\n#include <vector>\n#include <algorithm>\n#include <cmath>\n#include <string>\n#include <unordered_map>\n#include <memory>\n#include <numeric>\n#include <functional>\n#include <cstdint>\n\n#define BUFFER_SIZE 128\n#define HASH_PRIME 31\n#define MAGIC_CONST 0x9E3779B9\n#define MAX_NODES 16\n#define SCALE_FACTOR 1000\n\nstruct Node {\n    uint32_t value;\n    std::string label;\n    std::shared_ptr<Node> next;\n    double weight;\n    uint8_t flags;\n};\n\nstruct ComputationResult {\n    std::vector<Node> nodes;\n    std::vector<uint32_t> lookup_table;\n    std::string metadata;\n    std::vector<double> coefficients;\n    int active_count;\n    uint64_t checksum;\n    int final_output;\n};\n\nuint32_t custom_hash(const std::string& str, int multiplier) {\n    uint32_t hash = 5381;\n    for (char c : str) {\n        hash = ((hash << 5) + hash) + c * multiplier;\n    }\n    return hash;\n}\n\ndouble matrix_determinant_2x2(double a, double b, double c, double d) {\n    return (a * d) - (b * c);\n}\n\nint main() {\n    auto computation_result = std::make_unique<ComputationResult>();\n    \n    // Initialize lookup table\n    computation_result->lookup_table.resize(256);\n    for (int i = 0; i < 256; i++) {\n        computation_result->lookup_table[i] = (i * HASH_PRIME + MAGIC_CONST) & 0xFFFF;\n    }\n    \n    // Initialize coefficients with mathematical sequences\n    double phi = (1.0 + std::sqrt(5.0)) / 2.0;  // Golden ratio\n    computation_result->coefficients.resize(8);\n    for (int i = 0; i < 8; i++) {\n        computation_result->coefficients[i] = std::sin(i * M_PI / 4) * phi + std::cos(i * M_PI / 6);\n    }\n    \n    // Initialize nodes with complex calculations\n    std::vector<std::string> labels = {\n        \"Alpha\", \"Beta\", \"Gamma\", \"Delta\", \"Epsilon\", \"Zeta\", \"Eta\", \"Theta\",\n        \"Iota\", \"Kappa\", \"Lambda\", \"Mu\", \"Nu\", \"Xi\", \"Omicron\", \"Pi\"\n    };\n    \n    computation_result->active_count = 12;\n    uint64_t running_checksum = 0;\n    computation_result->nodes.resize(computation_result->active_count);\n    \n    for (int i = 0; i < computation_result->active_count; i++) {\n        Node& node = computation_result->nodes[i];\n        \n        // String operations and hashing\n        node.label = labels[i];\n        \n        uint32_t label_hash = custom_hash(node.label, i + 1);\n        node.value = (label_hash ^ computation_result->lookup_table[i * 16]) % 10000;\n        \n        // Weight calculation using coefficients\n        node.weight = computation_result->coefficients[i % 8] * (i + 1) * 0.1;\n        node.weight = std::round(node.weight * SCALE_FACTOR) / SCALE_FACTOR;\n        \n        // Flags with bitwise operations\n        node.flags = 0;\n        if (node.value % 2 == 0) node.flags |= 0x01;  // Even value\n        if (node.weight > 0) node.flags |= 0x02;      // Positive weight\n        if (node.label.length() > 4) node.flags |= 0x04; // Long label\n        if (i % 3 == 0) node.flags |= 0x08;            // Every 3rd node\n        \n        // Update running checksum\n        running_checksum += node.value;\n        running_checksum ^= ((uint64_t)node.flags << (i * 4));\n        running_checksum = (running_checksum << 1) | (running_checksum >> 63);\n    }\n    \n    computation_result->checksum = running_checksum;\n    \n    // Metadata string construction\n    computation_result->metadata = \"COMP_\" + std::to_string(computation_result->active_count) + \"_\" + \n                                   std::to_string((uint32_t)(computation_result->checksum & 0xFFFFFFFF));\n    \n    // Complex mathematical calculations\n    double matrix_a = computation_result->coefficients[0] + computation_result->coefficients[3];\n    double matrix_b = computation_result->coefficients[1] - computation_result->coefficients[4];\n    double matrix_c = computation_result->coefficients[2] * computation_result->coefficients[5];\n    double matrix_d = computation_result->coefficients[6] / (std::abs(computation_result->coefficients[7]) + 0.001);\n    \n    double determinant = matrix_determinant_2x2(matrix_a, matrix_b, matrix_c, matrix_d);\n    int det_contribution = (int)(std::abs(determinant) * 100) % 1000;\n    \n    // Node traversal with accumulation\n    int traversal_sum = 0;\n    int flag_accumulator = 0;\n    \n    for (const auto& node : computation_result->nodes) {\n        traversal_sum += node.value % 100;\n        flag_accumulator ^= node.flags;\n    }\n    \n    // Lookup table pattern analysis\n    int pattern_score = 0;\n    for (int i = 0; i < 16; i++) {\n        uint32_t lookup_val = computation_result->lookup_table[i * 8];\n        pattern_score += __builtin_popcount(lookup_val);  // Count set bits\n    }\n    \n    // String hash contribution\n    uint32_t metadata_hash = custom_hash(computation_result->metadata, 7);\n    int string_contrib = metadata_hash % 512;\n    \n    // Coefficient-based calculations\n    double coeff_product = 1.0;\n    for (int i = 0; i < 8; i += 2) {\n        if (std::abs(computation_result->coefficients[i]) > 1e-10) {\n            coeff_product *= computation_result->coefficients[i];\n        }\n    }\n    int coeff_contrib = (int)(std::abs(coeff_product) * 1000) % 256;\n    \n    // Memory address analysis (simplified)\n    uintptr_t addr_sum = 0;\n    for (const auto& node : computation_result->nodes) {\n        addr_sum += reinterpret_cast<uintptr_t>(&node);\n    }\n    int addr_contrib = (int)(addr_sum & 0xFF);\n    \n    // Final computation combining all elements\n    int temp_result = (\n        det_contribution +\n        traversal_sum +\n        (flag_accumulator * 10) +\n        pattern_score +\n        string_contrib +\n        coeff_contrib +\n        addr_contrib +\n        (computation_result->active_count * 25)\n    );\n    \n    // Apply checksum influence\n    temp_result ^= (int)(computation_result->checksum & 0x3FF);\n    \n    // Final modular arithmetic\n    computation_result->final_output = temp_result % 8888;\n    \n    // Print the target result\n    std::cout << \"Target result: \" << computation_result->final_output << std::endl;\n    \n    return 0;\n}",
      "answer": 2861,
      "cot": "First: The code initializes nodes, coefficients, and lookup tables using hashes, mathematical constants, and string operations with precise memory layout.  \nSecond: It computes contributions from determinants, flag patterns, metadata hashes, and memory addresses, combining them through bitwise and modular arithmetic.  \nThird: The final output is derived by applying checksum-based XOR and modulo operations, yielding 2861 as the result."
    }
  },
  {
    "id": "SL-MIX-S003",
    "metadata": {
      "category": "Statement-Level",
      "language": "python",
      "difficulty": 5,
      "intervention": 9
    },
    "task": {
      "description": "Given the following sophisticated Python code involving metaclasses, decorators, context managers, async operations simulation, and complex data transformations, what is the final value of orchestrator.get_final_computation()?",
      "code": "import asyncio\nimport functools\nimport itertools\nfrom collections import defaultdict, deque\nfrom dataclasses import dataclass\nfrom typing import Any, Dict, List, Callable\nimport threading\nimport time\nimport operator\n\n# Metaclass for tracking class creation\nclass TrackedMeta(type):\n    creation_order = 0\n    \n    def __new__(cls, name, bases, namespace):\n        TrackedMeta.creation_order += 1\n        namespace['_creation_id'] = TrackedMeta.creation_order\n        return super().__new__(cls, name, bases, namespace)\n\n# Decorator for method enhancement\ndef enhance_computation(multiplier: float):\n    def decorator(func: Callable) -> Callable:\n        @functools.wraps(func)\n        def wrapper(*args, **kwargs):\n            result = func(*args, **kwargs)\n            if isinstance(result, (int, float)):\n                return result * multiplier\n            return result\n        wrapper._multiplier = multiplier\n        return wrapper\n    return decorator\n\n# Context manager for computation tracking\nclass ComputationTracker:\n    def __init__(self):\n        self.operations = []\n        self.start_time = None\n        \n    def __enter__(self):\n        self.start_time = time.time()\n        return self\n        \n    def __exit__(self, exc_type, exc_val, exc_tb):\n        duration = time.time() - self.start_time\n        self.operations.append(('duration', int(duration * 1000000) % 1000))\n        \n    def log_operation(self, name: str, value: Any):\n        self.operations.append((name, value))\n\n@dataclass\nclass DataNode:\n    value: float\n    category: str\n    priority: int = 0\n    metadata: Dict[str, Any] = None\n    \n    def __post_init__(self):\n        if self.metadata is None:\n            self.metadata = {}\n            \n    def transform(self, func: Callable[[float], float]) -> 'DataNode':\n        return DataNode(\n            value=func(self.value),\n            category=self.category,\n            priority=self.priority,\n            metadata=self.metadata.copy()\n        )\n\nclass ProcessingEngine(metaclass=TrackedMeta):\n    def __init__(self, name: str):\n        self.name = name\n        self.buffer = deque(maxlen=100)\n        self.state = defaultdict(int)\n        self.processors = []\n        \n    @enhance_computation(1.618)  # Golden ratio multiplier\n    def fibonacci_transform(self, n: int) -> int:\n        if n <= 1:\n            return n\n        a, b = 0, 1\n        for _ in range(2, n + 1):\n            a, b = b, a + b\n        return b % 10000\n    \n    @enhance_computation(2.718)  # Euler's number multiplier\n    def prime_sieve_count(self, limit: int) -> int:\n        if limit < 2:\n            return 0\n        sieve = [True] * (limit + 1)\n        sieve[0] = sieve[1] = False\n        \n        for i in range(2, int(limit**0.5) + 1):\n            if sieve[i]:\n                for j in range(i*i, limit + 1, i):\n                    sieve[j] = False\n        \n        return sum(sieve)\n    \n    def add_processor(self, func: Callable):\n        self.processors.append(func)\n        \n    def process_batch(self, data_nodes: List[DataNode]) -> Dict[str, float]:\n        results = defaultdict(list)\n        \n        for node in data_nodes:\n            # Apply all processors\n            processed_value = node.value\n            for processor in self.processors:\n                processed_value = processor(processed_value)\n            \n            results[node.category].append(processed_value)\n            self.buffer.append(processed_value)\n            \n        # Aggregate by category\n        aggregated = {}\n        for category, values in results.items():\n            aggregated[category] = sum(values) / len(values) if values else 0.0\n            \n        return aggregated\n\nclass DataOrchestrator:\n    def __init__(self):\n        self.engines = {}\n        self.global_state = {}\n        self.computation_history = []\n        self.thread_results = {}\n        \n    def add_engine(self, name: str, engine: ProcessingEngine):\n        self.engines[name] = engine\n        \n    def simulate_async_operation(self, data: List[float], operation_id: int) -> float:\n        \"\"\"Simulate async operation without actual async/await\"\"\"\n        # Simulate some complex computation\n        result = 0.0\n        for i, value in enumerate(data):\n            result += value * (i + 1) ** 0.5\n            result = (result * 1.414213562) % 100000  # Multiply by sqrt(2)\n            \n        # Simulate thread-specific computation\n        thread_factor = (operation_id * 31 + 17) % 1000\n        self.thread_results[operation_id] = result + thread_factor\n        return result + thread_factor\n        \n    def complex_pipeline(self) -> int:\n        with ComputationTracker() as tracker:\n            # Initialize data\n            raw_data = [\n                DataNode(12.5, \"alpha\", 1, {\"source\": \"sensor_1\"}),\n                DataNode(23.7, \"beta\", 2, {\"source\": \"sensor_2\"}),\n                DataNode(8.9, \"alpha\", 3, {\"source\": \"sensor_3\"}),\n                DataNode(15.3, \"gamma\", 1, {\"source\": \"sensor_4\"}),\n                DataNode(31.2, \"beta\", 4, {\"source\": \"sensor_5\"}),\n                DataNode(19.8, \"gamma\", 2, {\"source\": \"sensor_6\"}),\n                DataNode(27.1, \"alpha\", 5, {\"source\": \"sensor_7\"}),\n                DataNode(42.6, \"delta\", 3, {\"source\": \"sensor_8\"})\n            ]\n            \n            # Create and configure engines\n            engine_a = ProcessingEngine(\"EngineA\")\n            engine_b = ProcessingEngine(\"EngineB\")\n            \n            # Add processors with lambda functions\n            engine_a.add_processor(lambda x: x * 1.1 + 5)\n            engine_a.add_processor(lambda x: x ** 1.2)\n            engine_b.add_processor(lambda x: x / 1.3 - 2)\n            engine_b.add_processor(lambda x: abs(x) * 0.9)\n            \n            self.add_engine(\"A\", engine_a)\n            self.add_engine(\"B\", engine_b)\n            \n            tracker.log_operation(\"engines_created\", len(self.engines))\n            \n            # Process data through different engines\n            alpha_beta_data = [node for node in raw_data if node.category in [\"alpha\", \"beta\"]]\n            gamma_delta_data = [node for node in raw_data if node.category in [\"gamma\", \"delta\"]]\n            \n            results_a = engine_a.process_batch(alpha_beta_data)\n            results_b = engine_b.process_batch(gamma_delta_data)\n            \n            tracker.log_operation(\"batch_processed\", len(results_a) + len(results_b))\n            \n            # Fibonacci and prime calculations\n            fib_results = []\n            for i in range(8, 15):\n                fib_val = engine_a.fibonacci_transform(i)\n                fib_results.append(fib_val)\n                \n            prime_results = []\n            for limit in [10, 20, 30, 50]:\n                prime_count = engine_b.prime_sieve_count(limit)\n                prime_results.append(prime_count)\n                \n            tracker.log_operation(\"math_operations\", len(fib_results) + len(prime_results))\n            \n            # Simulate concurrent operations\n            async_data_sets = [\n                [1.1, 2.2, 3.3, 4.4, 5.5],\n                [6.6, 7.7, 8.8, 9.9, 10.1],\n                [11.2, 12.3, 13.4, 14.5, 15.6]\n            ]\n            \n            async_results = []\n            for i, data_set in enumerate(async_data_sets):\n                result = self.simulate_async_operation(data_set, i)\n                async_results.append(result)\n                \n            tracker.log_operation(\"async_operations\", len(async_results))\n            \n            # Complex aggregations\n            all_category_results = {**results_a, **results_b}\n            category_sum = sum(all_category_results.values())\n            \n            fib_sum = sum(fib_results)\n            prime_sum = sum(prime_results)\n            async_sum = sum(async_results)\n            \n            # Matrix-like operations using itertools\n            combinations = list(itertools.combinations(fib_results[:5], 2))\n            combination_products = [a * b for a, b in combinations]\n            max_combination = max(combination_products) if combination_products else 0\n            \n            # Permutation-based calculations\n            small_primes = [2, 3, 5, 7]\n            permutations = list(itertools.permutations(small_primes, 3))\n            perm_sums = [sum(perm) for perm in permutations]\n            unique_perm_sums = len(set(perm_sums))\n            \n            tracker.log_operation(\"combinatorial_ops\", len(combinations) + len(permutations))\n            \n            # Thread results aggregation\n            thread_total = sum(self.thread_results.values()) if self.thread_results else 0\n            \n            # Creation ID influence\n            creation_influence = engine_a._creation_id * engine_b._creation_id\n            \n            # Buffer analysis\n            buffer_contents_a = list(engine_a.buffer)\n            buffer_contents_b = list(engine_b.buffer)\n            buffer_variance = 0\n            if buffer_contents_a:\n                mean_a = sum(buffer_contents_a) / len(buffer_contents_a)\n                buffer_variance += sum((x - mean_a) ** 2 for x in buffer_contents_a)\n            if buffer_contents_b:\n                mean_b = sum(buffer_contents_b) / len(buffer_contents_b)\n                buffer_variance += sum((x - mean_b) ** 2 for x in buffer_contents_b)\n                \n            # Final computation\n            final_value = (\n                int(category_sum * 100) +\n                fib_sum +\n                prime_sum +\n                int(async_sum) +\n                max_combination +\n                unique_perm_sums * 1000 +\n                int(thread_total) % 10000 +\n                creation_influence +\n                int(buffer_variance) % 1000 +\n                sum(op[1] for op in tracker.operations if isinstance(op[1], int))\n            ) % 100000\n            \n            tracker.log_operation(\"final_computation\", final_value)\n            self.computation_history.append(final_value)\n            \n            return final_value\n    \n    def get_final_computation(self) -> int:\n        return self.complex_pipeline()\n\n# Main execution\norchestrator = DataOrchestrator()\nresult = orchestrator.get_final_computation()\nprint(f\"Final computation result: {result}\")",
      "answer": 56556,
      "cot": "First: The code initializes data nodes, processing engines, and trackers for managing complex data transformations and computations.  \nSecond: It processes data through multiple stages including batch processing, mathematical calculations, async simulations, and combinatorial operations with thread-safe tracking.  \nThird: The final value of orchestrator.get_final_computation() is computed as 56556 after aggregating all results and applying modular arithmetic."
    }
  },
  {
    "id": "SL-MIX-S004",
    "metadata": {
      "category": "Statement-Level",
      "language": "c",
      "difficulty": 5,
      "intervention": 10
    },
    "task": {
      "description": "Given the following extremely complex C code involving advanced memory management, function pointers, unions, volatile variables, inline assembly simulation, and sophisticated bit manipulation, what is the final value of system_state->master_result?",
      "code": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n#include <stdint.h>\n#include <math.h>\n#include <time.h>\n#include <assert.h>\n\n#define QUANTUM_SIZE 64\n#define HASH_TABLE_SIZE 256\n#define MAGIC_PRIME 2147483647\n#define CRYPTO_ROUNDS 16\n#define MATRIX_DIM 8\n#define MAX_RECURSION 12\n\n// Portable popcount implementation\nint popcount64(uint64_t x)\n{\n    int count = 0;\n    while (x)\n    {\n        count += x & 1;\n        x >>= 1;\n    }\n    return count;\n}\n\n// Union for type punning and bit manipulation\ntypedef union\n{\n    uint64_t u64;\n    uint32_t u32[2];\n    uint16_t u16[4];\n    uint8_t u8[8];\n    double f64;\n    float f32[2];\n} DataWord;\n\n// Forward declaration\ntypedef struct QuantumNode QuantumNode;\n\n// Complex structure with bit fields\nstruct QuantumNode\n{\n    uint32_t timestamp : 20;\n    uint32_t priority : 4;\n    uint32_t flags : 8;\n    volatile uint32_t counter;\n    DataWord payload;\n    QuantumNode *next;\n    QuantumNode *prev;\n};\n\n// Function pointer types\ntypedef uint32_t (*HashFunction)(const void *data, size_t len);\ntypedef double (*TransformFunction)(double input, int iteration);\ntypedef void (*ProcessorFunction)(QuantumNode *node, void *context);\n\n// Main system state\ntypedef struct\n{\n    QuantumNode *quantum_ring[QUANTUM_SIZE];\n    uint32_t hash_table[HASH_TABLE_SIZE];\n    double transformation_matrix[MATRIX_DIM][MATRIX_DIM];\n    HashFunction active_hasher;\n    TransformFunction transformer;\n    ProcessorFunction processor;\n    volatile uint64_t cycle_counter;\n    DataWord accumulator;\n    uint32_t encryption_key[4];\n    int64_t master_result;\n} SystemState;\n\n// Custom hash implementations\nuint32_t polynomial_hash(const void *data, size_t len)\n{\n    const uint8_t *bytes = (const uint8_t *)data;\n    uint32_t hash = 0x811C9DC5; // FNV offset basis\n    for (size_t i = 0; i < len; i++)\n    {\n        hash ^= bytes[i];\n        hash *= 0x01000193; // FNV prime\n    }\n    return hash;\n}\n\nuint32_t jenkins_hash(const void *data, size_t len)\n{\n    const uint8_t *bytes = (const uint8_t *)data;\n    uint32_t hash = 0;\n    for (size_t i = 0; i < len; i++)\n    {\n        hash += bytes[i];\n        hash += (hash << 10);\n        hash ^= (hash >> 6);\n    }\n    hash += (hash << 3);\n    hash ^= (hash >> 11);\n    hash += (hash << 15);\n    return hash;\n}\n\nuint32_t djb2_hash(const void *data, size_t len)\n{\n    const uint8_t *bytes = (const uint8_t *)data;\n    uint32_t hash = 5381;\n    for (size_t i = 0; i < len; i++)\n    {\n        hash = ((hash << 5) + hash) + bytes[i];\n    }\n    return hash;\n}\n\n// Transformation functions\ndouble sine_transform(double input, int iteration)\n{\n    return sin(input + iteration * M_PI / 8) * (iteration + 1);\n}\n\ndouble exponential_transform(double input, int iteration)\n{\n    return exp(input / (iteration + 1)) * log(fabs(input) + 1);\n}\n\ndouble fibonacci_transform(double input, int iteration)\n{\n    if (iteration <= 1)\n        return input;\n    double a = 1, b = 1;\n    for (int i = 2; i <= iteration; i++)\n    {\n        double temp = a + b;\n        a = b;\n        b = temp;\n    }\n    return input * b / (b + 1);\n}\n\n// Simulated inline assembly operations (portable implementation)\nuint32_t rotleft32(uint32_t value, int shift)\n{\n    shift %= 32;\n    return (value << shift) | (value >> (32 - shift));\n}\n\nuint32_t rotright32(uint32_t value, int shift)\n{\n    shift %= 32;\n    return (value >> shift) | (value << (32 - shift));\n}\n\nuint64_t multiply_high64(uint64_t a, uint64_t b)\n{\n    // Simulate 64-bit multiply with high bits\n    uint64_t a_low = a & 0xFFFFFFFF;\n    uint64_t a_high = a >> 32;\n    uint64_t b_low = b & 0xFFFFFFFF;\n    uint64_t b_high = b >> 32;\n\n    uint64_t cross1 = a_low * b_high;\n    uint64_t cross2 = a_high * b_low;\n    uint64_t high = a_high * b_high;\n\n    uint64_t middle = cross1 + cross2;\n    return high + (middle >> 32) + ((a_low * b_low) >> 32) + (middle < cross1 ? (1ULL << 32) : 0);\n}\n\n// Encryption/Decryption (simplified AES-like)\nvoid encrypt_block(uint32_t *data, const uint32_t *key)\n{\n    for (int round = 0; round < CRYPTO_ROUNDS; round++)\n    {\n        for (int i = 0; i < 4; i++)\n        {\n            data[i] ^= key[i];\n            data[i] = rotleft32(data[i], 5 + i);\n            data[i] += (data[(i + 1) % 4] ^ data[(i + 3) % 4]);\n        }\n    }\n}\n\nvoid decrypt_block(uint32_t *data, const uint32_t *key)\n{\n    for (int round = 0; round < CRYPTO_ROUNDS; round++)\n    {\n        for (int i = 3; i >= 0; i--)\n        {\n            data[i] -= (data[(i + 1) % 4] ^ data[(i + 3) % 4]);\n            data[i] = rotright32(data[i], 5 + i);\n            data[i] ^= key[i];\n        }\n    }\n}\n\n// Matrix operations\nvoid matrix_multiply(double result[MATRIX_DIM][MATRIX_DIM],\n                     const double a[MATRIX_DIM][MATRIX_DIM],\n                     const double b[MATRIX_DIM][MATRIX_DIM])\n{\n    for (int i = 0; i < MATRIX_DIM; i++)\n    {\n        for (int j = 0; j < MATRIX_DIM; j++)\n        {\n            result[i][j] = 0.0;\n            for (int k = 0; k < MATRIX_DIM; k++)\n            {\n                result[i][j] += a[i][k] * b[k][j];\n            }\n        }\n    }\n}\n\ndouble matrix_determinant_recursive(double matrix[MATRIX_DIM][MATRIX_DIM], int n)\n{\n    if (n == 1)\n        return matrix[0][0];\n    if (n == 2)\n        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0];\n\n    double det = 0.0;\n    double temp[MATRIX_DIM][MATRIX_DIM];\n    int sign = 1;\n\n    for (int f = 0; f < n; f++)\n    {\n        int sub_i = 0;\n        for (int i = 1; i < n; i++)\n        {\n            int sub_j = 0;\n            for (int j = 0; j < n; j++)\n            {\n                if (j != f)\n                {\n                    temp[sub_i][sub_j] = matrix[i][j];\n                    sub_j++;\n                }\n            }\n            sub_i++;\n        }\n        det += sign * matrix[0][f] * matrix_determinant_recursive(temp, n - 1);\n        sign = -sign;\n    }\n    return det;\n}\n\n// Processor functions\nvoid quantum_processor(QuantumNode *node, void *context)\n{\n    SystemState *state = (SystemState *)context;\n\n    // Quantum-inspired bit manipulation\n    node->payload.u64 ^= state->cycle_counter;\n    node->payload.u64 = rotleft32(node->payload.u32[0], 7) |\n                        ((uint64_t)rotright32(node->payload.u32[1], 13) << 32);\n\n    // Update volatile counter atomically (simulated)\n    node->counter += (uint32_t)(state->cycle_counter & 0xFFFF);\n\n    // Modify accumulator\n    state->accumulator.f64 += sin(node->payload.f64) * cos(node->counter * M_PI / 1000);\n}\n\nvoid crypto_processor(QuantumNode *node, void *context)\n{\n    SystemState *state = (SystemState *)context;\n\n    uint32_t data_block[4] = {\n        node->payload.u32[0],\n        node->payload.u32[1],\n        node->counter,\n        (uint32_t)state->cycle_counter};\n\n    encrypt_block(data_block, state->encryption_key);\n\n    node->payload.u32[0] = data_block[0];\n    node->payload.u32[1] = data_block[1];\n\n    // Hash the encrypted data\n    uint32_t hash = state->active_hasher(data_block, sizeof(data_block));\n    state->hash_table[hash % HASH_TABLE_SIZE] ^= hash;\n}\n\nvoid transform_processor(QuantumNode *node, void *context)\n{\n    SystemState *state = (SystemState *)context;\n\n    // Apply transformation function\n    double transformed = state->transformer(node->payload.f64, node->counter % MAX_RECURSION);\n\n    // Store back with type punning\n    node->payload.f64 = transformed;\n\n    // Update matrix\n    int row = node->counter % MATRIX_DIM;\n    int col = (node->counter / MATRIX_DIM) % MATRIX_DIM;\n    state->transformation_matrix[row][col] += transformed * 0.001;\n}\n\nint main()\n{\n    SystemState *system_state = (SystemState *)calloc(1, sizeof(SystemState));\n    if (!system_state)\n        return -1;\n\n    // Initialize encryption key\n    system_state->encryption_key[0] = 0xDEADBEEF;\n    system_state->encryption_key[1] = 0xCAFEBABE;\n    system_state->encryption_key[2] = 0x12345678;\n    system_state->encryption_key[3] = 0x9ABCDEF0;\n\n    // Initialize hash functions array\n    HashFunction hashers[] = {polynomial_hash, jenkins_hash, djb2_hash};\n    TransformFunction transformers[] = {sine_transform, exponential_transform, fibonacci_transform};\n    ProcessorFunction processors[] = {quantum_processor, crypto_processor, transform_processor};\n\n    // Initialize transformation matrix with mathematical constants\n    for (int i = 0; i < MATRIX_DIM; i++)\n    {\n        for (int j = 0; j < MATRIX_DIM; j++)\n        {\n            system_state->transformation_matrix[i][j] = sin(i * M_PI / 4) * cos(j * M_PI / 6) +\n                                                        (i + j) * 0.1;\n        }\n    }\n\n    // Create quantum ring with complex initialization\n    for (int i = 0; i < QUANTUM_SIZE; i++)\n    {\n        QuantumNode *node = (QuantumNode *)malloc(sizeof(QuantumNode));\n        if (!node)\n            continue;\n\n        node->timestamp = (uint32_t)time(NULL) & 0xFFFFF;\n        node->priority = i % 16;\n        node->flags = (i * 7 + 13) & 0xFF;\n        node->counter = i * 17 + 23;\n\n        // Initialize payload with mathematical sequence\n        node->payload.f64 = sin(i * M_PI / 16) * exp(i * 0.1) +\n                            cos(i * M_E / 8) * log(i + 1);\n\n        // Link in ring\n        system_state->quantum_ring[i] = node;\n        node->next = system_state->quantum_ring[(i + 1) % QUANTUM_SIZE];\n        node->prev = system_state->quantum_ring[(i - 1 + QUANTUM_SIZE) % QUANTUM_SIZE];\n    }\n\n    // Fix ring linkage\n    for (int i = 0; i < QUANTUM_SIZE; i++)\n    {\n        if (system_state->quantum_ring[i])\n        {\n            system_state->quantum_ring[i]->next =\n                system_state->quantum_ring[(i + 1) % QUANTUM_SIZE];\n            system_state->quantum_ring[i]->prev =\n                system_state->quantum_ring[(i - 1 + QUANTUM_SIZE) % QUANTUM_SIZE];\n        }\n    }\n\n    // Initialize hash table with prime-based pattern\n    for (int i = 0; i < HASH_TABLE_SIZE; i++)\n    {\n        system_state->hash_table[i] = (i * 31 + 17) ^ (i * i * 7);\n    }\n\n    // Main processing loop with multiple phases\n    for (int phase = 0; phase < 3; phase++)\n    {\n        system_state->active_hasher = hashers[phase];\n        system_state->transformer = transformers[phase];\n        system_state->processor = processors[phase];\n\n        for (int cycle = 0; cycle < 16; cycle++)\n        {\n            system_state->cycle_counter++;\n\n            // Process each node in quantum ring\n            for (int i = 0; i < QUANTUM_SIZE; i++)\n            {\n                if (system_state->quantum_ring[i])\n                {\n                    system_state->processor(system_state->quantum_ring[i], system_state);\n                }\n            }\n\n            // Inter-phase hash table evolution\n            for (int i = 0; i < HASH_TABLE_SIZE; i += 4)\n            {\n                uint32_t temp = system_state->hash_table[i];\n                system_state->hash_table[i] =\n                    rotleft32(system_state->hash_table[i] ^\n                                  system_state->hash_table[(i + 1) % HASH_TABLE_SIZE],\n                              11);\n                system_state->hash_table[(i + 1) % HASH_TABLE_SIZE] = temp;\n            }\n        }\n    }\n\n    // Final computation combining all elements\n\n    // 1. Hash table contribution\n    uint64_t hash_contribution = 0;\n    for (int i = 0; i < HASH_TABLE_SIZE; i++)\n    {\n        hash_contribution += system_state->hash_table[i];\n    }\n    hash_contribution %= 1000000;\n\n    // 2. Quantum ring payload sum\n    double payload_sum = 0.0;\n    uint64_t counter_sum = 0;\n    for (int i = 0; i < QUANTUM_SIZE; i++)\n    {\n        if (system_state->quantum_ring[i])\n        {\n            payload_sum += system_state->quantum_ring[i]->payload.f64;\n            counter_sum += system_state->quantum_ring[i]->counter;\n        }\n    }\n\n    // 3. Matrix determinant\n    double determinant = matrix_determinant_recursive(system_state->transformation_matrix, MATRIX_DIM);\n\n    // 4. Accumulator analysis - using portable popcount\n    uint64_t accumulator_bits = system_state->accumulator.u64;\n    int popcount = popcount64(accumulator_bits);\n\n    // 5. Encryption key entropy\n    uint32_t key_xor = system_state->encryption_key[0] ^\n                       system_state->encryption_key[1] ^\n                       system_state->encryption_key[2] ^\n                       system_state->encryption_key[3];\n\n    // 6. Cycle counter contribution\n    uint64_t cycle_contribution = multiply_high64(system_state->cycle_counter, MAGIC_PRIME);\n\n    // Final master result calculation\n    int64_t master_result =\n        (int64_t)hash_contribution +\n        (int64_t)(fabs(payload_sum) * 1000) % 500000 +\n        (int64_t)(counter_sum % 100000) +\n        (int64_t)(fabs(determinant) * 100) % 50000 +\n        popcount * 10000 +\n        key_xor % 25000 +\n        (int64_t)(cycle_contribution % 75000);\n\n    system_state->master_result = master_result % 9999999;\n\n    printf(\"Master result: %ld\\n\", system_state->master_result);\n\n    // Cleanup\n    for (int i = 0; i < QUANTUM_SIZE; i++)\n    {\n        if (system_state->quantum_ring[i])\n        {\n            free(system_state->quantum_ring[i]);\n        }\n    }\n\n    int64_t result = system_state->master_result;\n    free(system_state);\n\n    return (int)result;\n}",
      "answer": 181202,
      "cot": "First: The system initializes quantum nodes, hash tables, encryption keys, and transformation matrices with mathematical and cryptographic values.  \nSecond: Three processing phases apply quantum, crypto, and transform operations, updating state variables across multiple cycles.  \nThird: Final result combines hash, payload, matrix, and cycle data, yielding master_result = 181202."
    }
  },
```

## config.py

```py
import os

# 文件路径配置
DATASET_PATH = "data/Statement-Level-MIX.json"
ANSWER_PATH = "data/answer.json"
TEMP_CODE_DIR = "temp_code"

# API配置
API_KEY = "sk-tT9Ddv4cOCl5BXW4kivhRQ"

# 请根据你的实际API提供商调整
BASE_URL = "https://llmapi.paratera.com/v1"

# 选择5个不同的模型进行评估
AI_APIS = {
    "qwen3_235b": {
        "base_url": BASE_URL,
        "api_key": API_KEY,
        "model": "Qwen3-235B-A22B-Instruct-2507"
    },
    "qwen3_coder": {
        "base_url": BASE_URL,
        "api_key": API_KEY,
        "model": "Qwen3-Coder-480B-A35B-Instruct"
    },
    "minimax_text": {
        "base_url": BASE_URL,
        "api_key": API_KEY,
        "model": "MiniMax-Text-01"
    },
    "glm4_plus": {
        "base_url": BASE_URL,
        "api_key": API_KEY,
        "model": "GLM-4-Plus"
    },
    "deepseek_v3": {
        "base_url": BASE_URL,
        "api_key": API_KEY,
        "model": "DeepSeek-V3-250324"
    }
}

# 确保目录存在
os.makedirs(TEMP_CODE_DIR, exist_ok=True)
os.makedirs("data", exist_ok=True)
```

## requirements.txt

```txt
openai>=1.0.0
```

## test_api.py

```py
import openai
from config import AI_APIS

def test_all_apis():
    """测试所有API连接"""
    for api_name, api_config in AI_APIS.items():
        print(f"\nTesting {api_name} ({api_config['model']})...")
        
        client = openai.OpenAI(
            api_key=api_config['api_key'],
            base_url=api_config['base_url']
        )
        
        try:
            response = client.chat.completions.create(
                model=api_config['model'],
                messages=[{"role": "user", "content": "Hello, can you respond with just the number 42?"}],
                max_tokens=10
            )
            
            result = response.choices[0].message.content
            print(f"✓ {api_name}: {result}")
            
        except Exception as e:
            print(f"✗ {api_name}: Error - {str(e)}")

if __name__ == "__main__":
    test_all_apis()
```

