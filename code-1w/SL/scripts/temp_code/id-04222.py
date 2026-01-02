temperatures_celsius = [23.5, 19.0, 27.3, 31.2, 16.8]

# Calculate average temperature
total = sum(temperatures_celsius)
adjusted_avg = total / len(temperatures_celsius)

# Apply calibration offset
offset = 2.1
final_temperature = adjusted_avg + offset

# Irrelevant tracking variable (minimal distraction)
count_above_20 = len([t for t in temperatures_celsius if t > 20])

Result: final_temperature