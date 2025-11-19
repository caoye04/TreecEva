import math
from functools import reduce

# Simulated sensor readings (in degrees Celsius)
sensor_readings = [22.5, 25.0, 27.3, 30.1, 19.8, 21.4, 26.7, 23.9, 28.2, 24.6]

# Apply logarithmic scaling to each reading
scaled_readings = list(map(lambda x: math.log(x) if x > 0 else 0, sensor_readings))

# Filter out readings below a threshold (log(22.0))
threshold = math.log(22.0)
filtered_readings = list(filter(lambda x: x >= threshold, scaled_readings))

# Apply exponent-based normalization
normalized_readings = [math.exp(x) for x in filtered_readings]

# Compute aggregate using reduce
aggregate = reduce(lambda a, b: a + b, normalized_readings, 0)

# Apply conditional normalization based on aggregate value
if aggregate > 100:
    normalized_aggregate = math.log(aggregate) * 10
elif aggregate > 50:
    normalized_aggregate = math.sqrt(aggregate) * 5
else:
    normalized_aggregate = aggregate * 2

# Apply final string transformation for logging (not affecting numerical result)
log_entry = f"Processed {len(sensor_readings)} readings. Final aggregate: {normalized_aggregate}"

print(f"Result: {normalized_aggregate}")