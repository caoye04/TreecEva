import math

def analyze_signal_strength(signal_data, threshold=0.75):
    filtered = [x for x in signal_data if x > threshold]
    return sum(filtered) / len(filtered) if filtered else 0.0

def compute_entropy(values):
    total = sum(values)
    probabilities = [v / total for v in values if v > 0]
    return -sum(p * math.log2(p) for p in probabilities)

def validate_checksum(record):
    return sum(ord(c) for c in record) % 256

def transform_dataset(raw_data, mode='encode'):
    if mode == 'encode':
        return {k: pow(v, 3) - v for k, v in raw_data.items()}
    else:
        return {k: int(round(pow(v + v, 1/3))) for k, v in raw_data.items()}

def simulate_buffer_overflow(data_stream):
    buffer = []
    overflow_flag = False
    for val in data_stream:
        buffer.append(val * 2)
        if len(buffer) > 100:
            overflow_flag = True
            break
    return overflow_flag

def evaluate_consistency(metrics_log):
    trends = [1 if metrics_log[i] <= metrics_log[i+1] else 0 for i in range(len(metrics_log)-1)]
    consistency_rate = sum(trends) / len(trends) if trends else 0
    return consistency_rate > 0.8

def generate_test_vector(size):
    vector = [0] * size
    for i in range(size):
        vector[i] = (i ** 2 + 3 * i + 7) % 19
    return vector

def deprecated_diagnostics(old_system_data):  # Unused function - red herring
    return [x ^ 0xFF for x in old_system_data]

def decode_transmission(transmission):
    decoded = []
    for ch in transmission:
        decoded.append(ord(ch) ^ 5)
    return decoded

def encrypt_payload(payload):  # Dead code path
    return ''.join(chr((ord(c) + 3) % 128) for c in payload)

def aggregate_metrics(log_entries, system_flags):
    base_score = 0
    
    # Relevant calculation block
    critical_count = sum(1 for entry in log_entries if entry['level'] == 'CRITICAL')
    warning_count = sum(1 for entry in log_entries if entry['level'] == 'WARNING')
    info_count = sum(1 for entry in log_entries if entry['level'] == 'INFO')
    
    severity_map = {'CRITICAL': 5, 'ERROR': 3, 'WARNING': 2, 'INFO': 1}
    weighted_severity = sum(
        severity_map.get(entry['level'], 0) * entry.get('weight', 1)
        for entry in log_entries
    )
    
    # Distractor: complex but unused entropy calculation
    entropy_values = [len(entry['message']) for entry in log_entries]
    signal_data = [len(entry['message']) / 10.0 for entry in log_entries]
    signal_quality = analyze_signal_strength(signal_data)
    entropy_metric = compute_entropy(entropy_values) if entropy_values else 0
    
    # Another distractor: checksum validation on irrelevant field
    checksums = [validate_checksum(entry['message']) for entry in log_entries]
    avg_checksum = sum(checksums) / len(checksums) if checksums else 0
    
    # Simulate unused system behavior
    test_vector = generate_test_vector(50)
    overflow_occurred = simulate_buffer_overflow(test_vector)
    
    # Key logic chain starts here
    base_score += critical_count * 25
    base_score += warning_count * 8
    base_score += info_count * 2
    
    if system_flags.get('high_power_mode', False):
        base_score *= 1.2
    
    if system_flags.get('debug_enabled', False):
        base_score -= 15
    
    temporal_trend = [entry['timestamp'] for entry in log_entries]
    is_monotonic = all(temporal_trend[i] <= temporal_trend[i+1] for i in range(len(temporal_trend)-1))
    if is_monotonic:
        base_score += 10
    
    consistency = evaluate_consistency([len(entry['message']) for entry in log_entries])
    if consistency:
        base_score += 7
    
    # Final transformation - relevant
    final_diagnostic = int(round(base_score + weighted_severity))
    
    # Decoy assignments (no effect)
    temp_result = transform_dataset({'a': 4, 'b': 9}, 'encode')
    decrypted = decode_transmission("HELLO")
    
    return final_diagnostic

# Main execution
log_entries = [
    {'level': 'CRITICAL', 'message': 'System overload detected', 'weight': 2, 'timestamp': 100},
    {'level': 'WARNING', 'message': 'High latency', 'weight': 1, 'timestamp': 105},
    {'level': 'WARNING', 'message': 'Memory pressure', 'weight': 1, 'timestamp': 110},
    {'level': 'INFO', 'message': 'User login', 'weight': 1, 'timestamp': 115},
    {'level': 'INFO', 'message': 'Configuration reload', 'weight': 1, 'timestamp': 120},
    {'level': 'CRITICAL', 'message': 'Data corruption', 'weight': 3, 'timestamp': 125}
]

system_flags = {
    'high_power_mode': True,
    'debug_enabled': True,
    'network_optimized': False,
    'legacy_support': True
}

# Execution point of interest
final_diagnostic = aggregate_metrics(log_entries, system_flags)
print(f"Target result: {final_diagnostic}")