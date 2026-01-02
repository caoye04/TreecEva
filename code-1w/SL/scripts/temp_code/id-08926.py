from collections import defaultdict
from itertools import cycle

# Simulated system metrics over time
timestamps = [100, 101, 102, 103, 104, 105]
raw_metrics = [85, 90, 78, 92, 88, 76]

# Irrelevant backup data (distractor)
backup_logs = ['log_001', 'log_002', 'log_003']
log_status = {log: 'archived' for log in backup_logs}

# Real processing begins
metric_data = defaultdict(int)
for t, val in zip(timestamps, raw_metrics):
    metric_data[t] = val * 1.1  # Apply scaling factor

# Decoy transformation (unused path)
scaled_copy = [x * 1.05 for x in raw_metrics if x > 80]

# Simulate noise injection (partially relevant)
noise_pattern = cycle([0.1, -0.2, 0.05])
noisy_values = []
for i, val in enumerate(metric_data.values()):
    adjusted = val + next(noise_pattern)
    if adjusted < 80:
        continue  # Filter out low performers
    noisy_values.append(round(adjusted, 2))

# Secondary distractor: string-based analysis (irrelevant)
status_flags = ['OK', 'WARN', 'CRIT']
flag_count = defaultdict(int)
for char in 'OK WARN OK OK CRIT WARN':
    if char.isalpha():
        flag_count[char] += 1  # Misleading accumulation

# Threshold logic with red herring condition
base_threshold = 82.5
activation_log = []
trigger_count = 0
for val in noisy_values:
    if val > base_threshold:
        activation_log.append(True)
        trigger_count += 1
        if trigger_count == 2:
            break  # Early exit red herring
    else:
        activation_log.append(False)

# Core evaluation function with hidden logic
def evaluate_performance(data, threshold):
    values = sorted(data.values())
    mid_point = len(values) // 2
    median_val = (values[mid_point] + values[~mid_point]) / 2
    
    # Hidden adjustment: only values above threshold contribute
    valid_contributions = [v for v in data.values() if v > threshold]
    if not valid_contributions:
        return 0
    
    # Complex scoring: weighted by position and magnitude
    score_components = []
    for i, v in enumerate(valid_contributions):
        weight = 1 + (i * 0.1)  # Increasing weight
        contribution = v * weight
        score_components.append(contribution)
    
    # Final aggregation
    raw_score = sum(score_components)
    penalty = len([v for v in data.values() if v < 80]) * 5
    final_score = raw_score - penalty  # Key assignment point
    
    # Dead code branch (never reached due to return)
    if final_score < 0:
        final_score = 100
    return int(final_score)

# Execute main logic
temp_buffer = [x for x in range(50, 55)]  # Unused buffer
config_mode = 'performance'
baseline_ref = sum(raw_metrics) / len(raw_metrics)

# Critical statement
final_score = evaluate_performance(metric_data, base_threshold)

# Output result
print(f"Result: {final_score}")