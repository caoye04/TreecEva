def analyze_metrics(raw_data):
    # Preprocess data using lambda for transformation
    processed = list(map(lambda x: (x[0], x[1] ** 2 + 3 * x[2]), raw_data))
    
    # Extract baseline values (distractor computation)
    baseline_total = sum([v[1] for v in processed]) / len(processed) if processed else 0
    
    # Filter relevant high-impact entries
    filtered = [p for p in processed if p[1] > 50]
    
    # Compute secondary metrics (partially relevant)
    magnitude_sum = sum([v[1] for v in filtered])
    count_bonus = len(filtered) * 2
    
    # Simulate conditional adjustment based on distribution
    adjustment = 0
    if len(filtered) > 3:
        adjustment = 10
    elif len(filtered) == 2:
        adjustment = 5
    
    # Distractor: irrelevant sorting and set operations
    sorted_names = sorted(set([f'item_{v[0]}' for v in filtered]))
    temp_shadow = [name[::-1] for name in sorted_names]  # Unused
    
    # Real contribution: derive core metric
    core_metric = magnitude_sum + count_bonus + adjustment
    
    # Return as tuple for unpacking simulation
    return (core_metric, baseline_total, len(raw_data))


def evaluate_performance(metrics):
    # Use set difference to filter out noise categories
    valid_keys = {'A', 'B', 'C', 'D'}
    noise_keys = {'X', 'Y'}
    clean_metrics = metrics - noise_keys
    
    # Weighted scoring with fixed coefficients
    score_map = {'A': 7, 'B': 5, 'C': 3, 'D': 2}
    base_score = sum(score_map[k] for k in clean_metrics if k in score_map)
    
    # Apply non-linear bonus using lambda
    bonus_fn = lambda s: int(s ** 0.5) if s > 10 else s // 2
    bonus = bonus_fn(base_score)
    
    # Dead code path (misleading)
    if False:
        bonus -= 100  # Never executed
    
    return base_score + bonus

# Main execution
raw_input = [(1, 4, 3), (2, 5, 4), (3, 6, 5), (4, 3, 4), (5, 7, 6)]
primary_result, _, _ = analyze_metrics(raw_input)

# Construct metric set based on result properties (key logic step)
threshold_met = primary_result > 150
metric_set = set()
if threshold_met:
    metric_set.update(['A', 'B', 'C'])
else:
    metric_set.update(['B', 'D', 'X'])  # Includes noise key

# Add distractor elements
metric_set.add('Y')
metric_set.discard('Z')  # No effect

# Critical statement
final_score = evaluate_performance(metric_set)
print(f"Result: {final_score}")