import math

# Simulated sensor fusion system for environmental monitoring
def collect_sensor_data():
    raw_values = [23.4, 18.9, 25.1, 20.3, 22.7, 19.8, 24.0, 21.2]
    timestamps = list(range(1000, 1008))
    statuses = ['OK', 'OK', 'ERROR', 'OK', 'WARNING', 'OK', 'OK', 'WARNING']
    
    # Irrelevant pre-processing (distractor)
    normalized = [round((v - min(raw_values)) / (max(raw_values) - min(raw_values)), 3) for v in raw_values]
    weighted_sum = sum(v * 0.9 for v in raw_values)
    
    return list(zip(timestamps, raw_values, statuses))

# Redundant transformation function (dead path)
def legacy_transform(data_seq):
    if not data_seq:
        return []
    transformed = []
    for t, v, s in data_seq:
        adj_val = v * 1.02 if s == 'OK' else v * 0.95
n        transformed.append((t + 100, round(adj_val, 2), s))
    return transformed  # Never actually used

# Core processing with meaningful logic
def filter_anomalies(sensor_stream):
    valid_entries = []
    error_count = 0
    warning_flags = []
    
    # Distractor: irrelevant counters
    temp_aggregate = 0
    correction_factor = 1.0
    
    for ts, val, stat in sensor_stream:
        if stat == 'ERROR':
            error_count += 1
            continue
        if val < 19.0 or val > 25.0:
            warning_flags.append(ts)
            if len(warning_flags) > 2:
                correction_factor = 0.98  # Unused distraction
        else:
            valid_entries.append(val)
        temp_aggregate += val ** 0.5  # Meaningless accumulation
    
    # Real logic: only entries within range are kept
    return valid_entries

# Secondary processing with decoy operations
def smooth_signal(readings):
    if len(readings) < 3:
        return readings[:]
    
    smoothed = [readings[0]]
    
    # Heavily distracting loop with no real impact
    debug_stats = {
        'peak': max(readings),
        'trough': min(readings),
        'delta': max(readings) - min(readings),
        'entropy': sum(math.log(x) for x in readings if x > 0) / len(readings)
    }
    
    for i in range(1, len(readings) - 1):
        neighbor_avg = (readings[i-1] + readings[i+1]) / 2
        new_val = 0.6 * readings[i] + 0.4 * neighbor_avg
        smoothed.append(round(new_val, 2))
    
    smoothed.append(readings[-1])
    
    # Fake optimization path
    optimized = list(map(lambda x: x * 1.01, smoothed))  # Not returned
    return smoothed

# Misleading analysis chain
def compute_stability_index(seq):
    if len(seq) == 0:
        return 0.0
    
    diffs = [abs(seq[i+1] - seq[i]) for i in range(len(seq)-1)]
    avg_change = sum(diffs) / len(diffs) if diffs else 0
    
    # Complex but irrelevant formula
    volatility = sum(d**2 for d in diffs) / (len(diffs) or 1)
    inertia = sum(1 for d in diffs if d < 0.5)
    
    # This looks important but isn't used later
    phantom_score = (inertia * 100) / len(diffs) if diffs else 0
    
    return round(avg_change * 100, 4)

# Actual critical computation
def calculate_entropy(values):
    if not values:
        return 0.0
    mean_val = sum(values) / len(values)
    variance = sum((x - mean_val) ** 2 for x in values) / len(values)
    return round(math.sqrt(variance), 6)

# Final decision logic buried in distractions
def analyze_readings(logs):
    # Distractor variables
    summary_report = {}
    audit_trail = []
    anomaly_window = None
    recalibration_needed = False
    
    # More red herrings
    thresholds = {
        'high_risk': 26.0,
        'moderate': 24.0,
        'baseline': 20.0
    }
    
    # Conditional expression with actual relevance
    risk_flag = 'critical' if len(logs) == 0 else ('elevated' if len(logs) < 5 else 'normal')
    
    # Real calculation path
    signal_strength = sum(math.sin(x / 10) for x in logs) if logs else 0
    diversity_metric = calculate_entropy(logs)
    
    # Key logic hidden among distractions
    adjustment = 1.5 if risk_flag == 'normal' else 0.8
    diagnostic_value = (diversity_metric * 1000) + (signal_strength * 10) + adjustment
    
    # Dead branch
    if len(logs) > 100:
        post_analysis = compute_stability_index(logs)
        return int(post_analysis)
    
    final_diagnostic = int(round(diagnostic_value))
    
    # Decoy output (never reached)
    debug_payload = {'raw': logs, 'score': final_diagnostic * 0.97}
    
    return final_diagnostic

# Orchestration with misleading call sequence
sensor_data = collect_sensor_data()
suppressed_errors = 0
for _, _, status in sensor_data:
    if status == 'ERROR':
        suppressed_errors += 1

# Call to unused function (distractor)
legacy_data = legacy_transform(sensor_data)

filtered_readings = filter_anomalies(sensor_data)
processed_logs = smooth_signal(filtered_readings)

# Phantom intermediate step
stability = compute_stability_index(processed_logs)
stability_diagnostic = int(stability * 10) if stability > 1.0 else 0

# Critical execution point
final_diagnostic = analyze_readings(processed_logs)

# Output requirement
print(f"Target result: {final_diagnostic}")