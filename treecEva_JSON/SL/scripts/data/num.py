import json
import re

def renumber_dataset(input_file, output_file):
    """
    重新编号JSON数据集，使ID变成连续的
    
    Args:
        input_file: 输入的JSON文件路径
        output_file: 输出的JSON文件路径
    """
    # 读取JSON文件
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # 提取ID前缀（假设格式为 "SL-MIX-S001"）
    # 从第一个有ID的项目中提取前缀
    prefix = None
    for item in data:
        if 'id' in item:
            # 使用正则表达式提取前缀和数字部分
            match = re.match(r'([A-Z]+-[A-Z]+-[A-Z])(\d+)', item['id'])
            if match:
                prefix = match.group(1)
                break
    
    if not prefix:
        print("警告：未找到ID前缀，使用默认前缀 'SL-MIX-S'")
        prefix = "SL-MIX-S"
    
    # 重新编号
    counter = 1
    for item in data:
        if 'id' in item:
            # 生成新的ID，保持三位数格式
            new_id = f"{prefix}{counter:03d}"
            item['id'] = new_id
            counter += 1
    
    # 保存到新文件
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print(f"重新编号完成！")
    print(f"处理了 {counter - 1} 个数据项")
    print(f"结果已保存到: {output_file}")

def renumber_dataset_inplace(file_path):
    """
    直接在原文件上重新编号（会覆盖原文件）
    
    Args:
        file_path: JSON文件路径
    """
    renumber_dataset(file_path, file_path)

# 使用示例
if __name__ == "__main__":
    # 方式1：生成新文件
    # renumber_dataset('TreecEva_data.json', 'TreecEva_data_renumbered.json')
    
    # 方式2：直接修改原文件（谨慎使用）
    renumber_dataset_inplace('TreecEva_data.json')