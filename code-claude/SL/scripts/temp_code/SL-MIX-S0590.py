# Temperature monitoring system for a greenhouse
# Processing hourly temperature readings to find unique values in range

morning_readings = [18.5, 19.0, 20.5, 22.0, 23.5, 23.5]
day_readings = [24.0, 25.5, 26.0, 26.0, 25.5, 24.5]
evening_readings = [23.0, 21.5, 20.0, 19.5, 19.5]
night_readings = [18.0, 17.5, 17.5, 17.0, 16.5]

# Combine all readings
all_readings = morning_readings + day_readings
all_readings.extend(evening_readings)
all_readings.extend(night_readings)

# Process readings within optimal growing range (18.0 - 24.0 degrees)
filtered_readings = []
for i, temp in enumerate(all_readings):
    if 18.0 <= temp <= 24.0:
        filtered_readings.append(temp)

# Count unique temperature readings in the optimal range
unique_count = len(set(filtered_readings))

# Calculate average temperature for reference
avg_temp = sum(all_readings) / len(all_readings)

print(f"Result: {unique_count}")