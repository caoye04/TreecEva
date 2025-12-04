# Weather data analysis for temperature anomalies

# Raw temperature readings (Celsius) from multiple stations
temperature_readings = [23.4, 22.1, 25.7, -999.0, 21.5, 24.3, -999.0, 26.2, 19.8]

# Filter out invalid readings (marked as -999.0) and calculate statistics
invalid_marker = -999.0
valid_temps = [t for t in temperature_readings if t != invalid_marker]

# Calculate temperature thresholds
min_valid = min(valid_temps)
max_valid = max(valid_temps)
threshold = (max_valid + min_valid) / 2

# Extract temperatures above threshold using lambda and filter
above_threshold = list(filter(lambda x: x > threshold, valid_temps))

# Extract temperatures in the middle range using slicing
sorted_temps = sorted(valid_temps)
middle_temps = sorted_temps[1:-1]

# Combine specific temperatures for analysis
analysis_set = middle_temps + above_threshold[-2:]

# Apply correction factor based on modular arithmetic
correction = len(analysis_set) % 3
if correction == 0:
    corrected_temps = analysis_set
else:
    corrected_temps = analysis_set[:-correction]

# Filter temperatures within 20% of the maximum
filter_threshold = 0.8 * max_valid
filtered_temps = [t for t in corrected_temps if t >= filter_threshold]

# Calculate sum of filtered temperatures
filtered_sum = sum(filtered_temps)
print(f"Result: {filtered_sum}")