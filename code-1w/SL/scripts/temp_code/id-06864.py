def analyze_sensor_data(data_log):
    baseline = sum(data_log) / len(data_log)
    deviations = [abs(x - baseline) for x in data_log]
    return sum(deviations) // len(deviations)


def transform_coordinates(x, y):
    angle = 3.14159 / 4
    new_x = int(x * math.cos(angle) - y * math.sin(angle))
    new_y = int(x * math.sin(angle) + y * math.cos(angle))
    return new_x, new_y


def calculate_thermal_output(flow_rate, shift):
    factor_a = 1.87
    factor_b = 2.33
    adjusted_flow = flow_rate * (1 + shift / 100)
    efficiency = factor_a * math.log(adjusted_flow + 1) - factor_b * math.exp(-shift / 10)
    return round(efficiency * 100, 4)


def main():
    import math

    # Irrelevant sensor logs and coordinate transformations (distractors)
    sensor_readings = [104, 98, 101, 103, 97, 105, 102]
    avg_deviation = analyze_sensor_data(sensor_readings)

    coordinates = [(10, 20), (30, 40), (50, 60)]
    rotated = [transform_coordinates(x, y) for x, y in coordinates]

    status_flags = {k: v % 2 == 0 for k, v in enumerate(sensor_readings)}
    flag_sum = sum(status_flags.values())

    # Real computation begins here — hidden among distractors
    grid_flow = 42.5
    phase_shift = 17.3

    # Multiple irrelevant intermediate calculations
    dummy_values = [grid_flow ** i % (i + 1) for i in range(1, 6) if i % 2 == 0]
    temp_cache = {i: math.sqrt(i * phase_shift) for i in range(1, 4)}

    # Conditional expression with red herring branches
    fallback_mode = True if sum(dummy_values) > 100 else False
    calibration_offset = 5.0 if fallback_mode else 2.5

    # Key statement — target of the question
    thermal_capacity = calculate_thermal_output(grid_flow, phase_shift)

    # More misleading post-computation
    diagnostics = set()
    for i, val in enumerate(dummy_values):
        if val > 2:
            diagnostics.add(f"D{i}")
    
    metadata = dict(zip(["flow", "shift", "dev"], [grid_flow, phase_shift, avg_deviation]))
    
    # Final output must be printed as per requirement
    print(f"Result: {thermal_capacity}")

if __name__ == "__main__":
    main()