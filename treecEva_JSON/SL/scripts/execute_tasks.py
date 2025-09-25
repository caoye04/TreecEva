import json
import subprocess
import os
import tempfile
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from config import DATASET_PATH, ANSWER_PATH, TEMP_CODE_DIR

class TaskExecutor:
    def __init__(self):
        self.results = {}
        
    def execute_python_code(self, code, task_id):
        """执行Python代码"""
        try:
            # 创建临时文件
            temp_file = os.path.join(TEMP_CODE_DIR, f"{task_id}.py")
            with open(temp_file, 'w', encoding='utf-8') as f:
                f.write(code)
            
            # 执行代码
            result = subprocess.run(
                [sys.executable, temp_file],
                capture_output=True,
                text=True,
                timeout=30
            )
            
            if result.returncode == 0:
                # 提取输出中的数值
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
            temp_cpp = os.path.join(TEMP_CODE_DIR, f"{task_id}.cpp")
            temp_exe = os.path.join(TEMP_CODE_DIR, f"{task_id}.exe")
            
            # 写入源文件
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
            
            # 执行
            run_result = subprocess.run(
                [temp_exe],
                capture_output=True,
                text=True,
                timeout=30
            )
            
            if run_result.returncode == 0:
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
    
    def execute_java_code(self, code, task_id):
        """执行Java代码"""
        try:
            temp_java = os.path.join(TEMP_CODE_DIR, f"{task_id}.java")
            
            # 写入源文件
            with open(temp_java, 'w', encoding='utf-8') as f:
                f.write(code)
            
            # 编译
            compile_result = subprocess.run(
                ["javac", temp_java],
                capture_output=True,
                text=True,
                timeout=30,
                cwd=TEMP_CODE_DIR
            )
            
            if compile_result.returncode != 0:
                return {
                    "success": False,
                    "error": f"Compilation error: {compile_result.stderr}"
                }
            
            # 执行
            class_name = task_id  # 假设类名与文件名相同
            run_result = subprocess.run(
                ["java", class_name],
                capture_output=True,
                text=True,
                timeout=30,
                cwd=TEMP_CODE_DIR
            )
            
            if run_result.returncode == 0:
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
            temp_c = os.path.join(TEMP_CODE_DIR, f"{task_id}.c")
            temp_exe = os.path.join(TEMP_CODE_DIR, f"{task_id}.exe")
            
            # 写入源文件
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
            
            # 执行
            run_result = subprocess.run(
                [temp_exe],
                capture_output=True,
                text=True,
                timeout=30
            )
            
            if run_result.returncode == 0:
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
        import re
        
        # 常见的结果输出模式
        patterns = [
            r'Final result:\s*(\d+)',
            r'Target result:\s*(\d+)', 
            r'Master result:\s*(\d+)',
            r'Final output:\s*(\d+)',
            r'Final computation result:\s*(\d+)',
            r'Result:\s*(\d+)',
            r'Answer:\s*(\d+)',
            r'^(\d+)$'  # 只有数字的情况
        ]
        
        for pattern in patterns:
            match = re.search(pattern, output, re.MULTILINE | re.IGNORECASE)
            if match:
                return {
                    "success": True,
                    "result": int(match.group(1))
                }
        
        # 如果没有匹配到模式，尝试提取最后一个数字
        numbers = re.findall(r'\d+', output)
        if numbers:
            return {
                "success": True,
                "result": int(numbers[-1])
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
        expected_answer = task_data["task"]["answer"]
        
        print(f"Executing task {task_id} ({language})...")
        
        if language == "python":
            result = self.execute_python_code(code, task_id)
        elif language in ["cpp", "c++"]:
            result = self.execute_cpp_code(code, task_id)
        elif language == "java":
            result = self.execute_java_code(code, task_id)
        elif language == "c":
            result = self.execute_c_code(code, task_id)
        else:
            result = {
                "success": False,
                "error": f"Unsupported language: {language}"
            }
        
        # 验证结果
        if result["success"]:
            actual_result = result["result"]
            if actual_result == expected_answer:
                result["correct"] = True
            else:
                result["correct"] = False
                result["expected"] = expected_answer
                result["actual"] = actual_result
        
        return result
    
    def execute_all_tasks(self):
        """执行所有任务"""
        # 读取数据集
        with open(DATASET_PATH, 'r', encoding='utf-8') as f:
            dataset = json.load(f)
        
        # 跳过第一个元素（背景信息）
        tasks = dataset[1:] if len(dataset) > 1 else []
        
        for task in tasks:
            if "task" in task and "code" in task["task"]:
                result = self.execute_task(task)
                self.results[task["id"]] = result
        
        # 保存结果
        with open(ANSWER_PATH, 'w', encoding='utf-8') as f:
            json.dump(self.results, f, indent=2, ensure_ascii=False)
        
        print(f"Execution completed. Results saved to {ANSWER_PATH}")
        return self.results

if __name__ == "__main__":
    executor = TaskExecutor()
    executor.execute_all_tasks()