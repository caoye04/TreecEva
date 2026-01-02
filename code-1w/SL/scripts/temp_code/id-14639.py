from itertools import takewhile

# Sensor data simulation: daily temperature readings in Celsius
temperatures = [22, 24, 19, 25, 27, 23, 20, 26, 28, 21, 18]

# Calculate average temperature
sum_temp = sum(temperatures)
count = len(temperatures)
temp_average = sum_temp / count

# Define threshold for high temperature alert
threshold = 23.5

# Find midpoint index (for median approximation)
mid_index = len(temperatures) // 2

# Get extreme values
temperature_extremes = (min(temperatures), max(temperatures))

# Determine equilibrium point based on average vs threshold
equilibrium_point = temperatures[mid_index] if temp_average < threshold else temperature_extremes[1]

# Filter consecutive acceptable temperatures below threshold
acceptable_run = list(takewhile(lambda x: x < threshold, sorted(temperatures)))

# Irrelevant metric: count of acceptable readings (distractor)
acceptable_count = len(acceptable_run)

# Output the target result
print(f"Result: {equilibrium_point}")