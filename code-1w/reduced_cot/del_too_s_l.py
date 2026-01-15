import json

def remove_cases_by_json_files(input_file, id_json_files, output_file):
    """
    根据多个JSON文件中记录的ID，从原数据集中删除对应的case
    
    Args:
        input_file: 原始数据文件路径
        id_json_files: 包含要删除的case ID的JSON文件列表
        output_file: 输出文件路径
    """
    
    # 读取原始数据
    print(f"读取原始数据文件: {input_file}")
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # 第一个元素是background和requirements，需要保留
    background = data[0]
    cases = data[1:]
    
    original_count = len(cases)
    print(f"原始case数量: {original_count}")
    
    # 收集所有要删除的ID
    ids_to_remove = set()
    
    for json_file in id_json_files:
        try:
            print(f"\n读取ID文件: {json_file}")
            with open(json_file, 'r', encoding='utf-8') as f:
                id_data = json.load(f)
                case_ids = id_data.get('case_ids', [])
                ids_to_remove.update(case_ids)
                print(f"  从此文件获取 {len(case_ids)} 个要删除的ID")
        except FileNotFoundError:
            print(f"  警告: 文件 '{json_file}' 不存在，跳过")
        except json.JSONDecodeError:
            print(f"  警告: 文件 '{json_file}' 格式错误，跳过")
    
    print(f"\n总共需要删除 {len(ids_to_remove)} 个唯一ID")
    
    # 过滤掉要删除的case
    filtered_cases = []
    removed_cases = []
    
    for case in cases:
        case_id = case.get('id')
        if case_id in ids_to_remove:
            removed_cases.append(case_id)
        else:
            filtered_cases.append(case)
    
    # 构建新的数据结构
    new_data = [background] + filtered_cases
    
    # 保存到新文件
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(new_data, f, indent=2, ensure_ascii=False)
    
    # 输出统计信息
    print("\n" + "=" * 60)
    print("删除完成统计：")
    print("=" * 60)
    print(f"原始case数量: {original_count}")
    print(f"实际删除数量: {len(removed_cases)}")
    print(f"剩余case数量: {len(filtered_cases)}")
    print(f"删除比例: {len(removed_cases)/original_count*100:.2f}%")
    print("=" * 60)
    
    # 显示删除的ID示例
    if removed_cases:
        print(f"\n已删除的case ID示例（前10个）:")
        for case_id in removed_cases[:10]:
            print(f"  - {case_id}")
        if len(removed_cases) > 10:
            print(f"  ... 还有 {len(removed_cases) - 10} 个")
    
    print(f"\n新数据已保存到: {output_file}")
    
    # 检查是否有ID在原数据中不存在
    existing_ids = {case.get('id') for case in cases}
    not_found_ids = ids_to_remove - existing_ids
    if not_found_ids:
        print(f"\n警告: 以下 {len(not_found_ids)} 个ID在原数据中不存在:")
        for case_id in list(not_found_ids)[:10]:
            print(f"  - {case_id}")
        if len(not_found_ids) > 10:
            print(f"  ... 还有 {len(not_found_ids) - 10} 个")

def main():
    # 配置文件路径
    input_file = "TreecEva_data_reduced_natural_cot.json"
    
    # 要删除的ID来源文件列表
    id_json_files = [
        "cases_under_100_tokens.json",
        "cases_over_5000_tokens.json"
    ]
    
    # 输出文件路径
    output_file = "TreecEva_data_reduced_natural_cot.json"
    
    try:
        remove_cases_by_json_files(input_file, id_json_files, output_file)
    except FileNotFoundError as e:
        print(f"错误: 找不到文件 - {e}")
    except json.JSONDecodeError as e:
        print(f"错误: JSON格式错误 - {e}")
    except Exception as e:
        print(f"发生错误: {str(e)}")

if __name__ == "__main__":
    main()