from collections import defaultdict

# Simulate sensor readings with minor calibration offsets
calibration_factors = [0.98, 1.02, 0.99, 1.01, 1.00]
sensor_readings = [200, 180, 210, 195, 220]

# Apply calibration to each reading using zip
adjusted_readings = [reading * factor for reading, factor in zip(sensor_readings, calibration_factors)]

# Categorize readings by range using defaultdict
categorized = defaultdict(list)
for val in adjusted_readings:
    if val < 190:
        categorized['low'].append(val)
    elif val < 200:
        categorized['medium'].append(val)
    else:
        categorized['high'].append(val)

# Calculate derived weights based on category counts
category_weights = {}
for key, vals in categorized.items():
    category_weights[key] = len(vals) * 1.5

# Adjust weights by index position using enumerate
adjusted_weights = []
for i, weight in enumerate(category_weights.values()):
    adjusted_weights.append(weight + (i * 0.1))

total_weight = sum(adjusted_weights)
print(f"Result: {total_weight}")