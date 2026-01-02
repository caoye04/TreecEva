def calculate_total(deviations):
    weights = [0.2, 0.3, 0.5]
    weighted_sum = 0
    for i, (key, value) in enumerate(deviations.items()):
        weight = weights[i % len(weights)]
        weighted_sum += value * weight
    return round(weighted_sum, 3)

# Data preprocessing
readings = [102, 98, 100]
baseline = 100

# Compute deviations from baseline as percentages
deviation_percentages = [(abs(r - baseline) / baseline) * 100 for r in readings]

# Map sensor names to their deviation using zip and dictionary comprehension
sensors = ['sensor_A', 'sensor_B', 'sensor_C']
deviation_map = {k: v for k, v in zip(sensors, deviation_percentages)}

# Apply correction factor using lambda (irrelevant to final result but adds minor distraction)
correction_factor = lambda x: x * 1.05
adjusted_A = correction_factor(deviation_map['sensor_A'])

# Critical computation step
final_score = calculate_total(deviation_map)

print(f"Result: {final_score}")