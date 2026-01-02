def analyze_sensor(network_state):
    if not network_state['active']:
        return 0
    
    # Irrelevant calibration data (distractor)
    calibration_coefficients = [0.98, 1.02, 0.99, 1.01]
    baseline_offset = sum(calibration_coefficients) * 0.25
    adjusted_offsets = [abs(c - baseline_offset) for c in calibration_coefficients]
    
    readings = network_state['readings']
    timestamps = network_state['timestamps']
    
    # Misleading transformation (not used in final result)
    inverted_readings = [1.0 / (r + 1e-5) for r in readings]
    normalized = [r / max(readings) for r in readings]
    
    # Distractor: complex timestamp analysis (dead path)
    time_diffs = []
    for i in range(1, len(timestamps)):
        diff = timestamps[i] - timestamps[i - 1]
        time_diffs.append(diff)
    avg_interval = sum(time_diffs) / len(time_diffs) if time_diffs else 0
    
    # Actual relevant filtering logic (buried in noise)
    valid_pairs = [(r, t) for r, t in zip(readings, timestamps) if 100 <= r <= 500 and t % 2 == 1]
    filtered_data = [p[0] for p in valid_pairs]  # Only readings matter
    
    return filtered_data


def generate_thresholds(base):  # Decoy function - looks important but unused
    levels = {}
    for i, factor in enumerate([0.8, 1.1, 1.3, 1.6], start=1):
        levels[f'level_{i}'] = base * factor + (i ** 0.5)
    return levels

def compute_entropy(data):  # Another decoy - looks scientific
    from math import log
    if not data or len(data) == 0:
        return 0.0
    freq = {}
    for d in data:
        freq[d] = freq.get(d, 0) + 1
    total = len(data)
    entropy = 0.0
    for count in freq.values():
        p = count / total
        entropy -= p * log(p, 2)
    return round(entropy, 4)

def process_readings(data, config_map):  # Core processing
    if not data:
        return -1
    
    # Real computation chain
    squared = [x * x for x in data]
    mod_filtered = [sq for sq in squared if sq % config_map['modulus'] == 0]
    
    # Bit manipulation layer (relevant)
    bitwise_sum = 0
    for val in mod_filtered:
        rotated = ((val << 3) & 0xFF) | (val >> 5)  # 8-bit rotate left by 3
        flipped = rotated ^ 0xFF
        bitwise_sum += (flipped & 0xF)  # Use lower 4 bits
    
    # Conditional aggregation
    adjustment = config_map['gain'] if len(mod_filtered) > 2 else config_map['gain'] * 0.5
    intermediate = sum(mod_filtered) // (len(mod_filtered) or 1)
    final_value = (intermediate + bitwise_sum) * adjustment
    
    # Secondary check using enumerate and zip (required features)
    indices_and_vals = list(enumerate(mod_filtered))
    pairs = list(zip([v**0.5 for v in mod_filtered], [v % 10 for v in mod_filtered]))
    consistency_score = 0
    for idx, (root, digit) in enumerate(pairs):
        if idx < len(indices_and_vals) and root > digit * 2:
            consistency_score += 1
    
    # Final adjustment based on distractor entropy (red herring!)
    fake_entropy = compute_entropy(data)
    # But we don't actually use fake_entropy in logic!
    
    return int(final_value)

# Main execution context
network_status = {
    'active': True,
    'readings': [85, 120, 205, 310, 405, 510, 295, 180, 95],
    'timestamps': [101, 102, 103, 104, 105, 106, 107, 108, 109]
}

# Distractor initialization
system_log = {
    'errors': [],
    'checksum': sum([ord(c) for c in 'diagnostic']) % 1000
}

# Build real configuration (needed)
threshold_map = {
    'modulus': 7,
    'gain': 1.25,
    'version': 'v2.1'
}

# Fake model parameters (misleading)
fake_model_weights = [
    [0.1, 0.3], [0.4, 0.6], [0.7, 0.9]
]
weight_products = []
for row in fake_model_weights:
    prod = 1
    for w in row:
        prod *= w
    weight_products.append(prod)
system_log['product_trace'] = weight_products

# Actual signal flow
raw_output = analyze_sensor(network_status)
# What matters: raw_output becomes input to next stage

# Additional red herring: recursive checksum (looks deep but irrelevant)
def recursive_hash(seq, depth=0):
    if depth >= 3 or len(seq) == 0:
        return 1
    mid = len(seq) // 2
    left = seq[:mid]
    right = seq[mid+1:]
    return (recursive_hash(left, depth+1) + recursive_hash(right, depth+1)) * (seq[mid] % 9) if seq else 1

hash_clue = recursive_hash(raw_output)  # Computed but unused

# Critical statement
final_diagnostic = process_readings(raw_output, threshold_map)

print(f"Result: {final_diagnostic}")