import math

# Simulated sensor data processing with diagnostic analysis
def collect_sensor_readings():
    raw_samples = [0.8, -1.2, 3.5, 2.1, -0.4, 4.8, 1.9, -2.3]
    baseline = 1.5
    normalized = [(x - baseline) * 1.8 for x in raw_samples]
    return normalized

# Irrelevant helper: calculates unused statistical moment
def calculate_skewness(data):
    n = len(data)
    mean_val = sum(data) / n
    variance = sum((x - mean_val) ** 2 for x in data) / n
    if variance == 0:
        return 0
    skew = sum((x - mean_val) ** 3 for x in data) / n
    return skew / (variance ** 1.5) if variance > 0 else 0

# Distraction function: operates on decoy data
def legacy_filter_chain(signal):
    if not signal:
        return []
    filtered = []
    for x in signal:
        if x > 1.0:
            filtered.append(x * 0.9)
        elif x < -1.0:
            filtered.append(x * 0.7)
    # This function is called but its result ignored
    return filtered

# Core transformation pipeline
def preprocess_signal(raw):
    shifted = [x + 0.5 for x in raw]
    amplified = [x * 2.3 for x in shifted]
    clipped = [min(max(x, -3.0), 5.0) for x in amplified]  # Clamp range
    return clipped

# Data segmentation using slicing - relevant operation
def segment_data(stream):
    mid = len(stream) // 2
    first_half = stream[:mid]
    second_half = stream[mid:]
    # Only second half is used in actual computation
    return first_half, second_half

# Recursive frequency counter (simple recursion over list)
def count_peaks(values, idx=0):
    if idx >= len(values):
        return 0
    is_peak = (idx == 0 or values[idx] > values[idx-1]) and \
               (idx == len(values)-1 or values[idx] > values[idx+1])
    return (1 + count_peaks(values, idx + 1)) if is_peak else count_peaks(values, idx + 1)

# Conditional transformation based on pattern detection
def detect_anomaly_pattern(seq):
    if len(seq) < 3:
        return False
    # Look for rising-falling-rising triplet
    for i in range(len(seq) - 2):
        if seq[i] < seq[i+1] > seq[i+2] and seq[i+2] > seq[i]:
            return True
    return False

# Main analysis engine
def analyze_signal(data_segment):
    # Apply conditional expression based on length
    working_buffer = data_segment if len(data_segment) % 2 == 0 else data_segment[1:]
    
    # Bit manipulation red herring
    magic_offset = (0b1011 ^ 0b1101) & 0b1111  # evaluates to 6, unused later
    
    # Decoy variables with plausible names
    calibration_factor = 1.07
    stability_ratio = 0.94
    entropy_metric = sum(math.log(abs(x) + 1) for x in working_buffer)
    
    # Real computation begins
    positive_count = sum(1 for x in working_buffer if x > 0)
    negative_total = sum(x for x in working_buffer if x < 0)
    
    # Slicing used meaningfully: analyze trend in last three elements
    recent_trend = 0
    if len(working_buffer) >= 3:
        tail = working_buffer[-3:]
        for i in range(1, len(tail)):
            if tail[i] > tail[i-1]:
                recent_trend += 1
            elif tail[i] < tail[i-1]:
                recent_trend -= 1
    
    # Linear search for first significant drop
    threshold = max(working_buffer) * 0.6
    first_drop_index = -1
    for i in range(1, len(working_buffer)):
        if working_buffer[i] < working_buffer[i-1] and working_buffer[i] < threshold:
            first_drop_index = i
            break
    
    # Key computation: composite diagnostic score
    peak_count = count_peaks(working_buffer)
    pattern_detected = detect_anomaly_pattern(working_buffer)
    
    # Final formula: combines multiple concepts
    base_score = positive_count * 7.3
    base_score -= abs(negative_total) * 1.8
    base_score += recent_trend * 4.2
    if pattern_detected:
        base_score += 15.0
    if first_drop_index != -1:
        base_score -= first_drop_index * 0.9
    
    # Distractor: unused normalization
    normalized_score = base_score / (1 + abs(entropy_metric)) if entropy_metric != 0 else base_score
    
    # Final diagnostic is only this one
    final_diagnostic = int(base_score + peak_count * 3.1)
    
    # Dead code path: never executed due to constant condition
    if False:
        fallback = math.ceil(normalized_score)
        return fallback
        
    return final_diagnostic

# Entry point
if __name__ == "__main__":
    # Step 1: Collect raw data
    raw_data = collect_sensor_readings()
    
    # Step 2: Preprocess signal (relevant)
    processed_data = preprocess_signal(raw_data)
    
    # Step 3: Segment data using slicing (relevant use)
    _, active_segment = segment_data(processed_data)
    
    # Step 4: Run legacy filter (result ignored - distraction)
    legacy_output = legacy_filter_chain(active_segment)
    
    # Step 5: Calculate irrelevant skewness (distraction)
    unused_skew = calculate_skewness(active_segment)
    
    # Step 6: Analyze signal - key execution point
    final_diagnostic = analyze_signal(active_segment)
    
    # Output target result
    print(f"Target result: {final_diagnostic}")