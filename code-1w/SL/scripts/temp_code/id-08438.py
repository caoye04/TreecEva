from collections import defaultdict
import math

def analyze_efficiency(metrics):
    efficiency = 0
    adjustments = [0.1, -0.2, 0.15, -0.05]
    temp_buffer = []
    for i, val in enumerate(metrics):
        adjusted_val = val + adjustments[i % len(adjustments)]
        if adjusted_val > 0:
            efficiency += math.log(adjusted_val) * (i + 1)
        temp_buffer.append(efficiency)  # unused buffer (distractor)
    return efficiency

def calculate_stress_level(workload, breaks):
    stress_index = workload / (breaks + 1)
    penalty = 0
    if stress_index > 5:
        penalty = (stress_index - 5) * 2
    return stress_index - penalty

def evaluate_performance(output_log, risk_threshold):
    stats = defaultdict(int)
    total_entries = len(output_log)
    
    for entry in output_log:
        category = entry['type']
        stats[category] += entry['value']
    
    raw_productivity = sum(stats.values())
    error_count = stats['glitch'] + stats['fail']
    
    # Distractor computation: historical average (not used)
    historical_data = [0.87, 0.91, 0.85, 0.89, 0.90]
    avg_historical = sum(historical_data) / len(historical_data)
    deviation_sum = sum((x - avg_historical) ** 2 for x in historical_data)
    
    normalized_productivity = raw_productivity / (total_entries or 1)
    safety_margin = (risk_threshold - error_count) / risk_threshold if risk_threshold else 0
    
    if safety_margin < 0:
        normalized_productivity *= 0.5  # penalty
    
    final_score = int(normalized_productivity * 100) + int(safety_margin * 10)
    
    # Irrelevant string processing (distractor)
    status_msg = f"Performance: {final_score}%"
    flagged_chars = [c for c in status_msg if c.isdigit()]
    digit_sum = sum(int(d) for d in flagged_chars)
    
    return final_score

# Main execution
work_metrics = [8.2, 7.9, 8.5, 9.1, 7.8]
baseline_efficiency = analyze_efficiency(work_metrics)
stress_level = calculate_stress_level(40, 3)

log_entries = [
    {'type': 'success', 'value': 120},
    {'type': 'warning', 'value': 15},
    {'type': 'glitch', 'value': 8},
    {'type': 'fail', 'value': 5},
    {'type': 'success', 'value': 200}
]
risk_cap = 20

productivity = baseline_efficiency + stress_level
risk_factor = risk_cap - 5

final_score = evaluate_performance(log_entries, risk_factor)
print(f"Result: {final_score}")