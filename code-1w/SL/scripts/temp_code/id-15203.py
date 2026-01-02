def calculate_stability_index(load, threshold=1000):
    return (load ** 0.5) / threshold if load > threshold else load / threshold

# Simulate sensor readings from a power regulation system
temperature_readings = [23.5, 24.1, 22.9, 25.3, 26.0]
pressure_levels = {"core": 88.2, "auxiliary": 45.6, "backup": 33.1}

# Irrelevant stability diagnostics (distractor)
stability_score = 0
for reading in temperature_readings:
    stability_score += calculate_stability_index(int(reading * 10))
stability_score = round(stability_score, 2)

# Core operational parameters
baseline_efficiency = 0.87
module_count = 12
efficiency_factor = baseline_efficiency

# Apply conditional efficiency boost based on pressure (relevant logic)
if pressure_levels["core"] > 85:
    efficiency_factor *= 1.08

# Secondary adjustment using modular arithmetic on sensor count
sensor_count = len(temperature_readings)
efficiency_factor += (sensor_count % 4) * 0.01

# Noise margin calculation (dead code path - does not affect result)
noise_margin = 0.0
for p in pressure_levels.values():
    noise_margin += p * 0.001
noise_margin = round(noise_margin, 3)

# Calculate thermal rating using conditional expression and min/max logic
def calculate_thermal_rating(eff, modules):
    base_rating = eff * 1000
    adjusted_rating = base_rating if modules >= 10 else base_rating * 0.9
    # Apply max constraint and add module bonus using min/max
    adjusted_rating = max(adjusted_rating, 850)
    module_bonus = min(modules * 5, 60)
    return adjusted_rating + module_bonus

# Key computation step
thermal_capacity = calculate_thermal_rating(efficiency_factor, module_count)

# Print final result for evaluation
print(f"Result: {thermal_capacity}")