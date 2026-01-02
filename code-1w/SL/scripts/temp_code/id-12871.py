import math

# Simulated sensor array data processing with diagnostic logic
def main():
    raw_readings = [3.2, 4.5, 6.7, 2.1, 9.8, 4.4, 3.3, 7.6]
    calibration_factor = 1.05
    baseline_offset = 0.25
    temporal_weight = 0.8
    decay_rate = 0.92

    # Irrelevant transformation (distractor)
    normalized = [math.log(x + 1) for x in raw_readings]
    inverted = [1.0 / (x + 0.1) for x in normalized]

    # Core signal processing
    adjusted = [round((x * calibration_factor) + baseline_offset, 2) for x in raw_readings]

    # Statistical summary (some used, some not)
    mean_val = sum(adjusted) / len(adjusted)
    variance = sum((x - mean_val) ** 2 for x in adjusted) / len(adjusted)
    stdev = math.sqrt(variance)
    median_val = sorted(adjusted)[len(adjusted)//2]

    # Unused statistical measures (dead code path)
    if stdev > 2.0:
        outlier_score = sum(1 for x in adjusted if abs(x - mean_val) > 2 * stdev)
    else:
        outlier_score = 0  # Never actually used

    # Data windowing
    window_size = 3
    rolled = [adjusted[i:i+window_size] for i in range(len(adjusted)-window_size+1)]
    smoothed = [round(sum(window)/window_size, 2) for window in rolled]

    # Red herring: complex frequency simulation
    freq_components = []
    for i in range(len(smoothed)):
        component = smoothed[i] * math.sin(i * math.pi / 4)
        freq_components.append(round(component, 3))
    spectral_energy = sum(x**2 for x in freq_components)

    # Actual relevant processing path
    processed_data = [x for x in adjusted if x > mean_val - 0.5 * stdev]

    # Decoy function that looks important but isn't called
    def predict_failure(data):
        return sum(math.exp(-x) for x in data) < 0.1

    # Threshold logic using lambda (required feature)
    threshold_func = lambda x: x > (mean_val + 0.75 * stdev)

    # String-based mode classifier (irrelevant but plausible)
    mode_labels = ['low', 'medium', 'high', 'critical']
    status_str = "sensor_status:v2"
    version = int(status_str.split(':')[1][1:]) if ':' in status_str else 1
    mode_index = min(int(mean_val) % 4, 3)
    operating_mode = mode_labels[mode_index].upper()

    # Diagnostic engine with branching logic
    def analyze_readings(data, threshold_fn):
        above_threshold = list(filter(threshold_fn, data))
        below_count = len(data) - len(above_threshold)
        
        # Bit manipulation red herring
        flag_register = 0
        for val in data:
            shifted = int(val * 10) << 1
            flag_register ^= shifted
            flag_register &= 0xFFFF  # Keep within 16 bits
        
        # Destructuring assignment (relevant concept)
        first, *middle, last = sorted(data)
        spread = last - first
        
        # Complex conditional with short-circuit evaluation
        if operating_mode == 'CRITICAL' and len(above_threshold) > 2 or \
           (spread > 5.0 and below_count == 0):
            level = 3
        elif len(above_threshold) >= 3:
            level = 2
        elif len(above_threshold) == 1 and mean_val > 5.0:
            level = 1
        else:
            level = 0
        
        # Final computation with summation and rounding
        base_score = sum(math.ceil(x) for x in above_threshold)
        penalty = max(0, 4 - len(above_threshold)) * 2
        raw_diagnostic = base_score - penalty
        
        # Final adjustment using string method (required feature)
        key_suffix = f"{raw_diagnostic:.1f}".split('.')[-1]
        suffix_value = int(key_suffix) if key_suffix.isdigit() else 0
        
        final_score = raw_diagnostic + (suffix_value * 0.1)
        
        # Dead code: complex state machine never executed
        states = {'init': 0, 'active': 1, 'alert': 2}
        transitions = []
        for k, v in states.items():
            transitions.append(f"{k}->{v}")
        
        return round(final_score, 1)

    # Critical execution point
    final_diagnostic = analyze_readings(processed_data, threshold_func)
    
    # Output requirement
    print(f"Result: {final_diagnostic}")

if __name__ == "__main__":
    main()