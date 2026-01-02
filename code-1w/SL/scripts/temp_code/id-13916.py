import itertools

# Simulated sensor data preprocessing with red herrings
def preprocess_sensor_stream(raw_samples):
    filtered = [x for x in raw_samples if x > -50 and x < 200]
    shifted = [x + 17 for x in filtered]  # Irrelevant offset
    return shifted

# Distractor function - never called but looks important
def deprecated_calibrate(signal, factor=1.05):
    return [round(x * factor, 2) for x in signal]

# Core transformation function
def apply_fourier_surrogate(data):
    result = []
    for i in range(len(data)):
        val = data[i]
        transformed = (val ** 2) % 97
        if transformed > 50:
            transformed -= 23
        result.append(transformed)
    return result

# Secondary processing with decoy logic
def compute_legacy_metrics(dataset):
    total = 0
    count = 0
    for item in dataset:
        if item % 4 == 0:
            total += item * 0.8  # Dead path: not used later
            count += 1
    average = total / (count or 1)
    return round(average, 3)

# Main analysis engine
def analyze_pattern(seq, limits):
    accumulator = 0
    threshold_met = 0

    # Complex interdependent logic
    for idx, value in enumerate(seq):
        if idx % 3 == 0:
            accumulator += value // 3
        elif idx % 4 == 0:
            accumulator -= value % 7
        else:
            accumulator += (value % 5) * 2

        # Conditional branching with misleading intermediate
        temp_flag = False
        if value > limits['high']:
            threshold_met += 1
            temp_flag = True
        elif value < limits['low']:
            threshold_met -= 1
            temp_flag = True

        # Bit manipulation red herring
        masked = value & 0b1111
        if masked == 12:
            accumulator += 5  # Rare case, doesn't trigger

    # Use of itertools - relevant step
    pairs = list(itertools.combinations(seq[:5], 2))
    pair_count = len(pairs)

    final_score = accumulator * 2 + pair_count - threshold_met

    # Decoy set operations (irrelevant to final result)
    unique_values = set(seq)
    expected_range = set(range(20, 60))
    overlap = unique_values.intersection(expected_range)
    coverage_ratio = len(overlap) / len(expected_range)

    # Final computation depends only on final_score
    diagnostic_code = final_score + 100

    # Critical assignment
    final_diagnostic = diagnostic_code

    return final_diagnostic

# Orchestration block
if __name__ == '__main__':
    # Initial input data
    readings = [12, 45, 67, 23, 89, 34, 78, 56, 19, 91]

    # Irrelevant transformations
    calibrated = [x * 1.02 for x in readings]
    normalized = [round(x / max(readings), 4) for x in readings]

    # Actual processing chain
    cleaned = preprocess_sensor_stream(readings)
    transformed_data = apply_fourier_surrogate(cleaned)

    # Unused statistical summary
    stats_summary = {
        'mean': sum(transformed_data) / len(transformed_data),
        'peak': max(transformed_data),
        'triggers': len([x for x in transformed_data if x > 40])
    }

    # Threshold configuration (only 'high' and 'low' are used)
    thresholds = {
        'high': 45,
        'low': 15,
        'window': 5,  # unused
        'hysteresis': 0.1  # unused
    }

    # Compute legacy metrics (distractor)
    legacy_index = compute_legacy_metrics(transformed_data)

    # Key execution point
    final_diagnostic = analyze_pattern(transformed_data, thresholds)
    
    print(f"Result: {final_diagnostic}")