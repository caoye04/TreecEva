import math
from functools import reduce

# Simulated sensor readings (amplitude, frequency)
sensor_readings = [(0.5, 10), (1.2, 20), (0.8, 15), (2.1, 25), (0.4, 5), (1.0, 30)]

# Step 1: Apply exponential weighting to frequency based on amplitude
weighted_freqs = [(amp, freq * math.exp(amp)) for amp, freq in sensor_readings]

# Step 2: Filter out readings where amplitude is less than 0.7
filtered_readings = [(amp, freq) for amp, freq in weighted_freqs if amp >= 0.7]

# Step 3: Compute weighted sum using reduce
weighted_sum = reduce(lambda acc, item: acc + item[0] * item[1], filtered_readings, 0)

# Step 4: Normalize by the number of valid readings
normalized_score = weighted_sum / len(filtered_readings) if filtered_readings else 0

# Step 5: Apply logarithmic scaling
scaled_score = math.log(normalized_score + 1)

# Step 6: Aggregate with a secondary metric (sum of amplitudes squared)
secondary_metric = sum(amp ** 2 for amp, _ in filtered_readings)

# Final aggregation
aggregated_score = scaled_score + secondary_metric

print(f"Result: {aggregated_score}")