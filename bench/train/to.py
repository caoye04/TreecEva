import json

def jsonl_to_json(input_file, output_file):
    """
    将JSONL文件转换为JSON数组格式
    
    参数:
        input_file: JSONL输入文件路径
        output_file: JSON输出文件路径
    """
    data = []
    
    # 读取JSONL文件
    with open(input_file, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line:  # 跳过空行
                data.append(json.loads(line))
    
    # 写入JSON文件
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print(f"成功转换 {len(data)} 条记录")
    print(f"输出文件: {output_file}")

# 使用示例
if __name__ == "__main__":
    # 方法1: 指定文件路径
    input_file = "train_dataset_500_format.jsonl"
    output_file = "train_dataset_500_format.json"
    jsonl_to_json(input_file, output_file)
    
    # 方法2: 从命令行参数获取文件路径
    # import sys
    # if len(sys.argv) >= 3:
    #     jsonl_to_json(sys.argv[1], sys.argv[2])
    # else:
    #     print("用法: python script.py <输入文件.jsonl> <输出文件.json>")