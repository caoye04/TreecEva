import math

# Simulated sensor network diagnostic system
def collect_diagnostics():
    raw_readings = [23.4, 19.5, 20.1, 25.3, 18.7, 22.0, 19.8, 24.6]
    calibration_offset = 1.2
    adjusted_readings = [r + calibration_offset for r in raw_readings]

    # Irrelevant temperature conversions (distractor)
    kelvin_values = [temp + 273.15 for temp in raw_readings]
    kelvin_filtered = [k for k in kelvin_values if k > 290]

    # Misleading statistical computation (red herring)
    mean_raw = sum(raw_readings) / len(raw_readings)
    variance = sum((x - mean_raw) ** 2 for x in raw_readings) / len(raw_readings)
    std_dev = math.sqrt(variance)

    # Dead code path - never executed (decoy)
    def deprecated_analysis(data):
        return sum(data) % 7

    # Unused transformation
    normalized = [round((v - min(adjusted_readings)) / 
                        (max(adjusted_readings) - min(adjusted_readings)), 3) 
                  for v in adjusted_readings]

    # Real processing begins here - relevant logic
    outlier_threshold = mean_raw + 1.5 * std_dev
    filtered_during_process = [val for val in adjusted_readings if val < outlier_threshold]

    # Simulate packet loss compensation
    recovery_factor = 0.9
    recovered_logs = [log * recovery_factor for log in filtered_during_process]

    # Critical: Only values above 20.5 are valid operational readings
    valid_mask = [1 if x > 20.5 else 0 for x in recovered_logs]
    total_valid_count = sum(valid_mask)

    # Secondary filter based on divisibility (bitwise distraction)
    checksum = 0
    for i, val in enumerate(recovered_logs):
        if valid_mask[i]:
            checksum ^= int(val)  # Use integer part for bit manipulation

    # Hidden rule: final value depends on count and checksum interaction
    processed_logs = {
        'readings': recovered_logs,
        'valid_count': total_valid_count,
        'checksum': checksum,
        'base_origin': 'sector_7'
    }

    return processed_logs


def analyze_readings(log_data):
    readings = log_data['readings']
    valid_count = log_data['valid_count']
    checksum = log_data['checksum']

    # Complex conditional expression chain (short-circuit red herring)
    fallback_correction = 5 if (valid_count > 3 and checksum < 50) or len(readings) == 0 else 2

    # Irrelevant formatting routine (dead code)
    def format_for_display(data_list):
        return [f'{val:.1f}U' for val in data_list]

    # Another decoy function
    def compute_entropy(values):
        from collections import Counter
        counts = Counter([int(v) for v in values])
        total = len(values)
        return -sum((count/total) * math.log2(count/total) for count in counts.values())

    # Actual diagnostic logic
    adjustment_curve = [math.sin(math.pi * i / (len(readings) + 1)) for i in range(1, len(readings)+1)]
    weighted_sum = sum(r * w for r, w in zip(readings, adjustment_curve))

    # Key inference step: combine valid_count with weighted_sum
    intermediate_diagnostic = weighted_sum * valid_count

    # Final obfuscation: use checksum to determine offset
    if checksum % 2 == 0:
        final_diagnostic = int(intermediate_diagnostic - checksum)
    else:
        final_diagnostic = int(intermediate_diagnostic + checksum)

    # Print required output
    print(f"Result: {final_diagnostic}")
    return final_diagnostic

# Execution flow
if __name__ == "__main__":
    collected = collect_diagnostics()
    final_diagnostic = analyze_readings(collected)