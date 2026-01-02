import math

# Simulated sensor array diagnostics with interference
sensor_ids = ['S101', 'S102', 'S103', 'S104']
temp_offsets = {'S101': 0.5, 'S102': -0.3, 'S103': 0.7, 'S104': 0.0}

def normalize(value, baseline=25.0):
    # Irrelevant normalization for unused path
    return (value - baseline) / baseline

def collect_raw_readings():
    # Simulate raw data collection (only some used)
    readings = {
        'S101': [24.3, 25.1, 26.0, 25.8],
        'S102': [23.9, 24.2, 24.0, 24.5],
        'S103': [26.2, 25.8, 26.5, 26.1],
        'S104': [24.9, 25.0, 25.2, 25.1]
    }
    return readings

def filter_outliers(data_list, threshold=1.5):
    # Unused filtering function (red herring)
    mean_val = sum(data_list) / len(data_list)
    stdev = (sum((x - mean_val) ** 2 for x in data_list) / len(data_list)) ** 0.5
    return [x for x in data_list if abs(x - mean_val) <= threshold * stdev]

def process_signal_sequence(raw_seq):
    # Applies transformation but only final aggregate matters
    smoothed = []
    accumulator = 0
    for i, val in enumerate(raw_seq):
        adjusted = val + math.sin(i)  # Minor perturbation
        smoothed.append(adjusted)
        accumulator += adjusted * 0.25
    return accumulator  # Only this value is relevant

def integrate_channels(signal_set):
    # Combines signals but introduces decoy logic
    keys = set(signal_set.keys())
    required = {'S101', 'S102', 'S103'}
    missing = required - keys
    if missing:
        raise ValueError("Missing sensors")
    
    # Decoy summation with unused result
    total_sum = sum(sum(vals) for vals in signal_set.values())
    
    # Only S101 and S103 are actually processed
    s101_proc = process_signal_sequence(signal_set['S101'])
    s103_proc = process_signal_sequence(signal_set['S103'])
    
    # Intermediate irrelevant rounding
    s101_proc = round(s101_proc, 3)
    s103_proc = round(s103_proc, 3)
    
    # Actual relevant computation
    combined_level = s101_proc + s103_proc
    
    # Dead code branch (never executed due to above)
    if 'S105' in signal_set:
        combined_level *= 1.1
        
    return combined_level

def adjust_for_environment(value, hour_of_day=12):
    # Environmental compensation - not actually needed
    time_factor = math.cos((hour_of_day - 6) * math.pi / 12)
    return value * (0.9 + 0.1 * time_factor)

def analyze_readings(composite_value):
    # Final diagnostic analysis
    baseline_ref = 50.0
    deviation = composite_value - baseline_ref
    
    # Complex conditional masking actual simple output
    if deviation < -5:
        risk_level = 3
    elif deviation < 0:
        risk_level = 2
    elif deviation < 5:
        risk_level = 1
    else:
        risk_level = 0  # No risk
    
    # Red herring: bit manipulation on risk (unused)
    encoded_flag = (risk_level << 2) | 0x02
    
    # The real answer is derived from an accumulation chain
    final_score = int(baseline_ref - deviation * 2)  # deterministic
    
    # Dead logic with string operations (distractor)
    status_msg = "OK" if risk_level == 0 else "WARNING"
    status_bits = ''.join(format(ord(c), '08b') for c in status_msg)
    
    return final_score

# Main execution flow
raw_data = collect_raw_readings()

# Process only specific sensors (S101 and S103)
processed_signals = 0
for sid, values in raw_data.items():
    if sid in ['S101', 'S103']:
        processed_signals += process_signal_sequence(values)

# Additional irrelevant set operation (decoy)
detected_sensors = set(raw_data.keys())
expected_sensors = {'S101', 'S102', 'S103', 'S104'}
redundant_intersection = detected_sensors & expected_sensors

# Critical statement
final_diagnostic = analyze_readings(processed_signals)

# Print result as required
print(f"Result: {final_diagnostic}")