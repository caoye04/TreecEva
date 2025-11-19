import math
from collections import defaultdict

def process_sensor_data(readings):
    normalized_readings = []
    for temp in readings:
        # Apply logarithmic normalization if temperature is positive
        if temp > 0:
            normalized_temp = math.log(temp) * 10
        else:
            normalized_temp = 0
        
        # Apply modular correction for sensor drift (every 7th degree adjustment)
        corrected_temp = normalized_temp + (normalized_temp % 7)
        
        # Filter out invalid readings (less than 5 or greater than 50 after correction)
        if not (corrected_temp < 5 or corrected_temp > 50):
            normalized_readings.append(corrected_temp)
    
    return normalized_readings

def calculate_stability_index(processed_temps):
    # Lambda function for weighted aggregation
    aggregate = lambda temps: sum(temp ** 1.5 for temp in temps) / len(temps) if temps else 0
    return aggregate(processed_temps)

# Simulated sensor readings
sensor_readings = [2.5, 10, 0, -5, 15, 100, 7, 3.3, 50, 20]

# Process data through climate model pipeline
valid_temperatures = process_sensor_data(sensor_readings)
stability_index = calculate_stability_index(valid_temperatures)

print(f"Result: {round(stability_index, 2)}")