import math
from functools import reduce

def outlier_filter(readings):
    mean_val = sum(readings) / len(readings)
    std_dev = (sum((x - mean_val) ** 2 for x in readings) / len(readings)) ** 0.5
    return [x for x in readings if abs(x - mean_val) <= 2 * std_dev]

sensor_data = [1023, 890, 1025, 2048, 1018, 1030, 900, 1020, 3000, 1022]
filtered_readings = outlier_filter(sensor_data)

normalize = lambda x: (x % 256) + (1.0 if x > 1024 else 0.5)
weights = [0.1, 0.15, 0.2, 0.25, 0.3]

processed_values = list(map(normalize, filtered_readings[:5]))
weighted_components = [val * wt for val, wt in zip(processed_values, weights)]
aggregated_signal_strength = round(reduce(lambda a, b: a + b, weighted_components) * 100)

print(f"Result: {aggregated_signal_strength}")