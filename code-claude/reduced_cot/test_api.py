
"""
测试API连接
"""

import sys
import os
from ai_analyzer import AIAnalyzer

# API配置
API_KEY = "sk-tT9Ddv4cOCl5BXW4kivhRQ"
BASE_URL = "https://llmapi.paratera.com/v1"

API_CONFIGS = {
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
}


def test_api_connection():
    """测试API连接"""
    print("="*60)
    print("API连接测试")
    print("="*60)
    
    # 测试代码
    test_code = """a = 1
b = 2
c = a + b
print(f"Result: {c}")"""
    
    test_description = "What is the value of variable 'c' after line 3?"
    
    for model_name, config in API_CONFIGS.items():
        print(f"\n测试模型: {model_name}")
        print(f"Base URL: {config['base_url']}")
        print(f"Model: {config['model']}")
        print("-"*60)
        
        try:
            analyzer = AIAnalyzer(config, timeout=30)
            result = analyzer.analyze_target(test_description, test_code, "TEST")
            
            if result:
                print(f"✓ 连接成功!")
                print(f"  目标行: {result['target_line']}")
                print(f"  目标变量: {result['target_var']}")
                print(f"  推理: {result['reasoning']}")
            else:
                print(f"✗ 分析失败")
                
        except Exception as e:
            print(f"✗ 连接失败: {e}")
    
    print("\n"+"="*60)


if __name__ == '__main__':
    test_api_connection()