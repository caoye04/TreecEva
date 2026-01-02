import itertools

def analyze_efficiency(logs):
    total_entries = len(logs)
    valid_logs = [entry for entry in logs if 'ERROR' not in entry]
    error_count = total_entries - len(valid_logs)
    
    # Irrelevant transformation
    reversed_logs = [log[::-1] for log in logs]
    palindrome_count = sum(1 for log in reversed_logs if log == log[::-1])
    
    return len(valid_logs), error_count


def compute_stability_index(metrics):
    base_stability = sum(metrics) / len(metrics)
    fluctuation = max(metrics) - min(metrics)
    
    # Distractor calculation with no impact
    smoothed = [abs(m - base_stability) for m in metrics]
    noise_level = sum(smoothed) / len(smoothed)
    
    adjusted_stability = base_stability - (fluctuation * 0.1)
    return adjusted_stability


def evaluate_performance(productivity, errors):
    efficiency_ratio = productivity / (errors + 1)
    bonus_factor = 1.0
    
    if efficiency_ratio > 8:
        bonus_factor = 1.5
    elif efficiency_ratio > 5:
        bonus_factor = 1.2
    
    raw_score = productivity * bonus_factor
    
    # Dead code branch (never executed due to logic)
    if productivity < 0:
        raw_score -= 100  # unreachable
    
    penalty = 0
    if errors > 10:
        penalty = 20
    
    final_score = raw_score - penalty
    return final_score

# Main execution
log_data = [
    'TASK_COMPLETE_1', 'TASK_FAIL_ERROR', 'TASK_COMPLETE_2', 'TASK_COMPLETE_3',
    'TASK_FAIL_ERROR', 'TASK_COMPLETE_4', 'TASK_COMPLETE_5', 'TASK_FAIL_WARNING'
]

metrics_data = [85, 90, 87, 92, 84, 88]

# Extract relevant stats
valid_count, error_count = analyze_efficiency(log_data)
stability = compute_stability_index(metrics_data)

# Simulate productivity based on valid tasks
productivity = valid_count * (stability / 10)

# Key statement
final_score = evaluate_performance(productivity, error_count)

print(f"Result: {final_score}")