def calculate_total(devs, scale):
    transform = lambda x: abs(x) ** 0.5
    total = 0
    for key in devs:
        if devs[key] < 0:
            total += transform(devs[key]) * scale
        else:
            total += devs[key] * scale
    return int(total)

# System calibration data
deviation_map = {'sensor_a': -16, 'sensor_b': 25, 'sensor_c': -9, 'sensor_d': 4}
scaling_factor = 2
offset_adjustment = 0.5  # Unused in computation (minimal interference)

final_score = calculate_total(deviation_map, scaling_factor)
print(f"Result: {final_score}")