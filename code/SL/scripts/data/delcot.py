import json
import os

def remove_cot_content(json_file_path):
    """
    读取JSON文件，去除所有数据中cot字段的内容，只保留空的"cot":""
    
    Args:
        json_file_path: JSON文件的路径
    """
    # 读取JSON文件
    with open(json_file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # 遍历数据并清空cot字段
    for item in data:
        if 'task' in item and 'cot' in item['task']:
            item['task']['cot'] = ""
    
    # 将修改后的数据写回文件
    with open(json_file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print(f"已成功处理文件: {json_file_path}")
    print(f"共处理 {len(data)} 条数据")

if __name__ == "__main__":
    # 获取脚本所在目录
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # JSON文件名（请根据实际文件名修改）
    json_filename = "TreecEva_data_without_cot.json"
    
    # 构建完整路径
    json_file_path = os.path.join(script_dir, json_filename)
    
    # 检查文件是否存在
    if os.path.exists(json_file_path):
        remove_cot_content(json_file_path)
    else:
        print(f"错误: 文件 {json_file_path} 不存在")
        print(f"请确保JSON文件与脚本在同一目录下，或修改 json_filename 变量")