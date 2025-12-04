# Weather station temperature analysis
# Analyzing temperature readings from different times of day

temperature_readings = [23.5, 22.8, 24.2, 21.9, 25.1, 23.0]

# Flag to determine if we should use Celsius or Fahrenheit
use_celsius = True

# Get number of valid readings (even-indexed values only)
valid_readings = len([i for i in range(len(temperature_readings)) if i % 2 == 0])

# Calculate the sum of temperatures at even positions
temperature_sum = 0
for i in range(len(temperature_readings)):
    # Only consider readings at even indices
    if i % 2 == 0:
        temperature_sum += temperature_readings[i]

# Alternative calculation using list comprehension
average_temperature = sum([temperature_readings[i] for i in range(len(temperature_readings)) if i % 2 == 0]) / valid_readings

# Convert to Fahrenheit if needed
if not use_celsius:
    average_temperature = average_temperature * 9/5 + 32

print(f"Result: {average_temperature}")