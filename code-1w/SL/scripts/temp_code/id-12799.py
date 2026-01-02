from itertools import combinations

# Simulate sensor data calibration and anomaly detection
def analyze_readings(readings):
    n = len(readings)
    valid_pairs = []
    temp_accumulator = 0
    outlier_threshold = sum(readings) / n * 1.5  # not directly used in final logic

    # Generate all possible pairs for interference
    all_pairs = list(combinations(readings, 2))
    pair_products = [a * b for a, b in all_pairs]

    # Real logic: count valid adjacent pairs above threshold
    for i in range(n - 1):
        product = readings[i] * readings[i + 1]
        if product > 50:
            valid_pairs.append(product)

    # Distractor: unused statistical measures
    squared_devs = [(x - sum(readings)/n)**2 for x in readings]
    variance_proxy = sum(squared_devs) / n if n > 1 else 0

    return len(valid_pairs)

# Data preprocessing with red herring transformations
def preprocess_signal(raw_data):
    processed = []
    checksum = 0
    shift_offset = 3

    for val in raw_data:
        shifted = val << 1  # bit shift - distractor
        adjusted = (shifted + shift_offset) % 256
        processed.append(adjusted)
        checksum ^= adjusted  # irrelevant to final result

    # Actual relevant transformation subset
    filtered = [x for x in processed if x % 2 == 0]
    return filtered[:len(processed)//2 + 1]  # trim to first half+1

# Core aggregation function
def compute_aggregate(data_stream):
    baseline = preprocess_signal(data_stream)
    
    # Irrelevant frequency map
    freq_map = {}
    for item in baseline:
        freq_map[item] = freq_map.get(item, 0) + 1
    
    # Secondary processing with actual impact
    stage_one = [x - 10 for x in baseline if x > 15]
    
    # Nested conditional accumulation
    accumulator = 0
    for x in stage_one:
        if x > 20:
            for _ in range(2):
                accumulator += x // 4
        elif x > 10:
            accumulator += x // 5

    # Final adjustment based on analysis side-channel
    side_analysis = analyze_readings(data_stream)
    final_score = accumulator * 2 - side_analysis

    # Dead code branch - never executed but adds cognitive load
    if False:
        backup = sum(baseline) // len(baseline)
        final_score = max(final_score, backup)

    return final_score

# Input data
data_input = [7, 12, 8, 14, 9, 13, 11]

# Execution point of interest
final_score = compute_aggregate(data_input)
print(f"Result: {final_score}")