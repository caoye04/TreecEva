from itertools import cycle

# Simulate environmental sensor data over time
temperature_readings = [22, 24, 19, 25, 27, 23, 20]
humidity_levels = [44, 55, 33, 60, 50, 45, 30]

# Initialize system parameters
base_rating = 85
efficiency_factor = 1.0
diagnostic_log = []
redundant_sum = 0

# Process each sensor pair with auxiliary tracking
for i, (temp, hum) in enumerate(zip(temperature_readings, humidity_levels)):
    # Irrelevant diagnostic accumulation (distractor)
    redundant_sum += temp % 7 * hum

    # State tracking for hypothetical fault detection (not used in final result)
    if temp > 24 and hum > 45:
        diagnostic_log.append((i, 'OVERHEAT_RISK'))
    elif temp < 20 and hum < 35:
        diagnostic_log.append((i, 'LOW_COND'))

    # Core logic: adjust efficiency based on conditions
    adjustment = 0.0
    if temp > 25:
        adjustment -= 0.05
    elif temp < 20:
        adjustment += 0.03

    if hum > 50:
        adjustment -= 0.04

    # Efficiency decays over cycles (additional complexity)
    cycle_iter = cycle([0.98, 0.99, 1.0])
    for _ in range(i % 3 + 1):
        decay_multiplier = next(cycle_iter)

    efficiency_factor = max(0.8, efficiency_factor + adjustment) * decay_multiplier

# Key assignment statement determining final output
target_stage = 'FINAL'
thermal_capacity = base_rating * efficiency_factor

# Additional irrelevant computation (dead-end path)
aggregated_diagnostic = sum(h * (r % 5) for r, h in zip(temperature_readings, humidity_levels)) // len(humidity_levels)

print(f"Result: {thermal_capacity}")