def transform_values(values, scale=1.0, invert=False):
    # Irrelevant transformation function (dead code path)
    if invert:
        return [round((1.0 / v) * scale, 4) if v != 0 else 0 for v in values]
    return [v * scale for v in values]


def analyze_pattern(seq):
    # Distractor: analyzes bit patterns but unused in final result
    bit_analysis = {}
    for i, val in enumerate(seq):
        bin_rep = bin(val & 0xFFFF)
        ones = bin_rep.count('1')
        zeros = len(bin_rep) - 2 - ones
        bit_analysis[i] = {'ones': ones, 'zeros': zeros, 'parity': ones % 2}
    return bit_analysis

# Unused helper that looks important
def compute_entropy(weights):
    from math import log2
    total = sum(weights)
    probs = [w / total for w in weights if w > 0]
    entropy = -sum(p * log2(p) for p in probs)
    return round(entropy, 6)

# Decoy data structures
auxiliary_map = {k: (k**2 % 17) for k in range(1, 50)}
decoys = [x ^ 3 for x in auxiliary_map.values()]

# Actual input data
raw_inputs = [84, 92, 76, 88, 95]
weights = [0.1, 0.2, 0.3, 0.25, 0.15]  # Must sum to 1.0

# Simulate preprocessing with red herring operations
preprocessed = []
for idx, val in enumerate(raw_inputs):
    adjusted = val + (idx % 3)  # Minor adjustment
    if idx % 2 == 0:
        adjusted = max(adjusted - 2, 0)
    preprocessed.append(adjusted)

data_points = [max(x - 70, 0) for x in preprocessed]  # Normalize base scores

# Set operation distractor
unique_set = set(data_points)
supplementary_set = {x * 2 for x in unique_set if x < 20}
disjoint_check = unique_set.isdisjoint(supplementary_set)

# Core logic hidden among distractions
def validate_weights(wgts):
    return abs(sum(wgts) - 1.0) < 1e-6

def calculate_weighted_sum(vals, wgts):
    if not validate_weights(wgts) or len(vals) != len(wgts):
        return -1
    
    temp_results = []
    for i, (v, w) in enumerate(zip(vals, wgts)):
        contribution = v * w
        temp_results.append(contribution)
    
    cumulative = sum(temp_results)
    correction_factor = 1.0
    
    # Conditional expression red herring
    status = 'valid' if cumulative > 0 else 'invalid'
    
    # Early return decoy — this looks like it might exit early but doesn't affect outcome
    if status == 'invalid':
        return 0
    
    # Additional distraction: case conversion on string representation
    str_cumulative = str(cumulative)
    inverted_case = ''.join(c.lower() if c.isupper() else c.upper() for c in str_cumulative)
    
    return cumulative

# Secondary processing chain
def filter_outliers_and_adjust(sequence):
    mean_val = sum(sequence) / len(sequence)
    std_dev = (sum((x - mean_val)**2 for x in sequence) / len(sequence)) ** 0.5
    threshold = 1.5 * std_dev
    filtered = [x for x in sequence if abs(x - mean_val) <= threshold]
    return filtered if len(filtered) >= 3 else sequence  # fallback

# Another decoy function that does nothing critical
def generate_metadata():
    import time
    return {
        'timestamp': int(time.time()) % 10000,
        'version': '2.1-alpha',
        'checksum': 0xDEADBEEF
    }

# Main processing function buried in complexity
def process_metrics(metrics, importance_weights):
    # Step 1: Filter potential outliers
    cleaned = filter_outliers_and_adjust(metrics)
    
    # Step 2: Apply dynamic scaling based on length
    scale = 1.0
    if len(cleaned) > 4:
        scale = 1.1
    scaled_metrics = [x * scale for x in cleaned]
    
    # Step 3: Re-align weights to match new size if needed
    if len(scaled_metrics) < len(importance_weights):
        trimmed_weights = importance_weights[:len(scaled_metrics)]
    else:
        trimmed_weights = importance_weights + [0.0] * (len(scaled_metrics) - len(importance_weights))
    
    # Step 4: Compute base score
    raw_score = calculate_weighted_sum(scaled_metrics, trimmed_weights)
    
    # Step 5: Apply bonus logic using enumerate and conditional expression
    bonus = 0
    for index, value in enumerate(scaled_metrics):
        if index % 2 == 1 and value > 20:
            bonus += 2.5 if value > 25 else 1.5
    
    # Step 6: Final adjustment using set difference (distractor logic)
    baseline_set = {int(x) for x in scaled_metrics}
    offset_set = {x - 1 for x in baseline_set}
    overlap = baseline_set & offset_set  # intersection
    bonus += len(overlap) * 0.5
    
    # Final computation
    final_result = raw_score + bonus
    
    # Critical print statement
    print(f"Result: {final_result}")
    return final_result

# Dead code block — looks like initialization but unused
config_data = {
    'mode': 'aggressive',
    'thresholds': [0.1, 0.4, 0.9],
    'flags': (True, False, True)
}

# Key execution point
final_score = process_metrics(data_points, weights)
