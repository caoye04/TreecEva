def analyze_signal(raw_samples, config_mode):
    # Irrelevant signal preprocessing (distractor)
    normalized = [round(x * 1.05, 2) for x in raw_samples if x > -50]
    shifted = [x - 32 for x in normalized]
    histogram = {i: shifted.count(i) for i in range(-10, 10) if shifted.count(i) > 1}

    # Core logic: filter and transform relevant data
    valid_range = [x for x in raw_samples if 10 <= x <= 90]
    exponent_weights = [2 ** (i % 4) for i in range(len(valid_range))]
    weighted_sum = sum(a * b for a, b in zip(valid_range, exponent_weights))

    # Decoy function that's never called
    def decrypt_cipher(data):
        return ''.join(chr(x % 90 + 33) for x in data)

    # String manipulation distractors
    mode_tag = config_mode.upper().replace('_', '').strip()
    if 'DEBUG' in mode_tag:
        debug_log = f"Mode: {mode_tag}, Samples: {len(raw_samples)}"
        checksum = sum(ord(c) for c in debug_log) % 1000

    # Set operations with red herring
    expected_values = set(range(10, 91, 3))
    actual_set = set(valid_range)
    missing_set = expected_values - actual_set  # Unused
    overlap_count = len(expected_values & actual_set)

    # Real processing begins here — heavily buried
    def smooth(data):
        if len(data) < 3:
            return data
        result = [data[0]]
        for i in range(1, len(data) - 1):
            result.append((data[i-1] + data[i] + data[i+1]) / 3)
        result.append(data[-1])
        return result

    smoothed = smooth(valid_range)
    truncated = [int(x) for x in smoothed]  # Convert to integers

    # Filter based on dynamic threshold
    avg_val = sum(truncated) / len(truncated) if truncated else 0
    threshold = avg_val * 0.75
    filtered_data = [x for x in truncated if x >= threshold]

    # Actual answer computation chain
    base_score = sum(filtered_data)
    penalty = len([x for x in filtered_data if x % 5 == 0]) * 10
    adjusted_score = base_score - penalty

    # Secondary transformation
    def process_readings(data, limit):
        if not data:
            return -1
        product = 1
        for val in data:
            product *= (val % 7) or 1  # Avoid zeroing
        modulation = product % 100
        return int(adjusted_score + modulation - (limit // 10))

    final_diagnostic = process_readings(filtered_data, threshold)

    # Dead code path — looks important but unused
    if len(filtered_data) > 5:
        backup = 0
        for i, v in enumerate(filtered_data):
            backup += v ^ (i + 1)
        alt_result = backup >> 2

    # Output the target variable
    print(f"Result: {final_diagnostic}")

# Input data
sample_input = [12, 15, 20, 25, 30, 35, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]
config = "CALIBRATE_HIGH_DEBUG_"

# Execute
analyze_signal(sample_input, config)