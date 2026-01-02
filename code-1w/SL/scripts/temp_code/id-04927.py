import itertools

def analyze_sequence(seq):
    # Irrelevant helper: computes sum of squares (not used in final path)
    return sum(x ** 2 for x in seq if x > 0)

def validate_entry(record):
    # Distractor function: checks format but not actually used
    return isinstance(record, dict) and 'id' in record

def accumulate_signals(values, threshold=5):
    # Dead code path: accumulates values above threshold (misleading)
    acc = 0
    for v in values:
        if v > threshold:
            acc += v * 0.1
    return acc

def filter_outliers(data_stream, limit=3):
    # Unused filtering logic (red herring)
    return [x for x in data_stream if abs(x - sum(data_stream)/len(data_stream)) < limit]

def extract_features(records):
    # Processes records but only partially relevant
    features = []
    for r in records:
        if 'signal' in r:
            features.append(r['signal'] * 2)  # Distraction: doubles signal
    return features

def compute_baseline(dataset):
    # Computes baseline average (looks important but unused)
    total, count = 0, 0
    for item in dataset:
        if isinstance(item, list):
            for val in item:
                total += val
                count += 1
    return total / count if count else 0

def derive_key_weights(factors):
    # Generates weights using bitwise mix (partially relevant)
    result = {}
    for i, f in enumerate(factors):
        key = f"w_{i}"
        weight = (f ^ (i + 1)) % 7 + 1  # Bitwise XOR red herring
        result[key] = weight
    return result

def process_metrics(log_data, weights):
    # Core logic hidden among distractions
    temp_values = []
    for idx, entry in enumerate(log_data):
        # Use enumerate and zip together
        keys = ['a', 'b', 'c']
        vals = [entry.get(k, 0) for k in keys]
        for k, v in zip(keys, vals):
            if k == 'a':
                temp_values.append(v * weights[f'w_{idx % 3}'])
    # Slice operation to take every second element
    selected = temp_values[::2]
    # Real computation buried here
    running_total = 0
    for i, val in enumerate(selected):
        if i % 2 == 0:
            running_total += val * 3
        else:
            running_total -= val * 2
    # Final transformation
    adjustment = len(log_data) & 7  # Bitwise AND distractor
    final_score = running_total + adjustment
    return final_score

# Simulated sensor log data (real input)
log_data = [
    {'id': 'A1', 'a': 4, 'b': 8, 'c': 2},
    {'id': 'B2', 'a': 6, 'b': 1, 'c': 9},
    {'id': 'C3', 'a': 3, 'b': 5, 'c': 7}
]

# Weight factors (used in real computation)
factors = [5, 3, 8]
weights = derive_key_weights(factors)  # Only w_0, w_1, w_2 matter

# Irrelevant data structures
dummy_matrix = [[1, 2], [3, 4]]
feature_set = extract_features(log_data)
baseline = compute_baseline(dummy_matrix)
signal_acc = accumulate_signals(feature_set)

# Critical execution point
final_score = process_metrics(log_data, weights)

# Print result as required
print(f"Result: {final_score}")