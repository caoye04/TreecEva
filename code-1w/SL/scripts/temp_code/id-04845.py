import math

# Simulated sensor data processing with noise filtering and pattern detection
def main():
    raw_readings = [145, 176, 201, 180, 255, 90, 130, 160, 190, 220, 240, 110, 150]
    calibration_offsets = [5, -3, 0, -10, 8, 0, 2, -4, 1, 0, -2, 3, -1]
    base_thresholds = [150, 170, 180, 160, 200, 100, 140, 155, 185, 210, 230, 120, 145]
    
    # Irrelevant transformation: frequency weights (not used in final path)
    freq_weights = [0.88, 0.91, 0.94, 0.85, 1.02, 0.77, 0.83, 0.89, 0.95, 0.99, 1.05, 0.80, 0.84]
    weighted_spectrum = [raw_readings[i] * freq_weights[i] for i in range(len(raw_readings))]
    avg_weighted = sum(weighted_spectrum) / len(weighted_spectrum)

    # Apply calibration (relevant)
    corrected_readings = [raw_readings[i] + calibration_offsets[i] for i in range(len(raw_readings))]

    # Noise reduction filter: moving average of window size 3 (relevant)
    smoothed_readings = []
    for i in range(1, len(corrected_readings) - 1):
        avg_val = (corrected_readings[i-1] + corrected_readings[i] + corrected_readings[i+1]) / 3
        smoothed_readings.append(int(avg_val))
    
    # Decoy smoothing method (dead code)
    def gaussian_smooth(data, sigma=1.0):
        kernel = [0.25, 0.5, 0.25]
        result = []
        for i in range(1, len(data) - 1):
            val = data[i-1]*kernel[0] + data[i]*kernel[1] + data[i+1]*kernel[2]
            result.append(round(val))
        return result
    
    # Identify high-variance segments (distractor)
    variance_flags = []
    for i in range(len(smoothed_readings) - 2):
        window = smoothed_readings[i:i+3]
        mean_win = sum(window) / 3
        var = sum((x - mean_win)**2 for x in window) / 3
        variance_flags.append(var > 25)

    # Map thresholds by environment mode (relevant)
    mode = 'high_sensitivity'
    threshold_map = {}
    for idx, base in enumerate(base_thresholds):
        if mode == 'low_power':
            threshold_map[idx] = base - 20
        elif mode == 'balanced':
            threshold_map[idx] = base
        else:  # high_sensitivity
            threshold_map[idx] = max(100, base - 35)

    # Filter data above dynamic thresholds (relevant)
    filtered_data = []
    for i, val in enumerate(smoothed_readings):
        if i + 1 in threshold_map and val > threshold_map[i + 1]:  # offset alignment
            filtered_data.append({'index': i, 'value': val, 'original_idx': i + 1})

    # Decoy classification system (unused)
    def classify_pattern(seq):
        if len(seq) < 3:
            return 'UNSTABLE'
        diffs = [seq[i+1] - seq[i] for i in range(len(seq)-1)]
        if all(d > 0 for d in diffs):
            return 'ASCENDING'
        elif all(d < 0 for d in diffs):
            return 'DESCENDING'
        return 'OSCILLATING'

    # Signal processor using bit flags and summation logic (key relevant function)
    def process_signals(signals, thresh_lookup):
        cumulative_score = 0
        activation_flags = 0
        
        for entry in signals:
            idx = entry['original_idx']
            value = entry['value']
            
            # Bitwise flag assignment based on modulo pattern
            if value % 4 == 0:
                activation_flags |= (1 << (idx % 8))
            elif value % 5 == 0:
                activation_flags ^= (1 << ((idx + 3) % 8))
            
            # Scoring logic with integer division and accumulation
            base_points = value // 10
            bonus = 1 if value > thresh_lookup[idx] + 10 else 0
            penalty = 0
            
            # Additional check using enumerate and zip (required python feature)
            context_window = smoothed_readings[max(0, idx-2):idx+1]
            for i, ctx_val in enumerate(context_window):
                if i > 0:
                    ratio = ctx_val / context_window[i-1] if context_window[i-1] != 0 else 1
                    if 0.9 <= ratio <= 1.1:
                        bonus += 0.5

            # Accumulate score with rounding
            step_score = base_points + bonus - penalty
            cumulative_score += round(step_score)
        
        # Final transformation using bit count and arithmetic
        flag_count = bin(activation_flags).count('1')
        final_value = cumulative_score * 100 + flag_count * 10
        
        # Dead computation branch (misleading)
        if flag_count > 5:
            temp_debug = math.log(flag_count) * 1000
            temp_debug = int(temp_debug)  # unused
            
        return final_value

    # Execution point of interest
    final_output = process_signals(filtered_data, threshold_map)
    
    # Red herring: secondary analysis (never used)
    anomaly_tracker = []
    for i, val in enumerate(smoothed_readings):
        if val > 200:
            anomaly_tracker.append({'pos': i, 'level': 'CRITICAL'})
        elif val > 170:
            anomaly_tracker.append({'pos': i, 'level': 'WARNING'})
    
    # Output result as required
    print(f"Result: {final_output}")

if __name__ == "__main__":
    main()