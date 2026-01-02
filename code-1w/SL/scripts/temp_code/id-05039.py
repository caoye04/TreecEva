from collections import defaultdict

# Simulate sensor readings with timestamps
timestamp_readings = [
    (1, 23.5), (2, 24.1), (3, 22.8), (4, 25.6), (5, 26.0),
    (6, 23.9), (7, 24.4), (8, 27.3), (9, 25.1), (10, 24.8)
]

# Irrelevant auxiliary mapping (minimal distraction)
status_map = defaultdict(lambda: 'unknown')
for i in range(1, 11):
    if i % 3 == 0:
        status_map[i] = 'calibrating'
    else:
        status_map[i] = 'active'

# Extract temperature values
temperatures = [temp for _, temp in timestamp_readings]

# Apply transformation: convert to Fahrenheit and round
temp_fahrenheit = [round((t * 9/5) + 32, 1) for t in temperatures]

# Define threshold function using lambda
critical_threshold = lambda x: x > 75.0

# Filter high-temperature readings
high_temp_flags = [critical_threshold(temp) for temp in temp_fahrenheit]
filtered_data = [temp for temp, flag in zip(temp_fahrenheit, high_temp_flags) if flag]

# Final computation step
filtered_sum = sum(filtered_data)

print(f"Result: {filtered_sum}")