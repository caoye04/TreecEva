import itertools

def preprocess_signal(raw_samples):
    # Irrelevant preprocessing with misleading normalization
    factor = 0.87
    offset = 3
    normalized = [(x * factor + offset) % 256 for x in raw_samples]
    return [n for n in normalized if n > 10]  # Filtering decoy

def generate_bands(frequencies):
    # Dead function: never actually used in critical path
    bands = {}
    for i, f in enumerate(frequencies):
        bands[f'band_{i}'] = f ** 2 if f % 2 else f // 2
    return bands

def shift_sequence(seq, key):
    # Bit manipulation red herring
    shifted = []
    for val in seq:
        temp = (val << 2) ^ key
        temp = (temp & 255) >> 1
        shifted.append(temp)
    return shifted

def filter_outliers(data_stream):
    # Distractor: complex logic that doesn't affect final result
    mean_val = sum(data_stream) / len(data_stream)
    std_dev = (sum((x - mean_val) ** 2 for x in data_stream) / len(data_stream)) ** 0.5
    threshold = mean_val + 2 * std_dev
    return [x for x in data_stream if x <= threshold]

def compute_checksum(chunk):
    # Unused cryptographic-style decoy
    checksum = 0
    for item in chunk:
        checksum = (checksum + item * 31) % 997
    return checksum

def transform_readings(readings):
    # Real transformation chain buried in noise
    base_shift = 7
    mod_base = 13
    transformed = []
    for v in readings:
        intermediate = (v + base_shift) * 2
        wrapped = intermediate % mod_base
        transformed.append(wrapped)
    return transformed

def analyze_pattern(seq):
    # Critical analysis function: computes product of even-indexed elements
    # Only even indices matter; odd ones are distractions
    relevant_elements = [seq[i] for i in range(0, len(seq), 2)]
    score = 1
    for val in relevant_elements:
        score *= val
    return score

# Main execution flow
if __name__ == '__main__':
    # Input signal - deterministic and fixed
    sensor_input = [12, 5, 21, 8, 3, 17, 4, 9]

    # Step 1: Preprocess signal (partially relevant)
    cleaned_signal = preprocess_signal(sensor_input)

    # Step 2: Transform readings - this is where real computation begins
    processed_readings = transform_readings(cleaned_signal)

    # Step 3: Apply bit shift (red herring - result unused)
    secret_key = 5
    obfuscated = shift_sequence(processed_readings, secret_key)  # Not used later

    # Step 4: Filter outliers (distractor - operates on wrong data)
    filtered_main = filter_outliers(processed_readings)

    # Step 5: Generate frequency bands (completely irrelevant)
    dummy_freqs = [100, 200, 150]
    spectral_info = generate_bands(dummy_freqs)

    # Step 6: Compute checksum on decoy data
    _ = compute_checksum(obfuscated)

    # Step 7: Core transformation using itertools to create pairs (required feature)
    paired = list(itertools.pairwise(filtered_main))  # Used nowhere critical

    # Step 8: Final transformation before analysis
    transformed_data = []
    for idx, val in enumerate(filtered_main):
        if idx % 2 == 0:
            transformed_data.append((val * 3) % 11)
        else:
            transformed_data.append((val + 4) % 11)

    # Step 9: Analyze pattern - this is the key statement
    final_diagnostic = analyze_pattern(transformed_data)

    print(f"Result: {final_diagnostic}")