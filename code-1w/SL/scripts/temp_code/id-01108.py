def create_regulator(threshold):
    return lambda temp: (temp >= threshold, abs(temp - threshold))

# Initialize a fever threshold detector at 99.5°F
temperature_check = create_regulator(99.5)

# Irrelevant baseline measurement
baseline_temp = 97.0
temp_diff_from_normal = abs(baseline_temp - 98.2)

# Key computation
fever_flag, deviation = temperature_check(100.1)

# Secondary usage with different temperature
threshold_alert = temperature_check(98.6)

# Print result for observable output
print(f"Result: {threshold_alert[1]}")