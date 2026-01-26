import json
from collections import Counter
import re

def count_functions_in_code(code):
    """统计代码中定义的函数数量"""
    # 匹配 def function_name( 的模式
    pattern = r'^\s*def\s+\w+\s*\('
    lines = code.split('\n')
    count = 0
    for line in lines:
        if re.match(pattern, line):
            count += 1
    return count

def count_function_calls(code):
    """统计代码中函数调用的次数"""
    # 先提取所有定义的函数名
    def_pattern = r'^\s*def\s+(\w+)\s*\('
    lines = code.split('\n')
    function_names = set()
    for line in lines:
        match = re.match(def_pattern, line)
        if match:
            function_names.add(match.group(1))
    
    # 统计这些函数被调用的次数
    call_count = 0
    for line in lines:
        for func_name in function_names:
            # 匹配函数调用: function_name(
            # 要避免匹配到 def function_name(
            if f'{func_name}(' in line and not re.match(r'^\s*def\s+' + func_name, line):
                # 统计该行中该函数被调用的次数
                call_count += line.count(f'{func_name}(')
    
    return call_count

def analyze_dataset(input_file, output_file):
    # 存储统计数据
    code_line_counts = []
    function_counts = []
    function_call_counts = []
    samples = []  # 存储完整样本信息用于后续筛选
    
    # 读取JSONL文件
    with open(input_file, 'r', encoding='utf-8') as f:
        for line in f:
            if line.strip():  # 跳过空行
                data = json.loads(line)
                
                # 提取代码相关信息
                code = data.get('task', {}).get('code', '')
                
                # 统计代码行数（排除空行）
                lines = [l for l in code.split('\n') if l.strip()]
                line_count = len(lines)
                code_line_counts.append(line_count)
                
                # 统计函数数量
                func_count = count_functions_in_code(code)
                function_counts.append(func_count)
                
                # 统计函数调用次数
                call_count = count_function_calls(code)
                function_call_counts.append(call_count)
                
                # 保存样本信息
                samples.append({
                    'id': data.get('id', 'unknown'),
                    'description': data.get('task', {}).get('description', '')[:100] + '...',
                    'line_count': line_count,
                    'func_count': func_count,
                    'call_count': call_count,
                    'code': code
                })
    
    # 生成分析报告
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("=" * 80 + "\n")
        f.write("跨函数级代码推理数据集分析报告\n")
        f.write("=" * 80 + "\n\n")
        
        # 基本统计
        f.write(f"数据集总样本数: {len(code_line_counts)}\n\n")
        
        # 1. 代码行数分布（更细致的区间）
        f.write("-" * 80 + "\n")
        f.write("1. 代码行数分布\n")
        f.write("-" * 80 + "\n")
        
        # 定义更细致的区间
        ranges = [
            (0, 10), (11, 20), (21, 30), (31, 40), (41, 50),
            (51, 60), (61, 70), (71, 80), (81, 90), (91, 100),
            (101, 110), (111, 120), (121, 130), (131, 140), (141, float('inf'))
        ]
        
        for start, end in ranges:
            if end == float('inf'):
                count = sum(1 for x in code_line_counts if x > start)
                percentage = (count / len(code_line_counts)) * 100
                f.write(f"  {start}+ 行: {count:4d} 样本 ({percentage:5.2f}%)\n")
            else:
                count = sum(1 for x in code_line_counts if start <= x <= end)
                percentage = (count / len(code_line_counts)) * 100
                f.write(f"  {start:3d}-{end:3d} 行: {count:4d} 样本 ({percentage:5.2f}%)\n")
        
        f.write(f"\n  平均行数: {sum(code_line_counts) / len(code_line_counts):.2f}\n")
        f.write(f"  中位数: {sorted(code_line_counts)[len(code_line_counts)//2]}\n")
        f.write(f"  最少行数: {min(code_line_counts)}\n")
        f.write(f"  最多行数: {max(code_line_counts)}\n\n")
        
        # 2. 函数数量分布
        f.write("-" * 80 + "\n")
        f.write("2. 代码中函数数量分布\n")
        f.write("-" * 80 + "\n")
        function_counter = Counter(function_counts)
        for func_count in sorted(function_counter.keys()):
            count = function_counter[func_count]
            percentage = (count / len(function_counts)) * 100
            f.write(f"  {func_count:2d} 个函数: {count:4d} 样本 ({percentage:5.2f}%)\n")
        f.write(f"\n  平均函数数: {sum(function_counts) / len(function_counts):.2f}\n")
        f.write(f"  中位数: {sorted(function_counts)[len(function_counts)//2]}\n")
        f.write(f"  最少函数数: {min(function_counts)}\n")
        f.write(f"  最多函数数: {max(function_counts)}\n\n")
        
        # 3. 函数调用次数分布（更细致）
        f.write("-" * 80 + "\n")
        f.write("3. 函数调用次数分布\n")
        f.write("-" * 80 + "\n")
        
        # 先用Counter统计每个具体调用次数
        call_counter = Counter(function_call_counts)
        
        # 对于调用次数较少的，逐个列出
        f.write("详细分布（按调用次数）:\n")
        for call_num in sorted(call_counter.keys()):
            if call_num <= 15:  # 15次及以下逐个列出
                count = call_counter[call_num]
                percentage = (count / len(function_call_counts)) * 100
                f.write(f"  {call_num:2d} 次: {count:4d} 样本 ({percentage:5.2f}%)\n")
        
        # 统计15次以上的
        above_15 = sum(1 for x in function_call_counts if x > 15)
        if above_15 > 0:
            percentage = (above_15 / len(function_call_counts)) * 100
            f.write(f"  16+ 次: {above_15:4d} 样本 ({percentage:5.2f}%)\n")
        
        f.write(f"\n区间统计:\n")
        # 定义调用次数区间
        call_ranges = [
            (1, 1), (2, 2), (3, 3), (4, 5), (6, 7), (8, 10), (11, 15), (16, float('inf'))
        ]
        
        for start, end in call_ranges:
            if end == float('inf'):
                count = sum(1 for x in function_call_counts if x >= start)
                percentage = (count / len(function_call_counts)) * 100
                f.write(f"  {start}+ 次: {count:4d} 样本 ({percentage:5.2f}%)\n")
            elif start == end:
                count = sum(1 for x in function_call_counts if x == start)
                percentage = (count / len(function_call_counts)) * 100
                f.write(f"  {start} 次: {count:4d} 样本 ({percentage:5.2f}%)\n")
            else:
                count = sum(1 for x in function_call_counts if start <= x <= end)
                percentage = (count / len(function_call_counts)) * 100
                f.write(f"  {start:2d}-{end:2d} 次: {count:4d} 样本 ({percentage:5.2f}%)\n")
        
        f.write(f"\n  平均调用次数: {sum(function_call_counts) / len(function_call_counts):.2f}\n")
        f.write(f"  中位数: {sorted(function_call_counts)[len(function_call_counts)//2]}\n")
        f.write(f"  最少调用次数: {min(function_call_counts)}\n")
        f.write(f"  最多调用次数: {max(function_call_counts)}\n\n")
        
        # 4. 超短样本列表（行数 <= 15）
        f.write("=" * 80 + "\n")
        f.write("4. 超短样本列表（代码行数 <= 15）\n")
        f.write("=" * 80 + "\n\n")
        short_samples = [s for s in samples if s['line_count'] <= 15]
        short_samples.sort(key=lambda x: x['line_count'])
        
        for i, sample in enumerate(short_samples, 1):
            f.write(f"[{i}] ID: {sample['id']}\n")
            f.write(f"    行数: {sample['line_count']} | 函数数: {sample['func_count']} | 调用次数: {sample['call_count']}\n")
            f.write(f"    描述: {sample['description']}\n")
            f.write(f"    代码:\n")
            for line in sample['code'].split('\n'):
                if line.strip():
                    f.write(f"        {line}\n")
            f.write("\n")
        
        f.write(f"共 {len(short_samples)} 个超短样本\n\n")
        
        # 5. 超长样本列表（行数 >= 100）
        f.write("=" * 80 + "\n")
        f.write("5. 超长样本列表（代码行数 >= 100）\n")
        f.write("=" * 80 + "\n\n")
        long_samples = [s for s in samples if s['line_count'] >= 100]
        long_samples.sort(key=lambda x: x['line_count'], reverse=True)
        
        for i, sample in enumerate(long_samples, 1):
            f.write(f"[{i}] ID: {sample['id']}\n")
            f.write(f"    行数: {sample['line_count']} | 函数数: {sample['func_count']} | 调用次数: {sample['call_count']}\n")
            f.write(f"    描述: {sample['description']}\n")
            f.write(f"    代码预览（前20行）:\n")
            code_lines = [l for l in sample['code'].split('\n') if l.strip()]
            for line in code_lines[:20]:
                f.write(f"        {line}\n")
            if len(code_lines) > 20:
                f.write(f"        ... (省略剩余 {len(code_lines) - 20} 行)\n")
            f.write("\n")
        
        f.write(f"共 {len(long_samples)} 个超长样本\n\n")
        
        # 6. 函数数量极值样本
        f.write("=" * 80 + "\n")
        f.write("6. 函数数量极值样本\n")
        f.write("=" * 80 + "\n\n")
        
        # 最少函数样本（1个函数）
        f.write("6.1 单函数样本（前10个）:\n")
        f.write("-" * 80 + "\n")
        single_func_samples = [s for s in samples if s['func_count'] == 1]
        for i, sample in enumerate(single_func_samples[:10], 1):
            f.write(f"[{i}] ID: {sample['id']} | 行数: {sample['line_count']} | 调用次数: {sample['call_count']}\n")
            f.write(f"    描述: {sample['description']}\n\n")
        f.write(f"共 {len(single_func_samples)} 个单函数样本\n\n")
        
        # 最多函数样本
        max_funcs = max(function_counts)
        f.write(f"6.2 最多函数样本（{max_funcs}个函数）:\n")
        f.write("-" * 80 + "\n")
        max_func_samples = [s for s in samples if s['func_count'] == max_funcs]
        for i, sample in enumerate(max_func_samples, 1):
            f.write(f"[{i}] ID: {sample['id']} | 行数: {sample['line_count']} | 调用次数: {sample['call_count']}\n")
            f.write(f"    描述: {sample['description']}\n")
            f.write(f"    代码预览（前30行）:\n")
            code_lines = [l for l in sample['code'].split('\n') if l.strip()]
            for line in code_lines[:30]:
                f.write(f"        {line}\n")
            if len(code_lines) > 30:
                f.write(f"        ... (省略剩余 {len(code_lines) - 30} 行)\n")
            f.write("\n")
        
        # 7. 函数调用次数极值样本
        f.write("=" * 80 + "\n")
        f.write("7. 函数调用次数极值样本\n")
        f.write("=" * 80 + "\n\n")
        
        # 单次调用样本
        f.write("7.1 单次调用样本（前10个）:\n")
        f.write("-" * 80 + "\n")
        single_call_samples = [s for s in samples if s['call_count'] == 1]
        for i, sample in enumerate(single_call_samples[:10], 1):
            f.write(f"[{i}] ID: {sample['id']} | 行数: {sample['line_count']} | 函数数: {sample['func_count']}\n")
            f.write(f"    描述: {sample['description']}\n\n")
        f.write(f"共 {len(single_call_samples)} 个单次调用样本\n\n")
        
        # 最多调用样本
        max_calls = max(function_call_counts)
        f.write(f"7.2 最多调用样本（{max_calls}次调用）:\n")
        f.write("-" * 80 + "\n")
        max_call_samples = [s for s in samples if s['call_count'] == max_calls]
        for i, sample in enumerate(max_call_samples, 1):
            f.write(f"[{i}] ID: {sample['id']} | 行数: {sample['line_count']} | 函数数: {sample['func_count']}\n")
            f.write(f"    描述: {sample['description']}\n")
            f.write(f"    代码预览（前30行）:\n")
            code_lines = [l for l in sample['code'].split('\n') if l.strip()]
            for line in code_lines[:30]:
                f.write(f"        {line}\n")
            if len(code_lines) > 30:
                f.write(f"        ... (省略剩余 {len(code_lines) - 30} 行)\n")
            f.write("\n")
        
        # 高频调用样本（调用次数 >= 8）
        f.write("7.3 高频调用样本（调用次数 >= 8）:\n")
        f.write("-" * 80 + "\n")
        high_call_samples = [s for s in samples if s['call_count'] >= 8]
        high_call_samples.sort(key=lambda x: x['call_count'], reverse=True)
        for i, sample in enumerate(high_call_samples, 1):
            f.write(f"[{i}] ID: {sample['id']} | 调用次数: {sample['call_count']} | 行数: {sample['line_count']} | 函数数: {sample['func_count']}\n")
            f.write(f"    描述: {sample['description']}\n")
            f.write(f"    代码预览（前25行）:\n")
            code_lines = [l for l in sample['code'].split('\n') if l.strip()]
            for line in code_lines[:25]:
                f.write(f"        {line}\n")
            if len(code_lines) > 25:
                f.write(f"        ... (省略剩余 {len(code_lines) - 25} 行)\n")
            f.write("\n")
        f.write(f"共 {len(high_call_samples)} 个高频调用样本\n\n")
        
        # 8. 相关性分析
        f.write("=" * 80 + "\n")
        f.write("8. 多维度相关性分析\n")
        f.write("=" * 80 + "\n\n")
        
        # 按函数数量分组统计平均行数和调用次数
        func_to_stats = {}
        for sample in samples:
            fc = sample['func_count']
            if fc not in func_to_stats:
                func_to_stats[fc] = {'lines': [], 'calls': []}
            func_to_stats[fc]['lines'].append(sample['line_count'])
            func_to_stats[fc]['calls'].append(sample['call_count'])
        
        f.write("8.1 函数数量 -> 平均代码行数 & 平均调用次数:\n")
        f.write("-" * 80 + "\n")
        for func_count in sorted(func_to_stats.keys()):
            avg_lines = sum(func_to_stats[func_count]['lines']) / len(func_to_stats[func_count]['lines'])
            avg_calls = sum(func_to_stats[func_count]['calls']) / len(func_to_stats[func_count]['calls'])
            sample_count = len(func_to_stats[func_count]['lines'])
            f.write(f"  {func_count:2d} 个函数: 平均 {avg_lines:6.2f} 行, {avg_calls:5.2f} 次调用 ({sample_count:3d} 个样本)\n")
        
        # 按调用次数统计
        f.write("\n8.2 调用次数 -> 平均函数数 & 平均代码行数:\n")
        f.write("-" * 80 + "\n")
        
        # 按具体调用次数统计（只显示有足够样本的）
        call_to_stats = {}
        for sample in samples:
            cc = sample['call_count']
            if cc not in call_to_stats:
                call_to_stats[cc] = {'funcs': [], 'lines': []}
            call_to_stats[cc]['funcs'].append(sample['func_count'])
            call_to_stats[cc]['lines'].append(sample['line_count'])
        
        for call_count in sorted(call_to_stats.keys()):
            if len(call_to_stats[call_count]['funcs']) >= 5:  # 至少5个样本才显示
                avg_funcs = sum(call_to_stats[call_count]['funcs']) / len(call_to_stats[call_count]['funcs'])
                avg_lines = sum(call_to_stats[call_count]['lines']) / len(call_to_stats[call_count]['lines'])
                sample_count = len(call_to_stats[call_count]['funcs'])
                f.write(f"  {call_count:2d} 次调用: 平均 {avg_funcs:4.2f} 个函数, {avg_lines:6.2f} 行 ({sample_count:3d} 个样本)\n")
        
        f.write("\n" + "=" * 80 + "\n")
        f.write("分析完成！\n")
        f.write("=" * 80 + "\n")
    
    print(f"分析完成！结果已保存到 {output_file}")

if __name__ == "__main__":
    input_file = "cross_function.jsonl"
    output_file = "ana.txt"
    
    try:
        analyze_dataset(input_file, output_file)
    except FileNotFoundError:
        print(f"错误: 找不到文件 '{input_file}'")
        print("请确保 cross_function.jsonl 文件与脚本在同一目录下")
    except Exception as e:
        print(f"发生错误: {str(e)}")