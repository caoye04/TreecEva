import json

def merge_cot_files(formated_file, natural_file, output_file):
    """
    合并两个JSON文件,将formated_cot转换为think,natural_cot转换为response
    
    参数:
        formated_file: TreecEva_data_reduced_formated_cot.json 文件路径
        natural_file: TreecEva_data_reduced_natural_cot.json 文件路径
        output_file: 输出文件路径 Think_TreecEva_data_reduced_cot.json
    """
    
    # 读取两个JSON文件
    with open(formated_file, 'r', encoding='utf-8') as f:
        formated_data = json.load(f)
    
    with open(natural_file, 'r', encoding='utf-8') as f:
        natural_data = json.load(f)
    
    # 创建新的数据结构
    merged_data = []
    
    # 确保两个文件的长度相同
    if len(formated_data) != len(natural_data):
        print(f"警告: 两个文件的条目数量不同!")
        print(f"formated_file: {len(formated_data)} 条")
        print(f"natural_file: {len(natural_data)} 条")
    
    # 遍历数据并合并
    for i in range(min(len(formated_data), len(natural_data))):
        formated_item = formated_data[i]
        natural_item = natural_data[i]
        
        # 深拷贝以避免修改原始数据
        import copy
        new_item = copy.deepcopy(formated_item)
        
        # 检查ID是否匹配
        formated_id = formated_item.get('id', 'N/A')
        natural_id = natural_item.get('id', 'N/A')
        
        if formated_id != natural_id:
            print(f"警告: 第{i}条记录ID不匹配!")
            print(f"  formated ID: {formated_id}")
            print(f"  natural ID: {natural_id}")
        
        # 修改task部分
        if 'task' in new_item:
            # 获取formated的cot作为think
            formated_cot = formated_item.get('task', {}).get('cot', None)
            # 获取natural的cot作为response
            natural_cot = natural_item.get('task', {}).get('cot', None)
            
            # 调试信息
            if formated_cot is None:
                print(f"警告: ID={formated_id} 在formated文件中没有cot字段")
            if natural_cot is None:
                print(f"警告: ID={natural_id} 在natural文件中没有cot字段")
            
            # 删除原有的cot字段
            if 'cot' in new_item['task']:
                del new_item['task']['cot']
            
            # 添加think字段(来自formated_cot)
            if formated_cot is not None:
                new_item['task']['think'] = formated_cot
            else:
                print(f"  跳过添加think字段: ID={formated_id}")
            
            # 添加response字段(来自natural_cot)
            if natural_cot is not None:
                new_item['task']['response'] = natural_cot
            else:
                print(f"  跳过添加response字段: ID={natural_id}")
        
        merged_data.append(new_item)
    
    # 写入新的JSON文件
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(merged_data, f, ensure_ascii=False, indent=2)
    
    print(f"\n成功创建文件: {output_file}")
    print(f"共处理 {len(merged_data)} 条记录")

# 使用示例
if __name__ == "__main__":
    formated_file = "TreecEva_data_reduced_formated_cot.json"
    natural_file = "TreecEva_data_reduced_natural_cot.json"
    output_file = "Think_TreecEva_data_reduced_cot.json"
    
    merge_cot_files(formated_file, natural_file, output_file)