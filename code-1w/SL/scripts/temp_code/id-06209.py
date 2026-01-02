from collections import Counter
from itertools import groupby

# Simulated sensor readings with some noise
temperature_readings = [23.5, 24.0, 24.0, 23.5, 25.1, 25.1, 25.1, 26.3, 27.0, 27.0, 26.3]

# Step 1: Count frequency of each reading
reading_counts = Counter(temperature_readings)

# Identify stable readings (occur more than once)
stable_threshold = 2
stable_readings = [temp for temp, count in reading_counts.items() if count >= stable_threshold]

# Step 2: Filter original data to keep only stable temperature values
filtered_data = [temp for temp in temperature_readings if temp in stable_readings]

# Step 3: Apply small calibration adjustment using lambda
calibrate = lambda x: round(x + 0.1, 1)
adjusted_data = list(map(calibrate, filtered_data))

# Step 4: Compute sum of filtered (unadjusted) data
filtered_sum = sum(filtered_data)

# Irrelevant distraction: grouping by whole number part
grouped = {k: list(g) for k, g in groupby(adjusted_data, key=int)}

# Output target result
print(f"Result: {filtered_sum}")