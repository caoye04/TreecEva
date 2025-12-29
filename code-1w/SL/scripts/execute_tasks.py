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
    
    def extract_result_from_output(self, output):
        """从输出中提取结果 - 直接从字符串解析，保持原始精度"""
        patterns = [
            r'Final result:\s*(-?\d+(?:\.\d+)?)',
            r'Target result:\s*(-?\d+(?:\.\d+)?)', 
            r'Master result:\s*(-?\d+(?:\.\d+)?)',
            r'Final output:\s*(-?\d+(?:\.\d+)?)',
            r'Result:\s*(-?\d+(?:\.\d+)?)',
            r'Answer:\s*(-?\d+(?:\.\d+)?)',
        ]
        
        for pattern in patterns:
            match = re.search(pattern, output, re.MULTILINE | re.IGNORECASE)
            if match:
                value_str = match.group(1)
                # 直接使用字符串中的值，保持原样
                if '.' in value_str:
                    result = float(value_str)
                else:
                    result = int(value_str)
                
                return {
                    "success": True,
                    "result": result
                }
        
        # 提取最后一个数字
        numbers = re.findall(r'-?\d+(?:\.\d+)?', output)
        if numbers:
            value_str = numbers[-1]
            # 直接使用字符串中的值，保持原样
            if '.' in value_str:
                result = float(value_str)
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
                    # 直接使用原始结果，不做任何处理
                    dataset[i + 1]["task"]["answer"] = result["result"]
                    print(f"✓ Task {task['id']}: Answer updated to {result['result']}")
                    
                    # 调试：打印实际保存到dataset中的值
                    print(f"  DEBUG: Value in dataset object = {dataset[i + 1]['task']['answer']}")
                    print(f"  DEBUG: Value in results dict = {result['result']}")
                    print(f"  DEBUG: Are they equal? {dataset[i + 1]['task']['answer'] == result['result']}")
                else:
                    if task.get("metadata", {}).get("language") == "python":
                        print(f"✗ Task {task['id']}: Execution failed - {result.get('error', 'Unknown error')}")
        
        # 保存执行结果到answer.json
        print("\nSaving to answer.json...")
        with open(ANSWER_PATH, 'w', encoding='utf-8') as f:
            json.dump(self.results, f, indent=2, ensure_ascii=False)
        
        # 保存更新后的数据集
        print("Saving to dataset...")
        with open(DATASET_PATH, 'w', encoding='utf-8') as f:
            json.dump(dataset, f, indent=2, ensure_ascii=False)
        
        # 验证保存结果
        print("\n=== Verification ===")
        with open(DATASET_PATH, 'r', encoding='utf-8') as f:
            saved_dataset = json.load(f)
        
        with open(ANSWER_PATH, 'r', encoding='utf-8') as f:
            saved_results = json.load(f)
        
        # 检查前3个任务
        check_count = min(3, len(tasks))
        for i in range(check_count):
            task = tasks[i]
            task_id = task["id"]
            if task_id in self.results and self.results[task_id]["success"]:
                dataset_value = saved_dataset[i + 1]["task"]["answer"]
                answer_value = saved_results[task_id]["result"]
                
                print(f"\nTask {task_id}:")
                print(f"  In dataset.json: {dataset_value} (type: {type(dataset_value).__name__})")
                print(f"  In answer.json:  {answer_value} (type: {type(answer_value).__name__})")
                print(f"  Match: {dataset_value == answer_value}")
        
        print(f"\nExecution completed. Results saved to {ANSWER_PATH}")
        print(f"Dataset answers updated at {DATASET_PATH}")
        return self.results

if __name__ == "__main__":
    executor = TaskExecutor()
    executor.execute_all_tasks()