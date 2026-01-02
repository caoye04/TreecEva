import itertools

# Simulated sensor fusion system with noise filtering and state tracking
def analyze_readings(readings):
    filtered = [x for x in readings if 10 <= x <= 100]
    avg = sum(filtered) / len(filtered) if filtered else 0
    deviation = sum((x - avg) ** 2 for x in filtered) / len(filtered) if filtered else 0
    return avg, deviation

# Legacy compatibility wrapper (never used)
def legacy_process(x):
    return (x + 5) * 2

# Core transformation pipeline
def transform_sequence(seq, mode):
    if mode == 'encode':
        return [i * 2 + (idx % 3) for idx, i in enumerate(seq)]
    elif mode == 'decode':
        return [i // 2 - (idx % 3) for idx, i in enumerate(seq)]
    return seq

# Red herring: unused statistical function
def calculate_entropy(data):
    from math import log
    freq = {}
    for item in data:
        freq[item] = freq.get(item, 0) + 1
    total = len(data)
    return -sum((count / total) * log(count / total) for count in freq.values())

# Misleading intermediate computation (looks important but isn't)
def validate_checksum(arr):
    checksum = 0
    for i, val in enumerate(arr):
        checksum ^= (val + i) * 3
    return checksum % 17

# Key processing logic
def process_metrics(values, threshold=25):
    result = 0
    for v in values:
        if v > threshold:
            result += v // 3
        else:
            result -= v % 4
    return abs(result)

def build_lookup(keys, base_offset):
    lookup = {}
    for i, k in enumerate(keys):
        lookup[k] = (i + base_offset) ** 2 % 97
    return lookup

def evaluate_chain(steps):
    accumulator = 1
    for s in steps:
        if s % 2 == 0:
            accumulator *= (s % 7) + 1
        else:
            accumulator += (s % 5) * 2
    return accumulator % 1000

# Critical path function
def process_results(data_map, flags):
    # Irrelevant preprocessing block (distractor)
    temp_buffer = []
    for k, v in data_map.items():
        if len(k) % 2 == 0 and isinstance(v, list):
            temp_buffer.extend(v[:2])
    
    # Unused validation flag (misleading)
    integrity_check = sum(temp_buffer) % 13 if temp_buffer else 7
    
    # Main computation chain (relevant)
    raw_series = data_map['sequence']
    transformed = transform_sequence(raw_series, 'encode')
    metrics = process_metrics(transformed)
    
    # Secondary data processing
    key_list = ['alpha', 'beta', 'gamma', 'delta']
    lookup_table = build_lookup(key_list, base_offset=metrics % 40)
    
    # Another distraction: complex but unused structure
    decoy_matrix = [[(i*j + metrics) % 23 for j in range(4)] for i in range(4)]
    magic_factor = 0
    for row in decoy_matrix:
        magic_factor += row[::2][0] if len(row) >= 2 else 0
    
    # Actual answer derivation path
    step_chain = [lookup_table[k] for k in key_list if k in lookup_table]
    chain_result = evaluate_chain(step_chain)
    
    # Final computation with conditional override
    if flags.get('override_safety', False):
        final = chain_result * 2
    else:
        final = chain_result + metrics // 5
    
    # The target variable
    final_score = final * 3 + 17
    return final_score

# Initialization data (carefully constructed to yield deterministic result)
sensor_data = [15, 22, 8, 64, 91, 105, 43, 12]
main_sequence = [12, 18, 24, 30]
data_map = {
    'readings': sensor_data,
    'sequence': main_sequence,
    'labels': ['A1', 'B2', 'C3'],
    'config': {'mode': 'active', 'version': 2}
}
flags = {
    'debug_mode': True,
    'override_safety': False,
    'validate_input': False
}

# Dead code path (never executed)
def deprecated_route():
    return "This is never called"

# Orphaned variable assignments (red herrings)
x_ref = 999
intermediate_hash = hash(str(sensor_data))
temp_result = analyze_readings(sensor_data)
unused_tuple = ('placeholder', 42, 3.14)

# Key execution point
final_score = process_results(data_map, flags)
print(f"Result: {final_score}")