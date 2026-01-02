from itertools import cycle

# Simulate multi-phase crop growth with environmental factors
base_growth = 12
soil_quality = 85
pest_pressure = 3
water_stress = 2
temperature_deviation = 1.5

# Irrelevant tracking variables (distractors)
current_monitoring_status = True
sensor_array_active = [True, False, True]
data_log_count = 0
redundant_counter = 0

# Phase 1: Initial germination under soil conditions
initial_germination = base_growth * (soil_quality / 100)
if initial_germination > 10:
    stress_adjustment = pest_pressure * water_stress
else:
    stress_adjustment = 0

# Intermediate irrelevant computation (dead path)
if False:
    debug_value = 999
    for i in range(5):
        redundant_counter += i**2

# Phase 2: Weekly growth cycles with fluctuating conditions
growth_cycles = []
for week in range(1, 6):
    temp_effect = max(0.7, 1 - (temperature_deviation * 0.1 * week))
    weekly_growth = initial_germination * temp_effect
    growth_cycles.append(round(weekly_growth, 2))
    data_log_count += 1  # Tracking but not used

# Phase 3: Apply recovery factor if average growth improved in last 3 weeks
recent_growth = growth_cycles[-3:]
if recent_growth[2] > recent_growth[0]:
    recovery_boost = 1.15
else:
    recovery_boost = 1.0

# Phase 4: Cumulative growth with decay correction
decay_correction = 0.98 ** len(growth_cycles)
cumulative_growth = sum(growth_cycles) * decay_correction * recovery_boost

# Efficiency tuning based on resource cycling (using itertools)
resource_rotation = cycle([0.95, 1.05, 1.02])
efficiency_accum = 0
for _ in range(len(growth_cycles)):
    efficiency_accum += next(resource_rotation)
efficiency_factor = efficiency_accum / len(growth_cycles)

# Final yield calculation (target execution point)
final_yield = cumulative_growth * efficiency_factor

# Print result for evaluation
print(f"Result: {final_yield}")