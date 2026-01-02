import itertools

# Simulated sensor array diagnostics with red herrings
def analyze_sensor_array(raw_readings, calibration_offset=0.1):
    processed = []
    temp_cache = {}
    for idx, val in enumerate(raw_readings):
        adjusted = val + calibration_offset
        if idx % 3 == 0:
            adjusted *= 1.05
        elif idx % 4 == 0:
            adjusted -= 0.5
        processed.append(round(adjusted, 4))
    
    # Distractor: unused transformation path
    outlier_check = [x for x in processed if x > 100]
    if len(outlier_check) > 5:
        smoothed = [x * 0.9 for x in processed]
    else:
        smoothed = [x * 1.1 for x in processed]  # Dead code branch (not used)
    
    return processed

# Irrelevant utility function (decoy)
def compute_entropy(sequence):
    from math import log
    freq_map = {}
    for item in sequence:
        freq_map[item] = freq_map.get(item, 0) + 1
    total = len(sequence)
    entropy = 0
    for count in freq_map.values():
        p = count / total
        entropy -= p * log(p, 2)
    return round(entropy, 4)

# Core logic buried among distractions
def evaluate_trend_series(data_stream):
    # Apply windowed slicing and transformations
    window_size = 4
    trend_segments = []
    for i in range(0, len(data_stream) - window_size + 1, 2):
        segment = data_stream[i:i + window_size]
        avg = sum(segment) / len(segment)
        trend_segments.append(round(avg, 3))
    
    # Misleading intermediate calculation (unused)
    peak_magnitude = max(trend_segments) - min(trend_segments)
    normalized_peaks = [p / peak_magnitude for p in trend_segments if peak_magnitude != 0]
    
    # Actual relevant transformation
    filtered_trends = [t for t in trend_segments if t > 48.0]
    return filtered_trends

# Weighted aggregation with bit manipulation decoys
def apply_signal_mask(weights, mask_level=6):
    masked_weights = []
    for w in weights:
        # Bitwise red herring
        binary_rep = bin(int(w * 100))[2:]
        if len(binary_rep) > mask_level:
            shifted = int(binary_rep[:-1], 2) / 100.0
        else:
            shifted = w
        masked_weights.append(shifted)
    return masked_weights

# Main diagnostic aggregator
def aggregate_metrics(trends, weight_vector):
    # Use zip to align trend data with weights
    paired = list(zip(trends, weight_vector))
    
    # Dead code: unused permutation analysis
    perm_count = 0
    for _ in itertools.permutations(trends[:3]):
        perm_count += 1  # Distractor: no impact on result
    
    # Real computation
    products = [t * w for t, w in paired]
    base_score = sum(products)
    
    # Secondary adjustment using enumerate
    adjustment = 0
    for i, val in enumerate(products):
        if i % 2 == 1:
            adjustment += val * 0.1
    
    final_score = base_score + adjustment
    return round(final_score, 6)

# Simulated input data
sensor_input = [45.2, 47.1, 49.8, 51.3, 46.7, 53.2, 50.4, 48.9, 52.6, 54.1]
weights = [0.1, 0.15, 0.2, 0.25, 0.3]  # Mismatched length will be handled by zip

# Irrelevant preprocessing chain
calibrated = analyze_sensor_array(sensor_input, 0.05)
entropy_value = compute_entropy(calibrated[:6])

# Key processing steps
preliminary_trends = evaluate_trend_series(calibrated)
masked_weights = apply_signal_mask(weights, 5)

# Critical statement
final_diagnostic = aggregate_metrics(preliminary_trends, masked_weights)

print(f"Result: {final_diagnostic}")