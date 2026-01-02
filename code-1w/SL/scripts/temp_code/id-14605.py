def analyze_growth_potential(temp, moisture):
    if temp < 20 or temp > 45:
        return False
    if moisture < 30 or moisture > 80:
        return False
    return True

# Simulate sensor calibration offset (irrelevant to final result)
calibration_factor = 1.05
baseline_offset = 0.95

# Actual environmental data from greenhouse sensors
temperature_readings = [22, 25, 19, 35, 28, 41, 24]
moisture_levels = [65, 70, 82, 55, 38, 75, 60]

# Irrelevant derived metrics (distractor computations)
avg_temp = sum(temperature_readings) / len(temperature_readings)
highest_moisture = max(moisture_levels)
low_temp_count = len([t for t in temperature_readings if t < 22])

# Track valid growth windows using enumerate and conditional logic
effective_cycles = 0
for i, temp in enumerate(temperature_readings):
    moisture = moisture_levels[i]
    if analyze_growth_potential(temp, moisture):
        effective_cycles += 1

# Secondary calculation: cumulative stability index (partially relevant)
stability_score = 0
for i, (temp, moisture) in enumerate(zip(temperature_readings, moisture_levels)):
    if 20 <= temp <= 40 and 40 <= moisture <= 75:
        stability_score += 1

# Noise injection simulation (dead code path - never executed due to constant guard)
sensor_noise = []
if False:  # Simulated fault detection disabled
    for _ in range(10):
        sensor_noise.append(calibration_factor * baseline_offset)

# Core yield model: uses effective_cycles but ignores noise and most intermediates
def calculate_optimal_yield(temps, moistures):
    base_yield = 100
    penalty = 0
    
    # First adjustment: reduce by 5% per ineffective cycle
    total_days = len(temps)
    failed_cycles = total_days - effective_cycles
    penalty += failed_cycles * 5
    
    # Second adjustment: bonus if stability_score >= 4
    bonus = 10 if stability_score >= 4 else 0
    
    # Final formula (only this matters)
    result = base_yield - penalty + bonus
    return result

# Execute main computation
intermediate_yield = calculate_optimal_yield(temperature_readings, moisture_levels)

# Apply fake correction factor (never used)
adjusted_yield = intermediate_yield * calibration_factor  # Distractor

# Final assignment
final_yield = calculate_optimal_yield(temperature_readings, moisture_levels)

print(f"Result: {final_yield}")