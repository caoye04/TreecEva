import math

# Simulated telemetry data from distributed sensors
telemetry_data = [72.3, 68.9, 75.1, 80.4, 65.2, 70.8, 77.6, 73.0, 69.4, 74.5]

# Irrelevant auxiliary sensor list (distractor)
aux_sensors = ['S1', 'S2', 'S3', 'S4']
temp_offsets = {'S1': 0.5, 'S2': -0.3, 'S3': 0.8, 'S4': -1.2}

# System event log with mixed status types
log_entries = [
    {'timestamp': 1001, 'status': 'OK', 'load': 0.45},
    {'timestamp': 1002, 'status': 'WARN', 'load': 0.78},
    {'timestamp': 1003, 'status': 'OK', 'load': 0.33},
    {'timestamp': 1004, 'status': 'ERROR', 'load': 0.92},
    {'timestamp': 1005, 'status': 'OK', 'load': 0.51}
]

# Historical baselines (mostly unused)
historical_avg = 73.5
variance_threshold = 4.5

# Complex preprocessing pipeline with red herrings
def preprocess_telemetry(data):
    filtered = [x for x in data if 65 <= x <= 80]  # Only valid range
    normalized = [(x - min(filtered)) / (max(filtered) - min(filtered)) for x in filtered]
    weighted_sum = sum([n * i for i, n in enumerate(normalized)])
    return round(weighted_sum * 100)

# Unused function - decoy for signal processing
# def analyze_signal_strength(signal):
#     magnitude = lambda s: sum([ord(c) for c in s]) % 100
#     return magnitude(signal)

# Core diagnostic logic
system_load = sum([entry['load'] for entry in log_entries]) / len(log_entries)

# Simulated packet loss (irrelevant to final result)
packet_loss_rate = 0.023
packet_data = "ERR RETRY LOST"
retry_count = len([c for c in packet_data if c == 'R'])  # Distractor

# Bit manipulation for 'checksum' (fake security layer)
def calculate_checksum(value):
    bits = int(value * 100)
    b1 = bits & 0xFF
    b2 = (bits >> 8) & 0xFF
    return (b1 ^ b2) ^ 0xAA

# Diagnostic severity mapping (unused legacy)
severity_map = {
    'CRITICAL': 5,
    'ERROR': 4,
    'WARN': 3,
    'INFO': 2,
    'OK': 1
}

# Advanced metric processor with conditional branching and distractors
def process_metrics(events, avg_load):
    ok_count = len([e for e in events if e['status'] == 'OK'])
    warn_count = len([e for e in events if e['status'] == 'WARN'])
    error_count = len([e for e in events if e['status'] == 'ERROR'])

    # Compute derived metrics
    stability_score = ok_count * 10 + warn_count * 3 - error_count * 15
    
    # Fake entropy calculation (misleading)
    entropy = 0.0
    for e in events:
        p = e['load'] / (avg_load + 1e-8)
        entropy += p * math.log(p + 1e-8)
    entropy = abs(entropy)  # Nowhere used

    # Conditional weighting based on pattern matching
    pattern_match = any([
        events[i]['status'] == 'ERROR' and events[i+1]['status'] == 'OK'
        for i in range(len(events)-1)
    ])

    recovery_bonus = 8 if pattern_match else 0

    # Core accumulation logic
    base_metric = preprocess_telemetry(telemetry_data)
    adjustment_factor = 1.0
    
    if avg_load > 0.7:
        adjustment_factor *= 0.8
    elif avg_load < 0.4:
        adjustment_factor *= 1.2
    else:
        adjustment_factor *= 1.05

    # Decoy transformation using lambda and string method
    transform_key = "DIAGNOSTIC_OVERRIDE"
    shift_value = sum(map(lambda c: ord(c.lower()) % 5, transform_key)) % 7
    # This shift_value is computed but not used

    # Final computation chain
    intermediate = int(base_metric * adjustment_factor)
    load_influence = int(avg_load * 100)
    final_value = intermediate + load_influence + recovery_bonus - calculate_checksum(avg_load)

    # Additional irrelevant bit shift operation
    decoy_flag = (error_count << 3) | warn_count  # Never used

    return final_value

# Execute main logic
baseline_index = preprocess_telemetry(telemetry_data)

# Dead code path - unreachable under normal execution
if baseline_index < 0:
    fallback_mode = True
    final_diagnostic = -999
else:
    final_diagnostic = process_metrics(log_entries, system_load)

# Spurious string processing (distractor)
diag_tag = "FINAL:PASS"
if diag_tag.endswith("PASS"):
    tag_value = sum([ord(c) for c in diag_tag]) % 100

# Output result as required
print(f"Result: {final_diagnostic}")