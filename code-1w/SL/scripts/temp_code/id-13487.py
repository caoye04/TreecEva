import math

def sensor_calibrate(raw_value, offset=0.75):
    # Irrelevant calibration function (dead code path)
    return raw_value * 0.9 + offset

def accumulate_diagnostics(logs):
    # Accumulates diagnostic sum but with red herring operations
    temp_history = []
    debug_factor = 0
    cumulative = 1
    for entry in logs:
        if len(entry['data']) > 3:
            # Misleading branch: never taken due to data structure
            debug_factor += 1
        cumulative *= entry['sensor_id']
        temp_history.append(cumulative)
    # Distractor: returns unused value
    return temp_history[-1] if temp_history else 1

def decode_sequence(signal_str):
    # Counts specific characters as part of signal interpretation
    count_a = signal_str.count('A')
    count_x = signal_str.count('X')
    magic_offset = 42
    if count_a > 2:
        magic_offset -= 10
    return (count_a * 16) - (count_x * 5) + magic_offset

def recursive_filter(values, threshold):
    # Simple recursion that filters values above threshold
    if not values:
        return []
    head, tail = values[0], values[1:]
    filtered_rest = recursive_filter(tail, threshold)
    if head > threshold:
        return [head] + filtered_rest
    else:
        return filtered_rest + [head // 2]  # Subtle transformation

def process_signal_packet(packet):
    # Complex packet processing with distractors
    raw_data = packet.get('payload', [])
    scaling_factor = packet.get('scale', 1.0)
    adjustment_map = {"A": 3, "B": -1, "C": 5}
    adjusted = []
    for i, val in enumerate(raw_data):
        adjusted.append(val * scaling_factor + adjustment_map.get(f'{chr(65 + (i % 3))}', 0))
    # Dead computation: result not used downstream
    outlier_count = sum(1 for x in adjusted if x < -10)
    normalized = [round(x, 2) for x in adjusted]
    return normalized

def analyze_readings(logs_dict):
    # Core analysis function
    readings = logs_dict['readings']
    base_score = 0
    for r in readings:
        if r['active']:
            base_score += r['value']
    # Key dictionary operation
    mode = logs_dict['config'].get('mode', 'normal')
    multiplier = {'debug': 0.5, 'normal': 2, 'safe': 1}.get(mode, 1)
    intermediate = base_score * multiplier
    
    # Conditional branch based on string content
    flag_code = logs_dict['diagnostic_flag']
    if 'CRIT' in flag_code:
        intermediate -= 100
    elif 'WARN' in flag_code:
        intermediate -= 20
    
    # Character counting affects final outcome
    offset = decode_sequence(flag_code)
    
    # Recursive filtering on auxiliary data
    aux_values = logs_dict['aux_data']
    filtered_aux = recursive_filter(aux_values, 15)
    aux_contribution = sum(filtered_aux) // (len(filtered_aux) or 1)
    
    # Final computation
    result = intermediate + offset + aux_contribution
    
    # Distractor variables (irrelevant)
    temp_result = result * 0.1
    validation_chain = [temp_result, temp_result * 2, temp_result * 4]
    checksum = sum(validation_chain)
    
    # Only this matters
    return int(result)

# Simulated system logs (complex structure with distractors)
system_logs = {
    'timestamp': 1712345678,
    'source': 'sensor_array_7',
    'readings': [
        {'value': 12, 'sensor_id': 3, 'active': True},
        {'value': -5, 'sensor_id': 1, 'active': True},
        {'value': 8, 'sensor_id': 4, 'active': False},  # inactive
        {'value': 23, 'sensor_id': 2, 'active': True}
    ],
    'config': {
        'mode': 'normal',
        'version': '2.1',
        'timeout': 30
    },
    'diagnostic_flag': 'AXXWAXAWARNXXA',  # Triggers WARN and character logic
    'aux_data': [10, 20, 5, 30, 8],  # Used in recursive filter
    'metadata': {'location': 'grid_9', 'calibrated': False}
}

# Irrelevant preprocessing (distractor)
raw_logs = [entry['value'] for entry in system_logs['readings']]
processed_logs = {
    'readings': system_logs['readings'],
    'config': system_logs['config'],
    'diagnostic_flag': system_logs['diagnostic_flag'],
    'aux_data': system_logs['aux_data']
}

# Dead function call (no side effects)
diag_accum = accumulate_diagnostics(system_logs['readings'])

# Signal packet processing (unrelated to main logic)
signal_pkt = {'payload': [1.0, 2.0, 1.5], 'scale': 1.2}
packet_out = process_signal_packet(signal_pkt)

# Core execution point
final_diagnostic = analyze_readings(processed_logs)
print(f"Target result: {final_diagnostic}")