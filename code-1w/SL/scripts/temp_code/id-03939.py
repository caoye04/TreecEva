from collections import defaultdict

# Simulate thermal regulation system for a power plant
hourly_temperatures = [298, 305, 312, 309, 318, 325, 320, 315, 310, 307]
base_pressure = 101.3
efficiency_factor = 0.87

# Misleading variables - not used in final calculation
temp_offset = 273.15
pressure_ratio = 0.0
normalization_constant = 1.0e-4
calibration_data = [1.2, 0.9, 1.1, 1.0, 0.8]

# Compute derived thermal loads with conditional scaling
temperature_contributions = []
for temp in hourly_temperatures:
    if temp > 310:
        contribution = (temp - 273) ** 1.1
    else:
        contribution = (temp - 273) * 1.2
    temperature_contributions.append(contribution)

# Apply artificial dampening factor (distractor computation)
dampened_contributions = []
for val in temperature_contributions:
    damped = val * 0.95 + 5.2
    dampened_contributions.append(damped)

# Only this processed data matters
thermal_loads = [round(tc * 1.05, 2) for tc in temperature_contributions]

# Track cumulative metrics (semi-relevant but unused)
cumulative_load = sum(thermal_loads)
load_history = defaultdict(int)
for load in thermal_loads:
    bucket = int(load // 50)
    load_history[bucket] += 1

# Key computation point
peak_capacity = max(thermal_loads) * efficiency_factor

# Print result as required
print(f"Result: {peak_capacity}")