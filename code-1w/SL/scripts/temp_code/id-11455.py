import itertools

# Simulated sensor data processing with diagnostic evaluation
def process_sensor_readings(raw_data):
    # Irrelevant transformation: reverse and shift (red herring)
    shifted_data = [x >> 2 for x in raw_data]
    reversed_chunks = [raw_data[i:i+3][::-1] for i in range(0, len(raw_data), 3)]
    flat_reversed = list(itertools.chain.from_iterable(reversed_chunks))

    # Core computation: extract anomalies via bit analysis
    bit_frequencies = [0] * 8
    for val in raw_data:
        for i in range(8):
            if val & (1 << i):
                bit_frequencies[i] += 1

    # Derive entropy-like metric (relevant)
    total_bits = sum(bit_frequencies)
    entropy_score = 0.0
    for freq in bit_frequencies:
        if freq > 0:
            p = freq / total_bits
            entropy_score -= p * __import__('math').log2(p)

    # Distractor: unused statistical measures
    mean_val = sum(raw_data) / len(raw_data)
    variance = sum((x - mean_val) ** 2 for x in raw_data) / len(raw_data)
    std_dev = __import__('math').sqrt(variance)
    outlier_threshold = mean_val + 2 * std_dev
    outliers = [x for x in raw_data if x > outlier_threshold]  # Dead code path

    # Encoding phase: map segments to diagnostic codes (relevant)
    encoded_segments = []
    for i, chunk in enumerate(reversed_chunks):
        if len(chunk) == 3:
            # Nonlinear transform with cross-term
            code = (chunk[0] ^ chunk[1]) + (chunk[2] << 1) - (i * 3)
        else:
            code = sum(chunk)  # fallback (never reached due to input length)
        encoded_segments.append(code % 256)

    # Weighting schema based on position and entropy (relevant)
    base_weights = [abs(__import__('math').sin(i + entropy_score)) for i in range(len(encoded_segments))]
    normalized_weights = [w / sum(base_weights) for w in base_weights]
    weights = [round(w, 6) for w in normalized_weights]

    # Final aggregation (key statement)
    final_diagnostic = aggregate_metrics(encoded_segments, weights)
    return final_diagnostic


def aggregate_metrics(segments, weights):
    # Element-wise weighted sum
    weighted_sum = sum(seg * w for seg, w in zip(segments, weights))
    correction_factor = len(segments) / (weighted_sum or 1)
    adjusted = weighted_sum * correction_factor
    return int(adjusted * 100) / 100.0  # Two decimal precision

# Misleading initialization block (distractor)
data_stream = [243, 189, 77, 156, 201, 92, 115, 144, 67]
checksum = sum(data_stream) ^ 0xFF
buffer_status = 'FULL' if len(data_stream) > 5 else 'LOW'

# Unused signal processing chain (dead path)
def analyze_signal(x):
    return __import__('math').atan(x / 255.0)
signal_profiles = [analyze_signal(x) for x in data_stream]

# Actual entry point
result = process_sensor_readings(data_stream)

# Critical execution point
final_diagnostic = result

print(f"Result: {final_diagnostic}")