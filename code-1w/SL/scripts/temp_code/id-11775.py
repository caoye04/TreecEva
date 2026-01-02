def analyze_subsystem_state(config_vector, threshold_map):
    temp_accumulator = 0
    diagnostic_trace = set()
    for i, val in enumerate(config_vector):
        if i % 3 == 0:
            temp_accumulator += val * 2
        elif i % 3 == 1:
            temp_accumulator -= val // 3
        else:
            temp_accumulator ^= (val & 7)
        diagnostic_trace.add(temp_accumulator % 101)
    return temp_accumulator, diagnostic_trace

def validate_calibration_sequence(signal_chain):
    validation_key = 1
    for segment in signal_chain:
        if isinstance(segment, tuple) and len(segment) == 2:
            validation_key *= segment[0] + segment[1]
        else:
            validation_key += 5
    return validation_key

def decode_transmission_packet(raw_payload):
    # Irrelevant decoding logic (dead path)
    decoded_stream = []
    for token in raw_payload.split(','):
        try:
            decoded_stream.append(int(token.strip()) * 2)
        except ValueError:
            decoded_stream.append(0)
    return sum(decoded_stream)

def compute_integrity_score(flags, log_entries):
    base_score = 0
    flag_states = set()
    historical_marks = set()
    
    for entry in log_entries:
        parts = entry.split('|')
        if len(parts) < 2:
            continue
        code = parts[0].strip()
        timestamp_str = parts[1].strip()
        if code.startswith('ERR'):
            base_score -= 10
        elif code.startswith('WRN'):
            base_score -= 3
        else:
            base_score += 1
        
        time_parts = timestamp_str.split('.')
        if len(time_parts) > 1:
            ms_val = int(time_parts[1]) % 97
            historical_marks.add(ms_val)
    
    # Process flags
    for k, v in flags.items():
        if v and 'critical' in k:
            flag_states.add(k)
            base_score -= 5
        elif v:
            flag_states.add(k)
            base_score += 2
    
    # Red herring: unused complex structure
    decoy_analysis = {
        'trace_hash': len(flag_states) * 17 + len(historical_marks),
        'anomaly_pattern': (len(log_entries) + len(flag_states)) % 13,
        'dummy_metric': sum(historical_marks) if historical_marks else 0
    }
    
    # Distractor variables
    shadow_accumulator = 0
    for i in range(len(log_entries) // 2):
        shadow_accumulator += ord(log_entries[i][0]) if log_entries[i] else 0
    
    # Meaningful but obfuscated calculation
    adjustment_factor = len(flag_states) - len(historical_marks) % 7
    if adjustment_factor > 0:
        base_score *= adjustment_factor
    else:
        base_score += abs(adjustment_factor) * 4
    
    # Final red herring: irrelevant function call with side effect that doesn't affect result
    config_vec = [7, 14, 21, 28, 35]
    threshold_map = {'a': 5, 'b': 10}
    _, trace_set = analyze_subsystem_state(config_vec, threshold_map)
    
    # Another distraction: unused validation
    signal_seq = [(2, 3), (4, 5), 'X', (1, 1)]
    validate_calibration_sequence(signal_seq)
    
    # Core answer computation
    final_score = base_score + len(trace_set) // 5
    return final_score

# Main execution
if __name__ == '__main__':
    operational_flags = {
        'critical_power': True,
        'critical_io': False,
        'standby_mode': True,
        'debug_enabled': False,
        'cache_active': True
    }
    
    system_log = [
        'INF|1678452345.102',
        'WRN|1678452345.213',
        'ERR|1678452345.341',
        'INF|1678452345.456',
        'INF|1678452345.578',
        'WRN|1678452345.689'
    ]
    
    # Unused but distracting data structures
    packet_data = "13,42,invalid,55"
    decode_transmission_packet(packet_data)
    
    temporal_weights = (1.5, 2.0, 3.5, 4.0)
    weight_sum = sum(w ** 2 for w in temporal_weights) / len(temporal_weights)
    
    # Key execution point
    final_diagnostic = compute_integrity_score(operational_flags, system_log)
    print(f"Result: {final_diagnostic}")