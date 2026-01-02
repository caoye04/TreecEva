import math

def preprocess_sensor_data(raw):
    cleaned = []
    offset = 0.5
    scaling_factor = 2.0  # Unused in final logic, distractor
    for val in raw:
        if val < 0:
            adjusted = abs(val) + offset
        else:
            adjusted = val * 1.1  # Minor adjustment, not critical
        cleaned.append(round(adjusted))
    return cleaned

# Simulated system health logs with encoded status values
def decode_status_log(entries):
    decoded = []
    temp_store = []
    for e in entries:
        if isinstance(e, str):
            numeric_part = int(''.join(filter(str.isdigit, e)))
            temp_store.append(numeric_part)  # Collected but not used directly
        else:
            decoded.append(e)
    # Only using non-string entries; string parsing is distraction
    return decoded

# Core analysis function with conditional expression
analyze_readings = lambda data: sum(x if x > 25 else (40 if x == 25 else 20) for x in data)

# Secondary helper that looks important but isn't used
def calculate_stability_index(seq):
    if not seq:
        return 0.0
    mean_val = sum(seq) / len(seq)
    variance = sum((x - mean_val) ** 2 for x in seq) / len(seq)
    return round(math.sqrt(variance), 3)

# Main execution block
if __name__ == "__main__":
    raw_input_stream = [18, -12, 30, 45, 22, 25, 33]
    status_fragments = ["err5", "log9", 18, "id14", 30, 25]  # Mixed type log

    processed_logs = preprocess_sensor_data(raw_input_stream)
    
    # Decoding step that includes irrelevant computation
    parsed_diagnostics = decode_status_log(status_fragments)
    
    # Key interference: extra processing that doesn't affect final result
    aggregated_metrics = []
    for i, val in enumerate(processed_logs):
        noise_correction = (i + 1) * 0.01
        smoothed = val - noise_correction
        aggregated_metrics.append(math.floor(smoothed))

    # Final diagnostic depends only on processed_logs, not corrected version
    final_diagnostic = analyze_readings(processed_logs)
    
    # Dead code path - never executed, adds distraction
    if False:
        backup_result = calculate_stability_index(processed_logs)
        final_diagnostic = int(backup_result * 100)

    print(f"Result: {final_diagnostic}")