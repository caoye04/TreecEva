# test_cot/generate_cot_gdb.py
import json
import subprocess
import os
import re
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent.parent))
from config import AI_APIS
import openai

class GDBCoTGenerator:
    def __init__(self, case_file="case.json"):
        self.case_file = case_file
        self.case_data = None
        self.gdb_output = None
        self.temp_dir = "temp_gdb"
        os.makedirs(self.temp_dir, exist_ok=True)
        
    def load_case(self):
        """加载单个测试case"""
        with open(self.case_file, 'r', encoding='utf-8') as f:
            self.case_data = json.load(f)
        print(f"✓ Loaded case: {self.case_data['id']}")
        
    def get_cot_sentences_requirement(self):
        """根据难度决定CoT句数要求"""
        difficulty = self.case_data["metadata"]["difficulty"]
        
        if difficulty <= 3:
            return {
                "count": "3-5",
                "description": "3 to 5 sentences",
                "max_tokens": 400
            }
        elif difficulty == 4:
            return {
                "count": "5-10",
                "description": "5 to 10 sentences",
                "max_tokens": 800
            }
        else:  # difficulty == 5
            return {
                "count": "unlimited",
                "description": "as many sentences as needed (no limit, but be comprehensive)",
                "max_tokens": 1500
            }
    
    def create_gdb_commands(self, language, source_file):
        """根据语言创建GDB命令文件"""
        commands = []
        
        if language == "python":
            # Python的GDB调试相对复杂，我们使用print插桩的方式
            return None
        
        elif language in ["cpp", "c++", "c"]:
            # C/C++的GDB断点策略
            commands = [
                "set pagination off",
                "set print pretty on",
                "break main",
                "run",
                ""
            ]
            
            # 尝试识别关键变量和循环
            with open(source_file, 'r', encoding='utf-8') as f:
                code = f.read()
            
            # 查找关键变量声明
            var_patterns = [
                r'(?:int|float|double|uint32_t|uint64_t|long)\s+(\w+)\s*=',
                r'(\w+)\s*=.*(?:result|sum|count|total|value)',
            ]
            
            key_vars = set()
            for pattern in var_patterns:
                matches = re.findall(pattern, code, re.IGNORECASE)
                key_vars.update(matches)
            
            # 限制变量数量
            key_vars = list(key_vars)[:15]
            
            # 查找循环和条件语句的行号
            lines = code.split('\n')
            breakpoint_lines = []
            
            for i, line in enumerate(lines, 1):
                if re.search(r'\bfor\s*\(', line) or re.search(r'\bwhile\s*\(', line):
                    # 在循环体内设置断点
                    breakpoint_lines.append(i + 1)
                elif re.search(r'\bif\s*\(', line):
                    breakpoint_lines.append(i + 1)
            
            # 限制断点数量（每5个循环/条件设一个断点）
            breakpoint_lines = breakpoint_lines[::5][:8]
            
            # 添加断点和变量监控
            for line_num in breakpoint_lines:
                commands.append(f"break {line_num}")
            
            # 添加条件断点（在关键计算后）
            commands.extend([
                "continue",
                # 显示关键变量
            ])
            
            for var in key_vars:
                commands.append(f"print {var}")
            
            # 继续执行并在多个点采样
            for _ in range(5):
                commands.extend([
                    "continue",
                    "info locals",
                ])
            
            commands.extend([
                "continue",
                "quit",
                "y"
            ])
            
        return commands
    
    def insert_python_trace(self, code):
        """为Python代码插入追踪语句"""
        lines = code.split('\n')
        traced_lines = []
        trace_points = []
        
        indent_level = 0
        for i, line in enumerate(lines):
            traced_lines.append(line)
            
            # 计算缩进
            stripped = line.lstrip()
            if stripped:
                current_indent = len(line) - len(stripped)
                
                # 在关键操作后插入trace
                if '=' in line and not line.strip().startswith('#'):
                    # 提取变量名
                    var_match = re.match(r'\s*(\w+)\s*=', line)
                    if var_match:
                        var_name = var_match.group(1)
                        # 跳过一些不重要的变量
                        if var_name not in ['i', 'j', 'k', '_', 'temp']:
                            indent = ' ' * current_indent
                            trace_line = f"{indent}print(f'[TRACE] Line {i+1}: {var_name} = {{{var_name}}}')"
                            traced_lines.append(trace_line)
                            trace_points.append((i+1, var_name))
                
                # 在循环开始处插入trace
                if re.match(r'\s*for\s+', line) or re.match(r'\s*while\s+', line):
                    indent = ' ' * (current_indent + 4)
                    trace_line = f"{indent}print(f'[TRACE] Loop at line {i+1}')"
                    traced_lines.append(trace_line)
        
        return '\n'.join(traced_lines), trace_points
    
    def run_with_gdb(self, language, code):
        """使用GDB运行代码并收集中间状态"""
        if language == "python":
            return self.run_python_with_trace(code)
        else:
            return self.run_cpp_with_gdb(language, code)
    
    def run_python_with_trace(self, code):
        """运行带追踪的Python代码"""
        traced_code, trace_points = self.insert_python_trace(code)
        
        temp_file = os.path.join(self.temp_dir, "traced_code.py")
        with open(temp_file, 'w', encoding='utf-8') as f:
            f.write(traced_code)
        
        try:
            result = subprocess.run(
                [sys.executable, temp_file],
                capture_output=True,
                text=True,
                timeout=30
            )
            
            output = result.stdout + result.stderr
            
            # 提取TRACE信息
            trace_lines = [line for line in output.split('\n') if '[TRACE]' in line]
            
            return {
                "success": True,
                "trace_output": '\n'.join(trace_lines),
                "full_output": output,
                "trace_points": len(trace_points)
            }
            
        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }
    
    def run_cpp_with_gdb(self, language, code):
        """运行C/C++代码与GDB"""
        # 编译代码
        ext = "cpp" if language in ["cpp", "c++"] else "c"
        source_file = os.path.join(self.temp_dir, f"code.{ext}")
        exe_file = os.path.join(self.temp_dir, "code.exe")
        
        # 添加调试符号
        with open(source_file, 'w', encoding='utf-8') as f:
            f.write(code)
        
        # 编译
        compiler = "g++" if language in ["cpp", "c++"] else "gcc"
        compile_cmd = [compiler, "-g", "-O0", source_file, "-o", exe_file, "-lm", "-std=c++17" if language in ["cpp", "c++"] else "-std=c99"]
        
        compile_result = subprocess.run(compile_cmd, capture_output=True, text=True)
        if compile_result.returncode != 0:
            return {
                "success": False,
                "error": f"Compilation failed: {compile_result.stderr}"
            }
        
        # 创建GDB命令
        gdb_commands = self.create_gdb_commands(language, source_file)
        if not gdb_commands:
            return {"success": False, "error": "Could not create GDB commands"}
        
        cmd_file = os.path.join(self.temp_dir, "gdb_commands.txt")
        with open(cmd_file, 'w', encoding='utf-8') as f:
            f.write('\n'.join(gdb_commands))
        
        # 运行GDB
        try:
            gdb_result = subprocess.run(
                ["gdb", "-batch", "-x", cmd_file, exe_file],
                capture_output=True,
                text=True,
                timeout=30
            )
            
            output = gdb_result.stdout + gdb_result.stderr
            
            # 解析GDB输出
            variable_snapshots = self.parse_gdb_output(output)
            
            return {
                "success": True,
                "gdb_output": output,
                "variable_snapshots": variable_snapshots,
                "snapshot_count": len(variable_snapshots)
            }
            
        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }
    
    def parse_gdb_output(self, output):
        """解析GDB输出，提取变量快照"""
        snapshots = []
        current_snapshot = {}
        
        lines = output.split('\n')
        for line in lines:
            # 匹配变量打印输出 "$1 = value"
            var_match = re.match(r'\$\d+\s*=\s*(.+)', line)
            if var_match:
                value = var_match.group(1).strip()
                current_snapshot[f"var_{len(current_snapshot)}"] = value
            
            # 匹配 "Breakpoint N, ..."
            if 'Breakpoint' in line or 'Continuing' in line:
                if current_snapshot:
                    snapshots.append(current_snapshot.copy())
                    current_snapshot = {}
        
        if current_snapshot:
            snapshots.append(current_snapshot)
        
        return snapshots
    
    def generate_cot_with_gdb_info(self):
        """使用GDB信息生成增强的CoT"""
        language = self.case_data["metadata"]["language"]
        code = self.case_data["task"]["code"]
        description = self.case_data["task"]["description"]
        answer = self.case_data["task"]["answer"]
        difficulty = self.case_data["metadata"]["difficulty"]
        
        # 获取CoT句数要求
        cot_requirement = self.get_cot_sentences_requirement()
        
        print(f"\n{'='*70}")
        print(f"Running GDB analysis for {language} code...")
        print(f"Difficulty: {difficulty} -> CoT requirement: {cot_requirement['description']}")
        print(f"{'='*70}")
        
        # 运行GDB分析
        gdb_result = self.run_with_gdb(language, code)
        
        if not gdb_result["success"]:
            print(f"✗ GDB analysis failed: {gdb_result.get('error')}")
            return None
        
        # 构建包含GDB信息的提示
        if language == "python":
            trace_info = gdb_result["trace_output"]
            analysis_info = f"""
The code was executed with variable tracing. Key intermediate values observed:

{trace_info[:2000]}  # 限制长度

Total trace points captured: {gdb_result["trace_points"]}
"""
        else:
            snapshots = gdb_result["variable_snapshots"]
            snapshot_summary = "\n".join([
                f"Snapshot {i+1}: {snapshot}" 
                for i, snapshot in enumerate(snapshots[:5])
            ])
            analysis_info = f"""
The code was debugged with GDB. Variable states at key execution points:

{snapshot_summary}

Total snapshots captured: {gdb_result["snapshot_count"]}
"""
        
        # 根据难度构建不同的提示
        if difficulty <= 3:
            sentence_instruction = f"""
Generate a concise chain of thought in {cot_requirement['description']}:

Structure:
1. Sentence 1: Describe initialization with specific values from debugger
2. Sentence 2: Explain the first major computation step with intermediate results
3. Sentence 3: Describe the second major computation step with intermediate results
4. Sentence 4 (optional): Explain additional computation steps if needed
5. Last sentence: State how the final answer {answer} is derived

Each sentence should be 25-40 words and reference specific values when possible.
"""
        elif difficulty == 4:
            sentence_instruction = f"""
Generate a detailed chain of thought in {cot_requirement['description']}:

Structure:
1. Sentence 1: Initialization phase with specific values
2. Sentences 2-4: Major computation phases (one phase per sentence)
3. Sentences 5-8: Intermediate transformations and aggregations
4. Sentences 9-10 (optional): Additional complex steps if needed
5. Last sentence: Final derivation of answer {answer}

Each sentence should be 25-40 words and include specific intermediate values.
"""
        else:  # difficulty == 5
            sentence_instruction = f"""
Generate a comprehensive chain of thought with {cot_requirement['description']}:

You should cover ALL significant computation steps. Do NOT limit yourself.

Structure:
- Initial sentences: Setup and initialization with all key variables
- Multiple middle sentences: EVERY major computation step, loop iteration, conditional branch, transformation
- Each step should have its own sentence with specific values
- Final sentences: Aggregation and final answer derivation

Each sentence should be 25-45 words and must include specific variable values from debugger output.
Be thorough and detailed - this is complex code that requires comprehensive explanation.
"""
        
        # 调用API
        api_name = "qwen3_235b"
        api_config = AI_APIS[api_name]
        
        prompt = f"""
You are analyzing code execution with detailed runtime information from a debugger.

Task: {description}
Final Answer: {answer}
Code Difficulty Level: {difficulty} (0=easy, 5=extremely complex)

Code:
```{language}
{code[:1500]}  # 限制代码长度
```
Debugger Analysis:
{analysis_info}

{sentence_instruction}

Format your response as:
First: [sentence]
Second: [sentence]
Third: [sentence]
Fourth: [sentence]
...
Last: [sentence deriving answer {answer}]

Provide ONLY the numbered sentences, no other text.
"""
        client = openai.OpenAI(
            api_key=api_config['api_key'],
            base_url=api_config['base_url']
        )
        
        try:
            print(f"\nGenerating enhanced CoT with {api_config['model']}...")
            response = client.chat.completions.create(
                model=api_config['model'],
                messages=[
                    {
                        "role": "system",
                        "content": "You are an expert at analyzing code execution with debugger information. Provide detailed, value-specific explanations."
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                temperature=0.3,
                max_tokens=cot_requirement['max_tokens']
            )
            
            cot = response.choices[0].message.content
            
            print(f"\n{'='*70}")
            print("Generated CoT:")
            print(f"{'='*70}")
            print(cot)
            print(f"{'='*70}")
            
            return {
                "cot": cot,
                "gdb_analysis": analysis_info,
                "gdb_result": gdb_result,
                "cot_requirement": cot_requirement
            }
            
        except Exception as e:
            print(f"✗ API call failed: {e}")
            return None

    def save_result(self, result):
        """保存结果到文件"""
        if not result:
            return
        
        output = {
            "case_id": self.case_data["id"],
            "difficulty": self.case_data["metadata"]["difficulty"],
            "cot_requirement": result["cot_requirement"]["description"],
            "enhanced_cot": result["cot"],
            "gdb_analysis_summary": result["gdb_analysis"],
            "original_case": self.case_data
        }
        
        output_file = "enhanced_cot_output.json"
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(output, f, indent=2, ensure_ascii=False)
        
        print(f"\n✓ Results saved to {output_file}")

    def run(self):
        """运行完整流程"""
        self.load_case()
        result = self.generate_cot_with_gdb_info()
        self.save_result(result)
        return result

if __name__ == "__main__":
    generator = GDBCoTGenerator()
    generator.run()