import json
import sys

def filter_and_renumber(input_file, output_file):
    # 读取JSON文件
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # 分离背景信息和数据条目
    background = None
    entries = []
    
    for item in data:
        if 'background' in item and 'requirements' in item:
            # 这是背景信息，保留
            background = item
        elif 'id' in item and 'task' in item:
            # 这是数据条目，检查cot值
            cot_value = item.get('task', {}).get('cot', None)
            
            # 过滤掉cot为"1"或""的case
            if cot_value != "1" and cot_value != "":
                entries.append(item)
    
    # 组合结果
    result = []
    if background:
        result.append(background)
    result.extend(entries)
    
    # 写入输出文件
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
    
    print(f"处理完成！")
    print(f"原始数据条目数: {len([item for item in data if 'id' in item])}")
    print(f"过滤后数据条目数: {len(entries)}")
    print(f"结果已保存到: {output_file}")

if __name__ == "__main__":
    if len(sys.argv) == 3:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
    else:
        # 默认文件名
        input_file = "OLD_TreecEva_data_reduced_formated_cot.json"
        output_file = "TreecEva_data_reduced_formated_cot.json"
    
    filter_and_renumber(input_file, output_file)