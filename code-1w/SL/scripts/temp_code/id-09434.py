import math

# Simulate sensor readings with some noise
data_readings = [3.5, -2.1, 8.9, 0.0, -5.3, 12.7, 4.6]

# Irrelevant constant (mild distractor)
CALIBRATION_FACTOR = 1.02

# Apply threshold filter using list comprehension and lambda
valid_condition = lambda x: x > 0 and math.isclose(round(x * 2) / 2, x, abs_tol=0.01)
processed_data = [round(x * 1.1, 1) for x in data_readings]

# Filter valid measurements above zero and with precise decimal
filtered_data = [x for x in processed_data if valid_condition(x)]

# Compute final result
filtered_sum = sum(filtered_data)

# Print result as required
print(f"Result: {filtered_sum}")