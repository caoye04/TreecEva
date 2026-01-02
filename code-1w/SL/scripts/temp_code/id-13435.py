temperatures = [34.5, 45.2, 39.8, 42.1, 36.7]
pressure_readings = [101.3, 102.1, 100.9, 103.4, 101.8]

# Calculate derived thermal ratios using zip and list comprehension
derated_temps = [(t * (p / 100)) for t, p in zip(temperatures, pressure_readings)]

# Compute baseline and normalized overhead ratios
system_baseline = sum(derated_temps) / len(derated_temps)
overhead_ratios = [dt / system_baseline for dt in derated_temps]

# Key assignment: determine safety margin relative to average behavior
target_ratio = max(overhead_ratios)
reference_idx = [i for i, r in enumerate(overhead_ratios) if r == target_ratio][0]
thermal_margin = min(overhead_ratios) - system_baseline

# Print final result
print(f"Result: {thermal_margin}")