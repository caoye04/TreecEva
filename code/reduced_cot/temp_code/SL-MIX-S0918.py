from collections import namedtuple
import numpy as np

# Climate data structure
MonthData = namedtuple('MonthData', ['precipitation', 'weight'])

# Monthly precipitation measurements (mm) with temporal weights
climate_readings = [
    MonthData(precipitation=87.5, weight=1.0),
    MonthData(precipitation=92.3, weight=1.2),
    MonthData(precipitation=78.9, weight=1.4),
    MonthData(precipitation=105.2, weight=1.6),
    MonthData(precipitation=93.8, weight=1.8)
]

# Calculate weighted sum using functional approach
weighted_values = map(lambda reading: reading.precipitation * reading.weight, climate_readings)
weight_sum = sum(weighted_values)
total_weights = sum(map(lambda reading: reading.weight, climate_readings))

# Compute final climate index
climate_index = round(weight_sum / total_weights, 2)
print(f"Result: {climate_index}")