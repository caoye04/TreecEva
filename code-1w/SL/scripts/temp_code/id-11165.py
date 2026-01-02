def analyze_component_health(sensor_readings, thresholds):
    healthy_count = 0
    for reading in sensor_readings:
        if reading < thresholds['min'] or reading > thresholds['max']:
            continue
        healthy_count += 1
    return healthy_count

# Irrelevant helper function (decoy)
def compute_entropy(data):
    import math
    freq_map = {}
    for item in data:
        freq_map[item] = freq_map.get(item, 0) + 1
    entropy = 0.0
    total = len(data)
    for freq in freq_map.values():
        p = freq / total
        entropy -= p * math.log2(p)
    return entropy

# Another red herring: network simulation
def simulate_handshake(packet_size, retries):
    status_log = []
    for i in range(retries):
        if i % 3 == 0:
            status_log.append(f"Packet {i}: Failed")
        else:
            status_log.append(f"Packet {i}: Success")
    return len([s for s in status_log if "Failed" in s])

# Core logic disguised among distractions
def transform_key_metrics(raw_data, scaling_factor=1.7):
    processed = []
    for idx, val in enumerate(raw_data):
        if idx % 2 == 0:
            processed.append(val * scaling_factor)
        else:
            processed.append(val + scaling_factor)
    return [round(x, 2) for x in processed]

# Bit manipulation decoy (unused but plausible)
def obfuscate_id(device_id):
    return ((device_id << 3) & 0xFFFF) ^ 0xACE1

# Main evaluation engine
def evaluate_performance(metrics, benchmark_data):
    base_score = 0
    adjustment = 0
    
    # Real logic begins: string parsing of configuration
    config_flags = 'alpha-beta-gamma-delta'
    flags_list = config_flags.split('-')
    mode_offset = len([f for f in flags_list if 'a' in f or 'g' in f])
    
    # Actual metric processing
    transformed = transform_key_metrics(metrics)
    
    # Data structure cross-reference distraction
    lookup_table = {i: chr(65 + (i % 26)) for i in range(len(transformed))}
    symbolic_values = [lookup_table[i] for i in range(0, len(transformed), 2)]
    
    # Real scoring logic hidden here
    for i, (orig, trans) in enumerate(zip(metrics, transformed)):
        if i % 2 == 0:
            base_score += orig * (trans // 10)  # Integer division trap
        else:
            base_score -= int(trans % 4)
    
    # Conditional adjustment using boolean logic chain
    high_perf = all(m > 80 for m in metrics)
    balanced = abs(sum(metrics) - sum(benchmark_data)) < 50
    critical_flag = (len(metrics) + len(benchmark_data)) & 1  # Bitwise relevance
    
    if high_perf and balanced or not high_perf and critical_flag:
        adjustment = 17
    elif len(symbolic_values) >= 3 and 'beta' in flags_list:
        adjustment = -10
    else:
        adjustment = 5
    
    # Final computation with distractor variables present
    temp_result = base_score + adjustment + mode_offset
    debug_trace = [f"Step {i}: {val}" for i, val in enumerate(transformed)]
    final_score = temp_result
    
    # Print required result
    print(f"Result: {final_score}")
    return final_score

# Execution entry point
if __name__ == '__main__':
    # Input data
    metrics = [85, 76, 95, 68, 88]
    benchmark_data = [80, 75, 90, 70, 85]
    
    # Dead code path (never called)
    def deprecated_calib():
        return sum(range(10)) * 0.5
    
    # Unused but plausible variables
    calibration_matrix = [[1, 2], [3, 4]]
    system_uptime = 98765
    packet_loss_rate = 0.023
    encryption_key = 0xDEADBEEF
    
    # Trigger main computation
    final_score = evaluate_performance(metrics, benchmark_data)