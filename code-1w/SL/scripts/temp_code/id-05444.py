import itertools

# Simulated sensor array diagnostics with redundant and irrelevant computations
def analyze_signal_strength(signal):
    if len(signal) == 0:
        return 0
    magnitude = sum([x ** 2 for x in signal]) ** 0.5
    normalized = [x / (magnitude + 1e-9) for x in signal]
    return sum(normalized[i] * normalized[i+1] for i in range(len(normalized)-1))

# Legacy function - not used but looks important
def deprecated_checksum(data):
    checksum = 0
    for item in data:
        if isinstance(item, int):
            checksum ^= item
    return checksum

# Irrelevant transformation chain
def transform_sequence(seq):
    reversed_seq = seq[::-1]
    shifted = [x << 2 for x in reversed_seq]
    filtered = [x for x in shifted if x % 3 == 0]
    return filtered

# Core processing pipeline
def extract_features(dataset):
    features = []
    for entry in dataset:
        raw_values = entry['readings']
        window_size = 3
        # Sliding window slicing operations
        windows = [raw_values[i:i+window_size] for i in range(len(raw_values) - window_size + 1)]
        avg_power = [sum(w)**2 / len(w) for w in windows]
        features.append(sum(avg_power))
    return features

# Complex conditional mapping
def classify_risk(score, mode='strict'):
    if mode == 'strict':
        if score < 50:
            return 'LOW'
        elif score < 85:
            return 'MEDIUM'
        else:
            return 'HIGH'
    return 'UNKNOWN'

# Main logic with interdependent steps and red herrings
data_stream = [
    {'id': 'A7', 'readings': [3, 7, 2, 8, 5], 'meta': {'version': 1, 'active': True}},
    {'id': 'B2', 'readings': [1, 9, 4, 6, 3], 'meta': {'version': 1, 'active': False}},
    {'id': 'C9', 'readings': [5, 5, 7, 1, 9], 'meta': {'version': 1, 'active': True}}
]

# Distractor: unused but plausible data path
dummy_buffer = list(itertools.chain.from_iterable(
    [[i * j for j in range(1, 4)] for i in range(4)]
))

# Real feature extraction
feature_vector = extract_features(data_stream)

# Irrelevant combinatorial generation
combo_pool = list(itertools.combinations([2, 4, 6, 8], 3))
combo_sums = [sum(c) for c in combo_pool]
mean_combo = sum(combo_sums) / len(combo_sums) if combo_sums else 0

# Signal analysis red herring
total_correlation = 0
for record in data_stream:
    total_correlation += analyze_signal_strength(record['readings'])

# Threshold map construction with slicing distraction
temp_slice = feature_vector[1:]
offset_value = len(temp_slice) * 2.5

threshold_map = {
    'base': feature_vector[0] * 0.75,
    'adaptive': sum(feature_vector) / len(feature_vector) + offset_value,
    'floor': 10.0,
    'ceiling': 200.0
}

# Transform data using multiple slicing and filtering operations
def transform_entry readings = entry['readings']
        processed = [x for x in readings if x > 2]
        rolled = processed[1:] + processed[:1]  # rotation
        return {'transformed': rolled, 'length': len(rolled)}
    
    transformed_list = [transform_entry(e) for e in data_stream]
    flat_data = list(itertools.chain.from_iterable(
        [d['transformed'] for d in transformed_list]
    ))
    return flat_data

transformed_data = transform_dataset(data_stream)

# Diagnostic engine with misleading branches
def evaluate_integrity(data, thresholds):
    base_score = sum(data) / len(data) if data else 0
    peak = max(data) if data else 0
    
    # Dead code branch - never executed due to prior condition
    adjustment = 0
    if False and len(data) > 100:
        segments = [data[i:i+50] for i in range(0, len(data), 50)]
        adjustment = sum([max(s) - min(s) for s in segments])
    
    # Actual scoring logic
    if base_score < thresholds['floor']:
        final_score = thresholds['floor']
    elif base_score > thresholds['ceiling']:
        final_score = thresholds['ceiling']
    else:
        final_score = base_score
    
    # Additional modulation
    if peak > 8:
        final_score *= 1.2
    
    return final_score

# Another decoy function that computes but isn't used
def generate_audit_trace(data):
    trace = []
    for i, val in enumerate(data):
        if i % 3 == 0:
            trace.append(val ^ (i + 1))
    return trace

audit_results = [generate_audit_trace(d['readings']) for d in data_stream]

# Core metric processor - actually used
def process_metrics(data, config):
    if not data:
        return 0
    
    # Use of slicing and statistical aggregation
    segment_a = data[:len(data)//2]
    segment_b = data[len(data)//2:]
    
    mean_a = sum(segment_a) / len(segment_a)
    mean_b = sum(segment_b) / len(segment_b)
    
    # Logical combination of comparisons
    trend = (mean_b > mean_a) and (len(segment_b) >= len(segment_a))
    volatility = sum([(data[i] - data[i-1])**2 for i in range(1, len(data))])
    
    # Conditional branching with short-circuiting
    primary_weight = config['adaptive'] if trend else config['base']
    secondary_weight = config['ceiling'] > volatility or volatility < config['floor']
    
    intermediate = abs(mean_a - mean_b) * primary_weight
    
    if secondary_weight:
        intermediate += volatility * 0.1
    
    # Final clamping operation
    final_value = max(config['floor'], min(intermediate, config['ceiling']))
    
    return round(final_value, 6)

# Execution point of interest
final_diagnostic = process_metrics(transformed_data, threshold_map)

# Print result as required
print(f"Result: {final_diagnostic}")