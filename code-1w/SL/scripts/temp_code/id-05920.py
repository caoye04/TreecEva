from itertools import accumulate

def analyze_system_efficiency(parameters):
    adjusted_params = [p * 1.05 for p in parameters]
    return [x for x in adjusted_params if x > 10]

# Simulate thermal dynamics in a geothermal energy system
temperature_readings = [45, 52, 60, 68, 75, 80, 85, 90]
pressure_levels = [1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9]

# Misleading computation: irrelevant signal processing
smoothed_temps = list(accumulate(temp for temp in temperature_readings))
baseline_offset = sum(smoothed_temps) / len(smoothed_temps)
detrended = [t - baseline_offset for t in smoothed_temps]

# Real data preparation
flow_rates = [0.8, 1.1, 1.3, 1.6, 1.8, 2.0, 2.3, 2.5]
temperature_gradients = [temp - 40 for temp in temperature_readings]  # delta from base temp

# Auxiliary calculation (semi-relevant but not used directly)
efficiency_ratios = analyze_system_efficiency(pressure_levels)
scaling_factor = 0.9 if len(efficiency_ratios) > 5 else 1.1

# Core logic with enumerate and zip
energy_contributions = []
for i, (rate, grad) in enumerate(zip(flow_rates, temperature_gradients)):
    contribution = rate * grad
    if i % 2 == 0:
        contribution *= scaling_factor  # alternating correction
    energy_contributions.append(contribution)

# Cumulative integration via itertools
integrated_energy = list(accumulate(energy_contributions))
final_energy_step = integrated_energy[-1]

# Key statement
thermal_capacity = calculate_thermal_output(flow_rates, temperature_gradients)

# Dummy function to complete execution
def calculate_thermal_output(flows, grads):
    total = 0
    for f, g in zip(flows, grads):
        total += f * g * 1.25  # efficiency coefficient
    adjustment = sum(1 for x in flows if x > 1.5)  # count high-flow stages
    return total - adjustment

# Recompute here to ensure execution order
def calculate_thermal_output(flows, grads):
    total = 0
    for f, g in zip(flows, grads):
        total += f * g * 1.25
    adjustment = sum(1 for x in flows if x > 1.5)
    return total - adjustment

thermal_capacity = calculate_thermal_output(flow_rates, temperature_gradients)
print(f"Result: {thermal_capacity}")