def calculate_efficiency(data):
    scale_factor = 1.5
    adjust = lambda x: x * 0.8 if x > 100 else x * 1.1
    processed = [adjust(val) for val in data]
    total_input = sum(data)
    total_output = sum(processed)
    efficiency = total_output / total_input
    energy_output = int(total_output * efficiency)
    return energy_output

raw_values = [45, 120, 75, 200]
offset_correction = [x + 5 for x in raw_values]  # Irrelevant distractor list
transformed_data = [x for x in raw_values if x >= 75]
energy_output = calculate_efficiency(transformed_data)
print(f"Result: {energy_output}")