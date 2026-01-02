def calculate_efficiency(data):
    return sum(x ** 0.5 for x in data if x > 0) * 0.75

readings = [-4, 0, 9, 16, -1, 25]
offset = 3
adjusted_readings = [x + offset for x in readings]
filtered_readings = [x for x in adjusted_readings if x > 5]
energy_output = calculate_efficiency(filtered_readings)
print(f"Result: {energy_output}")