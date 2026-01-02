from itertools import pairwise

# Sensor readings in millivolts taken at consecutive time intervals
time_series = [230, 245, 240, 258, 262, 249, 271]

# Compute absolute differences between consecutive readings
differences = [abs(curr - prev) for prev, curr in pairwise(time_series)]

# Track cumulative fluctuation for diagnostic purposes (irrelevant to final answer)
cumulative_fluctuation = sum(differences)
baseline = min(time_series)
adjusted_readings = [voltage - baseline for voltage in time_series]

# Determine the maximum single-step change in sensor voltage
result = max(differences)

print(f"Result: {result}")