def analyze_signal(data, threshold=0.75):
    filtered = [x for x in data if x > threshold]
    return len(filtered) > 0 and sum(filtered) / len(filtered) > 0.85


def compute_entropy(sequence):
    from collections import Counter
    counts = Counter(sequence)
    total = len(sequence)
    entropy = 0.0
    for count in counts.values():
        p = count / total
        entropy -= p * (p ** 0.5)  # simplified pseudo-entropy
    return round(entropy, 4)


def validate_pattern(seq):
    if len(seq) < 3:
        return False
    for i in range(len(seq) - 2):
        if seq[i] == seq[i+1] == seq[i+2]:
            return True
    return False

# Irrelevant helper - decoy function
def normalize_vector(vec):
    mag = sum(x**2 for x in vec) ** 0.5
    return [x / mag for x in vec] if mag else vec

# Unused transformation chain
transformation_pipeline = [
    lambda x: x ** 2,
    lambda x: x + 1,
    lambda x: x * 0.9
]

# Main evaluation logic
base_metrics = [0.82, 0.76, 0.91, 0.68, 0.85]
dynamic_weights = [3, 2, 4, 1, 3]

# Distractor: complex-looking but unused weight scaling
scaled_weights = []
for idx, w in enumerate(dynamic_weights):
    adjustment = 1.1 if idx % 2 == 0 else 0.9
    scaled_weights.append(w * adjustment)

# Real weighting calculation (simpler)
weighted_sum = 0
weight_total = 0
for m, w in zip(base_metrics, dynamic_weights):
    weighted_sum += m * w
    weight_total += w

average_performance = weighted_sum / weight_total

# Additional signal analysis with red herring data
signal_data = [0.8, 0.92, 0.65, 0.88, 0.71]
strong_signal = analyze_signal(signal_data, threshold=0.65)

# Decoy data structure
auxiliary_cache = {
    'temporal': [0.1, 0.3, 0.2],
    'spatial': {'x': 1.0, 'y': 2.0},
    'flags': set()
}

# Another distraction: sequence validation on irrelevant pattern
test_sequence = [1, 2, 2, 3, 3, 3, 4]
pattern_found = validate_pattern(test_sequence)

# Pseudo-entropy of metric distribution
metric_entropy = compute_entropy([round(m, 1) for m in base_metrics])

# Tuple unpacking distraction
config_settings = ('algorithm_x', 'v3.2', True)
method_name, version, active = config_settings

# Key computation hidden among distractors
aggregation_log = []
metrics = base_metrics  # reference
weights = dynamic_weights  # reference

# Core accumulation logic with early termination possibility (unused)
cumulative = 0
for i, (val, wt) in enumerate(zip(metrics, weights)):
    contribution = val * wt * 100
    aggregation_log.append((i, contribution))
    cumulative += contribution
    if i == 2 and cumulative > 300:
        break  # early exit not triggered

# Final score calculation - this is the critical point
final_score = int(cumulative // 10) + (10 if strong_signal else 0)

# Irrelevant print statements (commented out)
# print(f'Entropy: {metric_entropy}')
# print(f'Pattern: {pattern_found}')

# Target result output
print(f"Target result: {final_score}")