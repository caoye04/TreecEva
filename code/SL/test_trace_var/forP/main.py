"""
倒序COT生成器（真正的倒推版本）
从目标行开始，不知道答案，逐步向前追溯依赖关系
"""

import os
import re
from openai import OpenAI


class ReverseCOTGenerator:
    """倒序COT生成器"""
    
    def __init__(self, api_config):
        """
        初始化生成器
        
        Args:
            api_config: API配置字典，包含 base_url, api_key, model
        """
        self.client = OpenAI(
            base_url=api_config['base_url'],
            api_key=api_config['api_key']
        )
        self.model = api_config['model']
    
    def load_forward_cot(self, cot_file):
        """加载正序COT文件"""
        with open(cot_file, 'r', encoding='utf-8') as f:
            return f.read()
    
    def extract_code_and_structure(self, forward_cot):
        """从正序COT中提取代码结构和执行轨迹（但不包含最终答案）"""
        # 提取目标行和目标变量
        target_match = re.search(r'Target: Find the value of variable (\w+) after \[line (\d+)\]', forward_cot)
        if target_match:
            target_var = target_match.group(1)
            target_line = target_match.group(2)
            lang = 'en'
        else:
            # 尝试中文模式
            target_match = re.search(r'目标: 求\[第(\d+)行\]执行后变量 (\w+)', forward_cot)
            if target_match:
                target_line = target_match.group(1)
                target_var = target_match.group(2)
                lang = 'zh'
            else:
                target_var = "unknown"
                target_line = "unknown"
                lang = 'en'
        
        # 提取所有的 [line n] 代码行和变量状态（不包含答案行）
        code_lines = []
        
        if lang == 'en':
            # 英文格式
            pattern = r'\[line (\d+)\]\s+(.+?)\n\[explain\]\s+(.+?)(?=\n\[line|\n\nAnswer:|$)'
        else:
            # 中文格式
            pattern = r'\[第(\d+)行\]\s+(.+?)\n\[解释\]\s+(.+?)(?=\n\[第|\n\n答案:|$)'
        
        matches = re.finditer(pattern, forward_cot, re.DOTALL)
        for match in matches:
            lineno = match.group(1)
            code = match.group(2).strip()
            explanation = match.group(3).strip()
            code_lines.append({
                'lineno': lineno,
                'code': code,
                'explanation': explanation
            })
        
        return {
            'target_var': target_var,
            'target_line': target_line,
            'code_lines': code_lines,
            'lang': lang
        }
    
    def generate_prompt(self, case_info):
        """生成AI提示词（不透露最终答案）"""
        lang = case_info['lang']
        
        # 构建代码执行轨迹（不包含值）
        code_execution = "\n".join([
            f"[line {item['lineno']}] {item['code']}" 
            for item in case_info['code_lines']
        ])
        
        if lang == 'zh':
            prompt = f"""你是一个代码推理专家。我会给你一段代码的执行轨迹，你需要用**倒序思维**来分析这段代码。

# 任务
求第{case_info['target_line']}行执行后变量 {case_info['target_var']} 的值

# 代码执行轨迹（按执行顺序）
{code_execution}

# 倒序分析要求
**核心思路：从目标出发，逆向追溯依赖关系**

1. **第一步**：分析第{case_info['target_line']}行的代码，识别 {case_info['target_var']} 依赖哪些变量或表达式
2. **第二步**：对于每个依赖变量，向前查找它最后一次被赋值的位置
3. **第三步**：递归分析这些依赖变量，直到追溯到常量或初始值
4. **第四步**：按照倒序路径，逐步计算出最终结果

# 输出格式要求
使用如下格式（倒序分析过程）：
```
目标: 求[第{case_info['target_line']}行]执行后变量 {case_info['target_var']} 的值

=== 倒序分析开始 ===

[分析第{case_info['target_line']}行] (代码)
[依赖识别] {case_info['target_var']} 依赖于: (列出依赖的变量和表达式)

[向前追溯] 查找依赖变量的定义位置...
[分析第X行] (代码)
[依赖识别] 该变量依赖于: (继续追溯)

... (继续向前追溯，直到找到所有初始值)

=== 倒推计算开始 ===

[第Y行初始值] 变量 = 值 (最早的初始值)
[第Z行计算] 变量 = ... = 值 (逐步向后计算)
...
[第{case_info['target_line']}行最终计算] {case_info['target_var']} = ... = 最终值

答案: {case_info['target_var']} = 最终值
```
请严格按照倒序思维分析，先找依赖，再追溯，最后计算。不要直接给出答案，要展示完整的倒推过程。
"""
        else:
            prompt = f"""You are a code reasoning expert. I will give you a code execution trace, and you need to analyze it using **reverse thinking**.

# Task
Find the value of variable {case_info['target_var']} after line {case_info['target_line']} executes

# Code Execution Trace (in execution order)
{code_execution}

# Reverse Analysis Requirements
**Core Idea: Start from the target, trace dependencies backwards**

1. **Step 1**: Analyze the code at line {case_info['target_line']}, identify what variables or expressions {case_info['target_var']} depends on
2. **Step 2**: For each dependency variable, search backwards to find where it was last assigned
3. **Step 3**: Recursively analyze these dependency variables until reaching constants or initial values
4. **Step 4**: Follow the reverse path to calculate the final result step by step

# Output Format Requirements
Use the following format (reverse analysis process):
```
Target: Find the value of variable {case_info['target_var']} after [line {case_info['target_line']}] executes

=== Reverse Analysis Begins ===

[Analyze line {case_info['target_line']}] (code)
[Identify Dependencies] {case_info['target_var']} depends on: (list dependent variables and expressions)

[Trace Backwards] Looking for where dependencies are defined...
[Analyze line X] (code)
[Identify Dependencies] This variable depends on: (continue tracing)

... (continue tracing backwards until all initial values are found)

=== Forward Calculation Begins ===

[Line Y Initial Value] variable = value (earliest initial value)
[Line Z Calculation] variable = ... = value (calculate step by step forward)
...
[Line {case_info['target_line']} Final Calculation] {case_info['target_var']} = ... = final_value

Answer: {case_info['target_var']} = final_value
```
Please strictly follow reverse thinking: first find dependencies, then trace back, finally calculate. Do not give the answer directly - show the complete reverse reasoning process.
"""
        
        return prompt
    
    def call_ai(self, prompt):
        """调用AI生成倒序COT"""
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {
                        "role": "system",
                        "content": "You are an expert in reverse code reasoning. You excel at dependency analysis and backward tracing."
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                temperature=0.3,  # 降低温度以获得更确定性的推理
                max_tokens=4000
            )
            
            return response.choices[0].message.content
        
        except Exception as e:
            print(f"[错误] AI调用失败: {e}")
            return None
    
    def save_reverse_cot(self, reverse_cot, output_file):
        """保存倒序COT"""
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(reverse_cot)
        return output_file
    
    def generate(self, forward_cot_file, output_file):
        """生成倒序COT的完整流程"""
        print("\n" + "=" * 60)
        print("倒序COT生成器 / Reverse COT Generator")
        print("（真正的倒推版本 - 不知道答案，逐步追溯）")
        print("=" * 60)
        
        # 1. 加载正序COT
        print("\n[步骤 1/4] 加载正序COT...")
        forward_cot = self.load_forward_cot(forward_cot_file)
        print(f"  ✓ 已加载: {forward_cot_file}")
        
        # 2. 提取代码结构（不包含答案）
        print("\n[步骤 2/4] 提取代码结构和执行轨迹...")
        case_info = self.extract_code_and_structure(forward_cot)
        print(f"  目标变量: {case_info['target_var']}")
        print(f"  目标行号: {case_info['target_line']}")
        print(f"  代码行数: {len(case_info['code_lines'])}")
        print(f"  语言: {case_info['lang']}")
        print(f"  注意: 不透露最终答案，需要AI自己倒推")
        
        # 3. 生成提示词
        print("\n[步骤 3/4] 生成AI提示词（倒序分析要求）...")
        prompt = self.generate_prompt(case_info)
        print(f"  ✓ 提示词已生成 (长度: {len(prompt)} 字符)")
        
        # 4. 调用AI
        print("\n[步骤 4/4] 调用AI进行倒序分析...")
        print(f"  模型: {self.model}")
        print(f"  分析模式: 从目标行开始，逆向追溯依赖，最后计算答案")
        reverse_cot = self.call_ai(prompt)
        
        if reverse_cot:
            # 保存结果
            self.save_reverse_cot(reverse_cot, output_file)
            print(f"  ✓ 倒序COT已生成: {output_file}")
            
            # 显示预览
            print("\n" + "-" * 60)
            print("倒序COT预览:")
            print("-" * 60)
            print(reverse_cot)
            print("-" * 60)
            
            return output_file
        else:
            print("  ✗ AI生成失败")
            return None
    
    @staticmethod
    def generate_reverse_cot(forward_cot_file, output_file, api_config):
        """静态方法：生成倒序COT（自动检测语言，不需要lang参数）"""
        generator = ReverseCOTGenerator(api_config)
        return generator.generate(forward_cot_file, output_file)


# 使用示例
if __name__ == '__main__':
    # API配置
    API_KEY = "sk-tT9Ddv4cOCl5BXW4kivhRQ"
    BASE_URL = "https://llmapi.paratera.com/v1"
    
    api_config = {
        "base_url": BASE_URL,
        "api_key": API_KEY,
        "model": "Qwen3-235B-A22B-Instruct-2507"
    }
    
    # 生成倒序COT
    forward_cot_file = "data_test/final_cot_test.txt"
    reverse_cot_file = "data_test/reverse_cot_test.txt"
    
    if os.path.exists(forward_cot_file):
        ReverseCOTGenerator.generate_reverse_cot(
            forward_cot_file,
            reverse_cot_file,
            api_config
        )
    else:
        print(f"错误: 找不到正序COT文件 {forward_cot_file}")