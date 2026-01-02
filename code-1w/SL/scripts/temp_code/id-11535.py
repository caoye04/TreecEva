import math

# Sensor data with some noise
temperature_readings = [20.5, 19.8, 21.0, 22.3, 18.7, 20.1, 19.9, 23.4, 24.0, 18.2]

# Irrelevant distraction: unused variable (minimal interference)
baseline_offset = 0.5

# Define a lambda to filter valid operating range (19.0 to 23.5 inclusive)
is_operational = lambda x: 19.0 <= x <= 23.5

# Use list comprehension to filter and round valid readings
cleaned_readings = [round(temp, 1) for temp in temperature_readings if is_operational(temp)]

# Further process: convert to set to remove duplicates (though none here)
unique_readings = set(cleaned_readings)

# Sort and convert back to list for consistent behavior
filtered_data = sorted(list(unique_readings))

# Key computation step
result = sum(filtered_data)

print(f"Result: {result}")