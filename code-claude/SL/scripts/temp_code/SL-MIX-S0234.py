def filtered_data(values):
    # Filter values based on temperature thresholds
    is_valid = lambda x: 15 <= x <= 30
    valid_temps = list(filter(is_valid, values))
    
    # Calculate average of valid temperatures
    if valid_temps:
        return sum(valid_temps) / len(valid_temps)
    return 0

# Weather station temperature readings (in Celsius)
temperatures = [12, 18, 25, 32, 16, 22, 28, 14, 19]

# Extra metadata about readings
timestamps = ['08:00', '10:00', '12:00', '14:00', '16:00', '18:00', '20:00', '22:00', '00:00']
station_id = 'WS-104'

# Process the temperature data
result = filtered_data(temperatures)
print(f"Result: {result}")