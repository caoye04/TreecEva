def analyze_system_metrics(input_data):
    baseline = 1.0
    offset = 0.05
    scaling_factor = 1.75
    
    # Preprocess input using string manipulation (simulated sensor data)
    raw_segments = input_data.split(':')
    cleaned = [seg.strip().replace('X', '') for seg in raw_segments]
    
    # Extract numeric values from formatted strings
    temp_a = float(cleaned[0]) + offset
    temp_b = float(cleaned[1]) * scaling_factor
    pressure = float(cleaned[2])

    # Misleading intermediate calculations (distractors)
    dummy_metric_1 = (temp_a + temp_b) / 2.0
    dummy_metric_2 = pressure ** 0.5
    auxiliary_state = dummy_metric_1 > dummy_metric_2

    # Core computation path
    if temp_a > temp_b:
        efficiency_ratio = (temp_b / temp_a) ** 2
    else:
        efficiency_ratio = (temp_a / temp_b) * 0.9

    phase_shift = int(cleaned[3]) % 4

    def calculate_thermal_output(eff, phase):
        base_output = eff * 1000
        # Conditional expression based on phase
        adjustment = 1.1 if phase == 0 or phase == 2 else (0.95 if phase == 1 else 0.88)
        return base_output * adjustment

    # Additional irrelevant tracking
    history_log = []
    for i in range(3):
        history_log.append(f'Stage {i}: inactive')

    # Key statement
    thermal_capacity = calculate_thermal_output(efficiency_ratio, phase_shift)

    # Unrelated post-processing
    final_status = 'OK' if auxiliary_state else 'WARNING'
    metadata_tag = f'TAG-{baseline*100:.0f}'

    print(f'Result: {thermal_capacity}')
    return thermal_capacity

# Simulated sensor input
sensor_input = '95.0X : 85.5X : 225.0 : 3'
analyze_system_metrics(sensor_input)