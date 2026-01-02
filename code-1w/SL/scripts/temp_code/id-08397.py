def calculate_efficiency(data, limit):
    total = sum(data)
    if total > limit:
        return total * 0.85
    else:
        return total * 1.1

# Sensor readings from power grid (in MW)
grid_load = [120, 150, 95, 200, 175]
threshold = 300

temp_buffer = [x * 0.9 for x in grid_load]  # Preprocessed backup data (irrelevant)
baseline_avg = sum(grid_load[:3]) / 3  # Historical average (distractor)

energy_output = calculate_efficiency(grid_load[2:], threshold)
print(f"Result: {energy_output}")