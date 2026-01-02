readings = [12.5, 18.3, 9.7, 22.1, 14.6, 8.9, 25.4, 11.8]

temperature_zones = ['low' if r < 10 else 'high' if r > 20 else 'normal' for r in readings]

valid_range = [r for r in readings if 10 <= r <= 20]

above_threshold = [r * 1.1 for r in valid_range if r > 15]

below_minimum = [r * 1.3 for r in readings if r < 10]

filtered_readings = above_threshold + below_minimum

energy_threshold = filtered_readings[-1] if filtered_readings else 0

print(f"Result: {energy_threshold}")