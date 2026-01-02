def analyze_signal(samples):
    filtered = [x for x in samples if abs(x) > 0.5]
    magnitude = sum(abs(s) for s in filtered)
    peaks = []
    for i in range(1, len(filtered) - 1):
        if filtered[i] > filtered[i-1] and filtered[i] > filtered[i+1]:
            peaks.append(i)
    return magnitude, peaks


def rolling_average(data, window):
    if window >= len(data):
        return [sum(data) / len(data)]
    avgs = []
    for i in range(len(data) - window + 1):
        avgs.append(sum(data[i:i+window]) / window)
    return avgs


def transform_sequence(seq):
    shifted = [(val << 1) ^ 3 for val in seq]
    reversed_chunks = [shifted[i:i+3][::-1] for i in range(0, len(shifted), 3)]
    flattened = [item for chunk in reversed_chunks for item in chunk]
    return flattened[:len(seq)]


def evaluate_stability(indices, threshold=5):
    if not indices:
        return 0
    diffs = [indices[i+1] - indices[i] for i in range(len(indices)-1)]
    stable_count = sum(1 for d in diffs if d <= threshold)
    return stable_count * threshold


def aggregate_metrics(data, key_param):
    # Core computation path
    base_slice = data[::2]
    processed = [x * 1.5 for x in base_slice]
    
    # Distractor: irrelevant transformation chain
    shadow_copy = data.copy()
    shadow_copy.reverse()
    temp_result = [x ** 0.5 for x in shadow_copy if x > 0][:5]
    dummy_aggregate = sum(temp_result) * 0.1  # Dead-end computation
    
    # Relevant: slicing and arithmetic chain
    windowed = rolling_average(processed, 3)
    adjusted = [round(val + 0.25) for val in windowed]
    
    # Distractor: unused but plausible function call
    _, peak_locations = analyze_signal([float(x) for x in data])
    peak_score = evaluate_stability(peak_locations, 3)  # Computed but not used
    
    # Core logic continues
    transformed = transform_sequence([int(x * 2) for x in adjusted])
    
    # Key interference: misleading intermediate with similar name
    diagnostic_sum = sum(transformed) + key_param
    final_diagnostic = diagnostic_sum * 2 - 8  # Actual answer variable
    
    # Red herring: another variable that looks important
    validation_check = (sum(transformed) + len(transformed)) // 2  # Unused
    
    # Final distractor block
    if len(transformed) > 10:
        correction_factor = max(transformed) // min(transformed)
        final_diagnostic += correction_factor  # Never reached
    
    return final_diagnostic

# Irrelevant global variables
system_threshold = 0.75
calibration_data = [1.2, 0.8, 3.1, 2.5, 0.9]
baseline_offset = -1

# Primary dataset
raw_readings = [4, 6, 2, 8, 5, 7, 3, 9, 1, 4]

# Signal preprocessing (distractor)
smoothed = rolling_average(raw_readings, 2)
scaled_view = [x * 1.1 for x in smoothed]

# Main execution
processed_trends = [x + (x % 3) for x in raw_readings]
trend_data = [val + 2 for val in processed_trends]

# Critical statement
final_diagnostic = aggregate_metrics(trend_data, 7)

print(f"Result: {final_diagnostic}")