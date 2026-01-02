from itertools import compress

# Simulate thermal grid load analysis with noise filtering
base_temperatures = [23.5, 24.1, 25.0, 26.8, 27.3, 28.0, 27.9, 26.4, 25.2]
load_factors = [0.78, 0.82, 0.85, 0.93, 0.96, 1.0, 0.98, 0.88, 0.81]
efficiency_curve = [0.72, 0.75, 0.79, 0.85, 0.89, 0.91, 0.90, 0.84, 0.77]

# Irrelevant auxiliary data (distractor)
power_cycles = [3, 1, 4, 1, 5, 9, 2, 6, 5]
dummy_weights = [x % 0.5 for x in base_temperatures]

# Compute derived thermal loads with conditional scaling
thermal_contributions = [
    temp * factor if temp > 25 else temp * 0.5 * factor
    for temp, factor in zip(base_temperatures, load_factors)
]

# Apply moving average filter (semi-relevant preprocessing)
smoothed_thermal = []
for i in range(1, len(thermal_contributions) - 1):
    avg = (thermal_contributions[i-1] + thermal_contributions[i] + thermal_contributions[i+1]) / 3
    smoothed_thermal.append(avg)

# Add edge values back (completion of filtering)
smoothed_thermal.insert(0, thermal_contributions[0])
smoothed_thermal.append(thermal_contributions[-1])

# Identify high-stress periods using boolean masking
stress_threshold = 22.0
is_critical = [value > stress_threshold for value in base_temperatures]
critical_loads = list(compress(smoothed_thermal, is_critical))

# Compute cumulative metrics (distractor computation)
total_exposure = sum(
    load * eff 
    for load, eff in zip(critical_loads, efficiency_curve[:len(critical_loads)])
)

# Efficiency degradation model (distractor function)
def calculate_degradation(x):
    return x * 0.98 ** (x / 10)

degraded_values = [calculate_degradation(x) for x in critical_loads]

# Core calculation: determine peak operational capacity
baseline_shift = sum(base_temperatures) / len(base_temperatures) - 20
adjustment_factor = 1 + (baseline_shift * 0.02)
efficiency_factor = sum(efficiency_curve) / len(efficiency_curve) * adjustment_factor

# Key statement
thermal_loads = [x * efficiency_factor for x in smoothed_thermal]
peak_capacity = max(thermal_loads) * efficiency_factor

# Additional irrelevant transformation (dead path)
if len(degraded_values) < 10:
    offset_correction = 0.5
    adjusted_capacity = peak_capacity - offset_correction

Result: peak_capacity