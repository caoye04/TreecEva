def process_telemetry_chunk(chunk_data, config):
    temp_accum = 0
    for i in range(len(chunk_data)):
        if i % 3 == 0:
            temp_accum += chunk_data[i] * config.get('scale', 1)
        elif i % 5 == 0:
            temp_accum -= config.get('offset', 0)
    return temp_accum // 2 if temp_accum > 100 else temp_accum + 10

def validate_checksum(data_seq):
    checksum = 0
    for val in data_seq:
        checksum ^= val
        checksum = (checksum << 1) & 0xFF
    return checksum == 0x7A

def decode_signal_pattern(signal):
    decoded = []
    for s in signal:
        if s > 100:
            decoded.append(s >> 2)
        elif s > 50:
            decoded.append(s + 8)
        else:
            decoded.append(s * 3)
    return decoded[::2]

def compute_health_score(metrics, weights):
    score = 0.0
    for k, v in metrics.items():
        if k in weights:
            score += v * weights[k]
    return round(score / len(weights), 4)

def filter_anomalies(log_stream):
    anomalies = []
    threshold = sum(log_stream) / len(log_stream) + 10
    for idx, val in enumerate(log_stream):
        if val > threshold and idx % 2 == 1:
            anomalies.append(idx)
    return anomalies if anomalies else [0]

def analyze_system_state(log, flags):
    # Core logic begins here
    base_sequence = log['readings'][5:15]
    transformed = [x * 2 + 3 for x in base_sequence if x < 90]
    
    # Irrelevant pre-processing
    dummy_config = {'scale': 7, 'offset': 5, 'mode': 'debug'}
    _ = process_telemetry_chunk(base_sequence, dummy_config)
    _ = validate_checksum(base_sequence)
    
    # Distractor: unused function call with side effects avoided
    _ = decode_signal_pattern(log['signal'])
    
    # Real computation path
    flag_sum = sum(f * (i+1) for i, f in enumerate(flags) if f % 4 == 3)
    
    # More distractions
    fake_metrics = {'cpu': 88, 'mem': 91, 'disk': 75}
    weight_map = {'cpu': 0.4, 'mem': 0.35, 'gpu': 0.25}
    _ = compute_health_score(fake_metrics, weight_map)
    
    # Critical step: filtering only even-positioned values above threshold
    filtered_indices = filter_anomalies(transformed)
    selected_values = [transformed[i] for i in filtered_indices if i < len(transformed)]
    
    # Red herring: complex but unused bitwise logic
    decoy_state = 0
    for f in flags:
        decoy_state ^= (f << 2) | (f >> 1)
        decoy_state = (decoy_state + 97) % 1000
    
    # Actual answer derivation
    adjustment_factor = len(selected_values) if selected_values else -5
    intermediate = sum(selected_values) + flag_sum
    final_diagnostic = intermediate * adjustment_factor
    
    # Another dead-end path
    if decoy_state > 500:
        final_diagnostic -= 100000  # never reached due to decoy_state constraints
    
    return final_diagnostic

# Main execution context
if __name__ == '__main__':
    telemetry_log = {
        'readings': [85, 92, 88, 76, 95, 67, 83, 91, 74, 80, 66, 77, 89],
        'signal': [45, 102, 58, 130, 44, 60]
    }
    system_flags = [3, 7, 11, 15, 19, 23, 27]
    final_diagnostic = analyze_system_state(telemetry_log, system_flags)
    print(f"Result: {final_diagnostic}")