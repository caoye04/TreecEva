# Function to analyze sensor readings and find unique remainder patterns
readings = [15, 22, 8, 36, 29, 43, 50, 15, 22]
base_value = 3
threshold = 20

# Filter readings above threshold
filtered_data = []
for reading in readings:
    if reading > threshold:
        filtered_data.append(reading)
    else:
        # Just tracking readings below threshold
        below_threshold = len(readings) - len(filtered_data)

# Calculate a metric based on filtered readings
total = sum(filtered_data)
average = total / len(filtered_data) if filtered_data else 0

# Find unique remainders when divided by 7
unique_count = len(set(map(lambda x: x % 7, filtered_data)))

# Final result - number of unique remainder patterns
print(f"Result: {unique_count}")