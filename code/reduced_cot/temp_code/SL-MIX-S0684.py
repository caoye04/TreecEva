from functools import reduce

temperature_readings = [22.5, 23.1, 21.8, 24.0, 22.9]
calibration_factors = [1.02, 0.98, 1.05, 0.99, 1.01]

# Apply calibration factors to each reading
adjusted_readings = list(map(lambda temp, factor: temp * factor, temperature_readings, calibration_factors))

# Calculate the sum of adjusted readings
sum_adjusted = reduce(lambda x, y: x + y, adjusted_readings)

# Compute the average
final_adjusted_avg = sum_adjusted / len(adjusted_readings)

print(f"Result: {final_adjusted_avg}")