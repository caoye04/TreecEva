import json

def convert_jsonl_to_json(input_file, output_file):
    """
    将TreecEva格式的JSONL文件转换为目标JSON格式
    
    Args:
        input_file: 输入的JSONL文件路径
        output_file: 输出的JSON文件路径
    """
    
    # 读取JSONL文件
    data_list = []
    with open(input_file, 'r', encoding='utf-8') as f:
        for line in f:
            if line.strip():  # 跳过空行
                data_list.append(json.loads(line))
    
    # 转换数据格式
    converted_data = []
    
    # 添加背景说明（只在第一个元素）
    background_entry = {
        "background": "I am developing a comprehensive evaluation benchmark for large language models in the code reasoning domain. This benchmark specifically focuses on assessing statement-level reasoning capabilities of LLMs across multiple computational paradigms: (1) Arithmetic Operations - including basic arithmetic (addition, subtraction, multiplication, division), advanced mathematical operations (exponentiation, logarithms, trigonometric functions), bitwise operations (AND, OR, XOR, shift operations), and composite calculations combining multiple operation types; (2) Boolean Logic - encompassing comparison operations (equality, inequality, relational comparisons), logical operations (AND, OR, NOT), and short-circuit evaluation patterns; (3) Variable Assignment - including simple assignments, multiple simultaneous assignments, tuple unpacking, and destructuring assignments; (4) Control Flow and Data Structures - covering conditional statements, loops, and basic container operations; (5) Complex Mixed Scenarios - integrating multiple reasoning types in sophisticated logical chains.",
        "requirements": "Generate additional examples following the provided template format with these specific criteria: (1) Create significantly more complex code samples with extended logical reasoning chains requiring multiple inference steps; (2) Ensure each example has a unique, deterministic answer that can be computed through step-by-step execution; (3) Maintain strict format consistency across all generated examples, matching the exact structure and field organization of the provided samples; (4) Incorporate diverse programming languages and paradigms while maintaining code complexity at an advanced level suitable for challenging LLM reasoning capabilities; (5) Minimize reliance on external library functions and API calls, focusing instead on algorithmic reasoning with basic language constructs."
    }
    converted_data.append(background_entry)
    
    # 转换每个数据项
    for idx, item in enumerate(data_list, 1):
        # 从prompt中提取描述和代码
        prompt_parts = item['prompt'].split('---CODE---')
        description = prompt_parts[0].strip() if len(prompt_parts) > 0 else ""
        code = prompt_parts[1].strip() if len(prompt_parts) > 1 else ""
        
        # 构建新格式
        converted_item = {
            "id": item['id'],
            "metadata": item['metadata'],
            "task": {
                "description": description,
                "code": code,
                "answer": item['answer'],
                "cot": item['cot']
            }
        }
        
        converted_data.append(converted_item)
    
    # 写入JSON文件
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(converted_data, f, indent=2, ensure_ascii=False)
    
    print(f"转换完成！共处理 {len(data_list)} 条数据")
    print(f"输出文件: {output_file}")

# 使用示例
if __name__ == "__main__":
    input_file = "TreecEva_data_old_235.jsonl"
    output_file = "converted_data.json"
    
    convert_jsonl_to_json(input_file, output_file)