def calculate_efficiency(data):
    process_lambda = lambda x: x * 0.85 if x > 100 else x * 0.75
    processed = [process_lambda(val) for val in data]
    total_input = sum(data)
    total_output = sum(processed)
    efficiency = total_output / total_input
    return int(total_output * efficiency)

raw_values = [120, 95, 150, 80]
offset = 5
adjusted_values = [v + offset for v in raw_values]
transformed_data = [val for val in adjusted_values if val > 100]
energy_output = calculate_efficiency(transformed_data)
print(f"Result: {energy_output}")