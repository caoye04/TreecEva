from collections import defaultdict
import itertools

# Simulate sensor readings over time for environmental monitoring
temperature_readings = [22, 24, 19, 25, 27, 23, 20, 26]
humidity_readings = [45, 50, 60, 55, 40, 65, 70, 58]

# Misleading auxiliary computation (distractor)
avg_humidity = sum(humidity_readings) / len(humidity_readings)
humidity_variance = sum((h - avg_humidity) ** 2 for h in humidity_readings) / len(humidity_readings)

data_points = list(zip(temperature_readings, humidity_readings))

event_counter = defaultdict(int)
for temp, hum in data_points:
    if temp > 23:
        event_counter['high_temp'] += 1
    if hum < 50:
        event_counter['low_hum'] += 1

# Complex filtering using itertools (semi-relevant)
filtered_periods = list(itertools.combinations(data_points, 2))
valid_transitions = 0
for pair in filtered_periods:
    t1, h1 = pair[0]
    t2, h2 = pair[1]
    if abs(t1 - t2) <= 3 and h1 != h2:
        valid_transitions += 1

# Core system parameters
base_rating = 85
system_age = 7  # years
maintenance_records = [True, False, True, True, False, True, True]

# Efficiency model with red herring variables
age_factor = max(0.5, 1 - (system_age * 0.08))
degradation_penalty = 0.0 if all(maintenance_records) else 0.15

# Dead code path (distractor)
if len(maintenance_records) > 10:
    degradation_penalty *= 0.5

utilization_history = [0.8, 0.9, 0.7, 0.95, 0.82, 0.88, 0.79]
performance_trend = sum(1 for u in utilization_history if u > 0.8)

# Key efficiency calculation influenced by conditional logic
efficiency_factor = age_factor - degradation_penalty
if performance_trend >= 5:
    efficiency_factor *= 1.1

# Critical assignment point
thermal_capacity = base_rating * efficiency_factor

# Additional irrelevant transformation (distractor)
normalized_capacity = [round(thermal_capacity / (i + 1), 2) for i in range(3)]

print(f"Result: {thermal_capacity}")