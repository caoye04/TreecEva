def analyze_productivity(logs):
    total_entries = len(logs)
    valid_count = 0
    temp_sum = 0
    for log in logs:
        if not log.get('active', True):
            continue
        duration = log.get('duration', 0)
        if duration <= 0:
            continue
        adjustment_factor = 1.0
        if 'overtime' in log and log['overtime']:
            adjustment_factor *= 1.2
        if 'breaks_taken' in log:
            breaks = log['breaks_taken']
            if isinstance(breaks, int) and breaks > 2:
                adjustment_factor *= 0.85
        processed_time = duration * adjustment_factor
        temp_sum += processed_time
        valid_count += 1

    if valid_count == 0:
        return 0.0

    average_effort = temp_sum / valid_count
    return round(average_effort, 4)


def compute_baseline_reference(data_stream):
    # Distractor function: computes something irrelevant
    cumulative_xor = 0
    for item in data_stream:
        if isinstance(item, dict) and 'id' in item:
            cumulative_xor ^= item['id'] % 256
    return cumulative_xor

# Simulated system monitoring logs
task_logs = [
    {'duration': 120, 'active': True, 'overtime': False, 'breaks_taken': 1},
    {'duration': 95, 'active': True, 'overtime': True, 'breaks_taken': 0},
    {'duration': 0, 'active': True, 'overtime': False, 'breaks_taken': 3},
    {'duration': 150, 'active': True, 'overtime': True, 'breaks_taken': 2},
    {'duration': 80, 'active': False, 'overtime': False, 'breaks_taken': 1},
    {'duration': 110, 'active': True, 'overtime': False, 'breaks_taken': 4}
]

# Irrelevant data stream for distraction
data_packets = [
    {'id': 101, 'payload': 'A'},
    {'id': 205, 'payload': 'B'},
    {'id': 312, 'payload': 'C'},
    {'id': 407, 'payload': 'D'}
]

# Compute meaningless baseline (distractor computation)
baseline_hash = compute_baseline_reference(data_packets)

# Real processing begins
raw_metrics = {}
raw_metrics['avg_duration'] = analyze_productivity(task_logs)

# Apply weighting schema using dictionary operations and lambda
weight_map = {
    'avg_duration': 0.6,
    'consistency': 0.3,
    'overtime_ratio': 0.1
}

# Simulate consistency score with string-based analysis (use of string method)
log_strings = [str(log) for log in task_logs]
consistency_flag = all('overtime' in s and 'breaks_taken' in s for s in log_strings)
consistency_score = 90.0 if consistency_flag else 60.0

# Compute overtime ratio from raw count
overtime_count = sum(1 for log in task_logs if log.get('overtime', False))
overtime_ratio = overtime_count / len(task_logs) if task_logs else 0

# Assemble full metrics
efficiency_metrics = {
    'avg_duration': raw_metrics['avg_duration'],
    'consistency': consistency_score,
    'overtime_ratio': overtime_ratio
}

# Weighted evaluation using lambda for dynamic scaling
scaler = lambda x, w: round(x * w / 100, 4)
scaled_components = {
    key: scaler(efficiency_metrics[key], weight_map.get(key, 1) * 100) 
    for key in efficiency_metrics if key in weight_map
}

# Final aggregation
final_score = 0
for component in scaled_components:
    final_score += scaled_components[component]

# Additional distractor variables
phantom_score = 0
for i in range(3):
    phantom_score += baseline_hash % (i + 1) if i > 0 else 0

# Dead code path (never executed but looks plausible)
if final_score > 100:
    final_score = 100
elif final_score < 0:
    final_score = 0

# Key execution point
final_score = evaluate_performance(efficiency_metrics, weight_map)

# Redefine evaluate_performance to complete execution
def evaluate_performance(metrics, weights):
    total = 0.0
    for k, v in weights.items():
        if k in metrics:
            contribution = metrics[k] * v
            if k == 'avg_duration':
                contribution /= 10  # Normalize duration impact
            total += contribution
    return round(total, 4)

# Print result for verification
print(f"Result: {final_score}")