def analyze_pattern(sequence):
    if not sequence:
        return 0
    peak = max(sequence)
    trough = min(sequence)
    amplitude = peak - trough
    normalized = [round((x - trough) / amplitude * 100) for x in sequence if amplitude != 0]
    return sum(normalized) // len(normalized) if normalized else 0


def validate_readings(readings):
    valid_count = 0
    for val in readings:
        if isinstance(val, float) and 0.0 <= val <= 100.0:
            valid_count += 1
    return valid_count > len(readings) // 2


def calculate_performance(base, data):
    adjustment_factor = 1.0
    temp_result = 0
    outlier_detected = False

    # Simulate preprocessing steps with some irrelevant computation
    filtered_data = [x for x in data if x > base * 0.8]
    squared_offsets = [abs(x - base) ** 2 for x in filtered_data]
    avg_offset_sq = sum(squared_offsets) / len(squared_offsets) if squared_offsets else 0
    std_dev_estimate = avg_offset_sq ** 0.5

    # Irrelevant string-based distractor
    status_msg = "Processing complete".upper().replace(" ", "_")
    log_entry = f"STATUS:{status_msg}:COUNT:{len(data)}"
    entry_length = len(log_entry)

    # Core logic with conditional expression
    performance_ratio = (sum(filtered_data) / len(filtered_data)) / base if filtered_data else 0
    
    # Additional noise: unused intermediate variables
    theoretical_max = base * 1.5
    safety_margin = theoretical_max * 0.1
    compliance_check = "pass" if std_dev_estimate < safety_margin else "fail"

    # Actual score calculation
    raw_score = performance_ratio * 100
    bonus = 10 if performance_ratio >= 1.0 else 0
    penalty = 5 if std_dev_estimate > 15 else 0

    # Final decision with early return possibility (not triggered here)
    if not validate_readings([float(x) for x in filtered_data]):
        return 0

    final_score = raw_score + bonus - penalty  # This will be printed

    return int(final_score)

# Main execution
baseline = 42
readings = [45.0, 49.5, 38.2, 42.1, 50.3, 40.8, 46.7]

# Unused but plausible-looking analysis
pattern_metric = analyze_pattern([int(x) for x in readings])
diagnostic_code = "DGN-" + "-".join([str(int(x) % 10) for x in readings[:3]])

final_score = calculate_performance(baseline, readings)
print(f"Result: {final_score}")