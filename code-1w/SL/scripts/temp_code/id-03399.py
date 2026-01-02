import itertools

# Simulated sensor data preprocessing with multiple red herrings
def analyze_signal_strength(raw_samples):
    if not raw_samples:
        return [0]
    normalized = [x / max(raw_samples) for x in raw_samples if x > 0]
    smoothed = [sum(normalized[i:i+3]) / 3 for i in range(len(normalized) - 2)]
    return smoothed

# Irrelevant auxiliary function (decoy)
def calculate_entropy(data):
    from math import log
    freq = {}
    for d in data:
        freq[d] = freq.get(d, 0) + 1
    total = len(data)
    entropy = 0
    for count in freq.values():
        p = count / total
        entropy -= p * log(p)
    return round(entropy, 4)

# Core transformation chain
def extract_features(signal_sequence):
    indexed = list(enumerate(signal_sequence))
    # Distractor: unused intermediate
    paired = list(zip(indexed[::2], indexed[1::2]))
    amplified = [i * val for i, val in indexed]
    thresholded = [x for x in amplified if x > 1.5]
    return thresholded

# Another decoy function with misleading name
def validate_checksum(arr):
    if len(arr) < 2:
        return False
    checksum = sum(arr[:-1]) % 256
    return checksum == arr[-1]

# Critical processing step
def process_signals(clean_data):
    if not clean_data:
        return -1
    # Real computation path
    base_shift = clean_data[0] * 2
    transformed = [base_shift + (i * x // 2) for i, x in enumerate(clean_data)]
    # Complex filtering using itertools (real usage)
    grouped = [list(g) for k, g in itertools.groupby(transformed, key=lambda y: y % 4)]
    flattened = [item for group in grouped for item in group]
    final_value = sum(flattened) // len(flattened) if flattened else 0
    return final_value

# Main execution flow with distractions
if __name__ == "__main__":
    # Simulated input (real data source)
    sensor_input = [3, 1, 4, 1, 5, 9, 2, 6, 5]

    # Dead code path 1: Unused transformation
    reversed_scaled = [round(x * 0.5, 2) for x in sensor_input[::-1]]
    sorted_unique = sorted(set([x for x in sensor_input if x % 2 == 1]))

    # First real preprocessing step (but result partially misused)
    processed_stream = analyze_signal_strength(sensor_input)

    # Distractor: entropy calculation on irrelevant data
    entropy_score = calculate_entropy(sorted_unique)  # unused

    # Actual feature extraction begins here
    features = extract_features(processed_stream)

    # Dead code path 2: checksum validation never called on correct data
    dummy_with_checksum = [1, 2, 3, 4, 10]  # 1+2+3+4=10 → checksum valid
    is_valid = validate_checksum(dummy_with_checksum)  # misleading but unused

    # Real filtering that feeds into final computation
    filtered_data = [int(f * 10) for f in features if f > 0.5]

    # Key statement containing the target variable
    final_output = process_signals(filtered_data)

    # Red herring output
    debug_info = {"count": len(filtered_data), "max": max(filtered_data) if filtered_data else 0}

    # Correct output must be printed in this format
    print(f"Target result: {final_output}")