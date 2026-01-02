def analyze_readings(readings):
    cumulative_score = 0
    for val in readings:
        if val < 0:
            cumulative_score += abs(val) * 0.5
        elif val > 100:
            cumulative_score += (val - 100) * 1.2
    return cumulative_score

# Irrelevant helper (distractor)
def normalize_data(data):
    max_val = max(data) if data else 1
    return [x / max_val for x in data]

# Unused function (dead code path)
def legacy_calculate(x):
    return sum(i**2 for i in x if i % 2 == 0)

# Simulate sensor status codes (mostly irrelevant)
sensor_status = {
    'sensor_a': 'OK',
    'sensor_b': 'ERROR',
    'sensor_c': 'OK',
    'sensor_d': 'UNKNOWN'
}

status_weights = {
    'OK': 1,
    'ERROR': -3,
    'UNKNOWN': 0
}

# Calculate a misleading diagnostic index (red herring)
misleading_index = sum(status_weights[status] for status in sensor_status.values() if status in status_weights)

# Real data pipeline
raw_metrics = [85, 92, 67, 103, 44, 115, 76, 88]

# Apply non-linear transformation (partially relevant)
adjusted_metrics = [x + (x * 0.1) if x > 90 else x - (x * 0.05) for x in raw_metrics]

# Historical baselines (distractor)
historical_averages = {
    'Q1': 76.2,
    'Q2': 78.5,
    'Q3': 80.1,
    'Q4': 79.3
}

# Deviation analysis (partially distracting)
deviations = {k: abs(v - 77) for k, v in historical_averages.items()}
total_deviation = sum(deviations.values())

# Core logic hidden among noise
thresholds = {
    'critical': 100,
    'warning': 90,
    'normal': 70
}

health_data = {
    'readings': adjusted_metrics,
    'baseline': 77,
    'tolerance': 5
}

# Conditional expression with side effects (key construct)
def process_metrics(data_dict, limits):
    readings = data_dict['readings']
    baseline = data_dict['baseline']
    
    # Count how many exceed warning level (relevant)
    warning_count = sum(1 for r in readings if r > limits['warning'])
    
    # Count critical spikes (very relevant)
    critical_count = sum(1 for r in readings if r > limits['critical'])
    
    # Compute average deviation from baseline (somewhat relevant)
    avg_dev = sum(abs(r - baseline) for r in readings) / len(readings)
    
    # Secondary adjustment based on trend (distractor)
    trend_score = 0
    for i in range(1, len(readings)):
        if readings[i] > readings[i-1]:
            trend_score += 0.1
        else:
            trend_score -= 0.05
    
    # Final computation chain (key steps)
    stability_factor = 100 - (avg_dev * 1.5)
    risk_penalty = (warning_count * 3) + (critical_count * 8)
    trend_influence = abs(trend_score) * 10  # Misleading positive boost
    
    # Actual answer derived here through complex interaction
    preliminary = stability_factor - risk_penalty
    final = preliminary + (trend_influence if preliminary > 70 else -5)  # Conditional expression
    
    # Additional interference
    calibration_offset = sum(1 for s in sensor_status.keys() if 'sensor_' in s) * 0.2
    return int(final - calibration_offset)  # Key assignment happens here

# Trigger execution
intermediate = analyze_readings(raw_metrics)

# Dead code invocation (no effect)
if False:
    normalized = normalize_data(raw_metrics)

# Critical statement
final_diagnostic = process_metrics(health_data, thresholds)

print(f"Result: {final_diagnostic}")