from itertools import compress

# Sensor readings from a thermal monitoring system
time_stamps = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8]
raw_readings = [23.4, 24.1, 25.3, 26.0, 25.8, 27.2, 28.1, 29.0]

# Identify stable period using rate of change
rate_of_change = [abs(raw_readings[i+1] - raw_readings[i]) for i in range(len(raw_readings)-1)]
stable_mask = [rate < 1.0 for rate in rate_of_change]

# Extend mask to match original length (assume last point is stable if penultimate was)
stable_mask.append(stable_mask[-1])

# Filter readings during thermally stable periods
filtered_readings = list(compress(raw_readings, stable_mask))

# Scale by calibration factor
scaled_readings = [r * 1.02 for r in filtered_readings]

# Critical threshold determination
energy_threshold = max(scaled_readings)

Result: {energy_threshold}