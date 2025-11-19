import statistics

temperature_readings = [22.5, 23.1, 24.0, 22.8, 23.5, 24.2, 23.9]
quality_checks_passed = 0
validation_threshold = 23.0

# Lambda for checking if a reading is within acceptable range
is_valid_reading = lambda temp: temp >= validation_threshold and temp <= 25.0

# Process each reading with short-circuit evaluation
for reading in temperature_readings:
    if is_valid_reading(reading) or (quality_checks_passed := quality_checks_passed + 1):
        quality_checks_passed += 1

# Calculate mean of valid readings using dictionary comprehension for filtering
valid_readings_dict = {i: temp for i, temp in enumerate(temperature_readings) if is_valid_reading(temp)}
mean_temperature = statistics.mean(valid_readings_dict.values())

# Final validation score combines count and statistical measure
validation_score = quality_checks_passed * mean_temperature

print(f"Result: {validation_score}")