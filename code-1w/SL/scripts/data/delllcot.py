import json
from pathlib import Path

def clean_dataset(input_file, output_file):
    """
    清理数据集:
    1. 删除answer为真正小数(如48.5)的任务的cot字段
    2. 将answer为整数形式的浮点数(如7.0)转换为整数
    """
    # 读取数据集
    with open(input_file, 'r', encoding='utf-8') as f:
        dataset = json.load(f)
    
    # 统计信息
    removed_cot_count = 0
    converted_to_int_count = 0
    
    # 处理数据集(跳过第一个background元素)
    for i in range(1, len(dataset)):
        task = dataset[i]
        
        if "task" in task and "answer" in task["task"]:
            answer = task["task"]["answer"]
            
            # 检查是否为浮点数类型
            if isinstance(answer, float):
                # 检查是否为整数形式的浮点数(如7.0)
                if answer.is_integer():
                    # 转换为整数
                    dataset[i]["task"]["answer"] = int(answer)
                    converted_to_int_count += 1
                    print(f"✓ Task {task['id']}: Answer converted from {answer} to {int(answer)}")
                else:
                    # 真正的小数,删除cot字段
                    if "cot" in task["task"]:
                        del dataset[i]["task"]["cot"]
                        removed_cot_count += 1
                        print(f"✗ Task {task['id']}: Removed COT (decimal answer: {answer})")
    
    # 保存处理后的数据集
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(dataset, f, indent=2, ensure_ascii=False)
    
    # 输出统计信息
    print(f"\n{'='*50}")
    print(f"处理完成!")
    print(f"{'='*50}")
    print(f"移除COT的任务数: {removed_cot_count}")
    print(f"转换为整数的任务数: {converted_to_int_count}")
    print(f"输出文件: {output_file}")
    
    return removed_cot_count, converted_to_int_count

if __name__ == "__main__":
    # 配置路径
    input_file = "TreecEva_data.json"  # 输入文件路径
    output_file = "TreecEva_data_cleaned.json"  # 输出文件路径
    
    # 执行清理
    clean_dataset(input_file, output_file)