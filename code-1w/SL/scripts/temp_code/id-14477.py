import math

def preprocess_readings(raw_readings):
    # Irrelevant normalization function (dead path)
    return [x * 0.98 for x in raw_readings if x > 0]

def compute_entropy(values):
    # Distractor: computes Shannon entropy but unused in final result
    total = sum(values)
    probs = [v / total for v in values if v > 0]
    return -sum(p * math.log2(p) for p in probs)

def filter_anomalies(records, limit):
    # Dead code path — looks important but not used
    return [r for r in records if r['status'] != 'ERROR' and r['value'] < limit]

def shift_cipher(seq, key):
    # Bitwise obfuscation distractor
    return [(x ^ key) + 1 for x in seq]

def decode_signature(signal):
    # Unused cryptographic-style decoy
    sig = 0
    for i, val in enumerate(signal):
        sig += (val & 0xFF) << (i % 4)
    return sig % 10000

def evaluate_stability(indices, config):
    # Complex-looking but irrelevant stability analysis
    base = config.get('alpha', 1.0)
    factor = config.get('beta', 2.0)
    temp_score = 0
    for i in indices:
        if i % 3 == 0:
            temp_score += base * 1.5
        elif i % 5 == 0:
            temp_score -= factor * 0.7
    return abs(temp_score) * 0.1  # Never impacts final answer

def aggregate_metrics(dataset, rules):
    # Core logic embedded in noise
    cumulative = 0
    
    # Real preprocessing step disguised among distractors
    valid_entries = [item for item in dataset if item['active'] and item['source'] in rules]
    
    # Extract relevant operational codes using bitwise masking
    op_codes = [entry['diagnostics'] & 0b1111 for entry in valid_entries]
    
    # Real transformation: count occurrences of each code
    freq_map = {}
    for code in op_codes:
        freq_map[code] = freq_map.get(code, 0) + 1
    
    # Real conditional aggregation based on rule thresholds
    threshold = rules[valid_entries[0]['source']] if valid_entries else 0
    for code, count in freq_map.items():
        if code in [1, 3, 7]:
            cumulative += count * (code ** 2)
        elif code % 2 == 0 and count >= threshold:
            cumulative -= count

    # Decoy accumulation branch (never reached due to structure)
    secondary_sum = 0
    for entry in dataset:
        if entry.get('checksum') == -1:
            secondary_sum += 1  # No such checksum exists

    # Another red herring: complex tuple unpacking with no effect
    metadata_log = []
    for _ in range(3):
        metadata_log.append(('dummy', 'idle', (0, 0, {'flag': False})))
    
    # Final computation uses only 'cumulative'
    adjustment = len(metadata_log) * 0  # Neutralized term
    result = cumulative + adjustment
    
    # Key assignment point
    final_diagnostic = result
    return final_diagnostic

# Simulated turbine sensor data (real input)
turbine_data = [
    {'source': 'A', 'value': 104, 'diagnostics': 7, 'active': True, 'status': 'OK'},
    {'source': 'B', 'value': 201, 'diagnostics': 3, 'active': True, 'status': 'OK'},
    {'source': 'A', 'value': 98,  'diagnostics': 7, 'active': True, 'status': 'OK'},
    {'source': 'C', 'value': 150, 'diagnostics': 4, 'active': False,'status': 'ERROR'},  # inactive
    {'source': 'B', 'value': 190, 'diagnostics': 3, 'active': True, 'status': 'OK'},
    {'source': 'A', 'value': 102, 'diagnostics': 1, 'active': True, 'status': 'OK'},
    {'source': 'B', 'value': 205, 'diagnostics': 8, 'active': True, 'status': 'WARNING'},
    {'source': 'A', 'value': 95,  'diagnostics': 7, 'active': True, 'status': 'OK'},
    {'source': 'B', 'value': 195, 'diagnostics': 3, 'active': True, 'status': 'OK'},
    {'source': 'A', 'value': 100, 'diagnostics': 1, 'active': True, 'status': 'OK'}
]

# Threshold map actually used in logic
threshold_map = {'A': 2, 'B': 3, 'C': 1}

# Unused global variables as distractions
global_counter = sum([d['value'] for d in turbine_data]) // 100
reference_hash = decode_signature([7, 3, 4, 8])
system_entropy = compute_entropy([global_counter, reference_hash, 100])

# Real execution path
processed = preprocess_readings([100, 200, 300])
stability = evaluate_stability([1, 3, 5, 7, 9], {'alpha': 0.5, 'beta': 1.5})

# Critical statement
final_diagnostic = aggregate_metrics(turbine_data, threshold_map)

print(f"Result: {final_diagnostic}")