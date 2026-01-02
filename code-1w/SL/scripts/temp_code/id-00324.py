def analyze_workload(entries):
    total_load = 0
    peak_moment = -1
    overload_count = 0
    for i, entry in enumerate(entries):
        load = entry['cpu'] + entry['memory']
        if load > 80:
            overload_count += 1
        total_load += load
        if load > 50 and peak_moment == -1:
            peak_moment = i
    avg_load = total_load / len(entries) if entries else 0
    return avg_load, overload_count, peak_moment


def calculate_entropy(data):
    # Irrelevant helper: computes character frequency entropy
    from math import log2
    freq = {}
    for c in ''.join(data):
        freq[c] = freq.get(c, 0) + 1
    total = sum(freq.values())
    entropy = -sum((count/total) * log2(count/total) for count in freq.values())
    return round(entropy, 4)


def validate_checksum(record):
    # Distractor function: checksum validation (unused path)
    chk = 0
    for c in record:
        chk ^= ord(c)
    return chk == 42


def transform_data(raw):
    # Unused transformation with list comprehension red herring
    cleaned = [x.strip().lower() for x in raw if x.strip()]
    grouped = {}
    for item in cleaned:
        key = item[0] if item else 'x'
        grouped[key] = grouped.get(key, 0) + 1
    return {k: v for k, v in grouped.items() if v > 1}


def evaluate_performance(metrics, thresholds):
    score = 100
    penalty = 0
    warning_flags = []
    
    # Core logic begins
    stability_index = metrics.get('stability', 0)
    response_time = metrics.get('response_time', 0)
    error_rate = metrics.get('error_rate', 0)
    throughput = metrics.get('throughput', 0)
    
    if stability_index < thresholds['stability']:
        penalty += 15
        warning_flags.append('low_stability')
    
    if response_time > thresholds['latency']:
        delay_factor = (response_time - thresholds['latency']) // 10
        penalty += 5 * delay_factor
        warning_flags.append('high_latency')
    
    # Bitwise operation distractor
    encoded_flag = 0
    for flag in warning_flags:
        encoded_flag ^= hash(flag) & 0xF
    
    # Logical evaluation with conditional expression
    saturation_level = 'high' if throughput > thresholds['throughput'] * 0.9 else 'normal'
    bonus = 10 if saturation_level == 'high' and error_rate < 0.02 else 0
    
    # Red herring: complex but unused calculation
    projected_load = (throughput * response_time / (1 + error_rate)) if error_rate > 0 else throughput
    stress_factor = projected_load // 100
    dummy_score = (stability_index ^ int(response_time)) & 0xFFFF
    
    # Actual scoring logic
    score -= penalty
    score += bonus
    
    # Critical statement
    final_score = max(0, min(100, score))  # Clamp to [0,100]
    
    # Dead code branch (never executed due to clamping above)
    if final_score > 100:
        final_score = 100 + (final_score - 100) // 5  # Unused adjustment
    
    return final_score

# Main execution
log_entries = [
    {'timestamp': '00:01', 'cpu': 45, 'memory': 38},
    {'timestamp': '00:02', 'cpu': 60, 'memory': 40},
    {'timestamp': '00:03', 'cpu': 75, 'memory': 45},
    {'timestamp': '00:04', 'cpu': 85, 'memory': 55},
    {'timestamp': '00:05', 'cpu': 30, 'memory': 25}
]

config_strings = ['DebugMode', 'Verbose', 'Production', 'AuditEnabled']
security_record = 'payload_7b2f'

data_metrics = {
    'stability': 78,
    'response_time': 125,
    'error_rate': 0.015,
    'throughput': 950
}

threshold_settings = {
    'stability': 80,
    'latency': 100,
    'throughput': 1000
}

# Call analysis (irrelevant)
avg_load, overloads, first_peak = analyze_workload(log_entries)
entropy_value = calculate_entropy(config_strings)
dummy_transform = transform_data(config_strings)

# Key computation
final_score = evaluate_performance(data_metrics, threshold_settings)

# Output result
print(f"Result: {final_score}")