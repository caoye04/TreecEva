def calculate_efficiency(data):
    filter_positive = lambda x: [val for val in x if val > 0]
    processed = filter_positive(data)
    total_input = sum(processed)
    conversion_factor = 0.85
    energy_output = total_input * conversion_factor
    return energy_output

raw_measurements = [-5, 10, 0, 15, -3, 20]
offset = 5
transformed_data = [x + offset for x in raw_measurements]
default_threshold = 0.5
energy_output = calculate_efficiency(transformed_data)
Result: {energy_output}