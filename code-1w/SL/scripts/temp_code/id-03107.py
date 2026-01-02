from collections import defaultdict, Counter

# Simulated quantum sensor data and system diagnostics
def generate_quantum_signature(n):
    signature = []
    for i in range(n):
        if i % 3 == 0:
            signature.append((i ** 2) % 7)
        elif i % 5 == 0:
            signature.append((i + 1) * 2)
        else:
            signature.append(i - (i % 4))
    return signature

def evaluate_coherence_level(seq):
    coherence = 0
    decoy_counter = 0  # red herring variable
    for val in seq:
        if val > 0 and val % 2 == 0:
            coherence += 1
        elif val == 0:
            decoy_counter += 1
    return coherence

def compute_entropy(values):
    counts = Counter(values)
    total = len(values)
    entropy = 0.0
    for count in counts.values():
        p = count / total
        entropy -= p * (p).bit_length()  # simplified pseudo-entropy
    return round(entropy, 6)

def track_anomalies(log_entries):
    anomaly_map = defaultdict(int)
    temp_accumulator = 0  # misleading accumulator
    for entry in log_entries:
        if isinstance(entry, dict) and 'status' in entry:
            status = entry['status']
            if status in ['ERR', 'CRIT']:
                anomaly_map[entry['node']] += 1
                temp_accumulator += entry.get('code', 0)
    # Dead code path — never used later
    if temp_accumulator > 100:
        anomaly_map['OVERFLOW'] = 1
    return anomaly_map

def filter_redundant_data(raw_seq):
    filtered = []
    seen = set()
    for x in raw_seq:
        if x not in seen:
            filtered.append(x)
            seen.add(x)
    return filtered

def analyze_system_state(sequence, log):
    # Core logic begins here
    filtered_seq = filter_redundant_data(sequence)
    coherence = evaluate_coherence_level(filtered_seq)
    entropy = compute_entropy(filtered_seq)
    
    # Irrelevant transformation chain
    transform_a = [x ^ 3 for x in filtered_seq if x % 2 == 0]
    transform_b = [x + 2 for x in transform_a if x > 5]
    dummy_sum = sum(transform_b) * 0.1  # Distractor computation
    
    # Critical branching logic with conditional expressions
    base_score = coherence * 17 if entropy < 3.0 else coherence * 12
    adjustment = 5 if len(log) > 10 else -3
    
    # Simulated hardware offset from decoy analysis
    anomalies = track_anomalies(log)
    anomaly_penalty = len(anomalies) * 2

    # Hidden modular arithmetic path
    magic_offset = 0
    for i, val in enumerate(filtered_seq):
        if i % 4 == 0 and val % 2 == 1:
            magic_offset += (val % 6)
    
    # Final composition with bitwise manipulation
    intermediate = (base_score + adjustment - anomaly_penalty) ^ magic_offset
    final_diagnostic = (intermediate + int(dummy_sum)) % 10000  # dummy_sum contributes minimally

    # This print is required to expose the result
    print(f"Result: {final_diagnostic}")
    return final_diagnostic

# Setup input data
quantum_sequence = generate_quantum_signature(25)
system_log = [
    {'node': 'A1', 'status': 'OK', 'code': 0},
    {'node': 'B2', 'status': 'ERR', 'code': 4},
    {'node': 'C3', 'status': 'OK', 'code': 0},
    {'node': 'D4', 'status': 'CRIT', 'code': 9},
    {'node': 'E5', 'status': 'OK', 'code': 1},
    {'node': 'F6', 'status': 'ERR', 'code': 3},
    {'node': 'G7', 'status': 'OK', 'code': 0},
    {'node': 'H8', 'status': 'CRIT', 'code': 7},
    {'node': 'I9', 'status': 'OK', 'code': 2},
    {'node': 'J10', 'status': 'ERR', 'code': 5},
    {'node': 'K11', 'status': 'OK', 'code': 0}
]

# Entry point
final_diagnostic = analyze_system_state(quantum_sequence, system_log)