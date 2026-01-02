from collections import defaultdict, Counter

# Simulated sensor data with noise and redundant metrics
def generate_noisy_readings():
    base_values = [i ** 2 for i in range(15)]
    noise_offsets = [(-1) ** i * (i % 3) for i in range(15)]
    return [base_values[i] + noise_offsets[i] for i in range(len(base_values))]

def filter_outliers(data, threshold=25):
    # Irrelevant filtering for high values (distractor)
    return [x for x in data if x <= threshold]

def compute_checksum(seq):
    # Unused checksum function (dead code path)
    return sum(x ^ (x << 1) % 17 for x in seq) % 1000

def shift_window(sequence, offset=3):
    # Misleading transformation
    return sequence[offset:] + sequence[:offset]

def extract_signatures(raw):
    # Extract frequency patterns (partially relevant)
    freq_map = defaultdict(int)
    for val in raw:
        freq_map[val % 7] += 1
    return dict(freq_map)

def apply_mask(signal, mask=[1, 0, 1, 1]):
    # Bitwise decoy operation
    result = []
    for i, s in enumerate(signal):
        bit_decision = mask[i % len(mask)]
        if bit_decision:
            result.append(s & (s + 1))  # Some bit manipulation
        else:
            result.append(s | 5)
    return result

def aggregate_peaks(values):
    # Red herring: finds local maxima but not used in final result
    peaks = []
    for i in range(1, len(values) - 1):
        if values[i] > values[i-1] and values[i] > values[i+1]:
            peaks.append(values[i])
    return peaks

def normalize_sequence(seq):
    # Distracting normalization
    mean_val = sum(seq) / len(seq)
    return [round(x / mean_val, 3) for x in seq]

def transform_features(data_list):
    # Core relevant transformation mixed with noise
    modified = []
    for item in data_list:
        if item % 4 == 0:
            modified.append(item // 2)
        elif item % 3 == 0:
            modified.append(item * 2)
        else:
            modified.append(item + 1)
    return modified

def count_transitions(arr):
    # Decoy statistical measure
    up = down = 0
    for i in range(1, len(arr)):
        if arr[i] > arr[i-1]:
            up += 1
        elif arr[i] < arr[i-1]:
            down += 1
    return {'ups': up, 'downs': down}

def recursive_condense(seq, depth=0):
    # Complex-looking recursion that doesn't affect final output
    if depth >= 3 or len(seq) < 2:
        return seq
    reduced = [seq[i] + seq[i+1] for i in range(0, len(seq)-1, 2)]
    return recursive_condense(reduced, depth + 1)

def string_encode(numbers):
    # Use of string methods as required - irrelevant encoding
    encoded = ''.join([str(n) for n in numbers])
    shifted = encoded.translate(str.maketrans('0123456789', '9876543210'))
    chunks = [shifted[i:i+4] for i in range(0, len(shifted), 4)]
    return '|'.join(chunks)

def analyze_pattern(mapped_data):
    # Final computation: sum of squares of even-indexed elements
    total = 0
    for i in range(0, len(mapped_data), 2):  # Only even indices
        total += mapped_data[i] ** 2
    return total

# Main execution flow with heavy interference
if __name__ == '__main__':
    raw_sensor_log = generate_noisy_readings()  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196]

    # Irrelevant preprocessing chain
    filtered_data = filter_outliers(raw_sensor_log)
    shifted_data = shift_window(filtered_data, 2)
    signature_freq = extract_signatures(shifted_data)
    masked_readings = apply_mask(shifted_data)
    normalized_stream = normalize_sequence(masked_readings)
    transition_stats = count_transitions(normalized_stream)
    deep_reduced = recursive_condense(masked_readings)
    encoded_trace = string_encode(deep_reduced)

    # Key relevant transformation
    transformed_data = transform_features(raw_sensor_log)  # Actual input to analysis

    # Secondary irrelevant check
    peak_values = aggregate_peaks(transformed_data)
    checksum_value = compute_checksum(transformed_data)

    # CRITICAL EXECUTION POINT
    final_diagnostic = analyze_pattern(transformed_data)

    print(f"Result: {final_diagnostic}")