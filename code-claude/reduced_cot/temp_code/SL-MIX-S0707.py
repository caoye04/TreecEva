# Temperature sensor data processing

# Raw temperature readings (in Celsius) over a 24-hour period
temperature_readings = [22.5, 21.8, 21.3, 20.9, 20.5, 20.8, 
                       22.1, 23.4, 25.7, 27.3, 28.9, 29.8,
                       30.2, 30.5, 29.9, 29.1, 28.3, 27.2, 
                       26.1, 25.0, 24.2, 23.5, 23.0, 22.7]

# Extract afternoon readings (indices 6-17, representing 6am-5pm)
afternoon_slice = temperature_readings[6:18]

# Calculate average afternoon temperature
average_afternoon = sum(afternoon_slice) / len(afternoon_slice)

# Only keep readings above the afternoon average
filtered_readings = [temp for temp in afternoon_slice if temp > average_afternoon]

# Sum the filtered readings
filtered_sum = sum(filtered_readings)

# Number of readings above average
count_above_avg = len(filtered_readings)

# Average of readings above the afternoon average
average_high = filtered_sum / count_above_avg if count_above_avg > 0 else 0

print(f"Result: {filtered_sum}")