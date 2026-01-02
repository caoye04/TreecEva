from collections import defaultdict

# Simulate system performance metrics over time
task_durations = [12, 15, 10, 18, 22, 8, 14]
error_counts = [2, 0, 1, 3, 0, 1, 2]
resource_usage = [78, 85, 65, 90, 95, 60, 80]

# Irrelevant preprocessing: normalize durations (not used in final logic)
norm_durations = [round(d / sum(task_durations), 3) for d in task_durations]

# Track phase-wise status using defaultdict
phase_status = defaultdict(lambda: 'inactive')
for i in range(len(task_durations)):
    if task_durations[i] > 12:
        phase_status[i] = 'extended'
    elif task_durations[i] < 10:
        phase_status[i] = 'rushed'
    else:
        phase_status[i] = 'standard'

# Misleading aggregation: compute weighted_error (semi-relevant but not decisive)
weighted_error = 0
for i, err in enumerate(error_counts):
    if resource_usage[i] > 80:
        weighted_error += err * 1.5
    else:
        weighted_error += err

# Bitwise interference: analyze resource pattern via XOR masking (distractor)
mask = 0
for usage in resource_usage:
    mask ^= int(usage / 10)  # Random XOR chain with no impact

# Core metric: count tasks meeting quality criteria
effective_tasks = 0
task_metrics = []
base_threshold = 1.25

for i in range(len(task_durations)):
    # Composite score combining duration efficiency and error rate
    time_efficiency = 20 / task_durations[i]  # hypothetical ideal is 20 units
    error_penalty = error_counts[i] * 2
    raw_score = time_efficiency - error_penalty
    
    # Boost score if resource usage was optimal (60-80 range)
    if 60 <= resource_usage[i] <= 80:
        raw_score *= 1.1
    
    task_metrics.append(raw_score)

# Additional red herring: sort and reverse (no effect on final computation)
sorted_metrics = sorted(task_metrics, reverse=True)
avg_metric = sum(sorted_metrics) / len(sorted_metrics)

# Evaluate performance based on threshold crossing
def evaluate_performance(metrics, threshold):
    count_above = 0
    for m in metrics:
        if m > threshold:
            count_above += 1
    return count_above * 10  # Scale by 10 for final score

# Execute key statement
final_score = evaluate_performance(task_metrics, base_threshold)

# Print result as required
print(f"Target result: {final_score}")