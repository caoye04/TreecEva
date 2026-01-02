def transform_signal(raw_values, factor):
    """Apply non-linear transformation to sensor signal (distractor function)"""
    return [round((x ** 1.5) / factor + 27.3) for x in raw_values if x > 0]


def accumulate_segments(data, window_size):
    """Aggregate data into sliding windows (partially relevant but misleading path)"""
    segments = []
    for i in range(0, len(data) - window_size + 1, window_size // 2):
        segment = data[i:i + window_size]
        segments.append(sum(segment) // len(segment))
    return segments


def extract_features(signal_stream):
    """Extract statistical features from signal (red herring)"""
    mean_val = sum(signal_stream) / len(signal_stream)
    variance = sum((x - mean_val) ** 2 for x in signal_stream) / len(signal_stream)
    peak = max(signal_stream)
    return {'mean': mean_val, 'variance': variance, 'peak': peak}


def decode_sequence(seq):
    """Recursive bit-decoding algorithm used in actual computation"""
    if len(seq) <= 1:
        return seq[0] if seq else 0
    mid = len(seq) // 2
    left = seq[:mid]
    right = seq[mid:]
    return (decode_sequence(left) ^ decode_sequence(right)) + (len(left) & 7)


def normalize_readings(readings):
    """Normalize readings using min-max scaling"""
    if not readings:
        return []
    min_r, max_r = min(readings), max(readings)
    if min_r == max_r:
        return [50] * len(readings)
    return [int(100 * (x - min_r) / (max_r - min_r)) for x in readings]


def filter_anomalies(dataset, limit=95):
    """Remove values above threshold (distractor with side effect)"""
    filtered = [x for x in dataset if x <= limit]
    anomaly_count = len(dataset) - len(filtered)
    # This modifies global state slightly but isn't directly used
    if anomaly_count > 5:
        return filtered[:len(filtered)//2]
    return filtered


def analyze_readings(data, config_map):
    """Core analysis logic that produces the final result"""
    # Step 1: Preprocess with slicing and shifting
    trimmed = data[1:-1]  # Remove first and last
    shifted = [x << 1 for x in trimmed]  # Bit shift left by 1

    # Step 2: Apply XOR-based reduction using recursion
    reduced_value = decode_sequence(shifted)

    # Step 3: Use config map for adjustment
    adjustment = config_map['base'] ^ config_map['mode']
    intermediate = reduced_value + adjustment

    # Step 4: Conditional amplification
    if intermediate < 100:
        intermediate *= 3
    else:
        intermediate += 50

    # Step 5: Final masking with bitwise AND
    final_score = intermediate & 0xFF  # Mask to 8 bits

    return final_score

# Simulated sensor input (real data)
sensor_input = [23, 88, 45, 12, 76, 39, 67, 52, 14, 81, 33]

# Irrelevant transformations (distraction block)
distorted_signal = transform_signal(sensor_input, 3.7)
coarse_features = extract_features(distorted_signal)

# Data preprocessing chain
normalized = normalize_readings(sensor_input)
window_aggregates = accumulate_segments(normalized, 4)

# Filtering operation that affects length
filtered_data = filter_anomalies(window_aggregates, limit=90)

# Add dummy padding to mislead indexing
padded_data = [0] + filtered_data + [0]

# Real processing begins here — slice to remove padding
processed_data = padded_data[1:-1]

# Configuration map used in analysis
threshold_map = {
    'base': 17,
    'mode': 240,
    'sensitivity': 3,
    'calibration': 99
}

# Critical execution point
final_diagnostic = analyze_readings(processed_data, threshold_map)

print(f"Target result: {final_diagnostic}")