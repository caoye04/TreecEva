import math

def analyze_sensor(input_val, threshold=75):
    if input_val < threshold:
        return (input_val * 1.3) + 8
    else:
        return (input_val * 0.8) - 12

def validate_readings(readings):
    valids = []
    for r in readings:
        if 10 <= r <= 100:
            valids.append(r)
    return valids

def calculate_entropy(data):
    # Irrelevant entropy calculation (dead-end function)
    total = sum(data)
    probs = [d / total for d in data]
    return -sum(p * math.log2(p) for p in probs)

def process_sequence(seq):
    processed = []
    for i, val in enumerate(seq):
        if i % 3 == 0:
            processed.append(val ** 0.5)
        elif i % 3 == 1:
            processed.append(val // 4)
        else:
            processed.append(abs(val - 50))
    return processed

def filter_anomalies(log_entries):
    # Distractor: this function is called but its result not used directly
    anomalies = []
    for entry in log_entries:
        if entry.get('status') == 'ERROR' or entry.get('value') > 95:
            anomalies.append(entry)
    return anomalies

def aggregate_diagnostics(log, flags):
    base_score = 0
    temp_result = []
    
    # Real logic begins
    for record in log:
        raw_val = record['value']
        adjusted = analyze_sensor(raw_val)
        if record['type'] == 'primary':
            base_score += adjusted * 1.2
        elif record['type'] == 'secondary':
            base_score += adjusted * 0.7
    
    # Conditional expression and slicing distraction
    sliced_window = log[1:6:2]  # unused slice
    peak_value = max([r['value'] for r in log])
    
    # Set operations as per requirement
    flag_keys = set(flags.keys())
    required_flags = {'calibrated', 'active', 'verified', 'stable'}
    missing_flags = required_flags - flag_keys
    
    # Decoy computation with intermediate values
    decoy_sum = 0
    for k in ['mode_a', 'mode_b', 'mode_c']:
        if k in flags:
            decoy_sum += len(k) * flags[k]
    
    # Real adjustment based on missing flags
    penalty = 10 * len(missing_flags)
    base_score -= penalty
    
    # Another red herring: complex transformation not affecting outcome
    transformed = [math.sin(x['value'] * 0.01) for x in log if x['value'] > 40]
    aux_accum = sum(transformed[:3]) if len(transformed) >= 3 else 0
    
    # Linear search for a specific condition
    emergency_override = False
    for entry in log:
        if entry['source'] == 'CORE_7' and entry['value'] > 88:
            emergency_override = True
            break
    
    if emergency_override:
        base_score += 25
    
    # Final aggregation with distractor variables
    extra_weight = flags.get('boost', 0)
    temp_result.append(base_score)
    final_value = int(sum(temp_result) + extra_weight - aux_accum)  # aux_accum nearly cancels out
    
    return final_value

# Main execution flow
sensor_data = [88, 62, 91, 45, 73, 84, 52]
valid_data = validate_readings(sensor_data)
processed_data = process_sequence(valid_data)
entropy = calculate_entropy(processed_data)  # computed but unused

# Build diagnostic log (core data structure)
diagnostics_log = [
    {'value': 88, 'type': 'primary',   'source': 'SENSOR_1'},
    {'value': 62, 'type': 'secondary', 'source': 'SENSOR_2'},
    {'value': 91, 'type': 'primary',   'source': 'CORE_7'},
    {'value': 45, 'type': 'secondary', 'source': 'SENSOR_4'},
    {'value': 73, 'type': 'primary',   'source': 'SENSOR_5'},
    {'value': 84, 'type': 'secondary', 'source': 'SENSOR_6'},
    {'value': 52, 'type': 'primary',   'source': 'SENSOR_7'}
]

# System flags with one missing to trigger penalty
system_flags = {
    'calibrated': True,
    'active': 1,
    'stable': 0,
    'boost': 7
    # 'verified' is missing → will cause penalty
}

# Dead code path: filtering not used in final logic
anomaly_list = filter_anomalies(diagnostics_log)

# Key statement
final_diagnostic = aggregate_diagnostics(diagnostics_log, system_flags)

# Print result
print(f"Result: {final_diagnostic}")