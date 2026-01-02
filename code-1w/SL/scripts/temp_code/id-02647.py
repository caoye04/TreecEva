def preprocess_signal(raw_samples):
    filtered = [x for x in raw_samples if abs(x) > 0.1]
    normalized = [x / max(filtered) for x in filtered]
    return normalized


def generate_frequency_map(data):
    # Irrelevant function - dead code path
    freq_map = {}
    for item in data:
        freq_map[item] = freq_map.get(item, 0) + 1
    return freq_map


def shift_window(sequence, offset):
    # Unused transformation
    return sequence[offset:] + sequence[:offset]


def compute_entropy(values):
    from math import log
    total = sum(values)
    probabilities = [v / total for v in values if v > 0]
    entropy = -sum(p * log(p) for p in probabilities)
    return round(entropy, 6)


def extract_features(dataset):
    peaks = []
    for i in range(1, len(dataset)-1):
        if dataset[i-1] < dataset[i] > dataset[i+1]:
            peaks.append(i)
    return peaks


def transform_sequence(seq):
    # Bit manipulation red herring
    transformed = []
    for x in seq:
        temp_val = (x * 100) ^ 42
        if temp_val % 3 == 0:
            transformed.append(temp_val >> 1)
        else:
            transformed.append(temp_val & 127)
    return transformed


def analyze_pattern(data, limit):
    # Core logic hidden among distractions
    base_sum = sum(data[:limit])
    subset = data[::2]  # slicing operation
    alternate_sum = sum(subset)
    
    # Decoy conditional with misleading result
    if alternate_sum > 1000:
        return alternate_sum // 100
    
    # Real computation path
    mirrored = data + data[::-1]  # slicing again - palindrome extension
    mid_point = len(mirrored) // 2
    left_half = set(mirrored[:mid_point])  # set conversion
    right_half = set(mirrored[mid_point:])
    overlap = left_half & right_half  # set intersection
    score = sum(overlap) * len(overlap)
    
    # Early return red herring
    if len(overlap) == 0:
        return -1
    
    # Actual answer path
    adjustment = 3 ** (len(overlap) % 4)
    final_score = score // adjustment
    
    # More misdirection
    outlier_check = [x for x in data if x < 0]
    if outlier_check:
        return sum(outlier_check)
    
    return final_score

# Main execution flow
raw_data = [0.15, 0.3, 0.25, 0.5, 0.4, 0.35, 0.45]
processed = preprocess_signal(raw_data)
scaled_data = [int(x * 1000) for x in processed]  # Convert to integers

# Unused data structures as distractors
frequency_analysis = generate_frequency_map(scaled_data)
decoy_windows = [shift_window(scaled_data, i) for i in range(3)]
feature_markers = extract_features(scaled_data)

# Transform but not use
transformed_distractor = transform_sequence(scaled_data)

# Key irrelevant entropy calculation
entropy_metric = compute_entropy(scaled_data)

# Actual input preparation
transformed_data = [x + 5 for x in scaled_data]  # Final relevant transformation
threshold = len(transformed_data) // 3

# Critical statement
final_diagnostic = analyze_pattern(transformed_data, threshold)

print(f"Target result: {final_diagnostic}")