from collections import defaultdict, Counter

# Simulate sensor readings over time with some noise
def generate_sensor_data():
    raw_readings = [23.5, 24.1, 23.9, 25.0, 26.2, 25.8, 24.5, 23.7]
    timestamps = list(range(len(raw_readings)))
    return list(zip(timestamps, raw_readings))

def analyze_trend(data):
    increases = 0
    decreases = 0
    for i in range(1, len(data)):
        if data[i][1] > data[i-1][1]:
            increases += 1
        elif data[i][1] < data[i-1][1]:
            decreases += 1
    return increases - decreases

def filter_outliers(values, tolerance=1.0):
    mean_val = sum(values) / len(values)
    return [v for v in values if abs(v - mean_val) <= tolerance]

# Track multiple metrics across systems
def collect_diagnostics():
    system_metrics = {
        'cpu_load': [0.65, 0.70, 0.75, 0.80, 0.82],
        'memory_usage': [0.55, 0.60, 0.70, 0.72, 0.78],
        'disk_io': [120, 135, 140, 130, 150]
    }
    
    # Irrelevant aggregation (distractor)
    avg_disk_io = sum(system_metrics['disk_io']) / len(system_metrics['disk_io'])
    peak_memory = max(system_metrics['memory_usage'])
    
    # Relevant metric: growth trend in CPU load
    cpu_trend = sum(1 for i in range(1, len(system_metrics['cpu_load'])) if system_metrics['cpu_load'][i] > system_metrics['cpu_load'][i-1])
    
    # Misleading calculation (not used later)
    projected_load = system_metrics['cpu_load'][-1] * 1.1
    
    return cpu_trend

# Main evaluation logic
def evaluate_performance(metrics, base_threshold):
    # metrics contains various performance counters
    trend_strength = metrics.get('trend', 0)
    stability = metrics.get('stability_factor', 1.0)
    anomalies = metrics.get('anomalies_detected', [])

    # Secondary calculations with distractors
    temp_adjustment = 0.9 if len(anomalies) > 2 else 1.0
    debug_value = sum(1 for x in anomalies if x > base_threshold)  # unused

    # Core scoring logic
    raw_score = trend_strength * 100 * stability
    penalty = len(anomalies) * 5
    adjusted_score = raw_score - penalty
    
    # Distractor block: irrelevant set operation
    unique_anomalies = set(anomalies)
    duplicate_count = len(anomalies) - len(unique_anomalies)
    if duplicate_count > 0:
        adjusted_score -= 2  # minor effect, but not triggered

    # Final nonlinear adjustment
    final_score = int((adjusted_score ** 0.5) * 2) if adjusted_score > 0 else 0
    return final_score

# Execution flow
sensor_data = generate_sensor_data()
cleaned_values = filter_outliers([x[1] for x in sensor_data], tolerance=0.8)

trend_index = analyze_trend(sensor_data)
system_trend = collect_diagnostics()  # returns cpu trend

# Build metric package
metric_data = defaultdict(float)
metric_data['trend'] = trend_index + system_trend
metric_data['stability_factor'] = 0.95

# Simulate anomaly detection (some misleading entries)
detected_list = [1, 3, 3, 7, 9, 9, 9]  # duplicates are distractor
anomaly_counter = Counter(detected_list)
filtered_anomalies = [k for k, v in anomaly_counter.items() if v >= 2]  # only frequent ones

# Add to metrics
metric_data['anomalies_detected'] = filtered_anomalies

threshold = 5
final_score = evaluate_performance(metric_data, threshold)
print(f"Target result: {final_score}")