from itertools import combinations

# Simulate sensor readings with noise and calibration offsets
temperature_readings = [23.5, 24.1, 22.9, 25.0, 23.8]
humidity_readings = [45, 47, 44, 49, 46]

# Irrelevant derived metric (distractor)
avg_humidity_power = sum(h ** 2 for h in humidity_readings) / len(humidity_readings)

# Calibration constants (some are misleading)
base_offset = 1.05
noise_floor = 0.02
scaling_factor = 1.1
exponent_tuning = 0.9

# Compute effective thermal index using only temperature subset
effective_temps = [t * base_offset for t in temperature_readings if t > 23.0]
thermal_index = sum(effective_temps) / len(effective_temps)

# Generate all possible paired fluctuations (semi-relevant, unused later)
pair_fluctuations = list(combinations([round(t - 23.0, 2) for t in temperature_readings], 2))

# Primary flow computation chain
raw_flow = sum(thermal_index * (1 + noise_floor) for _ in range(3))
dampened_flow = raw_flow * scaling_factor

# Conditional adjustment based on stability heuristic
is_stable = len(effective_temps) >= 3 and max(temperature_readings) - min(temperature_readings) < 2.5
adjustment_ratio = 0.95 if is_stable else 0.8
adjusted_flow = dampened_flow * adjustment_ratio

# Efficiency depends on logical combination of conditions
temp_condition = all(t < 25.5 for t in temperature_readings)
humid_condition = any(h < 50 for h in humidity_readings)
valid_environment = temp_condition and humid_condition

# Redundant string-based flag (distractor)
environment_flag = "STABLE" if valid_environment else "UNSTABLE"
environment_status = environment_flag.lower().replace('_', '-')

# Final efficiency determined by environment and exponent tuning
efficiency_factor = 0.88 if valid_environment else 0.75
efficiency_factor *= exponent_tuning  # Minor refinement

# Critical assignment point
final_flux = adjusted_flow * efficiency_factor

print(f"Result: {final_flux}")