from itertools import combinations

# Simulated sensor array data with noise and calibration offsets
def generate_sensor_data():
    base_values = [2.1, 3.5, 4.0, 5.2, 6.8]
    noise_offset = sum([i * 0.1 for i in range(5)])  # Irrelevant summation distraction
    calibrated = [round(val + 0.25, 2) for val in base_values]
    return calibrated

# Legacy function - unused but looks relevant
def legacy_normalization(arr):
    max_val = max(arr)
    return [x / max_val for x in arr]

# Advanced filtering using sliding window (not used in final path)
def apply_filter(data, window_size=3):
    filtered = []
    for i in range(len(data) - window_size + 1):
        filtered.append(sum(data[i:i+window_size]) / window_size)
    return filtered

# Core processing pipeline
def transform_sequence(seq):
    transformed = []
    for x in seq:
        if x > 4.0:
            transformed.append(x ** 2)
        else:
            transformed.append(x * 1.5)
    return transformed

def calculate_entropy(values):
    total = sum(values)
    probs = [v / total for v in values if v > 0]
    from math import log2
    return -sum(p * log2(p) for p in probs)

# Decoy metric that looks important but is unused
def compute_robustness_index(data):
    sorted_data = sorted(data)
    q1 = sorted_data[1]
    q3 = sorted_data[3]
    iqr = q3 - q1
    return (q3 + q1) / iqr if iqr != 0 else 0.0

# Real weighting scheme disguised among distractions
def extract_key_features(raw):
    features = {}
    features['mean'] = sum(raw) / len(raw)
    features['peak'] = max(raw)
    features['complexity'] = len(list(combinations([1,2,3,4], 3)))  # Fixed combinatorial value
    features['delta'] = raw[-1] - raw[0]
    return features

def apply_correction(profile):
    profile['adjusted_mean'] = profile['mean'] * 0.95
    profile['penalty'] = 0.1 * profile['delta']  # Red herring: penalty not used
    return profile

def derive_weights(attrs):
    weight_map = {}
    weight_map['mean'] = 0.4
    weight_map['peak'] = 0.3
    weight_map['complexity'] = 0.2
    weight_map['delta'] = 0.1
    # Extra key added to confuse
    weight_map['phantom'] = 0.0  # This is never applied
    return weight_map

def integrate_system_metrics(sensors, config=None):
    # Unused configuration merge
    default_config = {'mode': 'standard', 'gain': 1.0}
    if config:
        default_config.update(config)
    
    processed = transform_sequence(sensors)
    features = extract_key_features(processed)
    corrected = apply_correction(features)
    weights = derive_weights(corrected)
    
    # Critical calculation buried in logic
    score_parts = [
        corrected['adjusted_mean'] * weights['mean'],
        corrected['peak'] * weights['peak'],
        corrected['complexity'] * weights['complexity'],
        abs(corrected['delta']) * weights['delta']
    ]
    
    # Final aggregation
    aggregate = sum(score_parts)
    
    # Distractor: secondary score that isn't used
    diversity_score = calculate_entropy(processed)
    robustness = compute_robustness_index(processed)
    
    return aggregate  # This is what feeds into final_score

# Main execution flow
data = generate_sensor_data()

# Unused transformations that look important
filtered_data = apply_filter(data)
denoised = [x for x in data if x > 3.0]

# Weight structure creation
base_weights = {k: v for k, v in zip(['mean', 'peak', 'complexity', 'delta'], [0.4, 0.3, 0.2, 0.1])}

# Dead code path: conditional that never triggers
if len(data) > 10:
    final_weights = {k: v * 1.1 for k, v in base_weights.items()}
else:
    # Slicing operation used meaningfully
    temp_slice = data[1:4]
    temp_slice.append(999)  # Mutation has no effect
    final_weights = base_weights

# Core processing call
final_score = integrate_system_metrics(data, config={'mode': 'enhanced'})

# Output result as required
print(f"Target result: {final_score}")