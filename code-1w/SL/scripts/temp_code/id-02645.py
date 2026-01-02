from collections import defaultdict, Counter
import math

# Irrelevant helper function (decoy)
def validate_input(x):
    return isinstance(x, list) and all(isinstance(i, int) for i in x)

# Misleading data transformation (dead path)
def transform_legacy_format(data):
    return [d * 2 for d in data if d > 5]

# Unused statistical function to distract
def calculate_entropy(values):
    counts = Counter(values)
    total = len(values)
    entropy = 0
    for count in counts.values():
        p = count / total
        entropy -= p * math.log2(p)
    return entropy

# Simulate sensor drift correction (irrelevant computation)
def correct_drift(signal):
    corrected = []
    for i, val in enumerate(signal):
        corrected.append(val - 0.1 * i)  # Decaying adjustment
    return corrected

# Core processing logic (relevant)
def preprocess_entry(entry):
    if entry['type'] == 'A':
        return entry['value'] * 1.5
    elif entry['type'] == 'B':
        return entry['value'] * 0.8
    else:
        return entry['value'] * 0.3

# Weighted aggregation with distractors
def apply_weights(items, w):
    weighted_sum = 0
    total_weight = 0
    for i, item in enumerate(items):
        weight = w.get(i % 4, 1.0)
        # Red herring: complex conditional that never triggers due to data
        if i > 100 and item > 1000:
            weight *= 1.5
        weighted_sum += item * weight
        total_weight += weight
    return weighted_sum / total_weight if total_weight != 0 else 0

# Main processing function
def process_results(raw_data, importance_weights):
    temp_storage = defaultdict(list)
    intermediate_metrics = []
    
    # Process each entry with side-channel accumulation (partially relevant)
    for record in raw_data:
        processed_val = preprocess_entry(record)
        temp_storage[record['type']].append(processed_val)
        intermediate_metrics.append(processed_val ** 0.5)  # Distractor metric
    
    # Extract values in order (A, B, C, D) regardless of input order
    ordered_vals = []
    for t in ['A', 'B', 'C', 'D']:
        if temp_storage[t]:
            # Use mean as representative value
            mean_val = sum(temp_storage[t]) / len(temp_storage[t])
            ordered_vals.append(mean_val)
    
    # Apply weighting scheme (core logic)
    score = apply_weights(ordered_vals, importance_weights)
    
    # Final nonlinear calibration (relevant)
    calibrated = math.tanh(score / 100) * 1000
    
    # Dead code branch: never reached due to logic
    if len(intermediate_metrics) < 0:
        fallback = sum(intermediate_metrics) / len(intermediate_metrics)
        calibrated = fallback
    
    # Final adjustment based on count diversity (relevant)
    type_count = len(set(r['type'] for r in raw_data))
    diversity_bonus = type_count * 5
    final_score = round(calibrated + diversity_bonus)
    
    # Extraneous logging (no effect)
    logs = []
    for k, v in temp_storage.items():
        logs.append(f"Type {k}: {len(v)} entries")
    
    return final_score

# Irrelevant global constants
data_threshold = 42
max_iterations = 1000
timeout_delay = 15

# Actual input data (crafted to follow specific path)
data = [
    {'type': 'A', 'value': 40}, {'type': 'A', 'value': 60},
    {'type': 'B', 'value': 50}, {'type': 'B', 'value': 70},
    {'type': 'C', 'value': 30}, {'type': 'C', 'value': 90},
    {'type': 'D', 'value': 20}
]

# Weight mapping (index modulo-based)
weights = {0: 2.0, 1: 1.5, 2: 1.0, 3: 0.5}

# Execute main logic
final_score = process_results(data, weights)
print(f"Result: {final_score}")