def analyze_sensor_chain(raw_input, config):
    # Irrelevant preprocessing block (dead path)
    temp_buffer = [x * 1.05 for x in raw_input if x > 0]
    adjusted = [int(x) for x in temp_buffer]
    offset_correction = sum(adjusted) // len(adjusted) if adjusted else 0

    # Distractor: complex but unused transformation
    shadow_copy = raw_input[::-1]  # reversed order, never used
    derived_meta = []
    for i, val in enumerate(shadow_copy):
        if i % 3 == 0:
            derived_meta.append(val ^ (i + 1))

    # Real data flow begins
    scaled_readings = [x * config['gain'] for x in raw_input]
    thresholded = [x for x in scaled_readings if abs(x) > config['noise_floor']]

    # Bit manipulation red herring
    bit_analysis = 0
    for x in thresholded:
        if x > 0:
            bit_analysis ^= int(x) & 0xFF

    # Actual filtering logic
    filtered_data = thresholded[1:-1]  # slice out first and last
    trigger_points = [i for i, x in enumerate(filtered_data) if x > config['activation_level']]

    # Decoy function call with side-effect that does nothing
    def log_anomaly(seq):
        return [x for x in seq if x < 0]  # never contributes to result

    anomaly_trace = log_anomaly(filtered_data)

    # Critical nested helper — only this matters
    def process_readings(data, levels):
        if not data:
            return -999
        base = 0
        for i, val in enumerate(data):
            if i % 2 == 0:
                base += val * levels[0]
            else:
                base -= val * levels[1]
        # Final twist: use slicing and integer division
        segment_avg = sum(data[len(data)//4 : len(data)//4*3]) // (len(data)//2 + 1)
        return base + (segment_avg & 0xFFFF)  # includes bitwise masking

    level_settings = [3, 2]
    extra_weights = [5, 1, 8]  # unused distractor

    # Another red herring: sorting without usage
    sorted_diags = sorted(thresholded, reverse=True)
    rank_index = [sorted_diags.index(x) for x in filtered_data]  # misleading intermediate

    # Key execution point
    final_diagnostic = process_readings(filtered_data, level_settings)

    # Print required output
    print(f"Result: {final_diagnostic}")

# Inputs
sensor_input = [12, -7, 9, 15, -3, 6, 8, 11]
params = {
    'gain': 2,
    'noise_floor': 5,
    'activation_level': 10
}

analyze_sensor_chain(sensor_input, params)