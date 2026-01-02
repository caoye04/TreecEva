from collections import defaultdict
from itertools import cycle

# Simulate sensor data streams with timestamps and readings
def generate_sensor_stream(base_value, noise_factor, count):
    return [(i, base_value + (i % 3 - 1) * noise_factor) for i in range(1, count + 1)]

# Generate multiple sensor logs
temperature_log = generate_sensor_stream(25.3, 0.7, 8)
pressure_log = generate_sensor_stream(101.2, 0.4, 8)
efficiency_logs = generate_sensor_stream(89.4, 0.6, 8)

# Extract values for processing
temp_values = [entry[1] for entry in temperature_log]
pres_values = [entry[1] for entry in pressure_log]
eff_values = [entry[1] for entry in efficiency_logs]

# Misleading auxiliary calculation (dead-end)
avg_temp = sum(temp_values) / len(temp_values)
stdev_pres = (sum((x - sum(pres_values)/len(pres_values))**2 for x in pres_values) / len(pres_values)) ** 0.5

# Weighting system based on sensor reliability (simulated)
sensor_reliability = {'temp': 0.88, 'pres': 0.91, 'eff': 0.85}
reliability_weights = []

for i in range(len(temp_values)):
    # Interleaved weighting pattern using cycling logic
    if i % 4 == 0:
        weight = sensor_reliability['temp'] * 1.05
    elif i % 3 == 0:
        weight = sensor_reliability['pres'] * 0.98
    else:
        weight = sensor_reliability['eff'] * 1.02
    reliability_weights.append(weight)

    # Distractor: tracking unused intermediate
    _ = (temp_values[i] + pres_values[i % len(pres_values)]) / 2

# Secondary irrelevant list comprehension
correlation_map = [abs(temp_values[i] - pres_values[i]) for i in range(len(temp_values))]
mean_correlation = sum(correlation_map) / len(correlation_map)

# Helper function to compute weighted aggregate
def compute_aggregate(weights, log):
    weighted_sum = 0.0
    total_weight = 0.0
    mask_pattern = [1 if w > 0.89 else 0.8 for w in weights]
    
    for idx, (w, val) in enumerate(zip(weights, log)):
        if mask_pattern[idx] > 0.75:  # Always true
            adjustment = 1.0 + (idx % 2) * 0.01
            weighted_sum += w * val * adjustment
            total_weight += w * adjustment
            
            # Red herring: update dummy tracker
            if idx % 5 == 0:
                dummy = (val ** 2) / (w + 1e-8)
    
    return weighted_sum / total_weight if total_weight > 0 else 0

# Critical execution point
final_score = compute_aggregate(reliability_weights, eff_values)

# Print result as required
print(f"Target result: {final_score}")