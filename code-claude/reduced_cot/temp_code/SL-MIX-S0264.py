# Weather station temperature processing
raw_temperatures = [22.5, 23.0, 22.5, 21.8, 24.1, 23.0, 20.5, 21.8, 24.1]

# Process temperatures and filter out any below 21 degrees
min_threshold = 21.0
filtered_temperatures = list(filter(lambda x: x >= min_threshold, raw_temperatures))

# Calculate the average temperature (not needed for final result)
avg_temp = sum(filtered_temperatures) / len(filtered_temperatures)

# Get the count of unique temperature readings
unique_count = len(set(filtered_temperatures))

# Calculate temperature range for reporting
temp_range = max(filtered_temperatures) - min(filtered_temperatures)

# Generate summary data
summary = {
    "unique_readings": unique_count,
    "average": round(avg_temp, 1),
    "range": temp_range
}

print(f"Result: {unique_count}")