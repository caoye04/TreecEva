import json
from pathlib import Path
from typing import Dict, List, Any

def load_json_file(filepath: str) -> List[Dict[str, Any]]:
    """加载JSON文件"""
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_json_file(data: List[Dict[str, Any]], filepath: str):
    """保存JSON文件"""
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def merge_cot_datasets():
    """合并三个CoT数据集"""
    
    # 定义文件路径
    files = {
        'simple_ai_cot': 'TreecEva_data_simple_ai_cot.json',
        'reduced_formated_cot': 'TreecEva_data_reduced_formated_cot.json',
        'reduced_natural_cot': 'TreecEva_data_reduced_natural_cot.json'
    }
    
    # 加载所有数据集
    print("正在加载数据集...")
    datasets = {}
    for key, filepath in files.items():
        try:
            datasets[key] = load_json_file(filepath)
            print(f"✓ 加载 {filepath}: {len(datasets[key])} 条记录")
        except FileNotFoundError:
            print(f"✗ 文件不存在: {filepath}")
            return
        except json.JSONDecodeError as e:
            print(f"✗ JSON解析错误 {filepath}: {e}")
            return
    
    # 验证数据集长度一致
    lengths = [len(d) for d in datasets.values()]
    if len(set(lengths)) != 1:
        print(f"警告: 数据集长度不一致: {dict(zip(files.keys(), lengths))}")
        return
    
    # 创建合并后的数据集
    print("\n正在合并数据集...")
    merged_data = []
    
    # 获取基础数据（使用第一个数据集作为基础）
    base_dataset = datasets['simple_ai_cot']
    
    for idx in range(len(base_dataset)):
        # 复制基础条目
        merged_entry = base_dataset[idx].copy()
        
        # 检查是否有task字段
        if 'task' in merged_entry:
            # 创建新的task字段，移除原来的cot
            new_task = {k: v for k, v in merged_entry['task'].items() if k != 'cot'}
            
            # 添加三个版本的CoT
            for cot_key, dataset in datasets.items():
                current_entry = dataset[idx]
                
                # 验证ID一致性
                if merged_entry.get('id') != current_entry.get('id'):
                    print(f"警告: 索引 {idx} 的ID不匹配!")
                    print(f"  Base: {merged_entry.get('id')}")
                    print(f"  {cot_key}: {current_entry.get('id')}")
                
                # 提取CoT内容
                if 'task' in current_entry and 'cot' in current_entry['task']:
                    new_task[cot_key] = current_entry['task']['cot']
                else:
                    print(f"警告: 索引 {idx} ({merged_entry.get('id')}) 在 {cot_key} 中缺少CoT")
                    new_task[cot_key] = None
            
            merged_entry['task'] = new_task
        
        merged_data.append(merged_entry)
    
    # 保存合并后的数据集
    output_file = 'TreecEva_data_merged_cot.json'
    print(f"\n正在保存到 {output_file}...")
    save_json_file(merged_data, output_file)
    
    print(f"✓ 成功合并 {len(merged_data)} 条记录")
    print(f"\n数据集统计:")
    print(f"  - 总记录数: {len(merged_data)}")
    
    # 检查第一条记录的CoT字段
    if merged_data and 'task' in merged_data[0]:
        cot_fields = [k for k in merged_data[0]['task'].keys() if 'cot' in k]
        print(f"  - CoT字段: {', '.join(cot_fields)}")
    
    print(f"\n输出文件: {output_file}")

if __name__ == "__main__":
    merge_cot_datasets()