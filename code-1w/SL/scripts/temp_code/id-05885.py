def analyze_temperature_readings():
    raw_readings = [23.5, 19.0, 27.3, 32.1, 18.8, 24.7, 31.2, 26.4, 20.9]
    
    # Normalize readings to integer Celsius for threshold filtering
    integer_readings = [int(temp) for temp in raw_readings]
    
    # Identify valid range (above freezing and below extreme heat)
    valid_temps = [t for t in integer_readings if 0 < t < 30]
    
    # Take the last four acceptable measurements in reverse chronological order
    reversed_valid_slice = valid_temps[-4:][::-1]
    
    # Compute total of reversed valid window
    filtered_sum = sum(reversed_valid_slice)
    
    # Auxiliary variable (irrelevant to final result)
    avg_temp = sum(raw_readings) / len(raw_readings)
    
    return filtered_sum

result = analyze_temperature_readings()
print(f"Result: {result}")