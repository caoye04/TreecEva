import itertools

def analyze_sensor_stream(raw_readings, calibration_factor):
    # Irrelevant transformation: base conversion distraction
    hex_labels = [hex(x)[2:] for x in range(16)]
    shifted_labels = [label.upper() + 'X' for label in hex_labels if len(label) == 1]

    # Distractor: complex but unused data structure
    decoy_matrix = [[i * j + 2 for j in range(5)] for i in range(5)]
    checksum = sum(sum(row) for row in decoy_matrix) % 100  # Unused

    # Real logic begins: filter valid sensor readings
    valid_range = (10, 100)
    scaled_readings = [x * calibration_factor for x in raw_readings]
    filtered_data = [x for x in scaled_readings if valid_range[0] <= x <= valid_range[1]]

    # Dead code path: never executed due to condition
    if len(filtered_data) > 1000:
        backup_mode = True
        recovery_state = [x / 2 for x in filtered_data[::-1]]
    else:
        backup_mode = False  # This branch always taken

    # Misleading intermediate aggregation
    average_proxy = sum([x ** 0.5 for x in filtered_data]) / len(filtered_data) if filtered_data else 0
    entropy_proxy = average_proxy * 1.618

    # Key distractor: fake threshold adjustment
    temp_adjustments = list(itertools.accumulate([0.1] * len(filtered_data), lambda a, b: a + b))
    adjusted_offsets = [t * 0.01 for t in temp_adjustments]  # Nowhere used

    # Real processing setup
    status_flags = []
    for idx, val in enumerate(filtered_data):
        if val > 50:
            status_flags.append(1)
        else:
            status_flags.append(0)
    
    # Critical map construction (used later)
    threshold_map = {}
    for i, flag in enumerate(status_flags):
        key = f"sensor_{i % 7}_bank"
        if flag:
            threshold_map[key] = 0.75
        else:
            threshold_map[key] = 0.45

    # Another red herring: zip with no side effect
    paired_diagnostics = list(zip(shifted_labels[:len(filtered_data)], filtered_data))
    diagnostic_trace = []
    for label, value in paired_diagnostics:
        if 'A' in label:
            diagnostic_trace.append(value * 2)

    # Unused recursive function (decoy)
    def compute_depth(x):
        return 1 + compute_depth(x // 2) if x > 1 else 1
    
    # Real target computation
    final_diagnostic = process_readings(filtered_data, threshold_map)
    return final_diagnostic


def process_readings(readings, thresholds):
    # Simulate multi-stage diagnostic scoring
    base_score = 0
    keys = [f"sensor_{i % 7}_bank" for i in range(len(readings))]
    
    for i, val in enumerate(readings):
        key = keys[i]
        threshold = thresholds.get(key, 0.5)
        contribution = val * threshold
        base_score += contribution
    
    # Secondary correction based on pattern density
    runs = 0
    for a, b in itertools.pairwise([int(r > 40) for r in readings]):
        if a == b == 1:
            runs += 1
    
    # Final adjustment: this is the true answer
    final_score = base_score + (runs * 1.5)
    return int(final_score)

# Main execution
if __name__ == "__main__":
    sensor_input = [12, 45, 67, 23, 89, 34, 78, 56, 14, 91, 65]
    calibration = 1.3
    result = analyze_sensor_stream(sensor_input, calibration)
    final_diagnostic = result
    print(f"Target result: {final_diagnostic}")