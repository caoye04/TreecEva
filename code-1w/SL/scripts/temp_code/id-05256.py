from itertools import compress, cycle

# Simulate sensor data validation and performance scoring in an autonomous drone system
def collect_diagnostics():
    # Real-time sensor array readings (simulated)
    sensors = [78, 85, None, 92, 67, 88, None, 76]
    timestamps = [1, 2, 3, 4, 5, 6, 7, 8]
    statuses = ['active', 'active', 'failed', 'active', 'warning', 'active', 'failed', 'active']
    
    # Filter out failed sensors using itertools.compress
    valid_readings = list(compress(sensors, [s == 'active' for s in statuses]))
    valid_timestamps = list(compress(timestamps, [s == 'active' for s in statuses]))
    
    # Fill missing sensor values with interpolated average (not used in final logic)
    filled_sensors = []
    for val in sensors:
        if val is None:
            filled_sensors.append(int(sum(v for v in sensors if v is not None) / len([v for v in sensors if v is not None])))
        else:
            filled_sensors.append(val)
    
    # Diagnostic checksum (distractor)
    checksum = sum(filled_sensors[i] * (i + 1) for i in range(len(filled_sensors))) % 1000
    
    return valid_readings, valid_timestamps, checksum

# System calibration baseline (irrelevant to final score but looks important)
calibration_sequence = lambda x: [i ** 2 % 73 for i in range(x) if i % 3 != 0]
baseline = calibration_sequence(50)
baseline_avg = sum(baseline) / len(baseline)

# Main evaluation function
def evaluate_performance(metrics, weights):
    weighted_sum = 0.0
    total_weight = sum(weights)
    for i, metric in enumerate(metrics):
        if i < len(weights):
            weighted_sum += metric * weights[i]
    return int(weighted_sum / total_weight)

# Data preprocessing pipeline
def preprocess_metrics(raw_data):
    raw_readings, _, _ = raw_data
    
    # Compute derived metrics
    avg_reading = sum(raw_readings) / len(raw_readings)
    peak = max(raw_readings)
    stability_ratio = (sum(1 for i in range(1, len(raw_readings)) if abs(raw_readings[i] - raw_readings[i-1]) < 10) / (len(raw_readings) - 1)) if len(raw_readings) > 1 else 1.0
    
    # Normalize metrics to 0-100 scale
    norm_avg = min(100, max(0, avg_reading))  # Clamp to range
    norm_peak = min(100, max(0, peak / 1.5))  # Artificial scaling
    norm_stability = int(stability_ratio * 100)
    
    # Hidden adjustment: only norm_avg and norm_stability actually matter
    adjusted_peak = (norm_peak + 40) // 2  # Distractor transformation
    
    return [norm_avg, norm_stability, adjusted_peak]  # Order matters

# Weight configuration for scoring (only first two used effectively)
benchmark_weights = [0.4, 0.6, 0.0]  # Third weight is zero — makes third metric irrelevant

# Additional red herring: historical trend analysis (unused)
historical_data = [collect_diagnostics() for _ in range(3)]
trend_variability = sum(abs(historical_data[i][0][0] - historical_data[i+1][0][0]) for i in range(2)) if len(historical_data) > 1 else 0

# Execution pipeline
raw_diagnostics = collect_diagnostics()
processed_metrics = preprocess_metrics(raw_diagnostics)
final_score = evaluate_performance(processed_metrics, benchmark_weights)

# Irrelevant state tracker (adds cognitive load)
status_log = []
for reading in raw_diagnostics[0]:
    status_log.append(f"Reading:{reading}")

# Output result
print(f"Result: {final_score}")