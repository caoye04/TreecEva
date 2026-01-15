import json
import tiktoken

def count_tokens(text):
    """使用tiktoken计算token数量"""
    encoding = tiktoken.get_encoding("cl100k_base")  # GPT-4使用的编码
    return len(encoding.encode(text))

def analyze_cot_tokens(input_file):
    """分析COT token数量"""
    
    # 读取数据
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # 跳过第一个元素（background和requirements）
    cases = data[1:]
    
    # 统计token数量
    token_counts = {}
    token_distribution = {}
    cases_over_5000 = []
    cases_under_100 = []  # 新增：记录低于100的case
    
    print("开始分析COT token数量...\n")
    
    for case in cases:
        case_id = case.get('id')
        cot = case.get('task', {}).get('cot', '')
        
        if cot:
            token_count = count_tokens(cot)
            token_counts[case_id] = token_count
            
            # 按1000尺度分类
            bucket = (token_count // 1000) * 1000
            token_distribution[bucket] = token_distribution.get(bucket, 0) + 1
            
            # 记录超过5000的case
            if token_count > 5000:
                cases_over_5000.append(case_id)
            
            # 记录低于100的case
            if token_count < 100:
                cases_under_100.append(case_id)
    
    # 输出统计信息
    print("=" * 60)
    print("Token数量分布（每1000为一档）：")
    print("=" * 60)
    
    for bucket in sorted(token_distribution.keys()):
        count = token_distribution[bucket]
        range_str = f"{bucket}-{bucket+999}"
        print(f"{range_str:>15} tokens: {count:>5} cases")
    
    print("\n" + "=" * 60)
    print(f"总case数量: {len(cases)}")
    print(f"token < 100 的case数量: {len(cases_under_100)}")
    print(f"token > 5000 的case数量: {len(cases_over_5000)}")
    print("=" * 60)
    
    # 导出低于100 token的case ID
    output_data_under_100 = {
        "total_cases": len(cases),
        "cases_under_100_count": len(cases_under_100),
        "case_ids": cases_under_100,
        "details": {case_id: token_counts[case_id] for case_id in cases_under_100}
    }
    
    output_file_under_100 = "cases_under_100_tokens.json"
    with open(output_file_under_100, 'w', encoding='utf-8') as f:
        json.dump(output_data_under_100, f, indent=2, ensure_ascii=False)
    
    print(f"\n已导出低于100 token的case到: {output_file_under_100}")
    
    # 导出超过5000 token的case ID
    output_data_over_5000 = {
        "total_cases": len(cases),
        "cases_over_5000_count": len(cases_over_5000),
        "case_ids": cases_over_5000,
        "details": {case_id: token_counts[case_id] for case_id in cases_over_5000}
    }
    
    output_file_over_5000 = "cases_over_5000_tokens.json"
    with open(output_file_over_5000, 'w', encoding='utf-8') as f:
        json.dump(output_data_over_5000, f, indent=2, ensure_ascii=False)
    
    print(f"已导出高于5000 token的case到: {output_file_over_5000}")
    
    # 显示一些统计信息
    if token_counts:
        min_tokens = min(token_counts.values())
        max_tokens = max(token_counts.values())
        avg_tokens = sum(token_counts.values()) / len(token_counts)
        
        print(f"\n详细统计：")
        print(f"  最小token数: {min_tokens}")
        print(f"  最大token数: {max_tokens}")
        print(f"  平均token数: {avg_tokens:.2f}")
        
        if cases_under_100:
            print(f"\ntoken < 100 的case示例:")
            for case_id in cases_under_100[:5]:  # 只显示前5个
                print(f"  {case_id}: {token_counts[case_id]} tokens")
            if len(cases_under_100) > 5:
                print(f"  ... 还有 {len(cases_under_100) - 5} 个case")
        
        if cases_over_5000:
            print(f"\ntoken > 5000 的case示例:")
            for case_id in cases_over_5000[:5]:  # 只显示前5个
                print(f"  {case_id}: {token_counts[case_id]} tokens")
            if len(cases_over_5000) > 5:
                print(f"  ... 还有 {len(cases_over_5000) - 5} 个case")

if __name__ == "__main__":
    input_file = "TreecEva_data_reduced_natural_cot.json"
    
    try:
        analyze_cot_tokens(input_file)
    except FileNotFoundError:
        print(f"错误: 找不到文件 '{input_file}'")
        print("请确保文件在当前目录下")
    except json.JSONDecodeError:
        print(f"错误: '{input_file}' 不是有效的JSON文件")
    except Exception as e:
        print(f"发生错误: {str(e)}")