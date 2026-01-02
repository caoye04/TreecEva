from itertools import compress

# Sensor data validation and filtering based on environmental thresholds
temperature_readings = [23.5, 19.0, 27.3, 30.1, 18.2, 25.8, 24.6]
humidity_readings = [45, 60, 30, 55, 70, 50, 40]

# Criteria: select readings where temp > 24.0 and humidity < 65
valid_conditions = [(t > 24.0) and (h < 65) for t, h in zip(temperature_readings, humidity_readings)]

# Extract valid temperature readings using boolean selection
selected_temps = list(compress(temperature_readings, valid_conditions))

# Apply calibration offset to sensor data
adjusted_temps = [round(t - 0.2, 1) for t in selected_temps]

# Filter out any adjusted values below 24.5 for final analysis
filtered_data = [t for t in adjusted_temps if t >= 24.5]

# Final aggregation
filtered_sum = sum(filtered_data)

print(f"Result: {filtered_sum}")