import math

# Simulated quantum telemetry data and system logs
def generate_quantum_sequence(seed):
    seq = []
    temp_val = seed
    for i in range(8):
        temp_val = (temp_val * 2 + i) % 17
        seq.append(temp_val)
    return seq

def parse_system_logs(raw_logs):
    parsed = {}
    for entry in raw_logs:
        node_id = entry & 0xF
        status_flag = (entry >> 4) & 0x3
        timestamp = (entry >> 6) & 0x3F
        if node_id not in parsed:
            parsed[node_id] = []
        parsed[node_id].append((status_flag, timestamp))
    return parsed

def compute_entropy(values):
    total = sum(values)
    if total == 0:
        return 0.0
    entropy = 0.0
    for v in values:
        p = v / total
        if p > 0:
            entropy -= p * math.log2(p)
    return round(entropy, 6)

def validate_checksum(data):
    # Irrelevant validation function (red herring)
    checksum = 0
    for d in data:
        checksum = (checksum ^ d) * 13 % 97
    return checksum == 42

def deprecated_diagnostics(logs):
    # Dead code path - never called
    count = 0
    for k, v in logs.items():
        count += len(v) * k
    return count * 2

def analyze_node_health(node_data):
    stable_count = 0
    for flag, ts in node_data:
        if flag == 1 and ts % 2 == 0:
            stable_count += 1
    return stable_count > 2

def transform_sequence(seq):
    # Distractor transformation with no impact on final result
    transformed = []
    for s in seq:
        transformed.append((s ^ 0x5A) % 23)
    return transformed

def calculate_coherence_index(seq):
    diffs = [abs(seq[i+1] - seq[i]) for i in range(len(seq)-1)]
    avg_diff = sum(diffs) / len(diffs)
    return int(avg_diff * 10)

def analyze_system_state(sequence, logs):
    # Core logic begins here
    log_dict = parse_system_logs(logs)
    
    # Misleading intermediate computation
    dummy_metric = 0
    for k in log_dict.keys():
        dummy_metric += k * 3
    dummy_metric = (dummy_metric ^ 123) % 50  # Unused later
    
    # Relevant: Compute sequence coherence
    coherence = calculate_coherence_index(sequence)
    
    # Extract relevant node 5 health (only node 5 matters)
    critical_node = 5
    if critical_node not in log_dict:
        node_health_score = 0
    else:
        node_health_score = analyze_node_health(log_dict[critical_node])
    
    # Bit manipulation red herring
    masked_coherence = coherence & 0xFF
    shifted = (masked_coherence << 2) ^ 0xAA
    inverted = (~shifted) & 0xFFFF  # Not used
    
    # Accumulation through dictionary stats
    duration_stats = {}
    for node_id, records in log_dict.items():
        for flag, ts in records:
            if ts not in duration_stats:
                duration_stats[ts] = 0
            duration_stats[ts] += 1
    
    # Only even timestamps contribute to weight
    time_weight = sum([cnt for ts, cnt in duration_stats.items() if ts % 2 == 0])
    
    # Final computation
    base_score = coherence * 17
    if node_health_score:
        base_score += 23
    final_diagnostic = base_score - time_weight
    
    # Irrelevant print (distractor)
    debug_info = {'coherence': coherence, 'health': node_health_score, 'time_weight': time_weight}
    
    return final_diagnostic

# Main execution flow
seed_input = 13
raw_log_entries = [0x1A3, 0x2B1, 0x1C2, 0x3D0, 0x2E3, 0x1F1, 0x2A2, 0x3B3, 0x1C1, 0x2D0]

quantum_sequence = generate_quantum_sequence(seed_input)
system_logs = raw_log_entries

# Execute key statement
final_diagnostic = analyze_system_state(quantum_sequence, system_logs)

print(f"Result: {final_diagnostic}")