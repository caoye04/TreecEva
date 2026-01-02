def analyze_signal(samples):
    # Irrelevant preprocessing: normalize string labels
    label_map = {i: str(i).zfill(3) for i in range(len(samples))}
    normalized_labels = [label.lstrip('0') for label in label_map.values()]

    # Distractor: complex-looking but unused transformation
    transformed = []
    for i, s in enumerate(samples):
        temp_val = (s ** 2 + i * 3) % 7
        if temp_val > 4:
            transformed.append(temp_val * 2)
    
    # Actual relevant logic begins: extract every third reading
    critical_indices = [i for i in range(0, len(samples), 3)]
    critical_readings = [samples[i] for i in critical_indices]

    # Misleading accumulation with XOR (partially irrelevant)
    xor_fingerprint = 0
    for val in samples:
        xor_fingerprint ^= int(abs(val)) % 100
    
    # Real signal processing: average of absolute values above threshold
    abs_readings = [abs(x) for x in critical_readings]
    high_magnitude = [x for x in abs_readings if x > 50]
    avg_magnitude = sum(high_magnitude) / len(high_magnitude) if high_magnitude else 0

    # Distractor: unused recursive function
    def recursive_denoise(data, depth=0):
        if depth >= 3 or len(data) < 2:
            return data
        mid = len(data) // 2
        return recursive_denoise(data[:mid], depth + 1) + recursive_denoise(data[mid:], depth + 1)

    # Fake diagnostic path
    dummy_analysis = ''.join([str(int(x) % 10) for x in samples[:5]])
    checksum = sum(int(d) for d in dummy_analysis)

    # Real filtering based on dynamic threshold
    dynamic_threshold = avg_magnitude * 0.6
    filtered_data = [x for x in samples if abs(x) > dynamic_threshold]

    return filtered_data


def process_readings(readings):
    # Use of enumerate and zip: align readings with weights
    weights = [0.8, 1.1, 0.9, 1.2][:len(readings) % 4 + 1] * 10
    weighted_sum = 0.0
    
    # Complex but partially redundant pairing logic
    for idx, (val, weight) in enumerate(zip(readings, weights)):
        adjusted = abs(val) * weight
        if idx % 2 == 0:
            adjusted = adjusted ** 0.9  # dampen even indices
        weighted_sum += adjusted

    # String slicing distractor
    reading_tag = ''.join([chr(65 + abs(int(r)) % 26) for r in readings])
    tag_suffix = reading_tag[2:6:2]  # unused slice

    # Real computation: apply decay factor based on length
    decay_factor = 0.95 ** len(readings)
    base_result = weighted_sum * decay_factor

    # Bit manipulation red herring
    bit_or_chain = 0
    for r in readings:
        bit_or_chain |= int(abs(r)) & 255
    
    # Final diagnostic depends only on base_result rounded to nearest int
    final_diagnostic = int(round(base_result))

    # Dead code path: never executed due to logic
    if len(readings) > 1000:
        fallback = sum(readings) // len(readings)
        final_diagnostic = fallback

    return final_diagnostic

# Main execution sequence
sensor_log = [-120, 85, -200, 45, 155, -90, 300, -75, 60, 210, -40]

# Unused alternate data paths
legacy_buffer = [x * 1.05 for x in sensor_log[::-1]]
sparse_sample = [sensor_log[i] for i in range(0, len(sensor_log), 2) if i % 4 != 0]

# Key processing pipeline
filtered_data = analyze_signal(sensor_log)
final_diagnostic = process_readings(filtered_data)

print(f"Target result: {final_diagnostic}")