def calculate_thermal_output(segments):
    base_factor = 1.75
    adjustment = 0.92
    cumulative_heat = 0
    transient_buffer = []

    for idx, segment in enumerate(segments):
        if idx % 2 == 0:
            raw_value = segment * base_factor ** idx
            smoothed = raw_value * adjustment
        else:
            shifted = segment << 1
            inverted = ~shifted + 100
            smoothed = abs(inverted) * 0.1

        cumulative_heat += smoothed
        transient_buffer.append(smoothed * 0.05)

        # Dead code - buffer not used later
        if len(transient_buffer) > 10:
            transient_buffer.pop(0)

    final_output = cumulative_heat / len(segments)
    return round(final_output, 4)

# Sensor data from thermal zones (in arbitrary units)
sensor_readings = [23, 18, 35, 41, 29, 33, 37]

# Irrelevant preprocessing - distractor
data_slice = sensor_readings[1:6:2]  # [18, 41, 33]
offset_correction = sum(data_slice) / len(data_slice)
adjusted_readings = [x - offset_correction for x in sensor_readings]

# Secondary unused calculation chain
aggregated = 0
for val in adjusted_readings:
    aggregated += val ** 0.5
scaling_proxy = aggregated / len(adjusted_readings)

# Core processing path
process_segments = sensor_readings[::2]  # [23, 35, 29, 37]

# Key computation with slicing and multiple logic steps
temperature_profile = [x * 1.1 for x in process_segments]
filtered_profile = temperature_profile[1:-1]  # [38.5, 31.9]

# Final function call that determines answer
termal_capacity = calculate_thermal_output(process_segments)

Result: {termal_capacity}