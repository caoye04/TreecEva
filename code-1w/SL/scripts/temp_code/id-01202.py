from itertools import combinations

# Simulate sensor data from a thermal regulation system
temperature_readings = [23.4, 25.1, 24.8, 26.3, 22.9, 27.0, 25.6]
pressure_readings = [101.3, 102.1, 100.7, 103.4, 99.8, 104.2, 101.9]

# Misleading auxiliary calculations
sum_sq_diffs = sum((t - p / 10) ** 2 for t, p in zip(temperature_readings, pressure_readings))
noise_floor = sum(abs(t - 25.0) for t in temperature_readings) * 0.01
redundant_total = 0
for i in range(len(temperature_readings)):
    redundant_total += temperature_readings[i] * (i + 1)

# Core processing: detect stable cycles
stable_cycles = []
for i in range(len(temperature_readings) - 2):
    if (abs(temperature_readings[i] - temperature_readings[i+1]) < 1.5 and 
        abs(temperature_readings[i+1] - temperature_readings[i+2]) < 1.5):
        avg_temp = (temperature_readings[i] + temperature_readings[i+1] + temperature_readings[i+2]) / 3
        stability_metric = 3 - (abs(pressure_readings[i] - 101.5) / 10)
        stable_cycles.append((avg_temp, stability_metric))

# Distractor: unused helper function
def calculate_entropy(data):
    from math import log
    total = sum(data)
    if total == 0:
        return 0
    entropy = 0
    for x in data:
        prob = x / total
        if prob > 0:
            entropy -= prob * log(prob)
    return entropy

# Real computation begins
baseline = 85.0
adjustment_factor = 1.0
if len(stable_cycles) > 3:
    adjustment_factor = 1.15

# Extract impact values using lambda and filter
impact_values = list(map(lambda x: x[1] * 5, filter(lambda x: x[0] > 24.0, stable_cycles)))
impact_sum = sum(impact_values)
cycle_count = len(impact_values) if impact_values else 1

# Key statement with distractors around it
intermediate_offset = noise_floor * 0.5  # irrelevant to final result
dummy_pairs = list(combinations([1, 2, 3, 4], 2))  # dead code, no effect
efficiency_score = 0  # initialization
final_calculation = baseline * adjustment_factor + (impact_sum / cycle_count)
efficiency_score = int(final_calculation + 0.5)  # round to nearest integer

print(f"Result: {efficiency_score}")