from collections import defaultdict
import math

# Simulate sensor data from industrial machines
temperature_readings = [23.5, 24.1, 25.0, 26.3, 27.8, 28.0, 29.1, 30.5]
vibration_levels = [0.02, 0.03, 0.05, 0.09, 0.15, 0.25, 0.4, 0.6]
uptime_hours = [8.2, 7.9, 8.0, 7.5, 6.8, 6.0, 5.2, 4.0]

# Irrelevant distraction: unused variable and dead computation
unused_baseline = sum([t**0.5 for t in temperature_readings]) / len(temperature_readings)
phantom_factor = 0
for i in range(len(vibration_levels)):
    if vibration_levels[i] > 1.0:  # Never true
        phantom_factor += 1

# Data aggregation using defaultdict (semi-relevant)
machine_stats = defaultdict(list)
for i, temp in enumerate(temperature_readings):
    machine_stats['temp'].append(temp)
    machine_stats['vibe'].append(vibration_levels[i])
    machine_stats['uptime'].append(uptime_hours[i])

# Normalize uptime to a 0-10 scale (relevant)
normalized_uptime = [(hour / 8.0) * 10 for hour in uptime_hours]

# Compute decay weights based on recency (distractor - not used later)
decay_weights = [math.exp(-0.2 * i) for i in range(len(temperature_readings))]
weighted_temp = sum(t * w for t, w in zip(temperature_readings, decay_weights))

# Process data: filter unstable operations (vibration > 0.25 implies instability)
stable_indices = [i for i, v in enumerate(vibration_levels) if v <= 0.25]
processed_data = []
for i in stable_indices:
    score = normalized_uptime[i] * 0.6 + (30.0 - temperature_readings[i]) * 0.4  # cooler = better
    processed_data.append(score)

# Distractor: unused lambda and irrelevant transformation
adjustment_func = lambda x: x * 1.1 if x < 6 else x * 0.95
adjusted_scores = [adjustment_func(s) for s in processed_data]  # computed but unused

# Helper function with nested logic
def calculate_efficiency(data):
    if not data:
        return 0.0
    
    avg = sum(data) / len(data)
    variance = sum((x - avg) ** 2 for x in data) / len(data)
    stability_bonus = 1.0 if variance < 4.0 else 0.8
    
    # Apply logarithmic scaling for non-linear efficiency perception
    raw_efficiency = math.log(avg + 1) * 10
    return raw_efficiency * stability_bonus

# Key statement
efficiency_score = calculate_efficiency(processed_data)

# Print result as required
print(f"Result: {efficiency_score}")