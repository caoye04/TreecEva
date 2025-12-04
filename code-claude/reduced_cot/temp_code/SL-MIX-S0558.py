def celsius_to_fahrenheit(temp):
    return temp * 9/5 + 32

def fahrenheit_to_celsius(temp):
    return (temp - 32) * 5/9

def kelvin_to_celsius(temp):
    return temp - 273.15

def temperature_conversion(readings):
    # Extract only the valid temperature readings (positive values)
    valid_readings = [r for r in readings if r > 0]
    
    # Calculate statistics for logging purposes
    stats = {
        "max": max(valid_readings) if valid_readings else 0,
        "min": min(valid_readings) if valid_readings else 0,
        "count": len(valid_readings)
    }
    
    # Process the readings based on different temperature scales
    celsius_values = []
    kelvin_values = []
    fahrenheit_values = []
    
    for i, reading in enumerate(valid_readings):
        # Every third reading is in Kelvin
        if i % 3 == 0:
            kelvin_values.append(reading)
            celsius_values.append(kelvin_to_celsius(reading))
        # Every fifth reading is in Fahrenheit
        elif i % 5 == 0:
            fahrenheit_values.append(reading)
            celsius_values.append(fahrenheit_to_celsius(reading))
        # All other readings are already in Celsius
        else:
            celsius_values.append(reading)
    
    # Calculate sensor health metrics (unused in final result)
    sensor_health = sum(abs(c - sum(celsius_values)/len(celsius_values)) 
                        for c in celsius_values) / len(celsius_values) if celsius_values else 0
    
    # Apply data quality filters
    filtered_celsius = [c for c in celsius_values if -50 <= c <= 60]
    
    # Process the data through a sliding window (distraction)
    window_size = 3
    sliding_averages = []
    for i in range(len(filtered_celsius) - window_size + 1):
        window_avg = sum(filtered_celsius[i:i+window_size]) / window_size
        sliding_averages.append(window_avg)
    
    # Calculate the median temperature (this is what we actually want)
    sorted_temps = sorted(filtered_celsius)
    n = len(sorted_temps)
    if n % 2 == 0:
        median = (sorted_temps[n//2 - 1] + sorted_temps[n//2]) / 2
    else:
        median = sorted_temps[n//2]
    
    # Apply some unnecessary transformations
    transformed_data = {(i, v) for i, v in enumerate(filtered_celsius)}
    data_hash = sum(hash(item) % 1000 for item in transformed_data)
    
    # Calculate alternative metrics (not used in final result)
    alternative_result = sum(filtered_celsius) / len(filtered_celsius) if filtered_celsius else 0
    weighted_result = sum(t * (i+1) for i, t in enumerate(filtered_celsius)) / sum(range(1, len(filtered_celsius)+1)) if filtered_celsius else 0
    
    # The actual result we want is the median, rounded to 2 decimal places
    return round(median, 2)

# Sample temperature readings from multiple sensors
all_readings = [301.15, 24.5, 22.8, 77.0, 19.2, 298.15, 25.7, -10.5, 80.6, 26.3, 300.0, 23.1]

# Filter out the invalid readings (below a certain threshold)
threshold = -5.0
filtered_readings = {x for x in all_readings if x > threshold}

# Extract specific readings for analysis
selected_readings = list(filtered_readings)[1:11]

# Apply the temperature conversion function
final_temperature = temperature_conversion(selected_readings)

# Print the result
print(f"Result: {final_temperature}")