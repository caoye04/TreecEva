from itertools import zip_longest
import math

# Weather monitoring system for multiple cities
def calculate_temperature_priority(readings, thresholds):
    # Convert readings to Celsius if needed
    celsius_readings = []
    for reading in readings:
        if reading['unit'] == 'F':
            # Convert Fahrenheit to Celsius
            celsius = (reading['value'] - 32) * 5/9
            celsius_readings.append(round(celsius, 1))
        else:
            celsius_readings.append(reading['value'])
    
    # Track cities exceeding thresholds
    cities_above_threshold = []
    for i, (reading, threshold) in enumerate(zip(readings, thresholds)):
        if celsius_readings[i] > threshold:
            cities_above_threshold.append(reading['city'])
    
    # Calculate temperature ranges (not used in final calculation)
    temp_range = max(celsius_readings) - min(celsius_readings)
    avg_temp = sum(celsius_readings) / len(celsius_readings)
    
    # Apply weighting based on deviation from average
    weighted_values = list(map(lambda x: abs(x - avg_temp), celsius_readings))
    
    # Apply transformation to readings
    transformed = []
    for i, temp in enumerate(celsius_readings):
        if i % 2 == 0:
            transformed.append(temp + 3)
        else:
            transformed.append(temp - 2)
    
    # Filter readings based on complex condition
    filtered_temperatures = [t for i, t in enumerate(transformed) 
                           if i < len(celsius_readings) // 2 or t > avg_temp]
    
    # This is the key calculation for priority value
    priority_value = sum(filtered_temperatures)
    
    # Additional calculations that don't affect the result
    adjustment_factor = math.sin(math.radians(30)) * temp_range
    normalized_priority = priority_value / len(filtered_temperatures)
    
    return {
        'priority': priority_value,
        'cities_at_risk': len(cities_above_threshold),
        'adjustment': adjustment_factor
    }

# Sample data
temperature_readings = [
    {'city': 'Berlin', 'value': 24, 'unit': 'C'},
    {'city': 'Paris', 'value': 77, 'unit': 'F'},
    {'city': 'Rome', 'value': 30, 'unit': 'C'},
    {'city': 'London', 'value': 68, 'unit': 'F'}
]

city_thresholds = [25, 22, 28, 18]

result = calculate_temperature_priority(temperature_readings, city_thresholds)
print(f"Result: {result['priority']}")