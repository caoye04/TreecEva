def calculate_efficiency(rate, pressure):
    if rate <= 0 or pressure <= 0:
        return 0.0
    efficiency = (rate * pressure) / (rate + pressure)
    return round(efficiency, 3)

flow_rate = 24.5
pressure = 18.3
baseline = 1.0  # unused baseline (minor distractor)
safety_factor = 1.2

# Critical computation step
temperature_status = "optimal" if flow_rate > 20 else "suboptimal"
energy_threshold = calculate_efficiency(flow_rate, pressure) * safety_factor

# Additional minor logic to reflect realistic context
if temperature_status == "optimal":
    energy_threshold += 0.5

print(f"Result: {energy_threshold}")