def calculate_efficiency(data, scale):
    process = lambda x: (x ** 0.5) * scale
    total = 0
    for val in data:
        if val > 0:
            total += process(val)
    return int(total)

# Irrelevant auxiliary variable (minimal distraction)
status_flag = True

consumption_data = [16, 9, 0, 25, 4]
scaling_factor = 2
energy_output = calculate_efficiency(consumption_data, scaling_factor)
print(f"Result: {energy_output}")