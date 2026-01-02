from collections import defaultdict

# Simulate system performance monitoring with multiple metrics
def monitor_system_load(base_load, duration):
    readings = []
    temp_buffer = []
    for i in range(duration):
        load = (base_load * (1.1 ** i)) % 95 + (i % 4)
        if load > 85:
            status = 'OVERHEAT'
        elif load > 70:
            status = 'HIGH'
        else:
            status = 'NORMAL'
        readings.append((load, status))
        temp_buffer.append(load * 0.1)  # Irrelevant accumulation
    
    # Misleading transformation
    processed = [round(r[0] * 0.95, 2) for r in readings if r[1] != 'OVERHEAT']
    avg_processed = sum(processed) / len(processed) if processed else 0
    return readings, avg_processed

# Analyze temporal patterns in metric drift
def analyze_drift(pattern_seq):
    drift_count = 0
    for i in range(1, len(pattern_seq)):
        if abs(pattern_seq[i] - pattern_seq[i-1]) > 5:
            drift_count += 1
    return drift_count > 3

# Core evaluation logic
def evaluate_performance(metrics, limits):
    score = 0
    penalty_adjustment = 0
    
    # Extract relevant time-series values
    raw_values = [m[0] for m in metrics]
    statuses = [m[1] for m in metrics]
    
    # Distractor: count state transitions (not used in final score)
    state_transitions = 0
    for i in range(1, len(statuses)):
        if statuses[i] != statuses[i-1]:
            state_transitions += 1
    
    # Actual scoring logic
    above_threshold = sum(1 for v in raw_values if v > limits['critical'])
    high_load_ratio = above_threshold / len(raw_values)
    
    if high_load_ratio > 0.3:
        score -= 15
    else:
        score += 10
    
    # Secondary condition based on trend stability
    stable_trend = not analyze_drift(raw_values)
    if stable_trend:
        score += 5
    
    # Red herring calculation
    outlier_buffer = []
    for v in raw_values:
        if v < limits['warning'] or v > limits['critical']:
            outlier_buffer.append(v * 1.1)
    buffer_sum = sum(outlier_buffer)  # Computed but unused
    
    # Final adjustment
    baseline_offset = raw_values[0] - raw_values[-1]
    if baseline_offset > 0:
        penalty_adjustment = -3
    else:
        penalty_adjustment = 2
    
    final_score = score + penalty_adjustment
    return final_score

# Setup and execution
duration_hours = 8
base_system_load = 62
threshold_config = {
    'warning': 70,
    'critical': 85
}

# Generate monitoring data
metric_readings, average_cleaned = monitor_system_load(base_system_load, duration_hours)

# Perform evaluation
final_score = evaluate_performance(metric_readings, threshold_config)

# Output result
print(f"Result: {final_score}")