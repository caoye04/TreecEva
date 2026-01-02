import itertools

# Simulated sensor data with noise and redundant readings
data_stream = [15, 0, 23, 0, 42, 11, 8, 19, 0, 7, 31, 4, 0, 16, 22]

def clean_sensor_noise(data):
    # Irrelevant filtering (distractor): removes zeros but not actually needed
    return [x for x in data if x != 0]

def extract_peaks(signal):
    # Find local maxima (actual relevant logic)
    peaks = []
    for i in range(1, len(signal) - 1):
        if signal[i-1] < signal[i] > signal[i+1]:
            peaks.append(signal[i])
    return peaks

def compute_entropy(values):
    # Dead function: never used in final path (red herring)
    from math import log
    freq = {}
    for v in values:
        freq[v] = freq.get(v, 0) + 1
    total = len(values)
    entropy = 0.0
    for count in freq.values():
        p = count / total
        entropy -= p * log(p, 2)
    return entropy

def generate_combinations(items):
    # Distractor: creates pairs but unused later
    return list(itertools.combinations(items, 2))

def apply_calibration(peaks):
    # Applies a non-linear transformation to simulate calibration
    calibrated = []
    for p in peaks:
        if p > 20:
            calibrated.append(p * 0.85)
        else:
            calibrated.append(p * 1.1)
    return [round(c, 2) for c in calibrated]

def validate_consistency(calib_vals):
    # Checks if values are within expected bounds (used in filter)
    return all(5 <= v <= 50 for v in calib_vals)

def aggregate_with_weights(vals):
    # Weighted sum using decreasing weights
    weights = [0.5 ** i for i in range(len(vals))]
    weighted_sum = sum(val * weights[i] for i, val in enumerate(vals))
    return round(weighted_sum, 2)

def calculate_final_score(data):
    # Main processing chain
    cleaned = clean_sensor_noise(data)  # Step 1: remove zeros (distractor step)
    raw_peaks = extract_peaks(cleaned)   # Step 2: find local maxima
    
    # Irrelevant combination generation (distractor)
    _ = generate_combinations(raw_peaks)
    
    calibrated_peaks = apply_calibration(raw_peaks)  # Step 3: apply scaling
    
    # Early return if inconsistent (control flow)
    if not validate_consistency(calibrated_peaks):
        return -1
    
    # Only use peaks that were originally above threshold
    filtered_originals = [p for p in raw_peaks if p > 15]  # Step 4: filter
    re_calibrated = apply_calibration(filtered_originals)    # Step 5: reapply calibration
    
    # Use set operations to deduplicate (though no dups here — subtle distractor)
    unique_recal = list(set(re_calibrated))
    sorted_recal = sorted(unique_recal, reverse=True)  # Step 6: sort descending
    
    # Apply weighted aggregation
    score = aggregate_with_weights(sorted_recal)  # Step 7: final computation
    
    # Final adjustment based on length (Step 8)
    adjustment_factor = len(sorted_recal) * 0.9
    final_adjusted = score + adjustment_factor
    
    return round(final_adjusted, 2)

# Extraneous variables (red herrings)
baseline_offset = 3.14159
temp_buffer = [0]*len(data_stream)
diagnostic_log = {'status': 'ok', 'errors': [], 'timestamp': 123456789}

# Real execution path
processed_data = data_stream
final_score = calculate_final_score(processed_data)
print(f"Result: {final_score}")