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
    
    def call_api(self, prompt, api_name="DeepSeek-V3.2-Exp", system_prompt=None):
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

    def generate_cot_for_task(self, task_data, api_name="DeepSeek-V3.2-Exp", max_retries=3):
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

    def update_dataset_with_cot(self, api_name="DeepSeek-V3.2-Exp", skip_existing=True):
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

    def regenerate_specific_tasks(self, task_ids, api_name="DeepSeek-V3.2-Exp"):
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
    parser.add_argument("--api", default="DeepSeek-V3.2-Exp",
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