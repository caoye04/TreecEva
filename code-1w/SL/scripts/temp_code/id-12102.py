def analyze_traffic_pattern(log):
    total_entries = len(log)
    suspicious_count = 0
    for entry in log:
        if 'error' in entry or 'timeout' in entry:
            suspicious_count += 1
    risk_score = suspicious_count / total_entries if total_entries > 0 else 0
    return risk_score


def calculate_efficiency(config_str):
    tokens = config_str.split(',')
    valid_tokens = [t.strip() for t in tokens if t.strip().isalnum()]
    efficiency = len(valid_tokens) / len(tokens) if tokens else 0
    return efficiency * 100


def adjust_latency_offset(base_offset, traffic_risk):
    if traffic_risk > 0.5:
        return base_offset * 1.5
    elif traffic_risk > 0.2:
        return base_offset * 1.2
    else:
        return base_offset


def optimize_bandwidth(config, log):
    # Extract base parameters
    raw_params = config['params']
    base_speed = int(raw_params[0:3])
    multiplier = int(raw_params[3])
    
    # Irrelevant string transformation (distractor)
    encoded_tag = ''.join([chr(ord(c) + 1) for c in config['tag']])
    decoded_tag = ''.join([chr(ord(c) - 1) for c in encoded_tag])
    
    # Real computation starts
    usage_length = len(log)
    pattern_score = analyze_traffic_pattern(log)
    
    # Bitwise adjustment (relevant)
    adjusted_speed = base_speed ^ 0b110011  # XOR with fixed pattern
    
    # Efficiency factor from string processing
    efficiency = calculate_efficiency(config['mode'])
    efficiency_bonus = adjusted_speed * (efficiency / 100) * 0.1
    
    # Simulate conditional latency adjustment
    offset = 50
    new_offset = adjust_latency_offset(offset, pattern_score)
    effective_speed = adjusted_speed - new_offset
    
    # Multiple assignments (distractor)
    temp_a, temp_b = 10, 20
    temp_a, temp_b = temp_b, temp_a  # Swap, irrelevant
    
    # Final bandwidth calculation
    final_bandwidth = effective_speed * multiplier + efficiency_bonus
    
    # Dead code path (distractor)
    if False:
        final_bandwidth *= 0.8
    
    # Print result as required
    print(f"Result: {final_bandwidth}")
    return final_bandwidth

# Inputs
base_config = {
    'params': '2453X9',
    'mode': 'high, throughput, , reliable',
    'tag': 'BETA'
}

usage_log = [
    'conn_ok', 'data_sent', 'error_retry', 'timeout', 'retry_ok',
    'conn_ok', 'error_retry', 'data_sent', 'data_sent', 'conn_ok',
    'timeout', 'conn_ok', 'data_sent'
]

# Execution point
final_bandwidth = optimize_bandwidth(base_config, usage_log)