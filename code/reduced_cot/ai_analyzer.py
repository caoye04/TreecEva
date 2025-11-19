"""
AI分析器 - 用于自动识别目标行和目标变量
"""

import json
import re
import time
from openai import OpenAI
import httpx


class AIAnalyzer:
    """AI分析器，用于识别代码的目标行和目标变量"""
    
    def __init__(self, api_config, timeout=60, max_retries=3):
        """
        初始化AI分析器
        
        Args:
            api_config: API配置字典，包含 base_url, api_key, model
            timeout: 请求超时时间（秒）
            max_retries: 最大重试次数
        """
        http_client = httpx.Client(
            timeout=timeout,
            verify=False,
            follow_redirects=True
        )
        
        self.client = OpenAI(
            base_url=api_config['base_url'],
            api_key=api_config['api_key'],
            http_client=http_client
        )
        self.model = api_config['model']
        self.max_retries = max_retries
    
    def analyze_target(self, description, code, case_id):
        """
        分析代码的目标行和目标变量
        
        Args:
            description: 问题描述
            code: Python代码
            case_id: case的ID
            
        Returns:
            dict: {'target_line': int, 'target_var': str, 'confidence': str}
        """
        prompt = self._build_analysis_prompt(description, code)
        
        for retry in range(self.max_retries):
            try:
                print(f"    [API调用] 尝试 {retry + 1}/{self.max_retries}...")
                
                response = self.client.chat.completions.create(
                    model=self.model,
                    messages=[
                        {
                            "role": "system", 
                            "content": "You are an expert Python code analyzer. Your task is to identify the EXACT target line and target variable based on the problem description."
                        },
                        {
                            "role": "user", 
                            "content": prompt
                        }
                    ],
                    temperature=0.1,
                    max_tokens=500
                )
                
                result = response.choices[0].message.content.strip()
                print(f"    [API响应] 成功获取")
                return self._parse_ai_response(result, case_id, code)
                
            except Exception as e:
                error_msg = str(e)
                print(f"    [API错误] {error_msg}")
                
                if retry < self.max_retries - 1:
                    wait_time = 2 ** retry
                    print(f"    [等待] {wait_time}秒后重试...")
                    time.sleep(wait_time)
                else:
                    print(f"    [AI分析错误] Case {case_id}: {error_msg}")
                    return None
        
        return None
    
    def _build_analysis_prompt(self, description, code):
        """构建分析提示词"""
        # 给代码添加行号
        lines = code.split('\n')
        numbered_code = '\n'.join([f"{i+1:3d} | {line}" for i, line in enumerate(lines)])
        
        prompt = f"""Given the following problem description and Python code, identify:
1. The EXACT target line number (the line that computes or assigns the final answer)
2. The target variable name (the variable we need to track)

Problem Description:
{description}

Python Code with Line Numbers:
{numbered_code}

IMPORTANT RULES:
1. The target variable is usually explicitly mentioned in the description (like "value of variable 'result_value'")
2. The target line is the line where this variable gets its FINAL VALUE (last assignment)
3. If the description mentions a specific variable name, that MUST be the target variable
4. The target line should be BEFORE the print statement (if any)
5. Look for the LAST assignment to the target variable
6. Count line numbers EXACTLY as shown in the numbered code above

Example:
If description says "value of variable 'result_value'" and line 29 is "result_value = total_variance ^ product_count"
Then target_line should be 29 and target_var should be "result_value"

Please respond in the following JSON format ONLY (no other text):
{{
    "target_line": <exact_line_number>,
    "target_var": "<exact_variable_name>",
    "reasoning": "<brief explanation of why you chose this line and variable>"
}}
"""
        return prompt
    
    def _parse_ai_response(self, response, case_id, code):
        """解析AI响应"""
        try:
            # 尝试提取JSON
            json_match = re.search(r'\{[^{}]*\}', response, re.DOTALL)
            if json_match:
                result = json.loads(json_match.group())
                
                # 验证必需字段
                if 'target_line' in result and 'target_var' in result:
                    target_line = int(result['target_line'])
                    target_var = str(result['target_var'])
                    
                    # 基本验证
                    if not self._quick_validate(code, target_line, target_var):
                        print(f"    [解析警告] AI响应未通过验证")
                        print(f"    [AI建议] Line {target_line}, Var '{target_var}'")
                        
                        # 尝试自动修正
                        corrected = self._try_auto_correct(code, target_var)
                        if corrected:
                            print(f"    [自动修正] Line {corrected['target_line']}, Var '{corrected['target_var']}'")
                            return corrected
                        
                        return None
                    
                    return {
                        'target_line': target_line,
                        'target_var': target_var,
                        'reasoning': result.get('reasoning', ''),
                        'confidence': 'high'
                    }
            
            print(f"    [解析警告] Case {case_id}: 无法解析AI响应")
            print(f"    [响应内容] {response[:200]}...")
            return None
            
        except Exception as e:
            print(f"    [解析错误] Case {case_id}: {e}")
            print(f"    [响应内容] {response[:200]}...")
            return None
    
    def _quick_validate(self, code, target_line, target_var):
        """快速验证目标信息"""
        lines = code.split('\n')
        
        # 检查行号范围
        if target_line < 1 or target_line > len(lines):
            return False
        
        # 检查变量是否在代码中
        if target_var not in code:
            return False
        
        # 检查目标行是否包含该变量的赋值
        target_line_code = lines[target_line - 1].strip()
        if not target_line_code or target_line_code.startswith('#'):
            return False
        
        # 检查该行是否对目标变量进行赋值
        if not re.search(rf'\b{re.escape(target_var)}\s*=', target_line_code):
            return False
        
        return True
    
    def _try_auto_correct(self, code, target_var):
        """尝试自动修正目标行"""
        lines = code.split('\n')
        
        # 查找所有对目标变量的赋值
        assignment_lines = []
        for i, line in enumerate(lines, 1):
            if re.search(rf'\b{re.escape(target_var)}\s*=', line):
                assignment_lines.append(i)
        
        if not assignment_lines:
            return None
        
        # 选择最后一个赋值行（在print之前）
        for line_num in reversed(assignment_lines):
            line_code = lines[line_num - 1].strip()
            # 确保不是在循环或条件语句的深层嵌套中
            if not line_code.startswith('print'):
                return {
                    'target_line': line_num,
                    'target_var': target_var,
                    'reasoning': 'Auto-corrected to last assignment before print',
                    'confidence': 'medium'
                }
        
        # 如果找不到，返回最后一个赋值
        return {
            'target_line': assignment_lines[-1],
            'target_var': target_var,
            'reasoning': 'Auto-corrected to last assignment',
            'confidence': 'low'
        }
    
    def validate_target(self, code, target_line, target_var):
        """
        验证目标行和变量是否合理
        
        Args:
            code: Python代码
            target_line: 目标行号
            target_var: 目标变量
            
        Returns:
            bool: 是否有效
        """
        return self._quick_validate(code, target_line, target_var)


class TargetValidator:
    """目标信息验证器"""
    
    @staticmethod
    def validate_by_execution(code_file, target_line, target_var):
        """通过执行代码验证目标信息"""
        try:
            import importlib.util
            import sys
            from io import StringIO
            
            spec = importlib.util.spec_from_file_location("test_module", code_file)
            module = importlib.util.module_from_spec(spec)
            
            old_stdout = sys.stdout
            sys.stdout = StringIO()
            
            try:
                spec.loader.exec_module(module)
                
                if hasattr(module, target_var):
                    return True
                
            finally:
                sys.stdout = old_stdout
            
            return False
            
        except Exception as e:
            print(f"    [验证错误] 执行验证失败: {e}")
            return False