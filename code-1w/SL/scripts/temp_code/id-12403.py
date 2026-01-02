def analyze_sensor_readings(readings):
    threshold = 0.75
    tolerance = 0.1
    adjusted_values = []
    outlier_count = 0
    temporal_weights = [0.8, 0.9, 1.0, 1.1, 1.2]
    weighted_sum = 0.0
    
    for i, val in enumerate(readings):
        if val > threshold + tolerance:
            adjusted_val = min(val * 1.05, 1.0)
            adjusted_values.append(adjusted_val)
            weighted_sum += adjusted_val * temporal_weights[i % len(temporal_weights)]
        elif val < threshold - tolerance:
            adjusted_val = max(val * 0.95, 0.0)
            adjusted_values.append(adjusted_val)
            outlier_count += 1
        else:
            adjusted_values.append(val)
    
    # Simulate auxiliary diagnostic check (not directly used)
    baseline_score = sum(1 for v in readings if v > 0.6) * 0.5
    penalty_factor = 0.2 * outlier_count
    
    # Sensor activation logic with set operations
    raw_indices = set(range(len(readings)))
    high_activity = set(i for i, v in enumerate(adjusted_values) if v > 0.8)
    stable_sensors = set(i for i, v in enumerate(adjusted_values) if 0.4 <= v <= 0.8)
    activated_sensors = high_activity.union(stable_sensors).intersection(raw_indices)
    
    # Secondary distraction: sorting and zipping unrelated metrics
    sorted_adjusted = sorted(adjusted_values, reverse=True)
    ranked_pairs = list(zip(sorted_adjusted, range(len(sorted_adjusted))))
    correction_offset = 0
    for rank, (value, orig_idx) in enumerate(ranked_pairs):
        if rank % 3 == 0:
            correction_offset += value * 0.05
    
    # Core computation chain
    signal_strength = sum(adjusted_values) / len(adjusted_values)
    fluctuation_index = sum(abs(adjusted_values[i] - adjusted_values[i-1]) for i in range(1, len(adjusted_values)))
    stability_ratio = (len(adjusted_values) - outlier_count) / len(adjusted_values)
    
    aggregate_score = int((signal_strength * 100) * stability_ratio - fluctuation_index * 10)
    
    # Critical execution point
    final_diagnostic = aggregate_score + len(activated_sensors)
    
    # Red herring: unused transformation
    normalized = [round((x - min(adjusted_values)) / (max(adjusted_values) - min(adjusted_values) + 1e-8), 3) for x in adjusted_values]
    entropy_proxy = 0
    for p in normalized:
        if p > 0:
            entropy_proxy -= p * __import__('math').log(p)
    
    return final_diagnostic

# Input data
sensor_input = [0.65, 0.82, 0.54, 0.91, 0.73]
result = analyze_sensor_readings(sensor_input)
print(f"Target result: {result}")