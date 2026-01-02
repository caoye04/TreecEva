import math

# Simulated sensor data processing system
def collect_diagnostics():
    raw_readings = [127, 255, 18, 93, 204, 77, 142, 63, 241, 50]
    calibration_offset = 17
    gain_factor = 1.08
    temp_buffer = [r + calibration_offset for r in raw_readings]  # Misleading preprocessing
    scaled_values = [round(v * gain_factor) for v in temp_buffer]  # Unused path

    # Actual relevant data filtering
    valid_range = range(100, 256)
    filtered_data = [x for x in raw_readings if x in valid_range]

    # Decoy statistical analysis (never used)
    mean_val = sum(raw_readings) / len(raw_readings)
    variance = sum((x - mean_val) ** 2 for x in raw_readings) / len(raw_readings)
    entropy = sum(- (x/sum(raw_readings)) * math.log2(x/sum(raw_readings)) for x in raw_readings)

    # Key set operations and slicing
    critical_peaks = {255, 241, 204}
    baseline_noise = {18, 50, 77, 93}
    threshold_set = critical_peaks.difference(baseline_noise).union({142})  # {255, 241, 204, 142}

    secondary_mask = filtered_data[1:4]  # Red herring slice
    inverted_slice = filtered_data[::-1][:3]  # Another distraction

    # Bit manipulation decoy
    bit_analysis = []
    for val in raw_readings:
        flipped = ((val << 1) & 255) | (val >> 7)
        bit_analysis.append(flipped ^ 42)

    # Control flow with red herrings
    status_flags = []
    for v in filtered_data:
        if v > 200:
            status_flags.append(1)
        elif v > 150:
            status_flags.append(2)  # This branch activates for 142
        else:
            status_flags.append(0)

    # Unused recursive function (decoy)
    def integrate_recursively(data, idx=0):
        if idx >= len(data):
            return 0
        return data[idx] + 0.98 * integrate_recursively(data, idx+1)

    # Real computation begins here — multiple assignment and destructuring
    primary_count, *secondary_components = filtered_data
    shift_correction = len(secondary_components) % 4

    # Core logic hidden among distractions
    def analyze_readings(data, thresholds):
        count_in_threshold = sum(1 for x in data if x in thresholds)
        total_power = sum(x for x in data if x in thresholds)
        base_metric = count_in_threshold * 1000
        adjustment = abs(total_power - 300) // 10
        return base_metric - adjustment  # Final result depends only on this

    # Critical execution point
    final_diagnostic = analyze_readings(filtered_data, threshold_set)

    # Dead code paths below
    diagnostic_summary = {
        'readings': raw_readings,
        'filtered': filtered_data,
        'flags': status_flags,
        'meta': {'version': '2.1', 'mode': 'diagnostic'}
    }

    # Output requirement
    print(f"Result: {final_diagnostic}")

    return final_diagnostic

# Execute
collect_diagnostics()