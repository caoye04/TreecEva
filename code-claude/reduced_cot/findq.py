import json

def find_ids_with_pattern(json_file):
    """
    读取JSON文件，找出所有cot字段中包含"= ? (las"的数据项的id末尾三位数
    """
    # 读取JSON文件
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # 存储匹配的id末尾三位数
    matching_ids = []
    
    # 遍历数据集
    for item in data:
        # 获取id和cot字段
        item_id = item.get('id', '')
        cot = item.get('task', {}).get('cot', '')
        
        # 检查cot中是否包含"= ? (las"
        if '= ? (las' in cot:
            # 提取id末尾三位数
            if len(item_id) >= 3:
                last_three = item_id[-3:]
                matching_ids.append(last_three)
                print(f"找到匹配项: {item_id} -> 末尾三位: {last_three}")
    
    return matching_ids

# 使用脚本
if __name__ == "__main__":
    json_file = "TreecEva_data_reduced_formated_cot.json"
    
    print("开始搜索包含'= ? (las'的数据项...")
    print("-" * 50)
    
    result = find_ids_with_pattern(json_file)
    
    print("-" * 50)
    print(f"\n共找到 {len(result)} 个匹配项")
    print(f"ID末尾三位数列表: {result}")