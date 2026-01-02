from itertools import combinations

# Simulated system metrics from a distributed task scheduler
task_durations = [120, 95, 134, 88, 105, 118, 97]
completion_codes = [1, 1, 0, 1, 1, 0, 1]
resource_usage = [0.67, 0.82, 0.71, 0.93, 0.64, 0.88, 0.77]
startup_times = [12, 14, 11, 15, 13, 16, 10]
heartbeat_intervals = [5, 5, 5, 5, 5, 5, 5]

# Irrelevant transformations (distractors)
decoy_transform = [round((x ** 0.5) * 1.8) for x in startup_times if x > 12]
shadow_sum = sum([a * b for a, b in zip(task_durations, completion_codes)]) // 2
temporal_pattern = list(combinations([x % 10 for x in task_durations], 3))

# Real metric calculations
efficiency_ratio = sum(d for i, d in enumerate(task_durations) if completion_codes[i] == 1) / sum(task_durations)
success_rate = sum(completion_codes) / len(completion_codes)
avg_resource = sum(r for i, r in enumerate(resource_usage) if completion_codes[i] == 1) / sum(1 for c in completion_codes if c == 1)

# Weighted metric fusion with decoy branches
weights = {
    'efficiency': 0.4,
    'success': 0.35,
    'resource': 0.25,
    'ghost_metric': 0.0  # unused weight (red herring)
}

# Fake control flow (dead path)
if len(heartbeat_intervals) > 10:
    correction_factor = 1.2
else:
    adjustment_offset = 0  # never used elsewhere

# Core logic hidden among distractions
def analyze_stability(data):
    diffs = [abs(data[i] - data[i-1]) for i in range(1, len(data))]
    return sum(diffs) / len(diffs)

def filter_outliers(series, threshold=1.5):
    median_val = sorted(series)[len(series)//2]
    return [x for x in series if abs(x - median_val) < threshold]

# Unused recursive function (decoy)
def cumulative_delay(seq, index=0):
    if index >= len(seq):
        return 0
    return seq[index] + 0.9 * cumulative_delay(seq, index + 1)

# Main evaluation function
def evaluate_performance(metrics, w):
    base_metrics = {
        'efficiency': efficiency_ratio,
        'success': success_rate,
        'resource': 1 - avg_resource,  # invert for optimization
    }
    
    # Hidden adjustment: penalize instability in successful tasks
    successful_durations = [task_durations[i] for i in range(len(completion_codes)) if completion_codes[i] == 1]
    stability_penalty = analyze_stability(successful_durations) / 100.0
    
    # Compute composite score
    raw_score = 0
    for key in ['efficiency', 'success', 'resource']:
        raw_score += base_metrics[key] * w[key]
    
    # Apply penalty
    adjusted_score = raw_score - stability_penalty
    
    # Final transformation via distractor method (looks complex but deterministic)
    candidate_pairs = list(combinations(successful_durations, 2))
    if candidate_pairs:
        pair_bias = sum(abs(a - b) for a, b in candidate_pairs[:5]) / 1000.0  # small influence
        adjusted_score -= pair_bias
    
    # Normalize to integer scale (target result)
    final_normalized = int(round(adjusted_score * 1000))
    
    # Dead assignment below (misleading)
    final_normalized = final_normalized + 5 if final_normalized < 500 else final_normalized
    
    return final_normalized

# Trigger execution
dropped_tasks = [i for i, c in enumerate(completion_codes) if c == 0]
baseline_projection = sum(task_durations) / len(task_durations) * len(completion_codes)

# Key statement
final_score = evaluate_performance(metrics=None, weights=weights)

# Output result
print(f"Result: {final_score}")