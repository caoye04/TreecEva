from itertools import compress

# Sensor data and quality flags
data_readings = [107, 214, 95, 301, 88, 152]
quality_flags = [True, True, False, True, False, True]

# Filtering valid readings using itertools.compress
valid_readings = list(compress(data_readings, quality_flags))

# System thresholds and computed weights
min_limit = 100
weight_func = lambda x: 0.1 if x < min_limit else 0.25

weighted_sum = 0
threshold_score = 0

for reading in valid_readings:
    weight = weight_func(reading)
    weighted_sum += reading * weight
    if weighted_sum > 100:
        threshold_score = int(weighted_sum)
        break

print(f"Target result: {threshold_score}")