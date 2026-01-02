from collections import defaultdict, Counter
import math

# Simulated health monitoring system with sensor data processing
def collect_sensor_readings():
    readings = [128, 135, 129, 142, 130, 137, 131, 126, 133, 134]
    timestamps = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    return list(zip(timestamps, readings))

def filter_outliers(data, limit=5):
    # Irrelevant filtering logic (not used in final path)
    avg = sum([x[1] for x in data]) / len(data)
    return [point for point in data if abs(point[1] - avg) < limit]

def compute_rolling_average(data, window=3):
    smoothed = []
    for i in range(len(data) - window + 1):
        window_avg = sum([data[i+j][1] for j in range(window)]) / window
        smoothed.append(round(window_avg, 2))
    return smoothed

def detect_anomalies(series, baseline=130, tolerance=3):
    anomalies = []
    for val in series:
        if abs(val - baseline) > tolerance:
            anomalies.append(val)
    return anomalies

def build_summary_stats(records):
    stats = defaultdict(int)
    values = [r[1] for r in records]
    stats['count'] = len(values)
    stats['max'] = max(values)
    stats['min'] = min(values)
    stats['range'] = stats['max'] - stats['min']
    stats['mode'] = Counter(values).most_common(1)[0][1]
    return stats

def calculate_entropy(data):
    # Distractor function: computes Shannon entropy but not used in final result
    from collections import Counter
    freqs = Counter(data)
    total = sum(freqs.values())
    entropy = 0.0
    for f in freqs.values():
        p = f / total
        entropy -= p * math.log2(p)
    return round(entropy, 4)

def normalize_series(raw_data):
    # Dead code path — never called
    base = raw_data[0][1]
    return [(t, round((v - base) / base, 4)) for t, v in raw_data]

def evaluate_trend_pattern(seq):
    # Another decoy analysis
    increasing = sum(1 for i in range(1, len(seq)) if seq[i] > seq[i-1])
    decreasing = sum(1 for i in range(1, len(seq)) if seq[i] < seq[i-1])
    return 'upward' if increasing > decreasing else 'downward'

def analyze_metrics(data_points, config_thresholds):
    # Core relevant logic starts here
    raw_values = [point[1] for point in data_points]
    
    # Step 1: Apply threshold filtering based on dynamic criteria
    valid_range = config_thresholds['range']
    filtered_vals = [v for v in raw_values if valid_range[0] <= v <= valid_range[1]]
    
    # Step 2: Compute transformed metrics
    transformed = [math.log(v) * 1.5 for v in filtered_vals]
    
    # Step 3: Calculate adjusted mean
    adj_mean = sum(transformed) / len(transformed)
    
    # Step 4: Apply correction factor from secondary metric
    anomaly_list = detect_anomalies(raw_values, baseline=132, tolerance=4)
    correction_factor = 0.95 if len(anomaly_list) > 2 else 1.05
    
    # Step 5: Adjust mean with factor
    adj_mean *= correction_factor
    
    # Step 6: Use list comprehension to flag high-risk values
    risk_flags = [1 if v > 134 else 0 for v in raw_values]
    risk_score = sum(risk_flags)
    
    # Step 7: Incorporate risk penalty if score exceeds threshold
    if risk_score >= 3:
        adj_mean *= 0.98
    
    # Step 8: Final diagnostic computed through multi-step transformation
    base_entropy = calculate_entropy([bin(int(x))[2:] for x in filtered_vals])  # Bit-pattern entropy (distractor input)
    final_diagnostic = int(round(adj_mean * 100 + risk_score * 2 - base_entropy * 10))
    
    return final_diagnostic

# --- Execution Block ---
sensor_log = collect_sensor_readings()
summary = build_summary_stats(sensor_log)
trends = evaluate_trend_pattern([x[1] for x in sensor_log])
smooth_data = compute_rolling_average(sensor_log)

# Unused intermediate computations (red herrings)
decoy_normalized = [(t, v*0.01) for t, v in sensor_log]
dummy_stat = sum(smooth_data) / len(smooth_data)

# Configuration map with meaningful and irrelevant keys
thresholds = {
    'range': (127, 140),
    'critical': 145,
    'warning_level': 138
}

health_data = sensor_log

# Key execution point
final_diagnostic = analyze_metrics(health_data, thresholds)

print(f"Result: {final_diagnostic}")