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
import json
import sys
import re
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
from threading import Lock
import time

sys.path.append(str(Path(__file__).parent.parent))
from config import DATASET_PATH, AI_APIS
import openai

class CoTGenerator:
    def __init__(self, max_workers=5):
        """
        初始化CoT生成器
        
        Args:
            max_workers: 并行处理的最大线程数 (建议3-10,根据API限流调整)
        """
        self.dataset = None
        self.max_workers = max_workers
        self.save_lock = Lock()
        self.progress_lock = Lock()
        
        # 统计信息
        self.stats = {
            "successful": 0,
            "skipped": 0,
            "failed": 0,
            "process_based": 0,  # 新增:基于思路的CoT数量
            "processed": 0
        }
        
        # 标准模式系统提示词
        self.standard_system_prompt = (
            "You are an expert in program reasoning and code analysis. "
            "Your task is to analyze the given problem, code, and the **provided correct answer**. "
            "You must independently derive the solution through a clear, step-by-step chain of thought, "
            "explaining your reasoning and all intermediate calculations.\n\n"
            "**IMPORTANT RULES:**\n"
            "1. DO NOT simply copy or reference the provided answer in your reasoning\n"
            "2. Your goal is to REPLICATE the process of reaching that answer through logical deduction\n"
            "3. Show ALL intermediate calculations and variable states\n"
            "4. Explain WHY each step is performed, not just WHAT is performed\n"
            "5. Track variable values as they change throughout execution\n\n"
            "After your independent reasoning, you MUST output your calculated final answer on a separate line:\n"
            "Output: <your_calculated_answer>\n\n"
            "CONSTRAINTS:\n"
            "✓ The reasoning must demonstrate YOUR OWN step-by-step calculation process\n"
            "✓ The final answer line MUST begin EXACTLY with 'Output:' followed by your calculated answer\n"
            "✓ The answer line must NOT contain any other text, explanations, or formatting\n"
            "✓ The <your_calculated_answer> should be the final value you derived (typically a number)"
        )
        
        # 思路导向模式系统提示词(不要求输出答案)
        self.process_oriented_system_prompt = (
            "You are an expert in program reasoning and code analysis. "
            "Your task is to provide a **methodological guide** for solving the given problem, "
            "WITHOUT calculating or revealing the final answer.\n\n"
            "**YOUR TASK:**\n"
            "Explain the APPROACH and METHODOLOGY to solve this problem, including:\n"
            "1. Key concepts and techniques needed\n"
            "2. Step-by-step methodology (what to track, what to calculate)\n"
            "3. Important edge cases or considerations\n"
            "4. The logical flow of solving such problems\n\n"
            "**CRITICAL RULES:**\n"
            "✗ DO NOT calculate intermediate values with actual numbers\n"
            "✗ DO NOT provide the final answer or any numerical result\n"
            "✗ DO NOT trace through the specific code execution with concrete values\n"
            "✓ DO explain what variables to track and HOW to track them\n"
            "✓ DO explain the problem-solving strategy and thought process\n"
            "✓ DO describe what calculations would be needed (without doing them)\n\n"
            "Think of yourself as a teacher explaining the METHODOLOGY, not a calculator providing the ANSWER.\n"
            "Your response should help someone understand HOW to approach similar problems."
        )
    
    def load_dataset(self):
        """加载数据集"""
        with open(DATASET_PATH, 'r', encoding='utf-8') as f:
            self.dataset = json.load(f)
        print(f"✓ Loaded dataset with {len(self.dataset) - 1} tasks")
    
    def call_api(self, prompt, api_name="qwen3_coder", system_prompt=None):
        """调用AI API生成CoT (线程安全)"""
        api_config = AI_APIS[api_name]
        
        client = openai.OpenAI(
            api_key=api_config['api_key'],
            base_url=api_config['base_url']
        )
        
        # 使用传入的系统提示词,如果没有则使用默认的
        if system_prompt is None:
            system_prompt = self.standard_system_prompt
        
        try:
            response = client.chat.completions.create(
                model=api_config['model'],
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7,
                max_tokens=4000
            )
            
            return response.choices[0].message.content
                
        except Exception as e:
            return f"API Error: {str(e)}"
    
    def generate_standard_cot_prompt(self, task_data):
        """生成标准CoT提示词(要求输出答案)"""
        description = task_data["task"]["description"]
        code = task_data["task"]["code"]
        answer = task_data["task"]["answer"]
        language = task_data["metadata"]["language"]
        
        prompt = f"""
Please analyze the following programming problem and provide a detailed chain of thought reasoning.

═══════════════════════════════════════════════════════════════════
PROBLEM DESCRIPTION
═══════════════════════════════════════════════════════════════════
{description}

═══════════════════════════════════════════════════════════════════
CODE TO ANALYZE (Language: {language})
═══════════════════════════════════════════════════════════════════
```{language}
{code}
```
═══════════════════════════════════════════════════════════════════
PROVIDED CORRECT ANSWER (For Reference)
═══════════════════════════════════════════════════════════════════
{answer}

═══════════════════════════════════════════════════════════════════
YOUR TASK
═══════════════════════════════════════════════════════════════════

Please provide a step-by-step reasoning process that:

Identifies the key variables and data structures in the code
Traces the execution flow line by line or block by block
Calculates intermediate values at each critical step
Explains the logic behind each operation or transformation
Shows your work for all mathematical operations
Arrives at the final answer through your own calculations
Remember:
• Be thorough but concise - focus on the reasoning, not just restating the code
• Show variable states as they change during execution
• Explain WHY operations are performed, not just WHAT they do
• Your calculated answer should match the provided answer (if it doesn't, recheck your reasoning)

Finally, output your calculated answer in this exact format:
Output: <your_calculated_numerical_answer>
"""
        return prompt
    
    def generate_process_oriented_prompt(self, task_data):
        """生成思路导向提示词(不要求输出答案)"""
        description = task_data["task"]["description"]
        code = task_data["task"]["code"]
        language = task_data["metadata"]["language"]
        
        prompt = f"""
```
Please provide a methodological guide for solving the following programming problem.

═══════════════════════════════════════════════════════════════════
PROBLEM DESCRIPTION
═══════════════════════════════════════════════════════════════════
{description}

═══════════════════════════════════════════════════════════════════
CODE TO ANALYZE (Language: {language})
═══════════════════════════════════════════════════════════════════
```
{code}
```
═══════════════════════════════════════════════════════════════════
YOUR TASK: EXPLAIN THE SOLVING METHODOLOGY
═══════════════════════════════════════════════════════════════════

Provide a clear guide on HOW to approach this problem, including:

1. Problem Analysis

What is the core problem being solved?
What are the key inputs and expected output type?
2. Solution Approach

What technique or algorithm does this code use?
What variables or data structures are critical to track?
What is the overall strategy or pattern?
3. Step-by-Step Methodology

Describe the logical steps needed (WITHOUT executing them with actual values)
Explain what to track at each stage (e.g., "track how variable X changes in each iteration")
Identify key decision points or conditions
4. Important Considerations

What edge cases should be considered?
What are common pitfalls in solving such problems?
What assumptions does the code make?
REMEMBER:

Focus on the METHODOLOGY and THOUGHT PROCESS
Do NOT calculate specific values or provide the final answer
Explain the "how" and "why", not the "what" of specific numbers
Think of this as teaching someone the approach, not solving it for them
Your response should enable someone to apply this methodology to solve the problem themselves.
"""
        return prompt
    
    def extract_cot_and_answer(self, response):
        """从API响应中提取CoT和答案"""
        output_match = re.search(r'^Output:\s*(\d+(?:\.\d+)?)\s*$', response, re.MULTILINE)
        
        if output_match:
            calculated_answer = output_match.group(1)
            output_position = output_match.start()
            cot = response[:output_position].strip()
            
            if '.' in calculated_answer:
                calculated_answer = int(round(float(calculated_answer)))
            else:
                calculated_answer = int(calculated_answer)
            
            return {
                "success": True,
                "cot": cot,
                "calculated_answer": calculated_answer
            }
        else:
            alternative_patterns = [
                r'(?:Final\s+)?Answer:\s*(\d+(?:\.\d+)?)',
                r'(?:Final\s+)?Result:\s*(\d+(?:\.\d+)?)',
                r'(?:The\s+)?(?:final\s+)?(?:answer\s+is|result\s+is):\s*(\d+(?:\.\d+)?)',
            ]
            
            for pattern in alternative_patterns:
                match = re.search(pattern, response, re.IGNORECASE | re.MULTILINE)
                if match:
                    calculated_answer = match.group(1)
                    if '.' in calculated_answer:
                        calculated_answer = int(round(float(calculated_answer)))
                    else:
                        calculated_answer = int(calculated_answer)
                    
                    return {
                        "success": True,
                        "cot": response.strip(),
                        "calculated_answer": calculated_answer
                    }
            
            return {
                "success": False,
                "error": "Could not extract answer from CoT response",
                "raw_response": response[:500]
            }

    def generate_cot_for_task(self, task_data, api_name="qwen3_coder", max_retries=3):
        """
        为单个任务生成CoT (线程安全)
        
        策略:
        1. 前3次尝试: 使用标准模式(要求输出答案),验证答案正确性
        2. 如果3次都失败: 切换到思路导向模式(不要求答案,只要思路)
        
        Args:
            task_data: 任务数据
            api_name: 使用的API名称
            max_retries: 标准模式最大重试次数
            
        Returns:
            包含success, cot等信息的字典
        """
        task_id = task_data["id"]
        correct_answer = task_data["task"]["answer"]
        
        # 阶段1: 标准模式尝试(要求输出答案)
        for attempt in range(max_retries):
            prompt = self.generate_standard_cot_prompt(task_data)
            response = self.call_api(prompt, api_name, self.standard_system_prompt)
            
            if response.startswith("API Error"):
                if attempt == max_retries - 1:
                    # API错误且达到重试上限,进入思路模式
                    break
                time.sleep(1)
                continue
            
            result = self.extract_cot_and_answer(response)
            
            if not result["success"]:
                if attempt == max_retries - 1:
                    # 无法提取答案且达到重试上限,进入思路模式
                    break
                time.sleep(0.5)
                continue
            
            # 验证答案是否正确
            if result["calculated_answer"] == correct_answer:
                return {
                    "success": True,
                    "cot": result["cot"],
                    "task_id": task_id,
                    "mode": "standard"
                }
            else:
                if attempt < max_retries - 1:
                    time.sleep(0.5)
                # 继续下一次尝试
        
        # 阶段2: 所有标准模式尝试都失败,切换到思路导向模式
        print(f"  ⚡ [{task_id}] Switching to process-oriented mode (no answer required)")
        
        prompt = self.generate_process_oriented_prompt(task_data)
        response = self.call_api(prompt, api_name, self.process_oriented_system_prompt)
        
        if response.startswith("API Error"):
            return {
                "success": False,
                "error": response,
                "task_id": task_id
            }
        
        # 思路模式下,只要有内容就算成功(不需要提取答案)
        if len(response.strip()) > 100:  # 确保有足够的内容
            # 添加说明标记
            process_oriented_cot = (
                "[Note: This is a methodology-focused explanation that guides the problem-solving approach "
                "without providing the specific calculated answer.]\n\n" + response.strip()
            )
            
            return {
                "success": True,
                "cot": process_oriented_cot,
                "task_id": task_id,
                "mode": "process_oriented"
            }
        else:
            return {
                "success": False,
                "error": "Process-oriented response too short or empty",
                "task_id": task_id
            }

    def process_single_task(self, task_index, task, api_name, skip_existing):
        """
        处理单个任务 (由线程池调用)
        
        Args:
            task_index: 任务在数据集中的索引
            task: 任务数据
            api_name: 使用的API名称
            skip_existing: 是否跳过已有CoT的任务
            
        Returns:
            包含处理结果的字典
        """
        task_id = task["id"]
        
        # 检查是否跳过
        if skip_existing and task["task"].get("cot", "").strip():
            return {
                "status": "skipped",
                "task_index": task_index,
                "task_id": task_id
            }
        
        # 生成CoT
        result = self.generate_cot_for_task(task, api_name)
        
        if result["success"]:
            return {
                "status": "success",
                "task_index": task_index,
                "task_id": task_id,
                "cot": result["cot"],
                "mode": result.get("mode", "standard")
            }
        else:
            return {
                "status": "failed",
                "task_index": task_index,
                "task_id": task_id,
                "error": result.get("error", "Unknown error")
            }

    def update_stats(self, status, mode=None):
        """线程安全的统计更新"""
        with self.progress_lock:
            self.stats[status] += 1
            self.stats["processed"] += 1
            if mode == "process_oriented":
                self.stats["process_based"] += 1

    def print_progress(self, total_tasks):
        """打印进度信息"""
        with self.progress_lock:
            processed = self.stats["processed"]
            successful = self.stats["successful"]
            skipped = self.stats["skipped"]
            failed = self.stats["failed"]
            process_based = self.stats["process_based"]
            
            percentage = (processed / total_tasks) * 100
            process_info = f" (🔄{process_based} process-based)" if process_based > 0 else ""
            print(f"Progress: [{processed}/{total_tasks}] {percentage:.1f}% "
                f"(✓{successful}{process_info} ⊘{skipped} ✗{failed})")

    def save_task_result(self, task_index, cot):
        """线程安全的保存单个任务结果"""
        with self.save_lock:
            self.dataset[task_index]["task"]["cot"] = cot

    def save_dataset(self):
        """线程安全的保存整个数据集"""
        with self.save_lock:
            with open(DATASET_PATH, 'w', encoding='utf-8') as f:
                json.dump(self.dataset, f, indent=2, ensure_ascii=False)

    def update_dataset_with_cot(self, api_name="qwen3_coder", skip_existing=True):
        """
        并行为所有任务生成CoT并更新数据集
        
        Args:
            api_name: 使用的API名称
            skip_existing: 是否跳过已有CoT的任务
        """
        self.load_dataset()
        
        tasks = self.dataset[1:] if len(self.dataset) > 1 else []
        total_tasks = len(tasks)
        
        print(f"\n{'='*70}")
        print(f"GENERATING CHAIN OF THOUGHT FOR ALL TASKS (PARALLEL)")
        print(f"{'='*70}")
        print(f"Total tasks: {total_tasks}")
        print(f"API: {api_name}")
        print(f"Skip existing CoT: {skip_existing}")
        print(f"Max parallel workers: {self.max_workers}")
        print(f"Strategy: Standard mode (3 attempts) → Process-oriented mode (fallback)")
        print(f"{'='*70}\n")
        
        start_time = time.time()
        
        # 重置统计
        self.stats = {
            "successful": 0,
            "skipped": 0,
            "failed": 0,
            "process_based": 0,
            "processed": 0
        }
        
        # 使用线程池并行处理
        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            # 提交所有任务
            future_to_task = {
                executor.submit(
                    self.process_single_task,
                    i + 1,  # task_index (从1开始,因为0是metadata)
                    task,
                    api_name,
                    skip_existing
                ): (i + 1, task["id"])
                for i, task in enumerate(tasks)
            }
            
            # 处理完成的任务
            for future in as_completed(future_to_task):
                task_index, task_id = future_to_task[future]
                
                try:
                    result = future.result()
                    status = result["status"]
                    
                    if status == "success":
                        # 保存CoT
                        self.save_task_result(result["task_index"], result["cot"])
                        mode = result.get("mode", "standard")
                        self.update_stats("successful", mode)
                        
                        mode_indicator = "🔄" if mode == "process_oriented" else "✓"
                        print(f"{mode_indicator} [{result['task_id']}] CoT generated successfully ({mode} mode)")
                        
                    elif status == "skipped":
                        self.update_stats("skipped")
                        print(f"⊘ [{result['task_id']}] Skipped (existing CoT)")
                        
                    elif status == "failed":
                        self.update_stats("failed")
                        print(f"✗ [{result['task_id']}] Failed: {result.get('error', 'Unknown')}")
                    
                    # 打印进度
                    self.print_progress(total_tasks)
                    
                    # 定期保存(每10个任务)
                    if self.stats["processed"] % 10 == 0:
                        self.save_dataset()
                        print(f"  💾 Progress saved")
                    
                except Exception as e:
                    self.update_stats("failed")
                    print(f"✗ [{task_id}] Exception: {str(e)}")
        
        # 最终保存
        self.save_dataset()
        
        elapsed_time = time.time() - start_time
        
        print(f"\n{'='*70}")
        print(f"COT GENERATION SUMMARY")
        print(f"{'='*70}")
        print(f"✓ Successful: {self.stats['successful']}/{total_tasks}")
        print(f"  - Standard mode (with answer): {self.stats['successful'] - self.stats['process_based']}")
        print(f"  - Process-oriented mode (methodology): {self.stats['process_based']}")
        print(f"⊘ Skipped (existing): {self.stats['skipped']}/{total_tasks}")
        print(f"✗ Failed: {self.stats['failed']}/{total_tasks}")
        print(f"⏱ Total time: {elapsed_time:.1f}s")
        print(f"⚡ Average: {elapsed_time/total_tasks:.2f}s per task")
        print(f"{'='*70}\n")
        
        return {
            "successful": self.stats["successful"],
            "skipped": self.stats["skipped"],
            "failed": self.stats["failed"],
            "process_based": self.stats["process_based"],
            "total": total_tasks,
            "elapsed_time": elapsed_time
        }

    def regenerate_specific_tasks(self, task_ids, api_name="qwen3_coder"):
        """
        并行重新生成指定任务的CoT
        
        Args:
            task_ids: 要重新生成的任务ID列表
            api_name: 使用的API名称
        """
        self.load_dataset()
        
        print(f"\n{'='*70}")
        print(f"REGENERATING COT FOR SPECIFIC TASKS (PARALLEL)")
        print(f"{'='*70}")
        print(f"Task IDs: {', '.join(task_ids)}")
        print(f"API: {api_name}")
        print(f"Max parallel workers: {self.max_workers}")
        print(f"Strategy: Standard mode (3 attempts) → Process-oriented mode (fallback)")
        print(f"{'='*70}\n")
        
        # 查找任务索引
        task_map = {}
        for i, task in enumerate(self.dataset[1:], start=1):
            if task["id"] in task_ids:
                task_map[task["id"]] = (i, task)
        
        # 检查未找到的任务
        not_found = set(task_ids) - set(task_map.keys())
        if not_found:
            print(f"⚠ Tasks not found: {', '.join(not_found)}\n")
        
        if not task_map:
            print("No valid tasks to process")
            return
        
        start_time = time.time()
        
        # 重置统计
        self.stats = {
            "successful": 0,
            "skipped": 0,
            "failed": 0,
            "process_based": 0,
            "processed": 0
        }
        
        # 使用线程池并行处理
        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            future_to_task = {
                executor.submit(
                    self.process_single_task,
                    task_index,
                    task,
                    api_name,
                    False  # 强制重新生成
                ): task_id
                for task_id, (task_index, task) in task_map.items()
            }
            
            for future in as_completed(future_to_task):
                task_id = future_to_task[future]
                
                try:
                    result = future.result()
                    
                    if result["status"] == "success":
                        self.save_task_result(result["task_index"], result["cot"])
                        mode = result.get("mode", "standard")
                        self.update_stats("successful", mode)
                        
                        mode_indicator = "🔄" if mode == "process_oriented" else "✓"
                        print(f"{mode_indicator} [{task_id}] CoT regenerated successfully ({mode} mode)")
                        
                    elif result["status"] == "failed":
                        self.update_stats("failed")
                        print(f"✗ [{task_id}] Failed: {result.get('error', 'Unknown')}")
                    
                except Exception as e:
                    self.update_stats("failed")
                    print(f"✗ [{task_id}] Exception: {str(e)}")
        
        # 最终保存
        self.save_dataset()
        
        elapsed_time = time.time() - start_time
        
        print(f"\n{'='*70}")
        print(f"REGENERATION SUMMARY")
        print(f"{'='*70}")
        print(f"✓ Successful: {self.stats['successful']}/{len(task_map)}")
        print(f"  - Standard mode (with answer): {self.stats['successful'] - self.stats['process_based']}")
        print(f"  - Process-oriented mode (methodology): {self.stats['process_based']}")
        print(f"✗ Failed: {self.stats['failed']}/{len(task_map)}")
        print(f"⏱ Total time: {elapsed_time:.1f}s")
        print(f"{'='*70}\n")
        
if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Generate Chain of Thought for code reasoning tasks (with parallel processing)")
    parser.add_argument("--api", default="qwen3_coder",
    choices=list(AI_APIS.keys()),
    help="API to use for CoT generation")
    parser.add_argument("--no-skip", action="store_true",
    help="Regenerate CoT even if it already exists")
    parser.add_argument("--tasks", nargs='+',
    help="Specific task IDs to regenerate (e.g., SL-MIX-S001 SL-MIX-S002)")
    parser.add_argument("--workers", type=int, default=5,
    help="Number of parallel workers (default: 5, recommended: 3-10)")
    args = parser.parse_args()
    generator = CoTGenerator(max_workers=args.workers)
    if args.tasks:
        generator.regenerate_specific_tasks(args.tasks, api_name=args.api)
    else:
        generator.update_dataset_with_cot(
            api_name=args.api,
            skip_existing=not args.no_skip
        )
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

    def should_evaluate_task(self, task, evaluate_mode="unrated"):
        """
        判断任务是否需要评估
        
        Args:
            task: 任务数据
            evaluate_mode: 评估模式
                - "all": 评估所有任务
                - "unrated": 只评估难度为-1的未评估任务（默认）
                - "difficulty_-1": 只评估难度为-1的任务（别名）
        
        Returns:
            bool: 是否需要评估
        """
        if task.get("metadata", {}).get("language") != "python":
            return False
        
        if evaluate_mode == "all":
            return True
        elif evaluate_mode in ["unrated", "difficulty_-1"]:
            difficulty = task.get("metadata", {}).get("difficulty", -1)
            return difficulty == -1
        else:
            # 可扩展：支持其他筛选模式
            # 例如 "difficulty_0-2" 只评估简单任务
            return False
    
    def evaluate_all_tasks(self, evaluate_mode="unrated"):
        """
        评估任务并根据结果更新难度
        
        Args:
            evaluate_mode: 评估模式
                - "all": 评估所有任务
                - "unrated": 只评估难度为-1的未评估任务（默认）
        """
        self.load_dataset()
        self.evaluation_results.clear()
        
        ai_names = list(AI_APIS.keys())
        
        # 统计信息
        total_tasks = 0
        evaluated_tasks = 0
        skipped_tasks = 0
        
        print(f"\n{'='*70}")
        print(f"AI EVALUATION MODE: {evaluate_mode.upper()}")
        print(f"{'='*70}\n")
        
        for i in range(1, len(self.dataset)):
            task = self.dataset[i]
            if "task" not in task:
                continue
            
            total_tasks += 1
            task_id = task["id"]
            
            # 检查是否需要评估
            if not self.should_evaluate_task(task, evaluate_mode):
                difficulty = task.get("metadata", {}).get("difficulty", "N/A")
                language = task.get("metadata", {}).get("language", "N/A")
                
                if language != "python":
                    reason = "Not Python"
                else:
                    reason = f"Difficulty={difficulty} (skip in '{evaluate_mode}' mode)"
                
                print(f"Skipping task {task_id} ({reason})")
                skipped_tasks += 1
                continue
            
            evaluated_tasks += 1
            expected_answer = task["task"]["answer"]
            original_difficulty = task["metadata"].get("difficulty", -1)
            
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
        
        # 打印统计信息
        print(f"\n{'='*70}")
        print(f"EVALUATION SUMMARY")
        print(f"{'='*70}")
        print(f"Total tasks in dataset: {total_tasks}")
        print(f"Tasks evaluated: {evaluated_tasks}")
        print(f"Tasks skipped: {skipped_tasks}")
        print(f"Evaluation mode: {evaluate_mode}")
        print(f"{'='*70}\n")
        
        # 保存更新后的数据集
        with open(DATASET_PATH, 'w', encoding='utf-8') as f:
            json.dump(self.dataset, f, indent=2, ensure_ascii=False)
        print(f"\nDataset difficulty updated at {DATASET_PATH}")
        
        # 生成统计数据
        if evaluated_tasks > 0:
            print("\nGenerating AI evaluation statistics...")
            summary_stats = self.generate_difficulty_statistics()
            
            # 创建简洁的任务详情
            task_details = {}
            for task_id, results in sorted(self.evaluation_results.items()):
                task_details[task_id] = results["result_line"]
            
            # 组合成最终报告
            final_report = {
                "evaluation_mode": evaluate_mode,
                "statistics": {
                    "total_tasks": total_tasks,
                    "evaluated_tasks": evaluated_tasks,
                    "skipped_tasks": skipped_tasks
                },
                "evaluation_summary": summary_stats,
                "task_details": task_details
            }
            
            # 保存报告
            report_path = "data/ai_evaluation_with_difficulty.json"
            with open(report_path, 'w', encoding='utf-8') as f:
                json.dump(final_report, f, indent=2, ensure_ascii=False)
            
            print(f"Summarized evaluation report saved to {report_path}")
        else:
            print("\nNo tasks were evaluated - skipping report generation")
        
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
    print("\n" + "="*70)
    print("EXECUTING TASKS ONLY")
    print("="*70)
    executor = TaskExecutor()
    executor.execute_all_tasks()
    print("✓ Task execution completed\n")

def run_cot_only(api_name="qwen3_coder", skip_existing=True, specific_tasks=None):
    """只生成思维链(CoT)"""
    print("\n" + "="*70)
    print("GENERATING CHAIN OF THOUGHT ONLY")
    print("="*70)
    cot_generator = CoTGenerator()
    
    if specific_tasks:
        # 重新生成特定任务
        cot_generator.regenerate_specific_tasks(specific_tasks, api_name=api_name)
    else:
        # 生成所有任务的CoT
        result = cot_generator.update_dataset_with_cot(
            api_name=api_name,
            skip_existing=skip_existing
        )
        print(f"✓ CoT generation completed: {result['successful']} successful, "
              f"{result['failed']} failed, {result['skipped']} skipped\n")

def run_evaluation_only(evaluate_mode="unrated"):
    """
    只评估AI模型正确性
    
    Args:
        evaluate_mode: 评估模式
            - "all": 评估所有任务
            - "unrated": 只评估难度为-1的未评估任务（默认）
    """
    print("\n" + "="*70)
    print(f"RUNNING AI EVALUATION ONLY (Mode: {evaluate_mode.upper()})")
    print("="*70)
    evaluator = AIEvaluator()
    evaluator.evaluate_all_tasks(evaluate_mode=evaluate_mode)
    print("✓ AI evaluation completed\n")

def run_generate_task_only(num_tasks=1):
    """只生成新任务"""
    print("\n" + "="*70)
    print(f"GENERATING {num_tasks} NEW TASK(S) ONLY")
    print("="*70)
    
    successful_generations = 0
    task_generator = TaskGenerator()
    
    for i in range(num_tasks):
        print(f"\n[Task {i+1}/{num_tasks}]")
        try:
            new_task = task_generator.generate_and_validate_task()
            if new_task:
                successful_generations += 1
                print(f"✓ Task {i+1} generated successfully (ID: {new_task['id']})")
            else:
                print(f"✗ Task {i+1} generation failed")
        except Exception as e:
            print(f"✗ Task {i+1} generation failed with error: {e}")
    
    print(f"\n{'='*70}")
    print(f"GENERATION SUMMARY: {successful_generations}/{num_tasks} tasks generated")
    print(f"{'='*70}\n")
    return successful_generations > 0

def run_single_cycle(cot_api="qwen3_coder", cot_skip_existing=True, 
                     eval_mode="unrated"):
    """
    运行一个完整的循环
    
    Args:
        cot_api: CoT生成使用的API
        cot_skip_existing: 是否跳过已存在的CoT
        eval_mode: 评估模式 ("all" 或 "unrated")
    """
    print("\n" + "="*70)
    print("STARTING NEW COMPLETE CYCLE")
    print("="*70)
    
    # 1. 执行任务
    print("\n[1/4] Executing tasks...")
    executor = TaskExecutor()
    executor.execute_all_tasks()
    
    # 2. 生成思维链
    print("\n[2/4] Generating chain of thought...")
    cot_generator = CoTGenerator()
    cot_result = cot_generator.update_dataset_with_cot(
        api_name=cot_api,
        skip_existing=cot_skip_existing
    )
    print(f"CoT: {cot_result['successful']} successful, "
          f"{cot_result['failed']} failed, {cot_result['skipped']} skipped")
    
    # 3. AI评估
    print(f"\n[3/4] Running AI evaluation (mode: {eval_mode})...")
    evaluator = AIEvaluator()
    evaluator.evaluate_all_tasks(evaluate_mode=eval_mode)
    
    # 4. 生成新任务
    print("\n[4/4] Generating new task...")
    task_generator = TaskGenerator()
    new_task = task_generator.generate_and_validate_task()
    
    print("\n" + "="*70)
    print("CYCLE COMPLETED")
    print("="*70 + "\n")
    return new_task is not None

def run_multiple_cycles(num_cycles=5, cot_api="qwen3_coder", 
                       cot_skip_existing=True, eval_mode="unrated"):
    """
    运行多个循环
    
    Args:
        num_cycles: 循环次数
        cot_api: CoT生成使用的API
        cot_skip_existing: 是否跳过已存在的CoT
        eval_mode: 评估模式 ("all" 或 "unrated")
    """
    print(f"\n{'='*70}")
    print(f"STARTING {num_cycles} COMPLETE CYCLES")
    print(f"{'='*70}\n")
    
    successful_cycles = 0
    for i in range(num_cycles):
        print(f"\n{'#'*70}")
        print(f"# CYCLE {i+1}/{num_cycles}")
        print(f"{'#'*70}")
        
        try:
            success = run_single_cycle(
                cot_api=cot_api,
                cot_skip_existing=cot_skip_existing,
                eval_mode=eval_mode
            )
            if success:
                successful_cycles += 1
                print(f"✓ Cycle {i+1} completed successfully")
            else:
                print(f"✗ Cycle {i+1} failed")
        except Exception as e:
            print(f"✗ Cycle {i+1} failed with error: {e}")
            import traceback
            traceback.print_exc()
    
    print(f"\n{'='*70}")
    print(f"ALL CYCLES COMPLETED")
    print(f"{'='*70}")
    print(f"Success Rate: {successful_cycles}/{num_cycles} cycles")
    print(f"{'='*70}\n")

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(
        description="Run the complete task generation and evaluation pipeline",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # 运行单个完整循环（只评估未评估的任务）
  python main_loop.py --single
  
  # 运行单个循环并评估所有任务
  python main_loop.py --single --eval-all
  
  # 运行5个循环
  python main_loop.py --cycles 5
  
  # 只执行代码
  python main_loop.py --execute
  
  # 只生成CoT（使用特定API）
  python main_loop.py --cot --cot-api qwen3_235b
  
  # 重新生成所有CoT（包括已存在的）
  python main_loop.py --cot --no-skip-cot
  
  # 重新生成特定任务的CoT
  python main_loop.py --cot --cot-tasks SL-MIX-S001 SL-MIX-S002
  
  # 只评估未评估的任务（默认）
  python main_loop.py --evaluate
  
  # 评估所有任务
  python main_loop.py --evaluate --eval-all
  
  # 只生成10个新任务
  python main_loop.py --generate 10
        """
    )
    
    # 单独执行选项
    parser.add_argument("--execute", action="store_true", 
                       help="Only execute tasks and generate answers")
    parser.add_argument("--cot", action="store_true", 
                       help="Only generate chain of thought")
    parser.add_argument("--evaluate", action="store_true", 
                       help="Only run AI evaluation")
    parser.add_argument("--generate", type=int, nargs='?', const=1, metavar='N',
                       help="Only generate N new tasks (default=1)")
    
    # CoT相关参数
    parser.add_argument("--cot-api", type=str, default="qwen3_coder",
                       help="API to use for CoT generation (default: qwen3_coder)")
    parser.add_argument("--no-skip-cot", action="store_true",
                       help="Regenerate CoT even if it already exists")
    parser.add_argument("--cot-tasks", nargs='+', metavar='TASK_ID',
                       help="Specific task IDs to regenerate CoT for")
    
    # 评估相关参数（新增）
    parser.add_argument("--eval-all", action="store_true",
                       help="Evaluate ALL tasks (default: only unrated tasks with difficulty=-1)")
    
    # 完整流程选项
    parser.add_argument("--single", action="store_true", 
                       help="Run a single complete cycle")
    parser.add_argument("--cycles", type=int, default=1, metavar='N',
                       help="Number of complete cycles to run (default=1)")
    
    args = parser.parse_args()
    
    # 确定评估模式
    eval_mode = "all" if args.eval_all else "unrated"
    
    try:
        # 单独执行选项（互斥）
        if args.execute:
            run_execute_only()
        elif args.cot:
            run_cot_only(
                api_name=args.cot_api,
                skip_existing=not args.no_skip_cot,
                specific_tasks=args.cot_tasks
            )
        elif args.evaluate:
            run_evaluation_only(evaluate_mode=eval_mode)
        elif args.generate is not None:
            run_generate_task_only(args.generate)
        elif args.single:
            run_single_cycle(
                cot_api=args.cot_api,
                cot_skip_existing=not args.no_skip_cot,
                eval_mode=eval_mode
            )
        else:
            # 默认行为：运行指定数量的完整循环
            run_multiple_cycles(
                num_cycles=args.cycles,
                cot_api=args.cot_api,
                cot_skip_existing=not args.no_skip_cot,
                eval_mode=eval_mode
            )
            
    except KeyboardInterrupt:
        print("\n\n⚠️  Process interrupted by user")
        sys.exit(130)
    except Exception as e:
        print(f"\n\n❌ Error occurred: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
```

## data

### ai_evaluation_with_difficulty.json

```

```

### answer.json

```json
{
  "SL-MIX-S0001": {
    "success": true,
    "result": 17
  },
  "SL-MIX-S0002": {
    "success": true,
    "result": 12
  },
  "SL-MIX-S0003": {
    "success": true,
    "result": 5
  },
  "SL-MIX-S0004": {
    "success": true,
    "result": 22
  },
  "SL-MIX-S0005": {
    "success": true,
```

### TreecEva_data.json

```json
[
  {
    "background": "I am developing a comprehensive evaluation benchmark for large language models in the code reasoning domain. This benchmark specifically focuses on assessing statement-level reasoning capabilities of LLMs across multiple computational paradigms: (1) Arithmetic Operations - including basic arithmetic (addition, subtraction, multiplication, division), advanced mathematical operations (exponentiation, logarithms, trigonometric functions), bitwise operations (AND, OR, XOR, shift operations), and composite calculations combining multiple operation types; (2) Boolean Logic - encompassing comparison operations (equality, inequality, relational comparisons), logical operations (AND, OR, NOT), and short-circuit evaluation patterns; (3) Variable Assignment - including simple assignments, multiple simultaneous assignments, tuple unpacking, and destructuring assignments; (4) Control Flow and Data Structures - covering conditional statements, loops, and basic container operations; (5) Complex Mixed Scenarios - integrating multiple reasoning types in sophisticated logical chains.",
    "requirements": "Generate additional examples following the provided template format with these specific criteria: (1) Create significantly more complex code samples with extended logical reasoning chains requiring multiple inference steps; (2) Ensure each example has a unique, deterministic answer that can be computed through step-by-step execution; (3) Maintain strict format consistency across all generated examples, matching the exact structure and field organization of the provided samples; (4) Incorporate diverse programming languages and paradigms while maintaining code complexity at an advanced level suitable for challenging LLM reasoning capabilities; (5) Minimize reliance on external library functions and API calls, focusing instead on algorithmic reasoning with basic language constructs."
  },
  {
    "id": "SL-MIX-S0001",
    "metadata": {
      "category": "Statement-Level",
      "language": "python",
      "difficulty": 5,
      "intervention": 5
    },
    "task": {
      "description": "What is the value of variable 'result_value' after executing the statement 'result_value = total_variance ^ product_count'?",
      "code": "# Sales matrix: rows are products, columns are regions\nsales_matrix = [\n    [25, 30, 28, 35],\n    [15, 20, 18, 22],\n    [40, 35, 38, 42],\n    [12, 15, 10, 14]\n]\n\n# Step 1: Find products with total sales > 100\nhigh_sales_products = []\nfor product_sales in sales_matrix:\n    total_sales = sum(product_sales)\n    if total_sales > 100:\n        high_sales_products.append(product_sales)\n\n# Step 2: Calculate variance for each high-sales product\nvariances = []\nfor product_sales in high_sales_products:\n    mean = sum(product_sales) / len(product_sales)\n    squared_diffs = [(x - mean) ** 2 for x in product_sales]\n    variance = sum(squared_diffs) / len(squared_diffs)\n    variances.append(int(variance))\n\n# Step 3: XOR operation\nproduct_count = len(high_sales_products)\ntotal_variance = sum(variances)\nresult_value = total_variance ^ product_count\n\nprint(f\"Result: {result_value}\")",
      "answer": 17,
      "cot": ""
    }
  },
  {
    "id": "SL-MIX-S0002",
    "metadata": {
      "category": "Statement-Level",
      "language": "python",
      "difficulty": 5,
      "intervention": 6
    },
    "task": {
      "description": "What is the value of variable 'strength_code' after executing the statement 'strength_code = (strength_level << 2) | (digit_count & 0x3)'?",
      "code": "password = \"SecurePass2024\"\n\n# Step 1: Count character types\nuppercase_count = sum(1 for c in password if c.isupper())\nlowercase_count = sum(1 for c in password if c.islower())\ndigit_count = sum(1 for c in password if c.isdigit())\n\n# Step 2: Calculate base score with weights\nbase_score = uppercase_count * 3 + lowercase_count * 2 + digit_count * 4\n\n# Step 3: Check for common patterns and apply penalty\nhas_consecutive = False\nfor i in range(len(password) - 1):\n    if ord(password[i+1]) - ord(password[i]) == 1:\n        has_consecutive = True\n        break\n\npenalty = 5 if has_consecutive else 0\nadjusted_score = base_score - penalty\n\n# Step 4: Encode strength using bitwise operations\nstrength_level = adjusted_score // 10\nstrength_code = (strength_level << 2) | (digit_count & 0x3)\n\nprint(f\"Result: {strength_code}\")",
      "answer": 12,
      "cot": ""
    }
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
    "GLM-4.6": {
        "base_url": BASE_URL,
        "api_key": API_KEY,
        "model": "GLM-4.6"
    },
    "DeepSeek-V3.2-Exp": {
        "base_url": BASE_URL,
        "api_key": API_KEY,
        "model": "DeepSeek-V3.2-Exp"
    },
    "DeepSeek-V3.1": {
        "base_url": BASE_URL,
        "api_key": API_KEY,
        "model": "DeepSeek-V3.1"
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







49\56\61\64\77\80\93\97\98

112\116\121\131\153\154\161\162\172\184\186\194\198\200

203\209\11\19\26\28\31\33\51\54\63\64\70\72\73\76\79\85\86\99

3 11 29 33 48 55 57 60 81 84 94 99



4

1 12 22 24 27 29 30 37 42 45 60 66 70 72 76 78 79 80 86 92 95 96



5

7 21 24 25 26 31 32 35 44 49 50 51 53 57 70 72 75 90 95 100



6

2 6 13 16 19 22 26 27 33 40 46 70 86

7

8 20 27 28 38 40 48 61 64 78 79 85 90 98 

8

11 12 14 16 21 26 44 46 49 55 56 58 60 77 87 92 96



1 7 11 16 25 31 35 42 45 51 53 63 66 72 
