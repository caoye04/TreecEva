def analyze_signal(samples, baseline):
    adjusted = [x - baseline for x in samples]
    squared = [x ** 2 for x in adjusted]
    filtered = [x for x in squared if x > 10]
    return sum(filtered) if filtered else 0

initial_offset = 5.5
raw_samples = [12, 9, 14, 7, 13]

# Irrelevant transformation chain (dead path)
def transform_sequence(seq):
    rev = seq[::-1]
    doubled = [x * 2 for x in rev]
    modded = [x % 7 for x in doubled]
    return modded

aux_data = transform_sequence([3, 6, 9])
scratch_buffer = [x + 2 for x in aux_data]

# Unused but plausible-looking processing functions
def compute_entropy(data):
    from math import log2
    freqs = {}
    for x in data:
        freqs[x] = freqs.get(x, 0) + 1
    total = len(data)
    entropy = -sum((count / total) * log2(count / total) for count in freqs.values())
    return round(entropy, 3)

entropy_value = compute_entropy([1, 1, 2, 3, 3, 3])

# Distractor: fake normalization with no downstream use
baseline_shift = 0.8
fake_normalized = [round(x * 0.95 + baseline_shift, 2) for x in raw_samples]

# Real processing begins
primary_adjusted = [x - initial_offset for x in raw_samples]
abs_values = [abs(x) for x in primary_adjusted]
scaled = [round(x * 1.7, 2) for x in abs_values]

# Conditional expression used
clamped = [x if x < 15 else 15 for x in scaled]

defect_flags = {i: clamped[i] > 10 for i in range(len(clamped))}

# Simulate sensor confidence levels (unused)
confidence_levels = [(i, 'high') if clamped[i] < 5 else (i, 'low') for i in range(len(clamped))]

# Key transformation: normalize and map thresholds
def normalize_readings(readings):
    min_val, max_val = min(readings), max(readings)
    if min_val == max_val:
        return [0.5] * len(readings)
    return [(x - min_val) / (max_val - min_val) for x in readings]

normalized_data = normalize_readings(clamped)

threshold_map = {}
for i, val in enumerate(normalized_data):
    category = 'A' if val < 0.4 else 'B' if val < 0.7 else 'C'
    threshold_map[f'sensor_{i}'] = {'category': category, 'limit': val * 2}

# Secondary metric based on bit patterns (distractor)
bit_analysis = []
for x in raw_samples:
    bits = bin(x).count('1')
    parity = 'even' if bits % 2 == 0 else 'odd'
    bit_analysis.append((x, bits, parity))

# Unused recursive helper
def cumulative_product(n):
    return 1 if n <= 1 else n * cumulative_product(n - 1)

# Main diagnostic processor
def process_metrics(norm_data, limits):
    categories = [v['category'] for v in limits.values()]
    cat_count = {c: categories.count(c) for c in set(categories)}
    
    # Conditional expression with arithmetic
    base_score = sum(norm_data) * (1.5 if cat_count.get('C', 0) > 0 else 1.0)
    
    penalty = 0
    for i, val in enumerate(norm_data):
        sensor_key = f'sensor_{i}'
        if sensor_key in limits:
            limit_val = limits[sensor_key]['limit']
            if val > limit_val * 0.9:
                penalty += 0.3
    
    # Final computation
    adjusted_score = base_score - penalty
    return int(round(adjusted_score * 100))

# Execution point of interest
final_diagnostic = process_metrics(normalized_data, threshold_map)

# Other red herring computations
aggregate_flag = any(x > 12 for x in clamped)
dummy_checksum = sum((i + 1) * round(v) for i, v in enumerate(clamped)) % 17

# Noise: fake state machine
states = ['idle', 'active', 'standby']
current_state = states[len(raw_samples) % 3]

# This prints the actual answer
print(f"Result: {final_diagnostic}")