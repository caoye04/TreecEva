def preprocess_signal(raw_samples):
    filtered = [x for x in raw_samples if abs(x) > 0.1]
    normalized = [x / max(filtered) for x in filtered]
    return normalized


def generate_checksum(sequence):
    checksum = 0
    for i, val in enumerate(sequence):
        checksum ^= int(val * 100) + i
    return checksum

def evaluate_stability(ratios):
    stable_count = 0
    for i in range(1, len(ratios)):
        if abs(ratios[i] - ratios[i-1]) < 0.05:
            stable_count += 1
    return stable_count > len(ratios) // 2

# Irrelevant helper (distractor)
def unused_helper(data):
    return sum(x ** 0.5 for x in data if x > 0)

def transform_sequence(values, mode='standard'):
    if mode == 'reverse':
        return [1.0 / x for x in values if x != 0]
    else:
        return [x * 2 for x in values]

# Simulate sensor readings
sensor_logs = [
    [1.2, 0.8, 0.5, 0.0, -0.3, 0.0, 1.1],
    [0.9, 0.0, 0.7, 0.6, 0.0, 0.4, 0.0],
    [1.1, 1.3, 0.0, 0.9, 0.8, 0.7, 1.0]
]

aggregated = []
for log in sensor_logs:
    cleaned = preprocess_signal(log)
    doubled = transform_sequence(cleaned, 'standard')
    aggregated.extend(doubled)

# Dead code path (misleading)
if len(aggregated) < 10:
    fallback = [x * 1.5 for x in aggregated]
    aggregated = fallback

# Construct threshold map with bitwise logic (red herring)
base_level = 0.5
shifted = int(base_level * 100) << 2
mapped = {i: (shifted + i) / 100 for i in range(len(aggregated))}
threshold_map = {k: v for k, v in mapped.items() if k % 2 == 0}

# Transform data using list comprehension and zip
index_vals = list(enumerate(aggregated))
multipliers = [1.1, 0.9, 1.05, 0.95] * (len(aggregated)//4 + 1)
scaled_pairs = zip(aggregated, multipliers)
transformed_data = [a * b for a, b in scaled_pairs]

# Analyze pattern with recursive helper
def count_peaks(data, idx=0):
    if idx >= len(data) - 1:
        return 0
    is_peak = data[idx] > data[idx-1] and data[idx] > data[idx+1] if idx > 0 else False
    return (1 + count_peaks(data, idx+1)) if is_peak else count_peaks(data, idx+1)

def compute_entropy(values):
    from math import log
    freq_map = {}
    for v in values:
        freq_map[v] = freq_map.get(v, 0) + 1
    total = len(values)
    entropy = 0.0
    for count in freq_map.values():
        p = count / total
        entropy -= p * log(p, 2)
    return entropy

# Unused recursive function (decoy)
def explore_branch(depth):
    if depth == 0:
        return 1
    return explore_branch(depth-1) + explore_branch(depth-2)

def analyze_pattern(data, thresholds):
    peak_count = count_peaks(data)
    data_set = set(round(x, 3) for x in data)
    reference_set = set(thresholds.values())
    overlap = len(data_set.intersection(reference_set))
    
    # Critical logic step chain
    stage1 = peak_count * 1000
    stage2 = stage1 + overlap * 100
    
    # Logical combination with short-circuit evaluation
    ratio_valid = len(data) > 0 and (max(data) / min(data)) < 10 if len(data) > 0 else False
    adjustment = 50 if ratio_valid and evaluate_stability(data) else -25
    
    intermediate = stage2 + adjustment
    
    # Final computation using bitwise and arithmetic mix
    checksum = generate_checksum(data)
    final_score = intermediate ^ checksum  # XOR fusion
    
    # Additional distractor: unused entropy call
    _ = compute_entropy(data)
    
    return final_score

# Key execution point
final_diagnostic = analyze_pattern(transformed_data, threshold_map)
print(f"Result: {final_diagnostic}")