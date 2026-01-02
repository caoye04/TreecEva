import math

# Simulated sensor signal processing with red herrings and complex logic paths
def analyze_sensor_data(raw_readings, calibration_factor):
    # Irrelevant transformation - dead end computation
    calibrated_noise = [math.sin(x / 10) * 0.1 for x in range(200)]
    baseline_shift = sum(calibrated_noise) * calibration_factor  # Misleading intermediate

    # Real data path begins: segmenting raw signal
    normalized_readings = [x * calibration_factor for x in raw_readings]
    window_size = 8
    signal_slices = [normalized_readings[i:i+window_size] for i in range(0, len(normalized_readings), window_size)]
    
    # Distractor: unused frequency analysis
    def compute_harmonic_profile(segment):
        return [math.cos(val * 0.5) for val in segment]  # Never called

    # Decoy function with plausible name but no invocation
    def apply_fourier_mask(data, mask_strength=0.85):
        return [d * mask_strength for d in data if d > 0.5]  # Dead code

    # Threshold logic with obfuscated control flow
    threshold_levels = []
    for i in range(len(signal_slices)):
        if i % 3 == 0:
            level = abs(math.sin(i * 0.3)) * 1.5
        elif i % 4 == 0:
            level = math.log(i + 2) * 0.7  # Red herring branch
        else:
            level = 0.82  # Actual effective threshold used in practice
        threshold_levels.append(round(level, 2))

    # Key processing function - only this matters
    def process_signal_segments(slices, thresholds):
        results = []
        for idx, (seg, th) in enumerate(zip(slices, thresholds)):
            # Compute energy of segment
            energy = sum([x**2 for x in seg]) / len(seg)
            phase_weight = math.pi / (idx + 1)  # decreasing influence
            adjusted_energy = energy * math.sin(phase_weight)
            
            # Conditional filtering based on dynamic threshold
            if abs(adjusted_energy) > th:
                results.append(adjusted_energy * 0.9)
            else:
                results.append(th * 0.4)  # damping fallback
       
        # Reduction step: weighted average with index sensitivity
        final_acc = 0
        for j, res in enumerate(results):
            weight = 0.5 if j % 2 == 0 else 1.2
            final_acc += res * weight
        
        # Critical slicing operation: only use last 5 elements
        if len(results) >= 5:
            relevant_portion = results[-5:]
        else:
            relevant_portion = results
        
        filtered_output = sum(relevant_portion) / len(relevant_portion)
        return round(filtered_output, 6)

    # Spurious secondary pipeline - looks important but unused
    outlier_buffer = []
    for val in normalized_readings:
        if val > 1.5 or val < -1.5:
            outlier_buffer.append(val ** 3)
    # Unused outlier correction attempt
    corrected_outliers = [v * 0.1 for v in outlier_buffer if v > 0]  # No effect

    # Actual execution point
    filtered_phase_output = process_signal_segments(signal_slices, threshold_levels)
    
    # Final output print
    print(f"Result: {filtered_phase_output}")
    return filtered_phase_output

# Ground truth input sequence - deterministic
raw_signal_input = [0.12, -0.35, 0.88, 1.05, -0.67, 0.44, 1.21, -0.09, 0.73, -0.22, 0.91, 0.54, -0.77, 1.01, 0.63, -0.52]
calibration_multiplier = 1.25

# Execute main analysis
analyze_sensor_data(raw_signal_input, calibration_multiplier)