import itertools

def preprocess_segment(segment):
    smoothed = [sum(segment[i:i+3]) / 3 for i in range(len(segment) - 2)]
    normalized = [(x - min(smoothed)) / (max(smoothed) - min(smoothed) + 1e-8) for x in smoothed]
    return normalized

def generate_harmonic_pattern(n):
    # Irrelevant function: generates harmonic series but not used in main logic
    return [1/i for i in range(1, n+1)]

def calculate_entropy(data):
    from collections import Counter
    counts = Counter(data)
    total = len(data)
    entropy = -sum((count/total) * (count/total).__log__(2) for count in counts.values())
    return entropy

def filter_outliers(values, factor=1.5):
    # Dead code path — never called
    q1, q3 = sorted(values)[len(values)//4], sorted(values)[-len(values)//4]
    iqr = q3 - q1
    return [v for v in values if q1 - factor*iqr <= v <= q3 + factor*iqr]

def rolling_window_stats(seq, window_size=3):
    if len(seq) < window_size:
        return []
    windows = list(itertools.windowed(seq, window_size))
    averages = [sum(w)/len(w) for w in windows if None not in w]
    variances = [sum((x - sum(w)/len(w))**2 for x in w) / len(w) for w in windows if None not in w]
    return list(zip(averages, variances))

def validate_calibration(signal):
    # Distractor function: looks important but unused
    baseline = signal[:len(signal)//2]
    test_seg = signal[len(signal)//2:]
    return abs(sum(baseline) - sum(test_seg)) < 0.5

def build_lookup_map(keys, default_val=1.0):
    # Unused helper — red herring
    return {k: default_val for k in keys}

def analyze_signal_quality(raw_buffer, threshold):
    # Main relevant logic starts here
    segments = [raw_buffer[i:i+5] for i in range(0, len(raw_buffer), 5) if len(raw_buffer[i:i+5]) == 5]
    
    processed_segments = []n    temp_diagnostics = []
    
    for seg in segments:
        # Apply preprocessing
        clean_seg = preprocess_segment(seg)
        
        # Compute signal energy
        energy = sum(x**2 for x in clean_seg)
        
        # Compute zero-crossing rate
        zero_crossings = sum(1 for i in range(1, len(clean_seg)) if clean_seg[i]*clean_seg[i-1] < 0)
        zcr = zero_crossings / len(clean_seg)
        
        # Evaluate quality metrics
        if energy > 0.1 and zcr > 0.2:
            temp_diagnostics.append(1)
        else:
            temp_diagnostics.append(0)
    
    # Simulate redundant validation
    validation_mask = [1 if d == 1 else 0 for d in temp_diagnostics]
    
    # Final decision logic
    if sum(temp_diagnostics) / len(temp_diagnostics) >= threshold:
        result_code = 42  # High quality
    else:
        result_code = -17  # Low quality
    
    # Introduce decoy calculation
    dummy_calc = sum(abs(a - b) for a, b in itertools.combinations(temp_diagnostics, 2))
    scaling_factor = len(temp_diagnostics) % 4 or 1
    fake_score = (dummy_calc * 1.75) / (scaling_factor + 1)
    
    # This is the actual answer path
    final_diagnostic = result_code * 2 + int(round(fake_score))
    
    # Never reached — dead code to mislead control flow analysis
    if False:
        fallback = calculate_entropy(temp_diagnostics)
        final_diagnostic = int(fallback * 100)
    
    return final_diagnostic

# --- Entry point ---
if __name__ == "__main__":
    # Simulated sensor data buffer (real input)
    diagnostic_buffer = [
        0.1, 0.6, 0.8, 0.3, 0.2,
        0.5, 0.7, 0.9, 0.4, 0.1,
        0.2, 0.8, 0.6, 0.7, 0.3,
        0.9, 0.1, 0.4, 0.8, 0.5,
        0.6, 0.7, 0.2, 0.3, 0.8
    ]
    
    # Irrelevant string processing — distractor using required feature
    log_tag = "SENS-DIA-2024"
    tags = [log_tag[0:4], log_tag[4:8], log_tag[8:]]
    formatted_tags = [t.lower().strip("-") for t in tags]
    tag_count = len(''.join(formatted_tags))
    
    # Another decoy list using itertools
    index_pairs = list(itertools.combinations(range(4), 2))
    pair_sum_metric = sum(a + b for a, b in index_pairs)
    
    # Critical execution point
    final_diagnostic = analyze_signal_quality(diagnostic_buffer, threshold=0.75)
    
    # Output result as required
    print(f"Result: {final_diagnostic}")