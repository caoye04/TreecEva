def calculate_humidity_factor(readings):
    indices = []
    for i, val in enumerate(readings):
        if i % 2 == 0:
            indices.append(val * 1.5)
        else:
            indices.append(val * 0.8)
    return sum(indices)

# Sensor readings in percentage humidity
readings = [40, 60, 50, 70, 30]

# Irrelevant baseline calibration (distractor)
baseline_offset = 2.5
adjusted_readings = [r + baseline_offset for r in readings]

# Main computation
smoothed_values = [round(v, 1) for v in adjusted_readings]  # unused distractor

# Key statement
total_humidity_index = calculate_humidity_factor(readings)

print(f"Result: {total_humidity_index}")