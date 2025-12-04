"""
AI分析器 - 使用AI辅助分析目标行和变量
"""

import json
import re
from typing import Dict, Optional
from openai import OpenAI


class TargetValidator:
    """目标验证器"""
    
    @staticmethod
    def validate_target(code: str, target_line: int, target_var: str) -> bool:
        """
        验证目标行和变量是否合理
        
        Args:
            code: 源代码
            target_line: 目标行号
            target_var: 目标变量名
            
        Returns:
            bool: 是否合理
        """
        lines = code.split('\n')
        
        # 检查行号是否在范围内
        if target_line < 1 or target_line > len(lines):
            return False
        
        # 获取目标行
        line = lines[target_line - 1]
        
        # 检查该行是否包含目标变量的赋值
        # 支持各种赋值形式: var =, var+=, var[...] =, etc.
        pattern = rf'\b{re.escape(target_var)}\s*(?:\[.*?\])?\s*[+\-*/&|^%]?='
        if not re.search(pattern, line):
            return False
        
        return True


class AIAnalyzer:
    """AI分析器 - 用于分析目标行和变量"""
    
    def __init__(self, api_config: Dict):
        """
        初始化AI分析器
        
        Args:
            api_config: API配置，包含base_url, api_key, model
        """
        self.client = OpenAI(
            api_key=api_config['api_key'],
            base_url=api_config['base_url']
        )
        self.model = api_config['model']
    
    def analyze_target(self, description: str, code: str, case_id: str = "") -> Optional[Dict]:
        """
        使用AI分析目标行和变量
        
        Args:
            description: 问题描述
            code: 源代码
            case_id: case ID（用于日志）
            
        Returns:
            dict: {'target_line': int, 'target_var': str, 'reasoning': str} 或 None
        """
        # 给代码添加行号
        code_lines = code.split('\n')
        numbered_code = '\n'.join([f"{i+1:3d} | {line}" for i, line in enumerate(code_lines)])
        
        prompt = f"""Given this code analysis question, extract the target line number and target variable name.

Question Description: {description}

Code (with line numbers):
{numbered_code}

Please analyze and return ONLY a JSON object in this exact format:
{{
    "target_line": <line_number>,
    "target_var": "<variable_name>",
    "reasoning": "<brief explanation of why this is the target>"
}}

Important:
- target_line should be the actual line number where the variable's final value is determined
- target_var should be the exact variable name being asked about
- Look for phrases like "after executing the statement" or "after line X" in the description
- The target line usually contains an assignment to the target variable
"""
        
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {
                        "role": "system",
                        "content": "You are a helpful assistant that extracts information from code analysis questions. Return only valid JSON."
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                temperature=0
            )
            
            result_text = response.choices[0].message.content.strip()
            
            # 尝试提取JSON
            json_match = re.search(r'\{[^}]+\}', result_text, re.DOTALL)
            if json_match:
                result = json.loads(json_match.group())
                
                # 验证必要字段
                if 'target_line' in result and 'target_var' in result:
                    return {
                        'target_line': int(result['target_line']),
                        'target_var': str(result['target_var']),
                        'reasoning': result.get('reasoning', ''),
                        'method': 'ai'
                    }
            
            return None
            
        except Exception as e:
            print(f"AI分析异常 ({case_id}): {e}")
            return None
    
    @staticmethod
    def validate_target(code: str, target_line: int, target_var: str) -> bool:
        """
        验证目标行和变量是否合理
        
        Args:
            code: 源代码
            target_line: 目标行号
            target_var: 目标变量名
            
        Returns:
            bool: 是否合理
        """
        return TargetValidator.validate_target(code, target_line, target_var)


class RegexTargetExtractor:
    """正则表达式目标提取器"""
    
    @staticmethod
    def extract_target(description: str, code: str) -> Optional[Dict]:
        """
        使用正则表达式从描述和代码中提取目标信息
        
        Args:
            description: 问题描述
            code: 源代码
            
        Returns:
            dict: {'target_line': int, 'target_var': str, 'method': str} 或 None
        """
        # 尝试从描述中提取变量名
        var_pattern = r"variable\s+'([^']+)'"
        var_match = re.search(var_pattern, description)
        
        if not var_match:
            return None
        
        target_var = var_match.group(1)
        
        # 尝试从描述中提取行号信息
        line_pattern = r"line\s+(\d+)"
        line_match = re.search(line_pattern, description, re.IGNORECASE)
        
        # 尝试从描述中提取语句关键词
        stmt_pattern = r"executing\s+(?:the\s+)?(?:statement\s+)?['\"]?([^'\"]+)['\"]?"
        stmt_match = re.search(stmt_pattern, description)
        
        # 在代码中查找目标行
        code_lines = code.split('\n')
        target_line = None
        
        # 如果描述中明确提到行号
        if line_match:
            potential_line = int(line_match.group(1))
            if 1 <= potential_line <= len(code_lines):
                line = code_lines[potential_line - 1]
                if target_var in line and '=' in line:
                    target_line = potential_line
        
        # 如果有语句关键词，尝试匹配
        if target_line is None and stmt_match:
            stmt_text = stmt_match.group(1)
            for i, line in enumerate(code_lines, 1):
                if target_var in line and '=' in line:
                    # 检查是否匹配语句
                    if any(part.strip() in line for part in stmt_text.split()):
                        target_line = i
                        break
        
        # 如果还没找到，尝试找最后一次赋值
        if target_line is None:
            for i in range(len(code_lines) - 1, -1, -1):
                line = code_lines[i]
                if re.search(rf'\b{re.escape(target_var)}\s*=', line):
                    target_line = i + 1
                    break
        
        if target_line:
            return {
                'target_line': target_line,
                'target_var': target_var,
                'method': 'regex'
            }
        
        return None