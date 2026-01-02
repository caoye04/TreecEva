def analyze_efficiency(data, threshold=0.75):
    efficiency_list = [x / (x + 1) for x in data if x > 0]
    filtered = [val for val in efficiency_list if val > threshold]
    return len(filtered) / len(efficiency_list) if efficiency_list else 0

# Irrelevant helper function (decoy)
def calculate_urgency(priority, time_left):
    urgency = priority * (1 / (time_left + 1))
    adjustment = 0.1 if urgency > 0.5 else -0.1
    return urgency + adjustment

# Unused but plausible function
def normalize_vector(vec):
    magnitude = sum(x ** 2 for x in vec) ** 0.5
    return [x / magnitude for x in vec] if magnitude else vec

# Simulate system health metrics (distraction context)
system_logs = {
    'cpu_load': [0.6, 0.7, 0.8, 0.9],
    'memory_usage': [0.5, 0.65, 0.78, 0.82],
    'disk_io': [0.3, 0.45, 0.6, 0.7],
    'network_latency': [120, 135, 150, 180]
}

# Misleading intermediate calculation
baseline_stress = sum([sum(log) / len(log) for log in system_logs.values()[:3]])

# Real metric preprocessing
raw_metrics = [0.88, 0.76, 0.91, 0.67, 0.83]
processed_metrics = {}
for i, val in enumerate(raw_metrics):
    if i % 2 == 0:
        processed_metrics[f'quality_{i}'] = round(val ** 2, 3)
    else:
        processed_metrics[f'latency_{i}'] = round(1 - val, 3)

# Add decoy entries to dictionary
decoy_keys = ['temp_cache', 'debug_flag', 'version', 'retry_count']
for key in decoy_keys:
    processed_metrics[key] = hash(key) % 100

# Weight assignment with red herring weights
weights = {
    'quality_0': 0.2,
    'latency_1': 0.1,
    'quality_2': 0.3,
    'latency_3': 0.15,
    'quality_4': 0.25,
    # Following are fake weights for non-existent metrics
    'fake_metric_x': 0.0,
    'placeholder_y': 0.0
}

# Spurious list comprehension (dead code path)
adjusted_weights = {k: v + 0.05 if 'latency' in k else v for k, v in weights.items() if v > 0}

# Core logic buried among distractions
def evaluate_performance(metrics, weight_map):
    score = 0.0
    count = 0
    for key, weight in weight_map.items():
        if weight > 0 and key in metrics:
            raw_val = metrics[key]
            # Non-linear boost for high performers
            adjusted_val = raw_val * (1.1 if raw_val >= 0.8 else 0.95)
            contribution = adjusted_val * weight
            score += contribution
            count += 1
    # Final adjustment based on consistency heuristic
    valid_vals = [metrics[k] for k in weight_map.keys() if k in metrics]
    if valid_vals:
        variance_penalty = (max(valid_vals) - min(valid_vals)) * 0.05
        score -= variance_penalty
    return round(score, 6)

# Unused but plausible conditional branch
if baseline_stress > 1.5:
    fallback_mode = True
    final_score = 0.5
else:
    # Actual execution path
    final_score = evaluate_performance(processed_metrics, weights)

# Print result as required
print(f"Result: {final_score}")