from itertools import compress

# Simulate sensor readings with periodic noise
timestamps = list(range(10, 20))
raw_readings = [4.5, 5.2, 3.8, 4.0, 5.5, 6.2, 3.9, 4.1, 5.0, 4.8]

# Identify valid intervals (every other 2-second window)
valid_windows = [i // 2 % 2 == 0 for i in range(len(timestamps))]

# Apply data filter using boolean mask
clean_readings = list(compress(raw_readings, valid_windows))

# Compute squares of cleaned readings above threshold
squared_values = [x ** 2 for x in clean_readings if x > 4.0]

# Filter out unusually high squares (potential residual spikes)
filtered_squares = [sq for sq in squared_values if sq < 25.0]

# Final aggregation
result = sum(filtered_squares)
print(f"Result: {result}")