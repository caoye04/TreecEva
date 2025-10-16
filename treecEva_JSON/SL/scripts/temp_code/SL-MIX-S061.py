import math
from functools import reduce
from collections import namedtuple

# Define a sensor reading structure
SensorData = namedtuple('SensorData', ['sensor_id', 'raw_value', 'timestamp'])

# Initial sensor readings
readings = [
    SensorData('THERMAL_01', 245.7, 1623456789),
    SensorData('THERMAL_02', 198.3, 1623456791),
    SensorData('THERMAL_03', 305.2, 1623456793),
    SensorData('THERMAL_04', 176.8, 1623456795),
    SensorData('THERMAL_05', 287.4, 1623456797)
]

# Process readings with mathematical transformations
processed_values = []
for reading in readings:
    # Apply logarithmic scaling
    scaled_value = math.log(reading.raw_value) * 10
    
    # Early return for outlier values
    if scaled_value < 50 or scaled_value > 60:
        continue
    
    # Apply exponential adjustment
    adjusted_value = math.exp(scaled_value / 20)
    processed_values.append(adjusted_value)

# Calculate stability index using functional programming
if len(processed_values) > 0:
    # Compute the geometric mean of processed values
    product = reduce(lambda x, y: x * y, processed_values)
    geometric_mean = product ** (1/len(processed_values))
    
    # Apply final transformation
    stability_index = round(math.log(geometric_mean) * 100)
else:
    stability_index = 0

print(f"Result: {stability_index}")