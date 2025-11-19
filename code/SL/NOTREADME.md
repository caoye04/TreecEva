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
│   │   ├── TreecEva_data.json
│   │   └── answer.json 
│   │   └── ai_evaluation_with_difficulty.json
│   ├── temp_code/
│   ├── execute_tasks.py
│   ├── generate_cot.py
│   ├── ai_evaluation.py
│   ├── generate_new_task.py
│   └── main_loop.py
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

````

### ai_evaluation.py

~~~py
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

```

### answer.json

```json

```

### Statement-Level-MIX.json

```json

```

## config.py

```py
import os

# 文件路径配置
DATASET_PATH = "data/TreecEva_data.json"
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
