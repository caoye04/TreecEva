from collections import defaultdict
import math

# Simulated sensor data feed (temperature, pressure, vibration)
sensor_feed = [
    (23.4, 98.2, 0.012), (24.1, 99.1, 0.015), (22.8, 97.3, 0.011),
    (45.6, 102.4, 0.032), (23.9, 98.7, 0.013), (24.5, 100.1, 0.016),
    (22.1, 96.8, 0.009), (67.3, 115.6, 0.089), (23.7, 99.4, 0.014),
    (24.0, 98.9, 0.012), (25.2, 101.3, 0.018), (22.5, 97.1, 0.010)
]

# Irrelevant function: analyzes network latency (not used in final result)
def analyze_network_performance(data):
    latency_log = [0.12, 0.15, 0.11, 0.22, 0.13, 0.14, 0.10, 0.32]
    avg_latency = sum(latency_log) / len(latency_log)
    jitter = max(latency_log) - min(latency_log)
    return {'avg': avg_latency, 'jitter': jitter, 'issues': jitter > 0.2}

# Decoy diagnostic flag (never updated)
critical_failure_mode = False
emergency_shutdown_initiated = False

# Data transformation: extract intervals where temperature > threshold
def extract_anomalies(feed, temp_thresh=30.0):
    anomalies = []
    for i, (temp, press, vib) in enumerate(feed):
        if temp > temp_thresh:
            # Complex calculation with bit manipulation (some irrelevant)
            severity_code = int((temp / 5.0) ** 2) | int(vib * 1000)
            pressure_deviation = abs(press - 100.0)
            normalized_risk = (severity_code * pressure_deviation) / (vib + 0.01)
            anomalies.append((i, temp, severity_code, normalized_risk))
    return anomalies

# Secondary processing: computes rolling averages (partially relevant)
def compute_rolling_average(data, window=3):
    rolling = []
    for i in range(len(data) - window + 1):
        window_avg = sum([d[0] for d in data[i:i+window]]) / window
        rolling.append(round(window_avg, 3))
    return rolling

# Core logic for log processing
log_data = defaultdict(list)
for idx, (t, p, v) in enumerate(sensor_feed):
    log_data['temps'].append(t)
    log_data['pressures'].append(p)
    log_data['vibrations'].append(v)
    log_data['indices'].append(idx)

# Misleading intermediate summary (not used later)
summary_stats = {
    'max_temp': max(log_data['temps']),
    'min_pressure': min(log_data['pressures']),
    'total_readings': len(log_data['indices'])
}

# Auxiliary function: determines if vibration correlates with heat
def has_thermal_vibration_correlation(data):
    high_temp = [t for t in data['temps'] if t > 30.0]
    corresponding_vib = [log_data['vibrations'][i] for i, t in enumerate(data['temps']) if t > 30.0]
    if not high_temp:
        return 0.0
    correlation = sum([t*v for t,v in zip(high_temp, corresponding_vib)]) / len(high_temp)
    return round(correlation, 4)

# Unused recursive helper (red herring)
def calculate_residual_depth(n, acc=0):
    if n <= 1:
        return acc
    return calculate_residual_depth(n // 2, acc + (n % 2))

# Main metric processor
system_threshold = 30.0
def process_metrics(logs, threshold):
    # Step 1: Identify anomalous entries
    anomaly_list = extract_anomalies(list(zip(logs['temps'], logs['pressures'], logs['vibrations'])), threshold)
    
    # Step 2: Compute risk accumulation using list comprehension and filtering
    significant_risks = [
        item for item in anomaly_list 
        if item[3] > 500 or (item[1] > 50.0 and item[2] > 200)
    ]
    
    # Step 3: Aggregate total risk score
    base_score = sum([int(risk[1]) for risk in significant_risks])
    
    # Step 4: Apply conditional adjustment based on pressure deviation pattern
    high_pressure_risks = [p for p in logs['pressures'] if p > 110.0]
    adjustment_factor = 2 if high_pressure_risks else 1
    
    # Step 5: Use conditional expression for stability check
    stability_flag = 'stable' if len(anomaly_list) < 5 else 'unstable'
    volatility_penalty = 15 if stability_flag == 'unstable' else 0
    
    # Step 6: Calculate derived index using mathematical operations
    raw_index = base_score * adjustment_factor - volatility_penalty
    
    # Step 7: Apply logarithmic normalization (only if non-zero)
    normalized_index = math.log(raw_index) if raw_index > 0 else 0
    
    # Step 8: Final diagnostic via bitwise combination with static offset
    diagnostic_code = int(normalized_index) ^ 1234
    
    # Step 9: Conditional override based on vibration correlation (this will NOT trigger)
    correlation_value = has_thermal_vibration_correlation(logs)
    final_value = diagnostic_code + 100 if correlation_value > 2.0 else diagnostic_code
    
    return final_value

# Execution point of interest
final_diagnostic = process_metrics(log_data, system_threshold)

# Print result as required
print(f"Result: {final_diagnostic}")