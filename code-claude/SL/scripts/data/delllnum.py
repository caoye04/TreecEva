import json
import re
from pathlib import Path

def has_more_than_2_decimals(value):
    """检查数字是否有3位或更多小数位"""
    if isinstance(value, (int, bool)):
        return False
    if isinstance(value, float):
        # 转换为字符串检查小数位数
        value_str = str(value)
        if '.' in value_str:
            # 提取小数部分
            decimal_part = value_str.split('.')[1]
            # 移除科学计数法部分(如果有)
            if 'e' in decimal_part.lower():
                decimal_part = decimal_part.split('e')[0]
            # 检查小数位数是否>=3
            return len(decimal_part) >= 3
    return False

def clean_dataset(input_file, output_file):
    """删除所有answer为三位以上小数的数据"""
    
    # 读取数据集
    with open(input_file, 'r', encoding='utf-8') as f:
        dataset = json.load(f)
    
    if not dataset:
        print("数据集为空")
        return
    
    # 保留第一个元素(背景和需求描述)
    cleaned_dataset = [dataset[0]]
    
    # 统计信息
    total_tasks = len(dataset) - 1
    removed_count = 0
    
    # 处理剩余数据
    for i in range(1, len(dataset)):
        task = dataset[i]
        
        # 检查是否有answer字段
        if "task" in task and "answer" in task["task"]:
            answer = task["task"]["answer"]
            
            # 检查是否为三位以上小数
            if has_more_than_2_decimals(answer):
                removed_count += 1
                print(f"删除 {task['id']}: answer = {answer}")
            else:
                cleaned_dataset.append(task)
        else:
            # 没有answer字段的数据保留
            cleaned_dataset.append(task)
    
    # 保存清理后的数据集
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(cleaned_dataset, f, indent=2, ensure_ascii=False)
    
    # 打印统计信息
    print(f"\n清理完成:")
    print(f"原始任务数: {total_tasks}")
    print(f"删除任务数: {removed_count}")
    print(f"保留任务数: {len(cleaned_dataset) - 1}")
    print(f"结果已保存到: {output_file}")

if __name__ == "__main__":
    # 修改为你的文件路径
    input_file = "TreecEva_data.json"  # 输入文件
    output_file = "new_TreecEva_data.json"  # 输出文件
    
    clean_dataset(input_file, output_file)