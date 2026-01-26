import json
import re
from collections import Counter
import matplotlib.pyplot as plt
import numpy as np

def setup_chinese_font():
    """设置中文字体，使用系统可用字体"""
    # 按优先级尝试字体
    font_names = [
        'PingFang SC',      # 苹方（最推荐）
        'Songti SC',        # 宋体
        'Heiti TC',         # 黑体
        'STHeiti',          # 华文黑体
        'Kaiti SC',         # 楷体
        'Baoli SC',         # 报隶
    ]
    
    for font_name in font_names:
        try:
            plt.rcParams['font.sans-serif'] = [font_name, 'Arial Unicode MS']
            plt.rcParams['axes.unicode_minus'] = False
            print(f"✓ 使用字体: {font_name}")
            return True
        except:
            continue
    
    print("⚠ 警告: 未能设置中文字体")
    return False

def count_functions_in_code(code):
    """统计代码中定义的函数数量"""
    pattern = r'^\s*def\s+\w+\s*\('
    lines = code.split('\n')
    count = 0
    for line in lines:
        if re.match(pattern, line):
            count += 1
    return count

def count_function_calls(code):
    """统计代码中函数调用的次数"""
    def_pattern = r'^\s*def\s+(\w+)\s*\('
    lines = code.split('\n')
    function_names = set()
    for line in lines:
        match = re.match(def_pattern, line)
        if match:
            function_names.add(match.group(1))
    
    call_count = 0
    for line in lines:
        for func_name in function_names:
            if f'{func_name}(' in line and not re.match(r'^\s*def\s+' + func_name, line):
                call_count += line.count(f'{func_name}(')
    
    return call_count

def plot_distributions(input_file):
    """生成3张分布图"""
    
    # 设置中文字体
    setup_chinese_font()
    
    # 收集数据
    code_line_counts = []
    function_counts = []
    function_call_counts = []
    
    print("\n正在读取数据...")
    with open(input_file, 'r', encoding='utf-8') as f:
        for line in f:
            if line.strip():
                data = json.loads(line)
                code = data.get('task', {}).get('code', '')
                
                lines = [l for l in code.split('\n') if l.strip()]
                line_count = len(lines)
                code_line_counts.append(line_count)
                
                func_count = count_functions_in_code(code)
                function_counts.append(func_count)
                
                call_count = count_function_calls(code)
                function_call_counts.append(call_count)
    
    total_samples = len(code_line_counts)
    print(f"✓ 成功读取 {total_samples} 个样本\n")
    
    # 创建图表
    fig, axes = plt.subplots(1, 3, figsize=(20, 6))
    fig.suptitle('跨函数级代码推理数据集分布分析', fontsize=18, fontweight='bold', y=0.98)
    
    # ===== 图1: 代码行数分布 =====
    print("生成图1: 代码行数分布...")
    ax1 = axes[0]
    
    line_ranges = [
        (0, 10), (11, 20), (21, 30), (31, 40), (41, 50),
        (51, 60), (61, 70), (71, 80), (81, 90), (91, 100),
        (101, 110), (111, 120), (121, 130), (131, 140)
    ]
    
    range_labels = []
    range_counts = []
    
    for start, end in line_ranges:
        count = sum(1 for x in code_line_counts if start <= x <= end)
        if count > 0:
            range_labels.append(f'{start}-{end}')
            range_counts.append(count)
    
    above_140 = sum(1 for x in code_line_counts if x > 140)
    if above_140 > 0:
        range_labels.append('141+')
        range_counts.append(above_140)
    
    bars1 = ax1.bar(range(len(range_labels)), range_counts, color='#3498db', alpha=0.8, edgecolor='black', linewidth=1.2)
    ax1.set_xlabel('代码行数区间', fontsize=14, fontweight='bold')
    ax1.set_ylabel('样本数量', fontsize=14, fontweight='bold')
    ax1.set_title(f'代码行数分布 (总计: {total_samples} 个样本)', fontsize=15, fontweight='bold', pad=15)
    ax1.set_xticks(range(len(range_labels)))
    ax1.set_xticklabels(range_labels, rotation=45, ha='right', fontsize=11)
    ax1.tick_params(axis='y', labelsize=11)
    ax1.grid(axis='y', alpha=0.3, linestyle='--', linewidth=0.8)
    
    for i, (bar, count) in enumerate(zip(bars1, range_counts)):
        height = bar.get_height()
        percentage = (count / total_samples) * 100
        ax1.text(bar.get_x() + bar.get_width()/2., height,
                f'{count}\n({percentage:.1f}%)',
                ha='center', va='bottom', fontsize=10, fontweight='bold')
    
    # ===== 图2: 函数数量分布 =====
    print("生成图2: 函数数量分布...")
    ax2 = axes[1]
    
    func_counter = Counter(function_counts)
    func_nums = sorted(func_counter.keys())
    func_counts_list = [func_counter[n] for n in func_nums]
    
    bars2 = ax2.bar(func_nums, func_counts_list, color='#2ecc71', alpha=0.8, edgecolor='black', linewidth=1.2)
    ax2.set_xlabel('函数数量', fontsize=14, fontweight='bold')
    ax2.set_ylabel('样本数量', fontsize=14, fontweight='bold')
    ax2.set_title(f'函数数量分布 (总计: {total_samples} 个样本)', fontsize=15, fontweight='bold', pad=15)
    ax2.set_xticks(func_nums)
    ax2.tick_params(axis='both', labelsize=11)
    ax2.grid(axis='y', alpha=0.3, linestyle='--', linewidth=0.8)
    
    for bar, count in zip(bars2, func_counts_list):
        height = bar.get_height()
        percentage = (count / total_samples) * 100
        ax2.text(bar.get_x() + bar.get_width()/2., height,
                f'{count}\n({percentage:.1f}%)',
                ha='center', va='bottom', fontsize=10, fontweight='bold')
    
    # ===== 图3: 函数调用次数分布 =====
    print("生成图3: 函数调用次数分布...")
    ax3 = axes[2]
    
    call_ranges = [
        ('1', 1, 1),
        ('2', 2, 2),
        ('3', 3, 3),
        ('4-5', 4, 5),
        ('6-7', 6, 7),
        ('8-10', 8, 10),
        ('11-15', 11, 15),
        ('16+', 16, float('inf'))
    ]
    
    call_labels = []
    call_counts_list = []
    
    for label, start, end in call_ranges:
        if end == float('inf'):
            count = sum(1 for x in function_call_counts if x >= start)
        else:
            count = sum(1 for x in function_call_counts if start <= x <= end)
        
        if count > 0:
            call_labels.append(label)
            call_counts_list.append(count)
    
    bars3 = ax3.bar(range(len(call_labels)), call_counts_list, color='#e74c3c', alpha=0.8, edgecolor='black', linewidth=1.2)
    ax3.set_xlabel('函数调用次数', fontsize=14, fontweight='bold')
    ax3.set_ylabel('样本数量', fontsize=14, fontweight='bold')
    ax3.set_title(f'函数调用次数分布 (总计: {total_samples} 个样本)', fontsize=15, fontweight='bold', pad=15)
    ax3.set_xticks(range(len(call_labels)))
    ax3.set_xticklabels(call_labels, fontsize=11)
    ax3.tick_params(axis='y', labelsize=11)
    ax3.grid(axis='y', alpha=0.3, linestyle='--', linewidth=0.8)
    
    for bar, count in zip(bars3, call_counts_list):
        height = bar.get_height()
        percentage = (count / total_samples) * 100
        ax3.text(bar.get_x() + bar.get_width()/2., height,
                f'{count}\n({percentage:.1f}%)',
                ha='center', va='bottom', fontsize=10, fontweight='bold')
    
    # 调整布局
    plt.tight_layout(rect=[0, 0, 1, 0.96])
    
    # 保存图片
    output_file = 'dataset_distribution.png'
    plt.savefig(output_file, dpi=300, bbox_inches='tight', facecolor='white')
    print(f"\n✓ 图表已保存到: {output_file}")
    
    # 显示图片
    print("正在显示图表...")
    plt.show()
    
    # 打印统计摘要
    print("\n" + "="*60)
    print("统计摘要:")
    print("="*60)
    print(f"代码行数 - 平均: {np.mean(code_line_counts):.1f}, 中位数: {np.median(code_line_counts):.0f}, 范围: {min(code_line_counts)}-{max(code_line_counts)}")
    print(f"函数数量 - 平均: {np.mean(function_counts):.1f}, 中位数: {np.median(function_counts):.0f}, 范围: {min(function_counts)}-{max(function_counts)}")
    print(f"调用次数 - 平均: {np.mean(function_call_counts):.1f}, 中位数: {np.median(function_call_counts):.0f}, 范围: {min(function_call_counts)}-{max(function_call_counts)}")
    print("="*60)

if __name__ == "__main__":
    input_file = "cross_function.jsonl"
    
    try:
        plot_distributions(input_file)
    except FileNotFoundError:
        print(f"❌ 错误: 找不到文件 '{input_file}'")
        print("请确保 cross_function.jsonl 文件与脚本在同一目录下")
    except Exception as e:
        print(f"❌ 发生错误: {str(e)}")
        import traceback
        traceback.print_exc()