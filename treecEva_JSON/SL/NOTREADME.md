# 代码推理训练集生成框架

## 任务背景

这里是一个基于AI muti-agent 框架生成代码推理训练集的系统。

目前有四大agent：

- Agent1：execute_tasks 根据目前数据集，转换成可运行的代码并记录问题对应位置的运行结果
- Agent2：generate_cot 根据单个case生成对应的cot
- Agent3：ai_evaluation 调用五个ai的API，预测对应case的答案，根据错误ai数目更新难度
- Agent4：generate_new_task 根据给出的背景和需求和已有数据集，并且根据已有数据集情况，均衡难度和提升多样性，扩展数据集

## 工作结构

```cmd
工作目录/
├── scripts/
│   ├── data/
│   │   ├── Statement-Level-MIX.json
│   │   └── answer.json 
│   │   └── ai_evaluation_with_difficulty.json
│   ├── temp_code/
│   ├── execute_tasks.py
│   ├── generate_cot.py
│   ├── ai_evaluation.py
│   ├── generate_new_task.py
│   └── main_loop.py
├── requirements.txt
├── web_interface.html
├── web_server.py
├── requirements.txt
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
    
    # (已删除) execute_cpp_code 方法
    # (已删除) execute_c_code 方法
    
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
        """执行单个任务 (已修改为仅限Python)"""
        task_id = task_data["id"]
        language = task_data["metadata"]["language"]
        code = task_data["task"]["code"]
        
        print(f"Executing task {task_id} ({language})...")
        
        if language == "python":
            result = self.execute_python_code(code, task_id)
        else:
            # (已修改) 对于非Python任务，直接跳过并报告
            print(f"  Skipping task {task_id}: Unsupported language ({language})")
            result = {
                "success": False,
                "error": f"Unsupported language (Python-only framework): {language}"
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
                    # 只有在任务是Python但执行失败时才打印错误
                    if task.get("metadata", {}).get("language") == "python":
                        print(f"✗ Task {task['id']}: Execution failed - {result.get('error', 'Unknown error')}")
                    # 非Python任务的跳过信息已在 execute_task 中打印
        
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
        """智能选择语言和特征组合 (已修改为仅限Python)"""
        
        # (已修改) 硬编码为 "python"
        selected_language = "python"
        
        # (已修改) 只保留 Python 的特征池
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
        constraints.append(f"- FOCUS on {selected_language}-specific idioms and best practices") # selected_language 将始终是 python
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
        
        # (已修改) 智能选择语言和特征 (现在只会返回Python)
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

                Fix all compilation/runtime errors The code has a clear variable value that can be queried at a key execution point This variable value should be a unique, deterministic number The code should print this variable value at the end, format: "Target result: {{variable_value}}" Maintain similar complexity level Please return the fixed task in JSON format:
                ```{{
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
        print("GENERATING NEW TASK (Python-only)")
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

### ai_evaluation_with_difficulty.json

```
{
  "evaluation_summary": {
    "difficulty_distribution": {
      "difficulty_0_(errors)": "0 tasks",
      "difficulty_1_(errors)": "2 tasks",
      "difficulty_2_(errors)": "2 tasks",
      "difficulty_3_(errors)": "0 tasks",
      "difficulty_4_(errors)": "0 tasks",
      "difficulty_5_(errors)": "6 tasks"
    },
    "overall_ai_accuracy": {
      "qwen3_235b": "3/10 (30.0%)",
      "qwen3_coder": "4/10 (40.0%)",
      "minimax_text": "1/10 (10.0%)",
      "glm4_plus": "3/10 (30.0%)",
      "deepseek_v3": "3/10 (30.0%)"
    },
    "total_tasks_evaluated": 10
  },
  "task_details": {
    "SL-MIX-S001": "SL-MIX-S001：难度：5 ai评估记录：0 0 0 0 0",
    "SL-MIX-S002": "SL-MIX-S002：难度：5 ai评估记录：0 0 0 0 0",
    "SL-MIX-S003": "SL-MIX-S003：难度：5 ai评估记录：0 0 0 0 0",
    "SL-MIX-S004": "SL-MIX-S004：难度：5 ai评估记录：0 0 0 0 0",
    "SL-MIX-S005": "SL-MIX-S005：难度：2 ai评估记录：1 1 0 1 0",
    "SL-MIX-S006": "SL-MIX-S006：难度：5 ai评估记录：0 0 0 0 0",
    "SL-MIX-S007": "SL-MIX-S007：难度：1 ai评估记录：1 1 0 1 1",
    "SL-MIX-S008": "SL-MIX-S008：难度：5 ai评估记录：0 0 0 0 0",
    "SL-MIX-S009": "SL-MIX-S009：难度：1 ai评估记录：1 1 1 0 1",
    "SL-MIX-S010": "SL-MIX-S010：难度：2 ai评估记录：0 1 0 1 1"
  }
}
```

### answer.json

```json
{
  "SL-MIX-S001": {
    "success": true,
    "result": 2147
  },
  "SL-MIX-S002": {
    "success": true,
    "result": 56556
  },
  "SL-MIX-S003": {
    "success": true,
    "result": 97
  },
  "SL-MIX-S004": {
    "success": true,
    "result": 51563
  },
  "SL-MIX-S005": {
    "success": true,
    "result": 7
  },
  "SL-MIX-S006": {
    "success": true,
    "result": 5
  },
  "SL-MIX-S007": {
    "success": true,
    "result": 6
  },
  "SL-MIX-S008": {
    "success": true,
    "result": 8
  },
  "SL-MIX-S009": {
    "success": true,
    "result": 25
  },
  "SL-MIX-S010": {
    "success": true,
    "result": 7
  }
}
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
      "cot": ""
    }
  },
  {
    "id": "SL-MIX-S002",
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
      "cot": ""
    }
  },
  {
    "id": "SL-MIX-S003",
    "metadata": {
      "category": "Statement-Level",
      "language": "python",
      "difficulty": 5,
      "intervention": 8
    },
    "task": {
      "description": "A cryptography research team is implementing a custom checksum algorithm for validating secure message blocks. The algorithm processes a sequence of integers using a divide-and-conquer approach on a linked list structure. Each node's value is transformed through a series of logical operations and set operations. At a critical validation point, a context manager tracks the intermediate results. What is the value of the variable 'checksum_result' after processing all nodes?",
      "code": "class ListNode:\n    def __init__(self, val=0, next=None):\n        self.val = val\n        self.next = next\n\nclass ChecksumTracker:\n    def __init__(self):\n        self.intermediates = []\n    \n    def __enter__(self):\n        return self\n    \n    def __exit__(self, exc_type, exc_val, exc_tb):\n        pass\n    \n    def record(self, value):\n        self.intermediates.append(value)\n\ndef build_linked_list(values):\n    if not values:\n        return None\n    head = ListNode(values[0])\n    current = head\n    for val in values[1:]:\n        current.next = ListNode(val)\n        current = current.next\n    return head\n\ndef divide_and_process(node, tracker):\n    if not node:\n        return frozenset()\n    \n    if not node.next:  # Base case: single node\n        # Transform node value using logical operations\n        transformed = (node.val & 0xF) | ((node.val >> 4) & 0xF) if node.val > 0 else node.val\n        tracker.record(transformed)\n        return frozenset([transformed])\n    \n    # Divide the list\n    slow = fast = node\n    prev = None\n    while fast and fast.next:\n        prev = slow\n        slow = slow.next\n        fast = fast.next.next\n    \n    # Split into two halves\n    prev.next = None\n    \n    # Conquer: process both halves\n    left_set = divide_and_process(node, tracker)\n    right_set = divide_and_process(slow, tracker)\n    \n    # Combine results with set operations\n    combined = left_set.union(right_set)\n    \n    # Apply checksum logic: XOR all elements, then apply mask\n    xor_result = 0\n    for item in combined:\n        xor_result ^= item\n    \n    masked = xor_result & 0xFF\n    tracker.record(masked)\n    return frozenset([masked])\n\n# Main execution\nmessage_blocks = [0x1A, 0x2B, 0x3C, 0x4D, 0x5E]\nhead = build_linked_list(message_blocks)\n\nwith ChecksumTracker() as tracker:\n    result_set = divide_and_process(head, tracker)\n    # Final checksum calculation\n    checksum_result = sum(tracker.intermediates) % 256\n\nprint(f\"Result: {checksum_result}\")",
      "answer": 97,
      "cot": ""
    }
  },
  {
    "id": "SL-MIX-S004",
    "metadata": {
      "category": "Statement-Level",
      "language": "python",
      "difficulty": 5,
      "intervention": 6
    },
    "task": {
      "description": "A genomic research lab is analyzing DNA sequences using rolling hash techniques for pattern detection. They apply a custom hash function where each nucleotide (A=1, T=2, G=3, C=4) contributes to a polynomial hash. Given a specific sequence transformation pipeline involving dynamic programming for optimal subsequence selection and recursive backtracking for verifying palindromic structures, what is the value of variable `final_score` after processing the sequence 'GATTACA' through this pipeline?",
      "code": "import heapq\n\ndef nucleotide_hash(nucleotide):\n    mapping = {'A': 1, 'T': 2, 'G': 3, 'C': 4}\n    return mapping.get(nucleotide, 0)\n\ndef rolling_hash(sequence, base=5, mod=1000000007):\n    hash_val = 0\n    for char in sequence:\n        hash_val = (hash_val * base + nucleotide_hash(char)) % mod\n    return hash_val\n\ndef max_subseq_sum(seq_values):\n    dp = [0] * len(seq_values)\n    dp[0] = seq_values[0]\n    for i in range(1, len(seq_values)):\n        dp[i] = max(dp[i-1] + seq_values[i], seq_values[i])\n    return max(dp)\n\nclass HashCache:\n    def __init__(self):\n        self.cache = {}\n    \n    def get_or_compute(self, s):\n        if s not in self.cache:\n            self.cache[s] = rolling_hash(s)\n        return self.cache[s]\n\ndef is_palindrome_recursive(s, memo={}):\n    if s in memo:\n        return memo[s]\n    if len(s) <= 1:\n        memo[s] = True\n        return True\n    if s[0] != s[-1]:\n        memo[s] = False\n        return False\n    result = is_palindrome_recursive(s[1:-1], memo)\n    memo[s] = result\n    return result\n\n# Main processing pipeline\nsequence = 'GATTACA'\nnucleotides = [nucleotide_hash(c) for c in sequence]\nhash_cache = HashCache()\n\n# Step 1: Compute rolling hash of entire sequence\nfull_hash = hash_cache.get_or_compute(sequence)\n\n# Step 2: Find maximum sum of any contiguous subsequence using DP\nmax_sum = max_subseq_sum(nucleotides)\n\n# Step 3: Identify all palindromic substrings and their hashes\npal_hashes = []\nfor i in range(len(sequence)):\n    for j in range(i+1, len(sequence)+1):\n        substr = sequence[i:j]\n        if is_palindrome_recursive(substr):\n            pal_hashes.append(hash_cache.get_or_compute(substr))\n\n# Step 4: Use min-heap to find smallest 3 palindromic hashes\nheapq.heapify(pal_hashes)\ntop_3_min = [heapq.heappop(pal_hashes) for _ in range(min(3, len(pal_hashes)))]\n\n# Final score calculation\nfinal_score = full_hash + max_sum + sum(top_3_min)\nprint(f\"Result: {final_score}\")",
      "answer": 51563,
      "cot": ""
    }
  },
  {
    "id": "SL-MIX-S005",
    "metadata": {
      "category": "Statement-Level",
      "language": "python",
      "difficulty": 2,
      "intervention": 6
    },
    "task": {
      "description": "A logistics company uses containers with unique IDs to track packages. Each container holds several items, represented as tuples of (item_id, weight). The company maintains two queues: one for incoming shipments and one for outgoing deliveries. During a system audit, they process shipments by moving items from incoming to outgoing only if their cumulative weight doesn't exceed the container's limit. After processing all shipments, what is the total number of items successfully transferred to the outgoing queue?",
      "code": "from collections import deque\n\nclass Container:\n    def __init__(self, max_capacity):\n        self.max_capacity = max_capacity\n        self.current_weight = 0\n        self.items = []\n    \n    def add_item(self, item):\n        item_id, weight = item\n        if self.current_weight + weight <= self.max_capacity:\n            self.items.append(item)\n            self.current_weight += weight\n            return True\n        return False\n\ndef process_shipments(incoming_queue, outgoing_queue, container_limit):\n    transferred_items = 0\n    \n    while incoming_queue:\n        shipment = incoming_queue.popleft()\n        container = Container(container_limit)\n        \n        for item in shipment:\n            if container.add_item(item):\n                outgoing_queue.append(item)\n                transferred_items += 1\n    \n    return transferred_items\n\n# Initialize queues\nincoming_shipments = deque([\n    [(101, 15), (102, 25), (103, 10)],\n    [(201, 30), (202, 20)],\n    [(301, 40), (302, 5), (303, 15), (304, 10)]\n])\n\noutgoing_deliveries = deque()\nmax_container_capacity = 50\n\nfinal_transfer_count = process_shipments(incoming_shipments, outgoing_deliveries, max_container_capacity)\nprint(f\"Result: {final_transfer_count}\")",
      "answer": 7,
      "cot": ""
    }
  },
  {
    "id": "SL-MIX-S006",
    "metadata": {
      "category": "Statement-Level",
      "language": "python",
      "difficulty": 5,
      "intervention": 4
    },
    "task": {
      "description": "A chef is organizing ingredients for a cooking competition. Each ingredient has a priority based on freshness (higher values are fresher). The chef wants to select ingredients greedily by priority until the total weight reaches at least 15 units. What is the value of variable 'selected_count' after the selection process completes?",
      "code": "import itertools\n\n# Ingredient data: (priority, weight)\ningredients = [\n    (8, 3),\n    (6, 4),\n    (9, 2),\n    (7, 5),\n    (5, 1)\n]\n\n# Sort ingredients by priority (descending)\ningredients.sort(key=lambda x: x[0], reverse=True)\n\ntotal_weight = 0\nselected_count = 0\n\nfor priority, weight in ingredients:\n    if total_weight >= 15:\n        break\n    total_weight += weight\n    selected_count += 1\n\nprint(f\"Result: {selected_count}\")",
      "answer": 5,
      "cot": ""
    }
  },
  {
    "id": "SL-MIX-S007",
    "metadata": {
      "category": "Statement-Level",
      "language": "python",
      "difficulty": 1,
      "intervention": 4
    },
    "task": {
      "description": "A bakery makes three types of pastries daily: croissants, muffins, and scones. The baker uses a special glazing technique where the number of glazed items equals the greatest common divisor (GCD) of the day of the month and the total items baked. On the 12th of the month, they made 24 croissants, 36 muffins, and 18 scones. Using Python's math library and collections.Counter to track pastry types, calculate how many pastries received the special glaze. What is the value of variable `glazed_count` after executing the GCD calculation?",
      "code": "from math import gcd\nfrom collections import Counter\n\ncroissants = 24\nmuffins = 36\nscones = 18\nday_of_month = 12\n\npastry_counter = Counter({'croissants': croissants, 'muffins': muffins, 'scones': scones})\ntotal_pastries = sum(pastry_counter.values())\n\n# Calculate special glaze count using GCD\nglazed_count = gcd(day_of_month, total_pastries)\n\nprint(f'Result: {glazed_count}')",
      "answer": 6,
      "cot": ""
    }
  },
  {
    "id": "SL-MIX-S008",
    "metadata": {
      "category": "Statement-Level",
      "language": "python",
      "difficulty": 5,
      "intervention": 5
    },
    "task": {
      "description": "A mathematician is designing a garden with flower beds arranged in a circular pattern. For aesthetic balance, they want to calculate a special arrangement value based on the number of prime positions and the greatest common divisor of bed counts. Given 18 flower beds, what is the value of variable `arrangement_score` at execution point after all calculations?",
      "code": "from math import gcd\n\n# Helper function to check if a number is prime\ndef is_prime(n):\n    if n <= 1:\n        return False\n    for i in range(2, int(n**0.5)+1):\n        if n % i == 0:\n            return False\n    return True\n\n# Total number of flower beds\nflower_beds = 18\n\n# Count prime numbers up to flower_beds\nprime_count = sum(1 for i in range(2, flower_beds + 1) if is_prime(i))\n\n# Calculate GCD of flower_beds and prime_count\nshared_divisor = gcd(flower_beds, prime_count)\n\n# Lambda to compute arrangement score\ncompute_score = lambda primes, divisor: (primes * 3) - (divisor ** 2)\n\n# Determine arrangement score using a switch-like dictionary\nscore_rules = {\n    0: lambda p, d: 0,\n    1: lambda p, d: p + d,\n    2: lambda p, d: p * d,\n    3: lambda p, d: p - d,\n    4: lambda p, d: p ** d,\n    5: lambda p, d: compute_score(p, d),\n    6: lambda p, d: p // (d + 1),\n    7: lambda p, d: (p + 1) * (d + 1)\n}\n\nrule_key = shared_divisor if shared_divisor in score_rules else 0\narrangement_score = score_rules[rule_key](prime_count, shared_divisor)\n\nprint(f'Result: {arrangement_score}')",
      "answer": 8,
      "cot": ""
    }
  },
  {
    "id": "SL-MIX-S009",
    "metadata": {
      "category": "Statement-Level",
      "language": "python",
      "difficulty": 1,
      "intervention": 4
    },
    "task": {
      "description": "A vending machine tracks its states using a state machine implementation. Each successful transaction increases the internal revenue counter. Using dynamic programming principles, the system also calculates cumulative earnings. After processing a sequence of transactions, what is the value of the variable 'final_revenue' at the completion of all transactions?",
      "code": "from functools import reduce\n\ndef vending_machine_state_machine(transactions):\n    states = {'idle': 0, 'processing': 1, 'completed': 2}\n    current_state = states['idle']\n    revenue_log = []\n    \n    dp_cumulative = [0] * (len(transactions) + 1)\n    \n    for i, amount in enumerate(transactions):\n        if current_state == states['idle']:\n            current_state = states['processing']\n        if current_state == states['processing']:\n            revenue_log.append(amount)\n            current_state = states['completed']\n        if current_state == states['completed']:\n            dp_cumulative[i+1] = dp_cumulative[i] + amount\n            current_state = states['idle']\n    \n    return dp_cumulative[-1]\n\n# Transaction log for the day\ntransaction_log = [5, 3, 7, 2, 8]\nfinal_revenue = vending_machine_state_machine(transaction_log)\nprint(f'Result: {final_revenue}')",
      "answer": 25,
      "cot": ""
    }
  },
  {
    "id": "SL-MIX-S010",
    "metadata": {
      "category": "Statement-Level",
      "language": "python",
      "difficulty": 2,
      "intervention": 6
    },
    "task": {
      "description": "A network administrator is simulating packet prioritization using a min-heap where each packet has a priority number. Initially, packets with priorities [7, 7, 7, 2, 1, 9] are pushed into the heap. After pushing all packets, the administrator removes the two highest priority packets (lowest numerical values). What is the value of the new root of the heap after these operations?",
      "code": "import heapq\n\npacket_priorities = [7, 7, 7, 2, 1, 9]\nheap = []\n\nfor priority in packet_priorities:\n    heapq.heappush(heap, priority)\n\nheapq.heappop(heap)  # Remove highest priority packet (lowest value)\nheapq.heappop(heap)  # Remove next highest priority packet\n\nfinal_root = heap[0] if heap else None\nprint(f\"Result: {final_root}\")",
      "answer": 7,
      "cot": ""
    }
  }
]
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
flask>=2.3.0
flask-cors>=4.0.0
```
