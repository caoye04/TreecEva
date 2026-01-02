from itertools import combinations

def analyze_efficiency(tasks):
    efficiency_list = []
    for i, task in enumerate(tasks):
        base_efficiency = len(task) * (i + 1)
        adjusted = base_efficiency / (sum(ord(c) for c in task[:3]) / 30)
        efficiency_list.append(round(adjusted, 3))
    return efficiency_list

def evaluate_performance(metrics, weights):
    weighted_sum = 0
    total_weight = sum(weights)
    normalized = [m / max(metrics) for m in metrics]
    
    # Distractor: complex but unused calculation with combinations
    combo_values = []
    for r in range(2, 4):
        for combo in combinations(normalized, r):
            combo_values.append(sum(combo) ** 0.5)
    
    # Actual logic
    for i in range(len(metrics)):
        contribution = normalized[i] * weights[i]
        weighted_sum += contribution
    
    # More distraction: unrelated string processing
    temp_text = "performance_log_2024"
    shift_val = len(temp_text.replace("_", "")) % 7
    dummy_offset = sum(shift_val for _ in range(3)) // 3
    
    final_value = int(weighted_sum * 1000) + dummy_offset  # dummy_offset ends up not affecting much
    return final_value

def main():
    task_set = ['compile', 'deploy', 'validate', 'rollback', 'monitor']
    weights = [5, 3, 8, 2, 4]
    
    # Intermediate distractor variables
    status_flags = {t: False for t in task_set}
    for idx, t in enumerate(task_set):
        if idx % 2 == 0:
            status_flags[t] = True
    
    raw_metrics = analyze_efficiency(task_set)
    
    # Key intervention point
    final_score = evaluate_performance(raw_metrics, weights)
    
    # Output required format
    print(f"Result: {final_score}")

if __name__ == "__main__":
    main()