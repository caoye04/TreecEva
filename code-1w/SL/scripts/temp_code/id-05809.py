def analyze_signal(data, threshold=0.5):
    above_threshold = [x for x in data if x > threshold]
    below_threshold = [x for x in data if x <= threshold]
    ratio = len(above_threshold) / len(below_threshold) if below_threshold else 0
    return ratio

# Irrelevant helper function (decoy)
def compute_entropy(sequence):
    from math import log
    freq_map = {}
    for item in sequence:
        freq_map[item] = freq_map.get(item, 0) + 1
    total = len(sequence)
    entropy = -sum((count / total) * log(count / total) for count in freq_map.values())
    return round(entropy, 4)

# Unused transformation chain
def transform_coordinates(coords):
    transformed = []
    for i, (x, y) in enumerate(coords):
        if i % 2 == 0:
            transformed.append((x * 1.5, y + 2))
        else:
            transformed.append((x - 1, y * 0.8))
    return transformed

# Distractor data
temp_readings = [22.1, 23.5, 21.0, 24.3, 25.6, 20.8]
signal_data = [0.1, 0.7, 0.4, 0.9, 0.6, 0.2, 0.8]
sequence_tags = ['A', 'B', 'A', 'C', 'B', 'A']
coord_pairs = [(1, 2), (3, 4), (5, 6)]

# Unused intermediate values
dummy_mask = [True if i % 3 == 0 else False for i in range(len(signal_data))]
offset_index = sum(i for i, val in enumerate(temp_readings) if val > 23)
scaling_factor = compute_entropy(sequence_tags) * 100

# Real computation begins here
def preprocess_metrics(raw):
    processed = []
    for idx, val in enumerate(raw):
        adjusted = val * (idx + 1)
        processed.append(adjusted if adjusted < 10 else 10)
    return processed

def calculate_weighted_sum(values, multipliers):
    total = 0
    for v, m in zip(values, multipliers):
        total += v * m
    return total

def normalize_vector(vec):
    max_val = max(vec)
    return [round(x / max_val, 6) for x in vec] if max_val != 0 else vec

def evaluate_reliability(indices):
    return sum(1 for i in indices if i > 0.3)

# Core logic obscured by noise
raw_metrics = [0.8, 0.5, 0.9, 0.3, 0.7]
weights = [1, 2, 3, 4, 5]

# Heavily distracted execution path
if len(raw_metrics) > 3:
    temp_result = [x * 1.2 for x in raw_metrics]
    if any(x > 0.85 for x in temp_result):
        processed_metrics = preprocess_metrics(temp_result)
        normalized_metrics = normalize_vector(processed_metrics)
        reliability_check = evaluate_reliability(normalized_metrics)
        if reliability_check >= 3:
            weighted_sum = calculate_weighted_sum(normalized_metrics, weights)
            adjustment_factor = analyze_signal(signal_data, threshold=0.5)
            # Critical red herring below
            fake_correction = scaling_factor * 0.01  # Looks important but unused
            final_score = weighted_sum * (1 + adjustment_factor)
            # Final result printed
            print(f"Result: {final_score}")
else:
    final_score = 0

# Dead code path (never reached due to condition)
if __name__ != "__main__":
    coords_transformed = transform_coordinates(coord_pairs)
    final_score = compute_entropy(sequence_tags)