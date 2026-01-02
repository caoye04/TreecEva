temperatures = [25, 30, 35, 40, 45]
humidity_levels = [50, 60, 65, 70, 80]

# Calculate heat index approximation using temperature and humidity
adjusted_temperatures = []
for i in range(len(temperatures)):
    temp = temperatures[i]
    humidity = humidity_levels[i]
    # Simplified heat index formula: T + 0.555*(0.55*RH - 14)
    adjusted_temp = temp + 0.555 * (0.55 * humidity - 14)
    adjusted_temperatures.append(round(adjusted_temp, 2))

# Slice to exclude the first reading (calibration period)
calibrated_readings = adjusted_temperatures[1:]

# Accumulate total heat index from calibrated data
total_heat_index = sum(calibrated_readings)

Result: {round(total_heat_index, 2)}