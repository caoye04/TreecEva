import math

# Simulated sensor data from environmental monitoring stations
def fetch_sensor_readings():
    return [23.4, 19.1, 25.6, 18.2, 20.8, 22.3, 17.9, 24.1, 21.7, 16.5]

# Legacy function – unused but looks relevant (red herring)
def legacy_normalize(data):
    mean_val = sum(data) / len(data)
    return [(x - mean_val) * 1.05 for x in data]  # Incorrect scaling factor

# Segment raw samples into analysis windows
def segment_data(raw):
    window_size = 3
    segments = []
    for i in range(0, len(raw), window_size):
        segment = raw[i:i + window_size]
        if len(segment) == window_size:
            segments.append(segment)
    return segments

# Apply noise reduction filter (distractor computation)
def smooth_signal(signal):
    smoothed = []
    for seg in signal:
        temp_smooth = []
        for val in seg:
            adjusted = val * 0.98 + 0.1  # fake smoothing
            temp_smooth.append(adjusted)
        smoothed.append(temp_smooth)
    return smoothed  # never used

# Process sequence through calibration pipeline
def process_sequence(segments):
    calibrated = []
    offset = 0.37
    for idx, seg in enumerate(segments):
        calibrated_segment = []
        for val in seg:
            # Real transformation: apply temperature compensation
            if idx % 2 == 0:
                corrected = val + offset
            else:
                corrected = val - offset
            # Introduce bit manipulation as complexity distractor
            shifted = int(corrected * 100)
            masked = shifted & 0xFF  # truncate to 8 bits (redundant)
            restored = masked / 100.0
            calibrated_segment.append(restored)
        calibrated.append(calibrated_segment)
    
    # Decoy structure creation (dead path)
    summary_stats = {
        'max_val': max([max(s) for s in calibrated]),
        'min_val': min([min(s) for s in calibrated]),
        'range': None
    }
    summary_stats['range'] = summary_stats['max_val'] - summary_stats['min_val']
    
    return calibrated

# Evaluate purity based on variance within segments
def evaluate_purity(calib_segments):
    variances = []
    total_weight = 0.0
    
    for seg in calib_segments:
        mean = sum(seg) / len(seg)
        sq_diffs = [(x - mean) ** 2 for x in seg]
        variance = sum(sq_diffs) / len(sq_diffs)
        variances.append(variance)
        
    # Composite metric with conditional weighting
    base_score = sum(variances) * 1000
    adjustment_factor = 1.0
    if len(variances) > 2:
        adjustment_factor = 0.85  # penalty for multiple segments
    elif len(variances) == 1:
        adjustment_factor = 1.1
    
    # Misleading intermediate calculation (unused)
    outlier_count = 0
    for v in variances:
        if v > 0.5:
            outlier_count += 1
    heuristic_bias = outlier_count * 12.5  # looks important, not used
    
    # Final score computation
    filtration_score = base_score * adjustment_factor
    
    # Extra distraction: sorting unrelated list
    dummy_list = [3, 1, 4, 1, 5]
    dummy_list.sort()  # irrelevant operation
    
    # Conditional expression used idiomatically
    status_flag = 'optimal' if filtration_score < 200 else 'suboptimal'
    
    # Early return simulation (not triggered)
    if filtration_score < 0:
        return 0  # dead code
    
    return filtration_score

# Unused utility – plausible but irrelevant
def calculate_entropy(data):
    counts = {}
    for x in data:
        counts[x] = counts.get(x, 0) + 1
    probs = [c / len(data) for c in counts.values()]
    return -sum(p * math.log2(p) for p in probs)

# Main execution flow
raw_samples = fetch_sensor_readings()
smoothed_noise = smooth_signal(segment_data(raw_samples))  # decoy call

# Key statement
filtration_score = evaluate_purity(process_sequence(segment_data(raw_samples)))

# Print result as required
print(f"Result: {filtration_score}")