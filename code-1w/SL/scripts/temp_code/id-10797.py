from itertools import combinations

def analyze_efficiency(tasks, overhead):
    base_efficiency = sum([len(task) for task in tasks]) / (overhead + 1)
    adjustment = 0
    for i in range(1, min(len(tasks), 4)):
        adjustment += len(list(combinations(tasks, i))) * 0.1
    return base_efficiency + adjustment

def calculate_stress_level(hours_worked, threshold=8):
    if hours_worked <= threshold:
        return 0
    return (hours_worked - threshold) ** 2  # quadratic stress increase

def evaluate_performance(output_quality, risk):
    scaled_quality = output_quality * 100
    penalty = 0
    if risk > 5:
        penalty = risk * 3
    return int(scaled_quality - penalty)

def main():
    task_list = ['dev', 'test', 'review', 'deploy', 'monitor']
    work_hours = 10
    base_productivity = 7.8
    overhead_cost = 3
    
    # Irrelevant tracking variables (distractors)
    daily_log = {day: [] for day in ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']}
    temp_result = None
    cumulative_load = 0
    
    for i, task in enumerate(task_list):
        cumulative_load += len(task) * (i + 1)
    
    # Misleading intermediate calculation
    theoretical_max = len(task_list) * 10
    efficiency_ratio = analyze_efficiency(task_list, overhead_cost)
    
    # Unused transformation
    normalized_tasks = [t.upper() for t in task_list]
    reversed_tasks = normalized_tasks[::-1]
    
    stress_level = calculate_stress_level(work_hours)
    risk_factor = stress_level if stress_level > 3 else 2
    
    # Key execution point
    final_score = evaluate_performance(base_productivity, risk_factor)
    
    # Additional red herring logic
    if final_score > 500:
        final_score = 500  # capping (never reached)
    elif final_score < 0:
        final_score = 0
    
    # Dead code branch (never executed)
    debug_mode = False
    if debug_mode:
        print(f'Debug: {cumulative_load=}, {theoretical_max=}')
    
    print(f'Result: {final_score}')

if __name__ == '__main__':
    main()