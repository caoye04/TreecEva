import math

# Simulated sensor data processing with embedded diagnostics
def collect_readings():
    raw_samples = [0.88, -0.12, 0.45, 1.23, -0.67, 0.09, 0.34, -0.22]
    scale_factor = 2.5
    adjusted = [round(x * scale_factor, 3) for x in raw_samples]
    return adjusted

# Irrelevant auxiliary function - dead code path
def deprecated_filter(data):
    filtered = []
    for x in data:
        if x > 1.0:
            filtered.append(x * 0.9)
    return filtered  # never called

# Signal conditioning with red herring transformations
def clean_signal(raw):
    offset = 0.5
    noise_floor = 0.05
    cleaned = []
    temp_stats = {'sum_sq': 0, 'count_above': 0}
    
    for val in raw:
        shifted = val + offset
        if abs(shifted) > noise_floor:
            cleaned.append(shifted ** 2)  # non-linear transformation
        else:
            cleaned.append(0)
        
        # Distractor computation - not used later
        temp_stats['sum_sq'] += val ** 2
        if val > 0.2:
            temp_stats['count_above'] += 1

    # Misleading normalization (unused)
    if temp_stats['sum_sq'] > 0:
        normalized_power = sum(cleaned) / temp_stats['sum_sq']
    else:
        normalized_power = 0
        
    return cleaned

# Data windowing - actual relevant step
def segment_data(signal):
    window_size = 4
    segments = []
    for i in range(0, len(signal), window_size):
        segment = signal[i:i+window_size]
        if len(segment) == window_size:
            segments.append(segment)
    return segments  # only full windows kept

# Decoy analysis function with plausible but unused metrics
def superficial_insight(segments):
    insights = []
    for seg in segments:
        peak = max(seg)
        avg = sum(seg) / len(seg)
        variance = sum((x - avg) ** 2 for x in seg) / len(seg)
        # These are computed but not returned or used
        zcr = sum(1 for i in range(1, len(seg)) if seg[i]*seg[i-1] < 0)
        spectral_centroid = sum(i * seg[i] for i in range(len(seg))) / sum(seg) if sum(seg) != 0 else 0
        insights.append({'peak': peak, 'avg': avg, 'var': variance})
    return []  # deliberately returns empty

# Core diagnostic logic - depends on correct data flow
def analyze_signal(segments):
    accumulation = 0
    weights = [0.1, 0.2, 0.3, 0.4]
    
    # Real computation: weighted sum of first segment
    if segments:
        first_segment = segments[0]
        for i in range(len(first_segment)):
            accumulation += first_segment[i] * weights[i]
    
    # Multiple irrelevant variables
    baseline_reference = 127
    calibration_flag = True
    historical_offset = -0.0034
    debug_checksum = sum(int(s*100) for s in first_segment) % 100
    
    # String-based decoy identifier
    status_tag = "DIAG_OK"
    if accumulation > 1.5:
        status_tag += "_HIGH"
    else:
        status_tag += "_LOW"
    
    # Final result derived from real computation
    final_diagnostic = int(round(accumulation * 1000)) + len(status_tag)
    
    # Unused complex transformation
    binary_rep = bin(baseline_reference)[2:]
    parity_check = binary_rep.count('1') % 2
    
    return final_diagnostic

# Orchestration with misleading intermediate prints
if __name__ == "__main__":
    readings = collect_readings()
    cleaned = clean_signal(readings)
    segmented = segment_data(cleaned)
    fake_insights = superficial_insight(segmented)  # no effect
    
    # Key execution point
    final_diagnostic = analyze_signal(segmented)
    
    # Print required output
    print(f"Result: {final_diagnostic}")