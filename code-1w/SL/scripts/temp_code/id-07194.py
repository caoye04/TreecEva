import itertools

# Simulate multi-sensor diagnostic signal analysis with noise filtering
def preprocess_signals(raw_signals):
    filtered = []
    noise_floor = 0.1
    for idx, val in enumerate(raw_signals):
        adjusted = val - noise_floor
        if abs(adjusted) > 0.05:
            filtered.append(round(adjusted, 4))
    return filtered

# Identify repeating pattern cycles in cleaned signal
def detect_cycles(seq):
    cycle_length = 0
    for i in range(1, min(6, len(seq)//2 + 1)):
        is_repeating = all(seq[j] == seq[j % i] for j in range(len(seq)))
        if is_repeating:
            cycle_length = i
            break
    return cycle_length

# Analyze signal against threshold bands to compute diagnostic metric
def analyze_signal_patterns(data, limits):
    high_pass, low_pass = limits[0], limits[1]
    band_filtered = [x for x in data if low_pass <= x <= high_pass]
    
    # Irrelevant intermediate: count transitions (not used in final result)
    transitions = 0
    temp_state = False
    for val in data:
        if val > 0.5 and not temp_state:
            transitions += 1
            temp_state = True
        elif val <= 0.5:
            temp_state = False
    
    # Key logic: use bitwise combination of statistical properties
    avg_val = sum(band_filtered) / len(band_filtered) if band_filtered else 0
    peak = max(band_filtered) if band_filtered else 0
    base_index = int(avg_val * 100)
    
    # Distractor computation: unused frequency analysis
    freq_counter = {}
    for v in band_filtered:
        rounded = round(v, 2)
        freq_counter[rounded] = freq_counter.get(rounded, 0) + 1
    dominant_freq = max(freq_counter.values()) if freq_counter else 0
    
    # Real computation path
    stability_score = 0
    sorted_vals = sorted(band_filtered)
    for a, b in zip(sorted_vals, sorted_vals[1:]):
        if abs(a - b) < 0.05:
            stability_score += 1
    
    # Combine using XOR and shifts - core of actual answer
    raw_metric = (base_index << 1) ^ stability_score
    scaled_metric = raw_metric * 0.75
    
    # Final diagnostic uses only scaled_metric and peak adjustment
    adjustment = int(peak * 10)
    final_diagnostic = int(scaled_metric) + adjustment
    
    # Dead code branch - never executed due to fixed input
    if len(data) > 1000:
        fallback = sum(itertools.chain(data))
        final_diagnostic = fallback % 100
        
    return final_diagnostic

# Main execution
if __name__ == "__main__":
    # Input data: synthetic sensor readings
    raw_input = [
        0.12, 0.15, 0.23, 0.23, 0.31, 0.32, 0.23, 0.23,
        0.45, 0.44, 0.46, 0.45, 0.51, 0.52, 0.51, 0.50
    ]
    
    # Irrelevant auxiliary data structure
    calibration_map = dict(zip(['c1','c2','c3'], [0.01, 0.02, 0.03]))
    baseline_offset = sum(calibration_map.values())
    
    processed = preprocess_signals(raw_input)
    cycle_len = detect_cycles(processed)
    
    # Unused transformation: Fourier-like dummy operation
    fourier_dummies = []
    for k in range(3):
        dummy_sum = 0
        for n, x in enumerate(processed):
            dummy_sum += x * (-1)**(k*n)
        fourier_dummies.append(round(dummy_sum, 3))
    
    # Thresholds for band-pass filter
    config_thresholds = (0.48, 0.22)
    
    # Critical execution point
    final_diagnostic = analyze_signal_patterns(processed, config_thresholds)
    
    # Output result as required
    print(f"Target result: {final_diagnostic}")