import json

def analyze_ai_performance(data):
    """
    分析AI性能统计
    
    参数:
        data: 包含任务数据的字典
    """
    # AI模型名称(按照ai_correctness数组的索引顺序)
    ai_names = [
        "qwen3_235b",
        "qwen3_coder", 
        "minimax_text",
        "glm4_plus",
        "deepseek_v3"
    ]
    
    # 初始化统计变量
    num_ais = len(ai_names)
    correct_counts = [0] * num_ais
    total_tasks = len(data)
    
    # 难度分布统计
    difficulty_distribution = {}
    
    # 遍历所有任务
    for task_id, task_info in data.items():
        ai_correctness = task_info['ai_correctness']
        difficulty = task_info['new_difficulty']
        
        # 统计每个AI的正确次数
        for i, correct in enumerate(ai_correctness):
            correct_counts[i] += correct
        
        # 统计难度分布
        if difficulty not in difficulty_distribution:
            difficulty_distribution[difficulty] = 0
        difficulty_distribution[difficulty] += 1
    
    # 打印结果
    print("=" * 70)
    print("AI性能统计报告")
    print("=" * 70)
    print(f"\n总任务数: {total_tasks}")
    
    print("\n--- 难度分布 ---")
    for difficulty in sorted(difficulty_distribution.keys()):
        count = difficulty_distribution[difficulty]
        percentage = (count / total_tasks) * 100
        print(f"难度 {difficulty}: {count:3d} 个任务 ({percentage:5.1f}%)")
    
    print("\n--- AI正确率统计 ---")
    for i, count in enumerate(correct_counts):
        accuracy = (count / total_tasks) * 100
        print(f"{ai_names[i]:15s}: {count:3d}/{total_tasks} ({accuracy:6.2f}%)")
    
    # 按难度统计各AI的表现
    print("\n--- 按难度统计AI表现 ---")
    difficulty_stats = {}
    
    for task_id, task_info in data.items():
        difficulty = task_info['new_difficulty']
        ai_correctness = task_info['ai_correctness']
        
        if difficulty not in difficulty_stats:
            difficulty_stats[difficulty] = {
                'total': 0,
                'ai_correct': [0] * num_ais
            }
        
        difficulty_stats[difficulty]['total'] += 1
        for i, correct in enumerate(ai_correctness):
            difficulty_stats[difficulty]['ai_correct'][i] += correct
    
    for difficulty in sorted(difficulty_stats.keys()):
        stats = difficulty_stats[difficulty]
        total = stats['total']
        print(f"\n难度 {difficulty} (共 {total} 题):")
        for i, correct in enumerate(stats['ai_correct']):
            accuracy = (correct / total) * 100 if total > 0 else 0
            print(f"  {ai_names[i]:15s}: {correct:3d}/{total:3d} ({accuracy:5.1f}%)")
    
    # 找出表现最好的AI
    print("\n--- 综合排名 ---")
    ai_performance = [(ai_names[i], correct_counts[i], (correct_counts[i]/total_tasks)*100) 
                      for i in range(num_ais)]
    ai_performance.sort(key=lambda x: x[1], reverse=True)
    
    for rank, (name, count, accuracy) in enumerate(ai_performance, 1):
        print(f"{rank}. {name:15s}: {count:3d} 次正确 ({accuracy:6.2f}%)")
    
    # 验证原始统计数据
    print("\n--- 验证原始统计 ---")
    glm4_index = ai_names.index("glm4_plus")
    deepseek_index = ai_names.index("deepseek_v3")
    print(f"glm4_plus   : {correct_counts[glm4_index]}/{total_tasks} ({correct_counts[glm4_index]/total_tasks*100:.1f}%)")
    print(f"deepseek_v3 : {correct_counts[deepseek_index]}/{total_tasks} ({correct_counts[deepseek_index]/total_tasks*100:.1f}%)")
    
    print("\n" + "=" * 70)
    
    return {
        'ai_names': ai_names,
        'correct_counts': correct_counts,
        'total_tasks': total_tasks,
        'difficulty_distribution': difficulty_distribution,
        'difficulty_stats': difficulty_stats,
        'ai_performance': ai_performance
    }


def main():
    """主函数"""
    json_file = 'ai_evaluation_with_difficulty.json'
    
    try:
        print(f"正在读取文件: {json_file}")
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        print(f"成功读取 {len(data)} 条数据\n")
        stats = analyze_ai_performance(data)
        
        # 可选: 保存统计结果到文件
        output_file = 'ai_statistics_report.json'
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(stats, f, indent=2, ensure_ascii=False)
        print(f"\n统计结果已保存到: {output_file}")
        
    except FileNotFoundError:
        print(f"错误: 未找到文件 '{json_file}'")
        print("请确保文件在当前目录下")
    except json.JSONDecodeError as e:
        print(f"错误: JSON解析失败 - {e}")
    except Exception as e:
        print(f"错误: {e}")


if __name__ == "__main__":
    main()