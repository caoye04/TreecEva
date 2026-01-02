def calculate_efficiency(load, thresh):
    base = 100 if load <= thresh else 80
    adjustment = sum([0.5 * (i % 3) for i in range(load)])
    return base - adjustment

network_load = 7
threshold = 5
energy_level = 0
energy_level = calculate_efficiency(network_load, threshold)
print(f"Result: {energy_level}")