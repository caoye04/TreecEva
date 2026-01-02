def analyze_sensor_data(raw_readings, calibration_sequence):
    # Irrelevant pre-processing: reverse and shift operations on unused copy
    shadow_copy = [x >> 2 for x in raw_readings]
    shadow_copy.reverse()

    # Distractor: complex but unused lambda transformation
    spectral_transform = lambda x: (x ** 3) % 7 if x % 2 else (x >> 1)
    transformed_noise = list(map(spectral_transform, calibration_sequence))

    # Dead path: never invoked function with confusing logic
    def decoy_filter(arr):
        return [a ^ b for a, b in zip(arr, arr[1:] + [arr[0]])]

    # Unused sorting with misleading comment
    sorted_diagnostics = sorted(transformed_noise, reverse=True)  # Not used in final result

    # Actual signal extraction: isolate valid windows above threshold
    valid_windows = []
    for i in range(len(raw_readings) - 3):
        window = raw_readings[i:i+4]
        avg = sum(window) / 4
        if avg > 50:
            valid_windows.append(int(avg))

    # Destructuring assignment with red herring variables
    peak_reading, *mid_tier, baseline_noise = sorted(valid_windows, reverse=True)

    # Bit manipulation distraction: XOR with shifting constants
    mask = 0b1010
    masked_values = [v ^ (mask << 1) & 255 for v in valid_windows]

    # Real computation begins: frequency analysis of high-readings
    frequency_map = {}
    for val in valid_windows:
        frequency_map[val] = frequency_map.get(val, 0) + 1

    # Use enumerate to track first occurrence over 60
    trigger_index = -1
    for idx, val in enumerate(valid_windows):
        if val > 60:
            trigger_index = idx
            break

    # Critical data pipeline: cumulative corrections based on frequency
    aggregate_metrics = []
    running_total = 0
    for freq in frequency_map.values():
        running_total += freq * 3
        aggregate_metrics.append(running_total)

    # Decoy arithmetic chain with no effect
    temp_accum = 0
    for _ in range(3):
        temp_accum += (temp_accum + 7) * 2
    temp_accum = temp_accum % 100  # Never used

    # Correction factor derived from calibration parity
    total_parity = sum(calibration_sequence) % 2
    correction_factor = 17 if total_parity else -8

    # Final diagnostic computed from last metric and parity-based correction
    final_diagnostic = aggregate_metrics[-1] + correction_factor

    # Print required output
    print(f"Result: {final_diagnostic}")

    # Return unused metrics to encourage misdirection
    return {
        'peak': peak_reading,
        'noise_floor': baseline_noise,
        'diagnostic_trace': aggregate_metrics,
        'irrelevant_flag': temp_accum
    }

# Inputs
sensor_readings = [45, 52, 58, 63, 54, 70, 68, 48, 55, 72]
calibration_codes = [12, 18, 24, 30]

# Execution
result = analyze_sensor_data(sensor_readings, calibration_codes)