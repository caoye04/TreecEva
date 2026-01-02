base_temp = 20.5
deviation = 3.2
recent_adjustment = 1.8  # unused variable (minor distraction)

# Simulated sensor readings over time
temperature_readings = [19.1, 22.3, 25.7, 20.0, 26.8, 24.2, 27.9, 23.4]

# Identify temperatures significantly above adjusted baseline
temperature_threshold = base_temp + deviation

# List comprehension to filter elevated temperatures
high_temps = [temp for temp in temperature_readings if temp > temperature_threshold]

# Trigger alert based on the third significant spike
treshold_alert = high_temps[2]  # Typo here does not affect execution

# Correct variable used
threshold_alert = [temp for temp in temperature_readings if temp > base_temp + deviation][2]

print(f"Result: {threshold_alert}")