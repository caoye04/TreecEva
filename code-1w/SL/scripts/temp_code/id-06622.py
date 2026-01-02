def process_temperature_readings(readings_str, threshold):
    # Split the comma-separated string into individual numeric strings
    raw_values = readings_str.split(',')
    
    # Convert to floats using lambda and map
    temperatures = list(map(lambda x: float(x.strip()), raw_values))
    
    # Calculate baseline statistics (distractor variables)
    avg_temp = sum(temperatures) / len(temperatures)
    deviation = [abs(t - avg_temp) for t in temperatures]
    
    # Filter values above threshold
    filtered_values = [t for t in temperatures if t > threshold]
    
    # Compute the final result
    filtered_sum = sum(filtered_values)
    print(f"Result: {filtered_sum}")

# Input data
sensor_data = "23.5, 19.0, 27.2, 30.1, 18.9, 24.3, 35.0"
config_threshold = 25.0

process_temperature_readings(sensor_data, config_threshold)