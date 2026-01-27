import json

def extract_ids_from_jsonl(input_file, output_file):
    """
    从JSONL文件中提取所有id并保存到文本文件
    
    Args:
        input_file: 输入的JSONL文件路径
        output_file: 输出的文本文件路径
    """
    ids = []
    
    # 读取JSONL文件
    with open(input_file, 'r', encoding='utf-8') as f:
        for line in f:
            # 跳过空行
            if line.strip():
                # 解析JSON
                data = json.loads(line)
                # 提取id
                if 'id' in data:
                    ids.append(data['id'])
    
    # 将id列表写入文件
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(str(ids))
    
    print(f"成功提取 {len(ids)} 个id到 {output_file}")
    print(f"ID列表: {ids}")

if __name__ == "__main__":
    input_file = "bench.jsonl"
    output_file = "bench_id.txt"
    extract_ids_from_jsonl(input_file, output_file)