from collections import defaultdict, Counter

# Simulated quantum sensor readings over time
def generate_quantum_trace():
    base_sequence = [3, 1, 4, 1, 5, 9, 2, 6]
    expanded = []
    for i, val in enumerate(base_sequence):
        expanded.extend([val] * (i % 3 + 1))
    return expanded

# Misleading auxiliary function - never actually used
def compute_entropy(arr):
    freq = {}
    for x in arr:
        freq[x] = freq.get(x, 0) + 1
    entropy = 0
    total = len(arr)
    for count in freq.values():
        p = count / total
        entropy -= p * p
    return round(entropy, 4)

# Distractor: Fake calibration routine
def calibrate_sensors(offset=1.5, mode='legacy'):
    adjustments = []
    for i in range(5):
        adjustments.append((i * offset) ** 0.5)
    return [round(x, 3) for x in adjustments]

# Core analysis function with relevant logic buried in noise
def analyze_system_state(sequence, log_map):
    # Irrelevant pre-processing
    temp_buffer = []
    for idx, val in enumerate(sequence):
        if idx % 4 == 0:
            temp_buffer.append(val ^ 3)
    
    # Real computation begins: frequency analysis
    freq_count = Counter(sequence)
    dominant_value = max(freq_count, key=freq_count.get)
    
    # Distractor: unused transformation
    transformed = [x * 2 + 1 for x in sequence if x < 7]
    size_metric = len(transformed) // 2
    
    # Critical path: analyze bit patterns in most frequent element
    binary_rep = bin(dominant_value)[2:]  # Remove '0b' prefix
    ones_count = binary_rep.count('1')
    zeros_count = binary_rep.count('0')
    
    # Simulated system diagnostics from log
    diagnostic_score = 0
    for entry in log_map.values():
        if entry['status'] == 'active':
            diagnostic_score += entry['node_id'] & 7  # Bitwise masking
    
    # Secondary check: sum of unique powers
    power_sum = 0
    seen = set()
    for x in sequence:
        if x not in seen:
            power_sum += x ** 2
            seen.add(x)
    
    # Main logic chain: combine metrics selectively
    intermediate = (ones_count * 100) + (diagnostic_score * 10)
    if len(binary_rep) > 3:
        intermediate += 5
    
    # Red herring: complex but unused calculation
    decoy_result = 0
    for i in range(len(sequence)):
        for j in range(i+1, min(i+4, len(sequence))):
            decoy_result += sequence[i] ^ sequence[j]
    decoy_result = decoy_result % 97
    
    # Final computation - depends only on specific derived values
    final_diagnostic = intermediate + (power_sum % 25)
    
    return final_diagnostic

# Setup: system telemetry log (simulated)
system_log = {
    'node_01': {'status': 'active', 'node_id': 13, 'priority': 2},
    'node_02': {'status': 'failed', 'node_id': 14, 'priority': 1},
    'node_03': {'status': 'active', 'node_id': 15, 'priority': 3},
    'node_04': {'status': 'active', 'node_id': 16, 'priority': 2},
    'node_05': {'status': 'inactive', 'node_id': 17, 'priority': 1}
}

# Generate main data sequence
quantum_sequence = generate_quantum_trace()

# Dead code path - creates confusion
if len(quantum_sequence) > 20:
    normalized = [x / max(quantum_sequence) for x in quantum_sequence]
    avg_normalized = sum(normalized) / len(normalized)

# Unused statistical summary
dist_summary = {}
for val, cnt in Counter(quantum_sequence).items():
    dist_summary[val] = {'count': cnt, 'weight': val * cnt}

# Key execution point
final_diagnostic = analyze_system_state(quantum_sequence, system_log)

# Output result
print(f"Result: {final_diagnostic}")