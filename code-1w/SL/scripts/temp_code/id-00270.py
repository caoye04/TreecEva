from collections import defaultdict, Counter

# Simulated sensor data processing pipeline
def collect_diagnostics():
    raw_readings = [105, 210, 150, 300, 250, 180, 190, 220, 310, 270, 140]
    calibration_offset = 50
    adjusted_readings = [x - calibration_offset for x in raw_readings]

    # Irrelevant statistical computation (distractor)
    mean_val = sum(adjusted_readings) / len(adjusted_readings)
    variance = sum((x - mean_val) ** 2 for x in adjusted_readings) / len(adjusted_readings)
    std_dev = variance ** 0.5

    # Threshold logic with red herring branches
    critical_limit = 200
    warning_limit = 150
    mode_filter = 'aggressive'

    # Misleading filter path (dead code due to condition)
    temp_result = []
    if mode_filter == 'conservative':
        temp_result = [x for x in adjusted_readings if x > warning_limit]
    else:
        # This branch is taken but adds noise
        shadow_copy = adjusted_readings.copy()
        temp_result = [x for x in shadow_copy if x >= critical_limit]

    # Actual relevant filtering
    filtered_data = [x for x in adjusted_readings if x > critical_limit]

    # Use of defaultdict as required (partially relevant, partially over-engineered)
    threshold_map = defaultdict(lambda: 'normal')
    threshold_map[200] = 'high'
    threshold_map[250] = 'critical'
    threshold_map[300] = 'extreme'

    # Unused counter (distractor)
    reading_frequencies = Counter(adjusted_readings)

    # Conditional expression used idiomatically
    status_flag = 'active' if len(filtered_data) > 3 else 'standby'

    # Red herring: complex bit manipulation on unrelated metric
    checksum = 0
    for val in raw_readings[:5]:
        checksum ^= (val << 1) | (val >> 2)
    checksum &= 0xFFFF

    # Auxiliary function defined inside (state encapsulation)
    def analyze_readings(data, thresholds):
        base_score = 0
        penalty = 0

        # Enumerate with zip usage (required feature)
        for i, (idx, val) in enumerate(zip(range(len(data)), data)):
            base_score += val * (i + 1)
            if val > 240:
                penalty += 15
            elif val > 200:
                penalty += 5

        # Complex scoring logic with conditional expression
        adjustment = 1.2 if status_flag == 'active' else 0.8
        intermediate = (base_score - penalty) * adjustment

        # More distraction: unused recursion (defined but not used)
        def recursive_sum(arr):
            return arr[0] + recursive_sum(arr[1:]) if arr else 0

        # Final irrelevant transformation
        result_code = int(intermediate // 10) & 0xFF
        return result_code

    # Key statement
    final_diagnostic = analyze_readings(filtered_data, threshold_map)

    # Output requirement
    print(f"Result: {final_diagnostic}")

    # Irrelevant final loop (dead code)
    for _ in range(3):
        checksum = (checksum * 2) % 1000

    return final_diagnostic

# Execute and capture result
collect_diagnostics()