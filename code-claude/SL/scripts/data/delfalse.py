import json
import re

def filter_and_renumber_dataset(answer_file, data_file, output_file=None):
    """
    根据answer.json中的false结果过滤TreecEva_data.json，并重新编号
    保留数据集的第一项元数据
    
    Args:
        answer_file: answer.json文件路径
        data_file: TreecEva_data.json文件路径
        output_file: 输出文件路径（如果为None，则覆盖原文件）
    """
    # 读取answer.json
    with open(answer_file, 'r', encoding='utf-8') as f:
        answer_data = json.load(f)
    
    # 统计所有success为false的编号
    false_ids = []
    for item_id, item_value in answer_data.items():
        if isinstance(item_value, dict) and item_value.get('success') == False:
            false_ids.append(item_id)
    
    print(f"发现 {len(false_ids)} 个 success 为 false 的条目：")
    for false_id in false_ids:
        print(f"  - {false_id}")
    
    # 读取TreecEva_data.json
    with open(data_file, 'r', encoding='utf-8') as f:
        tree_data = json.load(f)
    
    # 检查数据格式
    if not isinstance(tree_data, list) or len(tree_data) == 0:
        print("错误：数据集格式不正确")
        return
    
    # 保存第一项元数据
    metadata = tree_data[0]
    data_items = tree_data[1:]
    
    original_count = len(data_items)
    print(f"\n原始数据集包含 {original_count} 个数据条目（不含元数据）")
    
    # 过滤掉false_ids中的数据
    filtered_data = []
    for item in data_items:
        if 'id' in item and item['id'] not in false_ids:
            filtered_data.append(item)
    
    filtered_count = len(filtered_data)
    deleted_count = original_count - filtered_count
    print(f"删除了 {deleted_count} 个条目")
    print(f"剩余 {filtered_count} 个条目")
    
    # 提取ID前缀
    prefix = None
    for item in filtered_data:
        if 'id' in item:
            match = re.match(r'([A-Z]+-[A-Z]+-[A-Z])(\d+)', item['id'])
            if match:
                prefix = match.group(1)
                break
    
    if not prefix:
        print("警告：未找到ID前缀，使用默认前缀 'SL-MIX-S'")
        prefix = "SL-MIX-S"
    
    # 重新编号
    counter = 1
    for item in filtered_data:
        if 'id' in item:
            new_id = f"{prefix}{counter:04d}"
            item['id'] = new_id
            counter += 1
    
    # 重新组装数据集：元数据 + 过滤后的数据
    final_dataset = [metadata] + filtered_data
    
    # 保存到文件
    output_path = output_file if output_file else data_file
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(final_dataset, f, ensure_ascii=False, indent=2)
    
    print(f"\n重新编号完成！")
    print(f"最终数据集包含：")
    print(f"  - 1 个元数据项")
    print(f"  - {counter - 1} 个数据条目")
    print(f"  - 总计 {len(final_dataset)} 项")
    print(f"结果已保存到: {output_path}")
    
    return false_ids, final_dataset

def filter_and_renumber_inplace(answer_file, data_file):
    """
    直接在原文件上进行过滤和重新编号（会覆盖原文件）
    
    Args:
        answer_file: answer.json文件路径
        data_file: TreecEva_data.json文件路径
    """
    return filter_and_renumber_dataset(answer_file, data_file, None)

# 使用示例
if __name__ == "__main__":
    # 方式1：生成新文件（推荐，保留原文件作为备份）
    # filter_and_renumber_dataset('answer.json', 'TreecEva_data.json', 'TreecEva_data_filtered.json')
    
    # 方式2：直接修改原文件（谨慎使用）
    filter_and_renumber_inplace('answer.json', 'TreecEva_data.json')