def calculate_efficiency(data):
    process = lambda x: (x ** 2 + 3 * x) % 7
    processed = [process(val) for val in data]
    total = sum([val for val in processed if val > 3])
    return total * 1.5

data_points = [2, 4, 5, 6]
offset = 1
transformed_data = [val + offset for val in data_points]
energy_output = calculate_efficiency(transformed_data)
print(f"Result: {energy_output}")