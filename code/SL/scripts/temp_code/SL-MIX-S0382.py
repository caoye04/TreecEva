temperature_readings = [15.2, 18.7, 22.4, 19.8, 25.3, 17.9, 21.5]
calibration_offset = 0.5
threshold_temp = 20.0

# Process temperature data
adjusted_temps = [temp + calibration_offset for temp in temperature_readings]
filtered_temps = [temp for temp in adjusted_temps if temp >= threshold_temp]

# Distractor calculations (not used in final result)
avg_temp = sum(temperature_readings) / len(temperature_readings)
max_temp = max(temperature_readings)
min_temp = min(temperature_readings)
temp_variance = sum((temp - avg_temp) ** 2 for temp in temperature_readings) / len(temperature_readings)

# Process filtered data
processed_data = [round(temp * 1.1, 2) for temp in filtered_temps]
final_temperature = processed_data[-1]

print(f"Target result: {final_temperature}")