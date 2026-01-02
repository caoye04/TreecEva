def calculate_efficiency(data):
    process = lambda x: x * 0.85 if x > 100 else x * 0.75
    total = 0
    for val in data:
        if val % 2 == 0:
            total += process(val)
    return total

raw_readings = [80, 120, 95, 140, 105]
offset = 10
adjusted_readings = [x + offset for x in raw_readings]
filtered_data = [x for x in adjusted_readings if x >= 100]
transformed_data = [x * 1.1 for x in filtered_data]
system_mode = 'eco'
energy_output = calculate_efficiency(transformed_data)
print(f"Result: {energy_output}")