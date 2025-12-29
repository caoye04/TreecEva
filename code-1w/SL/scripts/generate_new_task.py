import json
import sys
import re
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from config import DATASET_PATH, AI_APIS
import openai
import random
from concurrent.futures import ThreadPoolExecutor, as_completed
from threading import Lock
import time

class TaskGenerator:
    def __init__(self, max_workers=10):
        """
        初始化任务生成器
        
        Args:
            max_workers: 并行生成的最大线程数（默认10，建议5-15）
        """
        self.dataset = None
        self.max_workers = max_workers
        self.save_lock = Lock()
        self.stats_lock = Lock()
        
        # 统计信息
        self.stats = {
            "total_attempts": 0,
            "successful": 0,
            "failed": 0,
            "parsed_errors": 0,
            "validation_errors": 0
        }
    
    def load_dataset(self):
        """Load dataset"""
        with open(DATASET_PATH, 'r', encoding='utf-8') as f:
            self.dataset = json.load(f)
    
    def call_api(self, prompt, api_name="DeepSeek-V3.2-Exp", retry=3):
        """
        Call API to generate content with retry mechanism
        
        Args:
            prompt: 提示文本
            api_name: API名称
            retry: 重试次数（默认3次）
        """
        api_config = AI_APIS[api_name]
        
        client = openai.OpenAI(
            api_key=api_config['api_key'],
            base_url=api_config['base_url']
        )
        
        for attempt in range(retry):
            try:
                response = client.chat.completions.create(
                    model=api_config['model'],
                    messages=[
                        {
                            "role": "system",
                            "content": "You are an expert in creating programming problems. Generate concise, focused code samples that are challenging but not overly complex."
                        },
                        {
                            "role": "user",
                            "content": prompt
                        }
                    ],
                    temperature=0.8,
                    max_tokens=3000
                )
                
                return response.choices[0].message.content
                    
            except Exception as e:
                if attempt < retry - 1:
                    wait_time = 2 ** attempt  # 指数退避
                    print(f"⚠️  API error (attempt {attempt+1}/{retry}), retrying in {wait_time}s: {str(e)[:100]}")
                    time.sleep(wait_time)
                else:
                    return f"API Error: {str(e)}"
        
        return "API Error: Max retries exceeded"
    
    def analyze_dataset_distribution(self):
        """分析数据集的intervention(干扰度)和语言分布"""
        existing_tasks = self.dataset[1:] if len(self.dataset) > 1 else []
        
        # 统计难度分布（0-5，后期评估的结果，仅用于统计）
        difficulty_counts = {i: 0 for i in range(6)}
        language_counts = {}
        # Intervention分布（4-10，代表代码干扰度）
        intervention_counts = {i: 0 for i in range(4, 11)}
        
        for task in existing_tasks:
            if "metadata" in task:
                # 难度是后期AI评估的结果（0-5），仅用于统计
                diff = task["metadata"].get("difficulty", -1)
                if diff >= 0:
                    difficulty_counts[diff] = difficulty_counts.get(diff, 0) + 1
                
                # 语言分布
                lang = task["metadata"].get("language", "python")
                language_counts[lang] = language_counts.get(lang, 0) + 1
                
                # Intervention分布（主要平衡指标）
                interv = task["metadata"].get("intervention", 6)
                intervention_counts[interv] = intervention_counts.get(interv, 0) + 1
        
        return {
            "difficulty_distribution": difficulty_counts,
            "language_distribution": language_counts,
            "intervention_distribution": intervention_counts,
            "total_tasks": len(existing_tasks)
        }
    
    def identify_missing_intervention_range(self, distribution):
        """识别缺失的intervention范围（基于代码干扰度）"""
        intervention_counts = distribution["intervention_distribution"]
        total = distribution["total_tasks"]
        
        if total == 0:
            # 第一个任务，生成高干扰度
            return "high"
        
        # 目标分布：调整为更高难度的分布
        target_ranges = {
            "low": {
                "intervention": (4, 5),
                "target_ratio": 0.15,  # 减少简单任务
                "description": "Minimal code interference"
            },
            "medium": {
                "intervention": (6, 7),
                "target_ratio": 0.35,  # 减少中等任务
                "description": "Moderate code interference"
            },
            "high": {
                "intervention": (8, 10),
                "target_ratio": 0.50,  # 增加困难任务
                "description": "Heavy code interference"
            }
        }
        
        # 计算每个范围的缺失度
        deficits = {}
        for range_name, range_info in target_ranges.items():
            min_int, max_int = range_info["intervention"]
            count = sum(intervention_counts.get(i, 0) for i in range(min_int, max_int + 1))
            actual_ratio = count / total
            deficit = range_info["target_ratio"] - actual_ratio
            deficits[range_name] = deficit
        
        # 80%选择最缺失的，20%随机选择
        if random.random() < 0.80:
            target_range = max(deficits, key=deficits.get)
        else:
            # 从缺失度>0的范围中随机选
            positive_deficits = {k: v for k, v in deficits.items() if v > 0}
            if positive_deficits:
                target_range = random.choice(list(positive_deficits.keys()))
            else:
                target_range = "medium"
        
        return target_range
    
    def map_intervention_range_to_complexity(self, target_range):
        """将目标intervention范围映射为代码复杂度和干扰度描述"""
        complexity_mapping = {
            "low": {
                "intervention_range": "4-5",
                "description": "Low code interference - clean and focused",
                "interference_level": "Minimal unnecessary code or distractions",
                "logic_steps": "3-5 sequential logic steps",
                "nesting": "1-2 levels of nesting",
                "concepts": "2-3 basic programming concepts",
                "code_style": "Moderate complexity with clear structure",
                "examples": "nested loops, list operations, basic conditionals",
                "distractor_code": "A few irrelevant variables or operations",
                "answer_range": "Answer should be a reasonable integer (typically -10000 to 10000) or a decimal with at most 3-4 decimal places"
            },
            "medium": {
                "intervention_range": "6-7",
                "description": "Moderate code interference - some distractions",
                "interference_level": "Significant unnecessary computations and misleading variables",
                "logic_steps": "5-8 logic steps with interdependencies",
                "nesting": "2-3 levels of nesting",
                "concepts": "3-4 programming concepts combined",
                "code_style": "Complex but readable, with deliberate complexity",
                "examples": "multiple nested loops, complex data structures, helper functions, state tracking",
                "distractor_code": "Multiple irrelevant variables, some dead code paths, misleading computations",
                "answer_range": "Answer should be a reasonable integer (typically -100000 to 100000) or a decimal with at most 4-5 decimal places"
            },
            "high": {
                "intervention_range": "8-10",
                "description": "High code interference - heavy distractions",
                "interference_level": "Extensive irrelevant code, multiple red herrings, and complex misleading paths",
                "logic_steps": "8-12 logic steps with complex interdependencies",
                "nesting": "3-4 levels of nesting (controlled complexity)",
                "concepts": "4-5 programming concepts combined",
                "code_style": "Highly complex with multiple abstraction layers",
                "examples": "recursive functions, complex data transformations, bit manipulation, multiple data structures with cross-references",
                "distractor_code": "Extensive irrelevant variables, multiple dead code paths, deliberately misleading intermediate results, decoy functions",
                "answer_range": "Answer can be a larger integer (typically -1000000 to 1000000) or a decimal with up to 6 decimal places"
            }
        }
        
        return complexity_mapping.get(target_range, complexity_mapping["medium"])
    
    def select_language_and_features(self, distribution):
        """智能选择语言和特征组合 (仅限Python)"""
        
        selected_language = "python"
        
        language_features = {
            "python": [
                "list comprehensions",
                "dictionary operations",
                "set operations",
                "string methods",
                "lambda functions",
                "enumerate and zip",
                "collections module (Counter, defaultdict)",
                "itertools basics",
                "slicing operations",
                "conditional expressions"
            ]
        }
        
        # 随机选择1-3个特征
        num_features = random.randint(1, 3)
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
                "simple bitwise operations (XOR, AND, OR)",
                "modular arithmetic",
                "integer division and rounding"
            ],
            "boolean": [
                "comparison operations",
                "logical operations (AND, OR, NOT)",
                "conditional expressions"
            ],
            "control_flow": [
                "simple loops",
                "conditional branches",
                "early returns or breaks"
            ],
            "data_structures": [
                "lists and arrays",
                "dictionaries/hash maps",
                "sets",
                "tuples"
            ],
            "algorithms": [
                "simple sorting",
                "linear search",
                "basic counting/grouping",
                "simple recursion"
            ],
            "string_ops": [
                "string manipulation",
                "character counting",
                "string splitting/joining",
                "case conversion"
            ],
            "mathematical": [
                "summation and accumulation",
                "basic sequences",
                "simple combinatorics",
                "min/max/average calculations"
            ]
        }
        
        # 根据干扰度决定选择多少个范式
        if complexity_level == "low":
            num_categories = random.randint(1, 2)
            num_paradigms_per_category = 1
        elif complexity_level == "medium":
            num_categories = random.randint(2, 3)
            num_paradigms_per_category = random.randint(1, 2)
        else:  # high
            num_categories = random.randint(2, 4)
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
            "calendar", "game", "sensor", "network", "database", "parser",
            "temperature", "score", "inventory", "transaction", "coordinate"
        ]
        
        for task in recent_tasks:
            if "task" in task and "description" in task["task"]:
                desc = task["task"]["description"].lower()
                for keyword in theme_keywords:
                    if keyword in desc:
                        used_themes.add(keyword)
        
        constraints = []
        
        if used_themes:
            constraints.append(f"- AVOID these recently used themes: {', '.join(sorted(used_themes))}")
        
        constraints.append("- CREATE a unique, realistic problem scenario")
        constraints.append("- USE meaningful and domain-specific variable names")
        constraints.append(f"- FOCUS on {selected_language} idioms and best practices")
        constraints.append("- KEEP the code concise and focused - avoid unnecessary complexity")
        
        return "\n".join(constraints)
    
    def select_target_intervention_value(self, target_range):
        """根据目标干扰度范围选择具体的intervention值"""
        intervention_ranges = {
            "low": (4, 5),
            "medium": (6, 7),
            "high": (8, 10)
        }
        
        min_val, max_val = intervention_ranges.get(target_range, (6, 7))
        return random.randint(min_val, max_val)

    def generate_task_prompt(self, task_id):
        """生成优化的任务生成提示（为单个任务）"""
        background = self.dataset[0] if self.dataset else {}
        existing_tasks = self.dataset[1:] if len(self.dataset) > 1 else []
        
        # 分析当前数据集分布
        distribution = self.analyze_dataset_distribution()
        
        # 识别缺失的intervention范围
        target_range = self.identify_missing_intervention_range(distribution)
        complexity_info = self.map_intervention_range_to_complexity(target_range)
        
        # 智能选择语言和特征
        selected_language, selected_features = self.select_language_and_features(distribution)
        
        # 选择计算范式
        selected_paradigms = self.select_computational_paradigms(target_range)
        
        # 选择目标intervention值
        target_intervention = self.select_target_intervention_value(target_range)
        
        # 生成多样性约束
        diversity_constraints = self.generate_diversity_constraints(existing_tasks, selected_language)
        
        prompt = f"""
Based on the following background and requirements, generate a new programming task:

Background: {background.get('background', '')}

Requirements: {background.get('requirements', '')}

═══════════════════════════════════════════════════════════════════
TASK SPECIFICATIONS
═══════════════════════════════════════════════════════════════════

1. Task ID: {task_id}
2. Language: {selected_language}
3. Target Intervention Level: {target_range.upper()} (Intervention = {target_intervention})

INTERVENTION REQUIREMENTS FOR "{target_range.upper()}" LEVEL:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
• Intervention Range: {complexity_info["intervention_range"]}
• Description: {complexity_info["description"]}
• Interference Level: {complexity_info["interference_level"]}
• Logic Steps: {complexity_info["logic_steps"]}
• Nesting Depth: {complexity_info["nesting"]}
• Concepts: {complexity_info["concepts"]}
• Code Style: {complexity_info["code_style"]}
• Examples: {complexity_info["examples"]}
• Distractor Code: {complexity_info["distractor_code"]}
• ANSWER RANGE: {complexity_info["answer_range"]}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

CRITICAL UNDERSTANDING OF "INTERVENTION":
  - Intervention = Code interference/distraction level (4-10)
  - Higher intervention = More irrelevant code, red herrings, misleading variables
  - Target intervention for this task: {target_intervention}
  - You MUST self-assess and set the intervention value based on how much
    irrelevant/distracting code you include
  - The intervention value should reflect the actual code interference you create

IMPORTANT ABOUT "DIFFICULTY":
  - Difficulty (0-5) will be determined LATER by AI evaluation
  - Difficulty = Number of AIs that answer incorrectly (out of 5 AIs)
  - For NOW, always set difficulty to -1 (placeholder for later evaluation)
  - Do NOT confuse difficulty with intervention!

═══════════════════════════════════════════════════════════════════
MANDATORY LANGUAGE-SPECIFIC FEATURES
═══════════════════════════════════════════════════════════════════
You SHOULD incorporate at least 1-2 of these {selected_language} features:

{chr(10).join(f'  • {feature}' for feature in selected_features)}

═══════════════════════════════════════════════════════════════════
SUGGESTED COMPUTATIONAL PARADIGMS
═══════════════════════════════════════════════════════════════════
Consider incorporating these computational elements:

{chr(10).join(f'  • {paradigm}' for paradigm in selected_paradigms)}

═══════════════════════════════════════════════════════════════════
DIVERSITY CONSTRAINTS (CRITICAL!)
═══════════════════════════════════════════════════════════════════
{diversity_constraints}

═══════════════════════════════════════════════════════════════════
CODE REQUIREMENTS WITH INTERVENTION LEVEL {target_intervention}
═══════════════════════════════════════════════════════════════════
1. The code MUST be syntactically correct and directly compilable/executable
2. The code MUST produce a unique, deterministic numerical result
3. The answer MUST be a reasonable number: {complexity_info["answer_range"]}
4. At some critical execution point, there should be a key variable whose value is the answer
5. The problem description should ask: "what is the value of variable X at execution point Y"
6. The code MUST print this variable value at the end
   Format: "Result: {{variable_value}}" or "Target result: {{variable_value}}"

INTERVENTION LEVEL {target_intervention} GUIDANCE:
{self._get_intervention_guidance(target_intervention, target_range)}

CODE COMPLEXITY GUIDELINES:
✓ Keep code FOCUSED and CONCISE - avoid over-engineering
✓ Prefer clarity over excessive cleverness
✓ Avoid unnecessarily long or verbose code
✓ Use appropriate abstraction without going overboard
✓ The code should be challenging through logic, not through length

ENSURE THE CODE:
✓ Has no syntax errors
✓ Has no undefined constants or missing imports
✓ Produces deterministic output (no randomness unless seeded)
✓ Has intervention level of approximately {target_intervention}
✓ Contains appropriate amount of code interference for {target_range.upper()} level
✓ Produces an answer in the specified range: {complexity_info["answer_range"]}

═══════════════════════════════════════════════════════════════════
RESPONSE FORMAT
═══════════════════════════════════════════════════════════════════
Please respond with ONLY the JSON (no additional text):

```json
{{
    "id": "{task_id}",
    "metadata": {{
        "category": "Statement-Level",
        "language": "{selected_language}",
        "difficulty": -1,
        "intervention": {target_intervention}
    }},
    "task": {{
        "description": "What is the value of variable '<variable_name>' after executing the statement '<key_statement>'?",
        "code": "<Executable code with intervention level {target_intervention}>",
        "answer": <correct_numerical_answer>,
        "cot": ""
    }}
}}```

CRITICAL REMINDERS:
🎯 Set difficulty to -1 (it will be evaluated later based on AI performance)
🎯 Set intervention to {target_intervention} (or nearby value if you assess differently)
🎯 Create code with {target_range.upper()} interference level
🎯 Include appropriate amount of distractor/irrelevant code for intervention {target_intervention}
🎯 Use meaningful variable names and realistic problem context
🎯 Avoid patterns similar to recent tasks
🎯 Ensure code is executable and produces deterministic output
🎯 Keep code CONCISE - quality over quantity
🎯 Answer must be a reasonable number: {complexity_info["answer_range"]}
"""
        return prompt
    
    def _get_intervention_guidance(self, intervention_value, range_name):
        """根据intervention值提供具体的代码干扰指导"""
        if intervention_value in [4, 5]:
            return """
✓ Keep code clean and straightforward
✓ Minimal or no irrelevant variables
✓ Direct computation path to the answer
✓ Very few distractions or red herrings
✓ Code should be easy to trace mentally
✓ Focus on clarity and simplicity
"""
        elif intervention_value in [6, 7]:
            return """
✓ Include some intermediate variables that aren't directly used in the final answer
✓ Add a few computational steps that don't affect the result
✓ Mix relevant and semi-relevant operations
✓ Create moderate cognitive load through code structure
✓ Balance between clarity and distraction
✓ Don't make it too convoluted
"""
        else:  # 8-10
            return """
✓ Include several irrelevant variables and computations
✓ Add some misleading intermediate results
✓ Create a few dead code paths or unused operations
✓ Mix relevant code with meaningful distractors
✓ Make the path to the answer non-obvious but still traceable
✓ Avoid excessive complexity - focus on smart distractions
"""
    
    def parse_task_response(self, response, task_id):
        """解析API响应，提取任务JSON"""
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
                return {"success": True, "task": new_task, "task_id": task_id}
            else:
                return {
                    "success": False,
                    "error": "Missing required fields",
                    "task_id": task_id
                }
                
        except json.JSONDecodeError as e:
            return {
                "success": False,
                "error": f"JSON parse error: {str(e)}",
                "task_id": task_id,
                "raw_response": response[:200]
            }
    
    def generate_single_task_async(self, task_id, api_name="DeepSeek-V3.2-Exp"):
        """
        异步生成单个任务（由线程池调用）
        
        Args:
            task_id: 任务ID
            api_name: 使用的API名称
            
        Returns:
            包含生成结果的字典
        """
        try:
            prompt = self.generate_task_prompt(task_id)
            response = self.call_api(prompt, api_name)
            
            if response.startswith("API Error"):
                return {
                    "status": "failed",
                    "task_id": task_id,
                    "error": response
                }
            
            result = self.parse_task_response(response, task_id)
            
            if result["success"]:
                return {
                    "status": "success",
                    "task_id": task_id,
                    "task": result["task"]
                }
            else:
                return {
                    "status": "failed",
                    "task_id": task_id,
                    "error": result.get("error", "Unknown error")
                }
                
        except Exception as e:
            return {
                "status": "failed",
                "task_id": task_id,
                "error": f"Exception: {str(e)}"
            }
    
    def update_stats(self, status):
        """线程安全的统计更新"""
        with self.stats_lock:
            self.stats[status] += 1
            if status in ["successful", "failed"]:
                self.stats["total_attempts"] += 1
    
    def save_tasks_batch(self, tasks):
        """线程安全的批量保存任务（追加模式）"""
        if not tasks:
            return
            
        with self.save_lock:
            self.dataset.extend(tasks)
            with open(DATASET_PATH, 'w', encoding='utf-8') as f:
                json.dump(self.dataset, f, indent=2, ensure_ascii=False)
    
    def get_existing_task_count(self):
        """获取已存在的任务数量（不包括background）"""
        return len(self.dataset) - 1 if len(self.dataset) > 1 else 0
    
    def generate_batch_tasks(self, batch_size=10, api_name="DeepSeek-V3.2-Exp", start_id=None):
        """
        批量并行生成多个任务（分批保存版本）
        
        Args:
            batch_size: 要生成的任务总数
            api_name: 使用的API名称
            start_id: 起始ID号（用于断点续传）
            
        Returns:
            成功生成的任务列表
        """
        self.load_dataset()
        
        # 重置统计
        self.stats = {
            "total_attempts": 0,
            "successful": 0,
            "failed": 0,
            "parsed_errors": 0,
            "validation_errors": 0
        }
        
        # 确定起始ID
        if start_id is None:
            existing_count = self.get_existing_task_count()
            start_id = existing_count
        
        # 生成任务ID列表
        task_ids = [f"SL-MIX-S{start_id + i:05d}" for i in range(batch_size)]
        
        print(f"\n{'='*70}")
        print(f"BATCH TASK GENERATION (PARALLEL)")
        print(f"{'='*70}")
        print(f"Batch size: {batch_size}")
        print(f"API: {api_name}")
        print(f"Max parallel workers: {self.max_workers}")
        print(f"Task IDs: {task_ids[0]} ~ {task_ids[-1]}")
        print(f"Existing tasks: {self.get_existing_task_count()}")
        print(f"{'='*70}\n")
        
        start_time = time.time()
        all_successful_tasks = []
        
        # 分批次提交和保存
        total_batches = (batch_size + self.max_workers - 1) // self.max_workers
        
        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            for batch_idx in range(total_batches):
                batch_start = batch_idx * self.max_workers
                batch_end = min(batch_start + self.max_workers, batch_size)
                current_batch_ids = task_ids[batch_start:batch_end]
                
                print(f"\n{'─'*70}")
                print(f"📦 BATCH {batch_idx + 1}/{total_batches}")
                print(f"   Tasks: {current_batch_ids[0]} ~ {current_batch_ids[-1]}")
                print(f"   Count: {len(current_batch_ids)}")
                print(f"{'─'*70}")
                
                # 提交当前批次的任务
                future_to_id = {
                    executor.submit(
                        self.generate_single_task_async,
                        task_id,
                        api_name
                    ): task_id
                    for task_id in current_batch_ids
                }
                
                # 收集当前批次的结果
                batch_successful_tasks = []
                
                for future in as_completed(future_to_id):
                    task_id = future_to_id[future]
                    
                    try:
                        result = future.result()
                        
                        if result["status"] == "success":
                            batch_successful_tasks.append(result["task"])
                            self.update_stats("successful")
                            
                            task = result["task"]
                            print(f"✓ [{task_id}] Generated | "
                                  f"Intervention: {task['metadata']['intervention']} | "
                                  f"Answer: {task['task']['answer']}")
                            
                        elif result["status"] == "failed":
                            self.update_stats("failed")
                            error_msg = result.get('error', 'Unknown')[:80]
                            print(f"✗ [{task_id}] Failed: {error_msg}")
                        
                    except Exception as e:
                        self.update_stats("failed")
                        print(f"✗ [{task_id}] Exception: {str(e)[:80]}")
                
                # 当前批次完成后立即保存
                if batch_successful_tasks:
                    self.save_tasks_batch(batch_successful_tasks)
                    all_successful_tasks.extend(batch_successful_tasks)
                    
                    current_total = len(all_successful_tasks)
                    print(f"\n💾 Saved {len(batch_successful_tasks)} tasks from this batch")
                    print(f"📊 Progress: {current_total}/{batch_size} "
                          f"({current_total/batch_size*100:.1f}%) | "
                          f"Success rate: {current_total/(batch_end)*100:.1f}%")
                else:
                    print(f"\n⚠️  No successful tasks in this batch to save")
        
        elapsed_time = time.time() - start_time
        
        print(f"\n{'='*70}")
        print(f"FINAL SUMMARY")
        print(f"{'='*70}")
        print(f"✓ Total successful: {self.stats['successful']}/{batch_size}")
        print(f"✗ Total failed: {self.stats['failed']}/{batch_size}")
        print(f"📈 Success rate: {self.stats['successful']/batch_size*100:.1f}%")
        print(f"⏱  Total time: {elapsed_time:.1f}s")
        print(f"⚡ Average: {elapsed_time/batch_size:.2f}s per task")
        print(f"💾 Dataset now contains: {self.get_existing_task_count()} tasks")
        print(f"{'='*70}\n")
        
        return all_successful_tasks
    
    # 保留原有的单个生成方法（向后兼容）
    def generate_new_task(self):
        """生成单个新任务（保留原有接口）"""
        results = self.generate_batch_tasks(batch_size=1)
        return results[0] if results else None
    
    def generate_and_validate_task(self):
        """生成并验证新任务（保留原有接口）"""
        new_task = self.generate_new_task()
        
        if new_task:
            print("\n🎉 Task generation completed successfully!")
            return new_task
        else:
            print("\n⚠️ Task generation failed!")
            return None

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(
        description="Generate new tasks for the dataset (with parallel batch generation)",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # 生成单个任务（原有功能）
  python generate_new_task.py
  
  # 批量生成10个任务（并行，每15个一批保存）
  python generate_new_task.py --batch 10
  
  # 批量生成30000个任务，使用不同的API
  python generate_new_task.py --batch 30000 --api qwen3_235b
  
  # 自定义并行线程数
  python generate_new_task.py --batch 10 --workers 15
        """
    )
    
    parser.add_argument("--batch", type=int, default=1,
                       help="Number of tasks to generate in parallel (default: 1)")
    parser.add_argument("--api", default="DeepSeek-V3.2-Exp",
                       help="API to use for task generation (default: DeepSeek-V3.2-Exp)")
    parser.add_argument("--workers", type=int, default=10,
                       help="Number of parallel workers (default: 10, recommended: 5-15)")
    
    args = parser.parse_args()
    
    generator = TaskGenerator(max_workers=args.workers)
    
    if args.batch == 1:
        # 单个任务生成（原有逻辑）
        generator.generate_and_validate_task()
    else:
        # 批量任务生成（新功能 - 分批保存）
        generator.generate_batch_tasks(batch_size=args.batch, api_name=args.api)