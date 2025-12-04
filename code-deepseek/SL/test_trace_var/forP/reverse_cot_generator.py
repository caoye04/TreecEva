"""
倒序COT生成器（优化版 - 精简结构）
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
        
        # 提取所有的 [line n] 代码行（不包含答案行）
        code_lines = []
        
        if lang == 'en':
            # 英文格式 - 只提取代码，不提取explain
            pattern = r'\[line (\d+)\]\s+(.+?)(?=\n|$)'
        else:
            # 中文格式
            pattern = r'\[第(\d+)行\]\s+(.+?)(?=\n|$)'
        
        matches = re.finditer(pattern, forward_cot)
        seen_lines = set()
        for match in matches:
            lineno = match.group(1)
            code = match.group(2).strip()
            
            # 跳过 [explain] 行
            if code.startswith('[explain]') or code.startswith('[解释]'):
                continue
            
            # 避免重复（同一行可能出现多次）
            key = (lineno, code)
            if key not in seen_lines:
                seen_lines.add(key)
                code_lines.append({
                    'lineno': lineno,
                    'code': code
                })
        
        return {
            'target_var': target_var,
            'target_line': target_line,
            'code_lines': code_lines,
            'lang': lang
        }
    
    def generate_prompt(self, case_info):
        """生成AI提示词（精简版）"""
        lang = case_info['lang']
        
        # 构建代码列表（按行号排序，去重）
        unique_lines = {}
        for item in case_info['code_lines']:
            lineno = int(item['lineno'])
            if lineno not in unique_lines:
                unique_lines[lineno] = item['code']
        
        code_lines_str = "\n".join([
            f"[line {lineno}] {code}" 
            for lineno, code in sorted(unique_lines.items())
        ])
        
        if lang == 'zh':
            prompt = f"""你是一个代码推理专家。请用倒序思维分析以下代码，求变量的值。

# 任务
求第{case_info['target_line']}行执行后变量 {case_info['target_var']} 的值

# 代码
{code_lines_str}

# 要求
1. **依赖分析**：从第{case_info['target_line']}行开始，识别 {case_info['target_var']} 依赖哪些变量
2. **向前追溯**：对每个依赖变量，找到它最后一次被赋值的位置
3. **递归追溯**：继续追溯，直到找到所有常量或初始值
4. **正向计算**：从初始值开始，逐步计算到最终结果

# 输出格式（精简版）
```
目标: 求第{case_info['target_line']}行变量 {case_info['target_var']} 的值

=== 步骤1: 依赖分析 ===
第{case_info['target_line']}行: (代码)
依赖变量: (列出所有依赖)

=== 步骤2: 向前追溯 ===
变量X 最后赋值于第Y行: (代码)
依赖: (继续列出)
变量Z 最后赋值于第W行: (代码)
依赖: (继续列出或标注为常量)
...

=== 步骤3: 正向计算 ===
初始值:
变量A = 值1 (第N行)
变量B = 值2 (第M行)

逐步计算:
第X行: 变量C = ... = 值3
第Y行: 变量D = ... = 值4
...
第{case_info['target_line']}行: {case_info['target_var']} = ... = 最终值

答案: {case_info['target_var']} = 最终值
```
**注意**：
- 保持简洁，避免冗余解释
- 循环要明确迭代次数
- 每个计算步骤都要展示中间值
"""
        else:
            prompt = f"""You are a code reasoning expert. Use reverse thinking to analyze the following code.

# Task
Find the value of variable {case_info['target_var']} after line {case_info['target_line']} executes

# Code
{code_lines_str}

# Requirements
1. **Dependency Analysis**: Starting from line {case_info['target_line']}, identify what variables {case_info['target_var']} depends on
2. **Backward Tracing**: For each dependency, find where it was last assigned
3. **Recursive Tracing**: Continue until all constants or initial values are found
4. **Forward Calculation**: Calculate from initial values to final result

# Output Format (Concise Version)
```
Target: Find {case_info['target_var']} value at line {case_info['target_line']}

=== Step 1: Dependency Analysis ===
Line {case_info['target_line']}: (code)
Dependencies: (list all)

=== Step 2: Backward Tracing ===
Variable X last assigned at line Y: (code)
Dependencies: (continue listing)
Variable Z last assigned at line W: (code)
Dependencies: (continue or mark as constant)
...

=== Step 3: Forward Calculation ===
Initial values:
Variable A = value1 (line N)
Variable B = value2 (line M)

Step-by-step:
Line X: Variable C = ... = value3
Line Y: Variable D = ... = value4
...
Line {case_info['target_line']}: {case_info['target_var']} = ... = final_value

Answer: {case_info['target_var']} = final_value
```
**Notes**:
- Keep it concise, avoid redundant explanations
- For loops, specify iteration count
- Show intermediate values for each calculation step
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
                        "content": "You are an expert in reverse code reasoning. You provide concise, structured analysis."
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                temperature=0.2,  # 进一步降低温度
                max_tokens=3000
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
        print("（精简版 - 结构化倒推分析）")
        print("=" * 60)
        
        # 1. 加载正序COT
        print("\n[步骤 1/4] 加载正序COT...")
        forward_cot = self.load_forward_cot(forward_cot_file)
        print(f"  ✓ 已加载: {forward_cot_file}")
        
        # 2. 提取代码结构（不包含答案）
        print("\n[步骤 2/4] 提取代码结构...")
        case_info = self.extract_code_and_structure(forward_cot)
        print(f"  目标变量: {case_info['target_var']}")
        print(f"  目标行号: {case_info['target_line']}")
        print(f"  代码行数: {len(case_info['code_lines'])}")
        print(f"  语言: {case_info['lang']}")
        
        # 3. 生成提示词
        print("\n[步骤 3/4] 生成精简提示词...")
        prompt = self.generate_prompt(case_info)
        print(f"  ✓ 提示词已生成 (长度: {len(prompt)} 字符)")
        
        # 4. 调用AI
        print("\n[步骤 4/4] 调用AI进行倒序分析...")
        print(f"  模型: {self.model}")
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
        """静态方法：生成倒序COT"""
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