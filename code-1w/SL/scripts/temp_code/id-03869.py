import math

# Simulated system telemetry data with mixed signal types
def generate_telemetry():
    timestamps = list(range(100, 200, 2))
    raw_signals = [round(math.sin(t / 10) * 50 + 40 + (t % 7), 2) for t in timestamps]
    return list(zip(timestamps, raw_signals))

# Legacy function - unused but looks relevant
def deprecated_analysis(data):
    cumulative = 0
    for item in data:
        if item[1] > 50:
            cumulative += item[0] * 0.3
    return cumulative

# Signal smoothing using moving window (not used in final path)
def smooth_signal(signal_pairs, window=3):
    smoothed = []
    values = [p[1] for p in signal_pairs]
    for i in range(len(values)):
        start = max(0, i - window // 2)
        end = min(len(values), i + window // 2 + 1)
        avg = sum(values[start:end]) / (end - start)
        smoothed.append(round(avg, 2))
    return smoothed

# Diagnostic engine core
system_thresholds = {
    'critical': 85.0,
    'elevated': 65.0,
    'normal': 40.0
}

# False alarm generator - red herring function
def trigger_false_alarms(data_list):
    alarms = []
    temp_cache = {}
    for idx, val in enumerate([d[1] for d in data_list]):
        if val > 70 and idx % 5 == 0:
            alarms.append(f"ALERT_{idx}")
        temp_cache[idx] = val * 1.05  # misleading intermediate scaling
    return alarms

# Real-time filter that masks transient spikes
def filter_transients(signal_seq, tolerance=1.5):
    filtered = []
    for pair in signal_seq:
        timestamp, value = pair
        if not filtered or abs(value - filtered[-1][1]) <= tolerance:
            filtered.append(pair)
    return filtered

# Core metric processor
log_data = generate_telemetry()

# Irrelevant transformation chain
transform_chain = [
    [x[1] * 1.02 for x in log_data],
    [round(y * 0.99 + 1.1, 2) for y in [x[1] for x in log_data]],
    sorted([z[1] for z in log_data], reverse=True)[:50]
]

# Unused statistical summary
mean_value = round(sum([x[1] for x in log_data]) / len(log_data), 2)
median_value = sorted([x[1] for x in log_data])[len(log_data)//2]
variance_proxy = sum([(x[1] - mean_value)**2 for x in log_data]) / len(log_data)

# Key processing function with distractors embedded
def process_metrics(telemetry, thresholds):
    # Distractor: initialize unused tracking map
    status_map = {i: 'nominal' for i in range(0, len(telemetry), 10)}
    
    # Actual relevant logic starts here
    critical_count = 0
    rolling_high = 0
    
    # Filter data first
    clean_log = filter_transients(telemetry, tolerance=2.0)
    
    # Extract values and apply calibration offset
    calibrated_values = [round(pair[1] + 3.7, 2) for pair in clean_log]
    
    # Misleading normalization block
    if calibrated_values:
        max_val = max(calibrated_values)
        normalized = [v / max_val * 100 for v in calibrated_values]  # not used later
    
    # Real diagnostic logic
    for val in calibrated_values:
        if val > thresholds['critical']:
            critical_count += 1
        if val > rolling_high:
            rolling_high = val
    
    # Secondary condition check
    duration_flag = len(clean_log) > 40
    
    # Final computation
    base_score = rolling_high * 1.3
    penalty = critical_count * 8.5
    time_factor = 1.1 if duration_flag else 0.9
    
    # Final diagnostic score
    result = (base_score - penalty) * time_factor
    return round(result, 4)

# Dead code path - appears important but unused
auxiliary_diagnostics = []
for entry in log_data:
    if entry[1] > 75:
        auxiliary_diagnostics.append({
            'time': entry[0],
            'level': 'high',
            'calculated_risk': (entry[1] - 75) * 2
        })

# Trigger decoy functions
deprecated_analysis(log_data)
trigger_false_alarms(log_data)

# Main execution point
final_diagnostic = process_metrics(log_data, system_thresholds)
print(f"Result: {final_diagnostic}")