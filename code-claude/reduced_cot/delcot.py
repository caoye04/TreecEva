import json
import os
import sys

def remove_cot_content(json_file_path, mode='all', case_id=None):
    """
    读取JSON文件，去除cot字段的内容，只保留空的"cot":""
    
    Args:
        json_file_path: JSON文件的路径
        mode: 删除模式，'all'表示删除所有，'single'表示只删除指定ID的case
        case_id: 当mode为'single'时，指定要删除cot的case ID
    """
    # 读取JSON文件
    with open(json_file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    processed_count = 0
    
    # 遍历数据并清空cot字段
    for item in data:
        # 检查是否是需要处理的项
        should_process = False
        
        if mode == 'all':
            should_process = True
        elif mode == 'single' and case_id:
            if 'id' in item and item['id'] == case_id:
                should_process = True
        
        # 处理cot字段
        if should_process and 'task' in item and 'cot' in item['task']:
            item['task']['cot'] = ""
            processed_count += 1
    
    # 将修改后的数据写回文件
    with open(json_file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print(f"已成功处理文件: {json_file_path}")
    print(f"共处理 {processed_count} 条数据")
    
    if mode == 'single' and processed_count == 0:
        print(f"警告: 未找到ID为 '{case_id}' 的case")

if __name__ == "__main__":
    # 获取脚本所在目录
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # JSON文件名（请根据实际文件名修改）
    json_filename = "TreecEva_data_before_reduced_natural_cot.json"
    
    # 构建完整路径
    json_file_path = os.path.join(script_dir, json_filename)
    
    # 检查文件是否存在
    if not os.path.exists(json_file_path):
        print(f"错误: 文件 {json_file_path} 不存在")
        print(f"请确保JSON文件与脚本在同一目录下，或修改 json_filename 变量")
        sys.exit(1)
    
    # 解析命令行参数
    if len(sys.argv) == 1:
        # 没有参数，显示帮助信息
        print("用法:")
        print("  python delcot.py --all              删除所有case的cot")
        print("  python delcot.py <case_id>          删除指定ID的case的cot")
        print("\n示例:")
        print("  python delcot.py --all")
        print("  python delcot.py SL-MIX-S0001")
        sys.exit(0)
    
    elif sys.argv[1] == '--all':
        # 删除所有
        remove_cot_content(json_file_path, mode='all')
    
    else:
        # 删除指定ID
        case_id = sys.argv[1]
        remove_cot_content(json_file_path, mode='single', case_id=case_id)