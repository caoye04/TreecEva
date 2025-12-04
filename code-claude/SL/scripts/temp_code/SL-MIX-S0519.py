# Environmental monitoring system analyzing air quality data

# Primary pollution measurement data (in parts per million)
pollution_readings = [4.2, 3.8, 5.1, 4.2, 3.9, 5.1, 6.3, 3.8, 4.5, 5.1]

# Reference safe levels for various environments (in parts per million)
safe_levels = [2.5, 3.8, 4.2, 5.1, 6.0, 7.2]

# Process pollution readings
pollution_level_set = set(pollution_readings)
processed_readings = (reading for reading in pollution_readings if reading > 3.5)

# Calculate statistical measures
max_pollution = max(pollution_readings)
min_pollution = min(pollution_readings)
mean_pollution = sum(pollution_readings) / len(pollution_readings)

# Process safe levels
safe_level_set = set(safe_levels)
reference_data = tuple(safe_levels)
warning_threshold = safe_level_set.union({max_pollution + 1})

# Analyze overlapping values between measurements and safe levels
overlap_count = len(pollution_level_set.intersection(safe_level_set))
unique_elements_count = len(pollution_level_set) + len(safe_level_set)

# Calculate elements that appear in both sets
common_elements = unique_elements_count - len(pollution_level_set.symmetric_difference(safe_level_set))

# Additional analysis (not directly related to result)
danger_readings = sum(1 for reading in pollution_readings if reading > max(safe_levels))
safety_index = 10 - (mean_pollution / max(safe_levels) * 5)

print(f"Result: {common_elements}")