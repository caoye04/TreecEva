def calculate_efficiency(rate, pressure):
    base_efficiency = rate * 0.8
    adjustment = pressure * 0.05
    return base_efficiency + adjustment

flow_rate = 150
pressure = 20
system_mode = True
is_stable = flow_rate > 100 and pressure > 15

# Key computation with conditional expression
temperature_factor = 1.1 if pressure > 18 else 0.9
energy_output = calculate_efficiency(flow_rate, pressure) * (is_stable if system_mode else not is_stable)
energy_output *= temperature_factor

print(f"Result: {energy_output}")