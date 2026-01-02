def analyze_productivity(logs):
    base_efficiency = 85
    overhead_penalty = 0
    for log in logs:
        if log['errors'] > 3:
            overhead_penalty += log['timeout_count'] * 2
    adjusted_efficiency = base_efficiency - overhead_penalty
    return max(adjusted_efficiency, 0)

logs_data = [
    {'errors': 5, 'timeout_count': 3, 'retry_attempts': 2},
    {'errors': 2, 'timeout_count': 1, 'retry_attempts': 0},
    {'errors': 7, 'timeout_count': 4, 'retry_attempts': 5}
]

raw_efficiency = analyze_productivity(logs_data)

# Simulate feedback processing with distractors
deprecated_flag = False
temp_buffer = [x['retry_attempts'] for x in logs_data]
legacy_mode = sum(temp_buffer) > 5  # unused logical check

feedback_summary = []
for entry in logs_data:
    if entry['errors'] > 0:
        feedback_summary.append({
            'impact': entry['errors'] * 10,
            'recovery_cost': entry['timeout_count'] + entry['retry_attempts']
        })

# Irrelevant precomputation block (distractor)
baseline_metrics = {
    'total_timeouts': sum(x['timeout_count'] for x in logs_data),
    'avg_retry': sum(x['retry_attempts'] for x in logs_data) / len(logs_data)
}
shadow_calc = baseline_metrics['total_timeouts'] // 2  # dead computation

# Core aggregation logic
recovery_costs = [f['recovery_cost'] for f in feedback_summary]
impact_scores = {i: f['impact'] for i, f in enumerate(feedback_summary)}

def aggregate_performance(feedback):
    total_impact = sum(f['impact'] for f in feedback)
    total_recovery = sum(f['recovery_cost'] for f in feedback)
    redundancy_factor = len(feedback) ^ 1  # bitwise XOR as light obfuscation
    adjustment = total_recovery // redundancy_factor if redundancy_factor else 0
    performance_ratio = (raw_efficiency / 100) * (total_impact or 1)
    score = performance_ratio - adjustment
    return int(score)

final_score = aggregate_performance(feedback_summary)
print(f"Target result: {final_score}")