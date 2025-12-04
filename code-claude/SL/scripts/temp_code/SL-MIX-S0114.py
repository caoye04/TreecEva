# Temperature analysis program
temperature_readings = [22.5, 19.8, 24.3, 25.1, 18.7, 23.9, 26.2, 20.5]
humidity_values = [45, 60, 52, 48, 70, 55, 42, 58]

# Calculate average temperature
avg_temp = sum(temperature_readings) / len(temperature_readings)

# Find the median temperature by sorting
sorted_temps = sorted(temperature_readings)
median_temp = (sorted_temps[3] + sorted_temps[4]) / 2

# Define temperature threshold based on median
threshold = median_temp - 1

# Create a dictionary mapping temperatures to humidity
temp_humidity_map = {temp: humid for temp, humid in zip(temperature_readings, humidity_values)}

# Filter temperatures above threshold
filtered_count = len(list(filter(lambda x: x > threshold, temperature_readings)))

# Get humidity values for temperatures above threshold
high_temp_humidities = [temp_humidity_map[temp] for temp in temperature_readings if temp > threshold]

print(f"Result: {filtered_count}")