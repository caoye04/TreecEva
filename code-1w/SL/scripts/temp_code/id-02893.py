import math

# Simulated sensor fusion system for environmental pattern detection
def collect_sensor_data():
    raw_readings = [127, 255, 192, 64, 31, 88, 143]
    filtered = [x for x in raw_readings if x > 50]
    normalized = [round(math.log(x) * 10) for x in filtered]
    return normalized

def generate_checksum(sequence):
    checksum = 0
    for i, val in enumerate(sequence):
        checksum ^= (val << 1) ^ (i + 1)
    return checksum & 255

def transform_sequence(data, key):
    # Irrelevant transformation branch (dead code path)
    if len(data) > 100:
        return [x | key for x in data]
    
    # Actual relevant transformation
    shifted = [(x >> 2) for x in data]
    masked = [x & 63 for x in shifted]
    return [x ^ key for x in masked]

def detect_anomalies(signal_stream):
    anomalies = []
    for i in range(1, len(signal_stream)):
        if abs(signal_stream[i] - signal_stream[i-1]) > 15:
            anomalies.append(i)
    return set(anomalies)

def build_reference_map(values):
    # Distractor: builds a map that's never used
    ref_map = {}
    for idx, v in enumerate(values):
        ref_map[f"V{idx}"] = {"raw": v, "squared": v**2, "log": math.log(v + 1)}
    return ref_map

def calculate_entropy(data):
    from collections import Counter
    counts = Counter(data)
    total = len(data)
    entropy = 0.0
    for count in counts.values():
        p = count / total
        entropy -= p * math.log2(p)
    return round(entropy, 4)

def recursive_condense(seq, limit):
    if len(seq) <= 1:
        return seq[0] if seq else 0
    reduced = [(seq[i] + seq[i+1]) // 2 for i in range(0, len(seq)-1, 2)]
    return recursive_condense(reduced, limit)

def analyze_pattern(input_signals, security_key):
    # Core logic with distractions
    stage_one = transform_sequence(input_signals, security_key)
    
    # Red herring: unused intermediate
    temp_analysis = [math.sin(x) for x in stage_one]
    avg_temp = sum(temp_analysis) / len(temp_analysis)
    
    # Real processing
    valid_nodes = [x for x in stage_one if x % 3 == 0]
    node_sum = sum(valid_nodes)
    
    # Decoy control flow
    if security_key < 0:
        node_sum = int(math.sqrt(node_sum))
    
    # Critical branching based on checksum
    verification_tag = generate_checksum(input_signals)
    if verification_tag % 7 == 0:
        node_sum *= 2
    elif verification_tag % 5 == 0:
        node_sum += 15
    else:
        node_sum += 7
    
    # Apply entropy-based weight (distractor calculation)
    entropy_weight = calculate_entropy(input_signals)
    weighted_score = node_sum * (1 + entropy_weight / 10)
    
    # Final transformation using lambda (required feature)
    process_fn = lambda x, k: (x ^ k) + (x & k)
    final_diagnostic = process_fn(int(weighted_score), security_key)
    
    # Unused complex structure (set operation - required feature)
    anomaly_positions = detect_anomalies(input_signals)
    critical_indices = {1, 3, 5, 7}
    intersection_flag = bool(anomaly_positions & critical_indices)
    
    return final_diagnostic

# Orchestration block
if __name__ == "__main__":
    collected_signals = collect_sensor_data()
    system_key = generate_checksum(collected_signals) ^ 17
    
    # Dead code path: irrelevant data generation
    shadow_buffer = [x * 3 + 2 for x in collected_signals if x < 40]
    buffer_key = sum(shadow_buffer) % 100 if shadow_buffer else 0
    
    # Key execution point
    final_diagnostic = analyze_pattern(collected_signals, system_key)
    
    # Output result
    print(f"Result: {final_diagnostic}")