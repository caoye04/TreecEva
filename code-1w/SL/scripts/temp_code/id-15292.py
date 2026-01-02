from itertools import compress

# Sensor readings with some noise
data_readings = [105, 203, 98, 0, 110, 200, 95, 0, 102]

# Validity mask based on non-zero and plausible range
validity_mask = [(0 < x < 250) for x in data_readings]

# Filter valid sensor data using compress
filtered_data = list(compress(data_readings, validity_mask))

# Remove potential outliers above 200
filtered_data = [x for x in filtered_data if x <= 200]

# Compute final sum of clean data
filtered_sum = sum(filtered_data)

print(f"Result: {filtered_sum}")