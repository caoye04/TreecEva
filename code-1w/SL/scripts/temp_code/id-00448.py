from itertools import dropwhile

# Sensor readings in degrees Celsius
temperature_readings = [22, 25, 28, 31, 33, 36, 38, 40]

# Filter out readings below freezing (irrelevant for this system)
filtered_readings = [temp for temp in temperature_readings if temp > 0]

# Apply conditional logic to detect first reading above operational threshold
threshold_flag = next(dropwhile(lambda x: x <= 30, filtered_readings), None)

Result: threshold_flag