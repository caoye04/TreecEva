import math

def collect_samples():
    # Simulated sensor readings (some relevant, some red herrings)
    raw_data = [127, 255, 0, 64, 191, 32, 223, 96]
    return raw_data

def filter_noise(data):
    # Irrelevant filtering for a different sensor type
    filtered = [x for x in data if x > 30]
    temp_offset = sum([x // 8 for x in data if x % 2 == 0])  # Distractor computation
    return filtered

def extract_features(data):
    # Extract bit patterns and statistical features
    bit_density = 0
    total_bits = 0
    for val in data:
        bit_density += bin(val).count('1')
        total_bits += val & 0b1111  # Lower nibble contribution
    avg_bit_count = bit_density / len(data) if data else 0
    return {'bit_density': bit_density, 'total_bits': total_bits, 'avg': avg_bit_count}

def transform_signal(features, mode='standard'):
    # Complex transformation with decoy branches
    result_vector = []
    scale_factor = 3.14159
    if mode == 'boost':
        scale_factor *= 2
    elif mode == 'eco':
        scale_factor /= 2
    else:
        scale_factor = math.sqrt(scale_factor)  # Actual path taken

    # Distractor: unused calculation
    hypothetical_loss = (features['avg'] ** 2) * 0.01

    for i in range(3):
        transformed = int(features['bit_density'] * (scale_factor / (i + 1)))
        result_vector.append(transformed)

    # Dead code path
    if False:
        result_vector = [x * 2 for x in result_vector]

    return result_vector

def compute_checksum(signal_list):
    # Checksum that looks important but is only partially used
    checksum = 0
    for val in signal_list:
        checksum ^= val
        checksum = (checksum + (checksum << 1)) % 256
    return checksum

def validate_integrity(payload):
    # Validation logic with misleading intermediate values
    reference_set = {100, 200, 300, 400}
    observed_set = set(payload)
    missing = reference_set - observed_set
    extra = observed_set - reference_set
    match_score = len(observed_set & reference_set)
    # The following line does nothing for final result
    anomaly_flag = len(missing) > 0 or len(extra) > 2
    return match_score

def recursive_diagnose(depth, accumulator):
    # Simple recursion to add complexity
    if depth <= 0:
        return accumulator
    new_acc = accumulator + (depth * 17) % 13
    return recursive_diagnose(depth - 1, new_acc)

def analyze_readings(signals):
    # Main analysis function with key logic hidden among distractors
    if not signals:
        return -1

    feature_summary = extract_features(signals)
    processed_vector = transform_signal(feature_summary, mode='default')

    # Critical path begins here
    base_diagnostic = feature_summary['bit_density'] * feature_summary['avg']

    # Distractor: irrelevant validation call
    validation_score = validate_integrity(processed_vector)

    # Real computation chain
    temp_result = int(base_diagnostic)
    temp_result ^= 0xAB      # Bitwise XOR with hex constant
    temp_result += len(processed_vector) * 5

    # Additional layer: recursion with fixed input
    recursive_seed = temp_result % 10
    final_value = recursive_diagnose(6, recursive_seed)

    # Set operation that seems critical but is actually just for show
    status_flags = {f"flag_{i}" for i in range(recursive_seed)}
    debug_flags = {f"flag_{i}" for i in range(temp_result % 7)}
    active_diagnostics = status_flags | debug_flags  # Union, never used again

    # Final adjustment
    final_diagnostic = final_value * 2 - 18
    return final_diagnostic

def main():
    # Orchestration with multiple irrelevant steps
    samples = collect_samples()
    
    # Distractor pipeline branch
    calibrated = [x + 10 for x in samples if x < 200]
    normalized = [x / 255.0 for x in calibrated]
    entropy = -sum(p * math.log(p) for p in normalized if p > 0)  # Unused metric

    cleaned = filter_noise(samples)
    processed_signals = cleaned[:4]  # Truncate to meaningful subset

    # Key execution point
    final_diagnostic = analyze_readings(processed_signals)
    
    # Print required output
    print(f"Result: {final_diagnostic}")

if __name__ == "__main__":
    main()