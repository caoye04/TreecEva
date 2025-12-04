# Weather station temperature analysis
temp_readings = [28.5, 27.3, 30.1, 25.8, 31.7, 29.2, 26.4]
threshold = 28.0

# Calculate average of all readings
avg_temp = sum(temp_readings) / len(temp_readings)

# Find the maximum temperature
max_temp = max(temp_readings)

# Count readings above threshold
above_count = sum(1 for temp in temp_readings if temp > threshold)

# Sum of temperatures above threshold
filtered_total = sum(temp_readings[i] for i in range(len(temp_readings)) if temp_readings[i] > threshold)

# Calculate the difference between max and average
max_diff = max_temp - avg_temp

# Determine final status based on conditions
status = "Warning" if above_count > 3 else "Normal"

print(f"Result: {filtered_total}")