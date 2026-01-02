def calculate_efficiency(data):
    process = lambda x: (x ** 2 + 3 * x) / 2
    total = 0
    for val in data:
        if val > 0:
            total += process(val)
    return int(total // len(data))

raw_values = [4, -1, 6, 0, 3]
filtered_data = [v for v in raw_values if v > 0]
scaled_data = [x * 2 for x in filtered_data]
transformed_data = list(map(lambda x: x - 1, scaled_data))
energy_output = calculate_efficiency(transformed_data)
print(f"Result: {energy_output}")