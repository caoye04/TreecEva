import math

# Simulated sensor array diagnostics with noise filtering and anomaly detection
def collect_sensor_readings():
    raw_readings = [23.1, 19.5, 1000.2, 21.0, 18.7, -999.0, 22.3, 20.8, 19.9, 21.4]
    baseline_offset = 10.0
    adjusted = [x + baseline_offset for x in raw_readings if x > 0 and x < 1000]
    return adjusted

def apply_noise_filter(data):
    # Moving average filter (window size 2)
    filtered = []
    for i in range(len(data)):
        if i == 0:
            filtered.append(data[i])
        else:
            filtered.append((data[i-1] + data[i]) / 2.0)
    return filtered

def generate_frequency_signature(values):
    # Irrelevant function: simulates spectral analysis but not used in final result
    total_power = 0.0
    for v in values:
        total_power += v * math.sin(v)
    normalized = total_power / len(values) if values else 0
    return round(normalized, 3)

def compute_entropy(data):
    # Another red herring: computes Shannon-like entropy but unused
    from collections import Counter
    counts = Counter([round(x) for x in data])
    entropy = 0.0
    n = len(data)
    for count in counts.values():
        p = count / n
        entropy -= p * math.log2(p)
    return round(entropy, 4)

def identify_outlier_bounds(data):
    mean_val = sum(data) / len(data)
    variance = sum((x - mean_val) ** 2 for x in data) / len(data)
    std_dev = math.sqrt(variance)
    lower = mean_val - 1.5 * std_dev
    upper = mean_val + 1.5 * std_dev
    return lower, upper

def flag_anomalies(readings, bounds):
    lower, upper = bounds
    flags = []
    for r in readings:
        if r < lower or r > upper:
            flags.append((r, 'ANOMALY'))
        else:
            flags.append((r, 'NORMAL'))
    return flags

def build_diagnostic_profile(flags):
    # Distractor: builds a complex structure but only one field matters later
    profile = {
        'timestamp': '2024-05-20T12:00:00Z',
        'system_id': 'SENS-ARRAY-7',
        'status': 'ACTIVE',
        'anomaly_count': len([f for f in flags if f[1] == 'ANOMALY']),
        'normal_count': len([f for f in flags if f[1] == 'NORMAL']),
        'recommendation': 'CALIBRATE' if len([f for f in flags if f[1] == 'ANOMALY']) > 2 else 'OK'
    }
    return profile

def analyze_signal(data, criteria_set):
    # Core logic hidden among distractions
    primary_metric = 0
    for x in data:
        if x in criteria_set:
            primary_metric += int(x)
        else:
            primary_metric -= int(x // 2)
    secondary_score = len(data) ^ len(criteria_set)  # XOR operation as bitwise distraction
    final_score = primary_metric + secondary_score
    return final_score

# Main execution flow
if __name__ == '__main__':
    # Step 1: Collect raw sensor data
    raw_data = collect_sensor_readings()  # Adds baseline offset, filters invalid
    
    # Step 2: Apply smoothing filter
    processed_signal = apply_noise_filter(raw_data)
    
    # Step 3: Generate irrelevant analytics (distraction)
    frequency_sig = generate_frequency_signature(raw_data)
    entropy_value = compute_entropy(raw_data)
    
    # Step 4: Determine statistical bounds
    limits = identify_outlier_bounds(processed_signal)
    
    # Step 5: Flag anomalies based on bounds
    flagged_results = flag_anomalies(processed_signal, limits)
    
    # Step 6: Build full diagnostic (only part used later)
    diagnosis = build_diagnostic_profile(flagged_results)
    
    # Step 7: Create threshold set using set operations (required python feature)
    base_thresholds = {15, 25, 30, 35}
    dynamic_caps = {int(limits[0]), int(limits[1]), 20, 25}
    threshold_set = base_thresholds.union(dynamic_caps).intersection({20, 25, 30, 35, 40})  # Set ops: union & intersect
    
    # Step 8: Filter data to only those within dynamic caps range (relevant)
    min_cap, max_cap = min(dynamic_caps), max(dynamic_caps)
    filtered_data = [x for x in processed_signal if min_cap <= x <= max_cap]
    
    # Step 9: Analyze signal using threshold set (critical statement)
    final_diagnostic = analyze_signal(filtered_data, threshold_set)
    
    # Print result as required
    print(f"Target result: {final_diagnostic}")