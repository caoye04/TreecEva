def calculate_efficiency(rate, press):
    if rate <= 0 or press <= 0:
        return 0
    efficiency_factor = (rate * 0.85) if press > 10 else (rate * 0.6)
    adjusted_yield = efficiency_factor * (press ** 0.5)
    return int(adjusted_yield)

flow_rate = 12
pressure = 15
temperature = 220  # irrelevant variable (minimal distraction)
material_type = "alloy"  # irrelevant variable
energy_output = calculate_efficiency(flow_rate, pressure)
print(f"Target result: {energy_output}")