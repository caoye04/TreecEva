from collections import defaultdict

# Sensor data simulation
temperature_readings = [22, 24, 26, 35, 37]
humidity_readings = [45, 50, 55, 62, 70]

# Aggregating average conditions
avg_temp = sum(temperature_readings) / len(temperature_readings)
avg_humidity = sum(humidity_readings) / len(humidity_readings)

# Categorizing temperature condition
temperature_status = 'high' if avg_temp > 30 else 'normal'

# Define critical states using set operations
critical_states = {'high', 'extreme'}

# Redundant but harmless distractor: default dict for unused metric
sensor_metrics = defaultdict(int)
sensor_metrics['stability_index'] += 1  # Not used in logic

# Main control flow with logical operations
humidity_level = int(avg_humidity)
threshold_alert = temperature_status in critical_states and humidity_level > 60

# Print result for evaluation
print(f"Result: {threshold_alert}")