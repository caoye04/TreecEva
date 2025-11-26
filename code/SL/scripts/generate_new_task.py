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
    
    def call_api(self, prompt, api_name="DeepSeek-V3.2-Exp"):
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
            return f"API Error: {str(e)}"
    
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
            # 第一个任务，生成中等干扰度
            return "medium"
        
        # 目标分布：基于intervention(干扰度)的分布
        # 4-5 (低干扰)：30% - 代码简洁，干扰少
        # 6-7 (中干扰)：40% - 有一定无效代码干扰
        # 8-10 (高干扰)：30% - 大量无效代码干扰
        target_ranges = {
            "low": {
                "intervention": (4, 5),
                "target_ratio": 0.30,
                "description": "Minimal code interference"
            },
            "medium": {
                "intervention": (6, 7),
                "target_ratio": 0.40,
                "description": "Moderate code interference"
            },
            "high": {
                "intervention": (8, 10),
                "target_ratio": 0.30,
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
    
    def map_intervention_range_to_complexity(self, target_range):
        """将目标intervention范围映射为代码复杂度和干扰度描述"""
        complexity_mapping = {
            "low": {
                "intervention_range": "4-5",
                "description": "Low code interference - clean and focused",
                "interference_level": "Minimal unnecessary code or distractions",
                "logic_steps": "1-3 sequential logic steps",
                "nesting": "Minimal nesting (prefer flat structure)",
                "concepts": "1-2 basic programming concepts",
                "code_style": "Concise and straightforward, avoid over-engineering",
                "examples": "simple loops, basic arithmetic, direct array/list operations",
                "distractor_code": "No or very few irrelevant variables/operations",
                "answer_range": "Answer should be a manageable integer (typically -1000 to 1000) or a decimal with at most 2-3 decimal places"
            },
            "medium": {
                "intervention_range": "6-7",
                "description": "Moderate code interference - some distractions",
                "interference_level": "Some unnecessary computations or variables that don't affect the final answer",
                "logic_steps": "3-5 logic steps with some interdependencies",
                "nesting": "1-2 levels of nesting (keep it moderate)",
                "concepts": "2-3 programming concepts combined",
                "code_style": "Balanced complexity, avoid excessive abstraction",
                "examples": "nested loops, dictionaries/hash maps, list comprehensions, basic recursion",
                "distractor_code": "A few variables or operations that seem relevant but are not",
                "answer_range": "Answer should be a reasonable integer (typically -10000 to 10000) or a decimal with at most 3-4 decimal places"
            },
            "high": {
                "intervention_range": "8-10",
                "description": "High code interference - heavy distractions",
                "interference_level": "Significant amount of irrelevant code and misleading computations",
                "logic_steps": "5-8 logic steps with complex interdependencies",
                "nesting": "2-3 levels of nesting (avoid deep nesting)",
                "concepts": "3-4 programming concepts combined",
                "code_style": "More complex but still readable, avoid extreme verbosity",
                "examples": "multiple data structures, helper functions, state tracking, bit operations",
                "distractor_code": "Multiple irrelevant variables, some dead code paths, misleading intermediate results",
                "answer_range": "Answer should be a reasonable integer (typically -100000 to 100000) or a decimal with at most 4-5 decimal places"
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

    def generate_task_prompt(self):
        """生成优化的任务生成提示"""
        background = self.dataset[0] if self.dataset else {}
        existing_tasks = self.dataset[1:] if len(self.dataset) > 1 else []
        
        used_ids = [task.get("id", "") for task in existing_tasks]
        next_id_num = len(used_ids) + 1
        next_id = f"SL-MIX-S{next_id_num:04d}"
        
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

1. Task ID: {next_id}
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
    "id": "{next_id}",
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
3. The output should be a reasonable number (not too large, prefer integers < 100000 or decimals with < 5 decimal places)
4. Ask for the value of a specific variable at some point in the code execution
5. Maintain the original intervention level (code interference)
6. Keep the code CONCISE - avoid unnecessary complexity

Current Task Information:
ID: {current_task['id']}
Language: {current_task['metadata']['language']}
Intervention: {current_task['metadata']['intervention']} (maintain this level of code interference)
Description: {current_task['task']['description']}

Current Code:
```{current_task['metadata']['language']}
{current_task['task']['code']}
```
Problem Encountered: {error_info}

Please generate the fixed complete task, ensuring:
1. Fix all compilation/runtime errors
2. The code has a clear variable value that can be queried at a key execution point
3. This variable value should be a reasonable, deterministic number
4. The code should print this variable value at the end, format: "Target result: {{variable_value}}"
5. Maintain similar intervention level ({current_task['metadata']['intervention']})
6. Keep the code concise and focused
Please return the fixed task in JSON format:
{{
    "id": "{current_task['id']}",
    "metadata": {{
        "category": "Statement-Level",
        "language": "{current_task['metadata']['language']}",
        "difficulty": -1,
        "intervention": {current_task['metadata']['intervention']}
    }},
    "task": {{
        "description": "<Fixed description asking for a variable value at some execution point>",
        "code": "<Fixed executable code>",
        "answer": <Correct numerical answer>,
        "cot": ""
    }}
}}
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

        self.load_dataset()
        
        print("\n" + "="*70)
        print("ANALYZING CURRENT DATASET DISTRIBUTION")
        print("="*70)
        
        distribution = self.analyze_dataset_distribution()
        
        print(f"📊 Total tasks: {distribution['total_tasks']}")
        
        print(f"\n🎯 Intervention Distribution (4=low interference, 10=high interference):")
        for interv in range(4, 11):
            count = distribution['intervention_distribution'].get(interv, 0)
            if distribution['total_tasks'] > 0:
                percentage = (count / distribution['total_tasks'] * 100)
                bar = "█" * int(percentage / 2)
                print(f"   Level {interv}: {count:2d} tasks ({percentage:5.1f}%) {bar}")
        
        print(f"\n🌐 Language Distribution:")
        for lang, count in sorted(distribution['language_distribution'].items()):
            percentage = (count / distribution['total_tasks'] * 100) if distribution['total_tasks'] > 0 else 0
            bar = "█" * int(percentage / 2)
            print(f"   {lang:8s}: {count:2d} tasks ({percentage:5.1f}%) {bar}")
        
        print(f"\n📈 Difficulty Distribution (post-evaluation, -1=not evaluated yet):")
        for diff in range(-1, 6):
            count = distribution['difficulty_distribution'].get(diff, 0)
            if count > 0:
                percentage = (count / distribution['total_tasks'] * 100) if distribution['total_tasks'] > 0 else 0
                bar = "█" * int(percentage / 2)
                diff_label = "Not evaluated" if diff == -1 else f"{diff} AI errors"
                print(f"   {diff_label:15s}: {count:2d} tasks ({percentage:5.1f}%) {bar}")
        
        print("\n" + "="*70)
        print("GENERATING NEW TASK (Python-only, Intervention-based)")
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
                print(f"   Intervention: {new_task['metadata']['intervention']} (code interference level)")
                print(f"   Difficulty: {new_task['metadata']['difficulty']} (will be evaluated later)")
                print(f"   Description: {new_task['task']['description'][:100]}...")
                print(f"   Answer: {new_task['task']['answer']}")
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