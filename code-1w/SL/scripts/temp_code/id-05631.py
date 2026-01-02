import itertools

def preprocess_records(raw_entries):
    # Irrelevant preprocessing function (dead end)
    return [e.strip().lower() for e in raw_entries if e]

def calculate_entropy(values):
    # Distractor: computes entropy but not used in final path
    from math import log2
    total = sum(values)
    if total == 0:
        return 0
    probabilities = [v / total for v in values]
    return -sum(p * log2(p) for p in probabilities if p > 0)

def shift_cipher(text, offset):
    # Misleading string manipulation (red herring)
    return ''.join(chr((ord(c) - 97 + offset) % 26 + 97) if c.isalpha() else c for c in text)

def generate_pairs(seq):
    # Uses itertools but produces unused data
    return list(itertools.combinations(seq, 2))

def normalize_readings(raw_readings, baseline=100):
    # Relevant but indirect: used in normalization chain
    adjusted = [(r - min(raw_readings)) for r in raw_readings]
    scale_factor = baseline / max(adjusted)
    return [x * scale_factor for x in adjusted]

def compute_weight_vector(n_features, decay=0.9):
    # Generates weights; partially relevant
    return [decay ** i for i in range(n_features)]

def filter_outliers(data, threshold=2):
    # Dead code path — never called
    mean = sum(data) / len(data)
    std = (sum((x - mean) ** 2 for x in data) / len(data)) ** 0.5
    return [x for x in data if abs(x - mean) <= threshold * std]

def accumulate_metrics(series, mode='additive'):
    # Complex-looking accumulation with misleading modes
    if mode == 'multiplicative':
        result = 1
        for s in series:
            result *= (s + 1)
        return result
    elif mode == 'exponential':
        return sum(s ** 2 for s in series)
    else:
        return sum(s for s in series)  # Only this branch is actually used later

def evaluate_performance(weights, metrics):
    # Core computation: dot product equivalent
    score = 0
    for w, m in zip(weights, metrics):
        score += w * m
    adjustment = len(metrics) % 7  # Minor deterministic tweak
    return score - adjustment

# --- MAIN EXECUTION BLOCK ---
raw_sensor_logs = ['  DATA1  ', 'DATA2', '', 'data3']  # Unused
log_data = preprocess_records(raw_sensor_logs)

data_stream = [85, 72, 90, 64, 77, 88, 93]  # Simulated input

# Irrelevant entropy calculation on raw stream
entropy_value = calculate_entropy(data_stream)

# Generate unused pairs using itertools
pair_combinations = generate_pairs([1, 2, 3, 4])

# Apply cipher to something meaningless (red herring)
ciphered_tag = shift_cipher('metric', 5)

# Normalize the actual data
normalized_data = normalize_readings(data_stream)

# Create weight vector based on number of metrics
metric_weights = compute_weight_vector(len(normalized_data), decay=0.85)

# Accumulate metrics in additive mode (only relevant usage)
aggregate_sequence = accumulate_metrics(normalized_data, mode='additive')

# UNUSED alternative paths
alt_metric_a = accumulate_metrics(normalized_data, mode='multiplicative')
alt_metric_b = accumulate_metrics(normalized_data, mode='exponential')

# Final evaluation uses weights and normalized data directly, NOT the accumulated sequence
final_score = evaluate_performance(metric_weights, normalized_data)

# Print result as required
print(f"Result: {final_score}")