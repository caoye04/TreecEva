def analyze_temperature_readings():
    base_offset = 273.15
    raw_readings = [25.4, 18.9, 22.1, 19.5, 20.3]
    adjusted_temperatures = [temp + base_offset for temp in raw_readings]
    
    # Extract mid-segment of readings and reverse to find latest in subset
    temperature_data = adjusted_temperatures
    
    # Irrelevant variable (mild distraction)
    average_temp = sum(temperature_data) / len(temperature_data)
    
    # Key computation branch
    is_stable = len(temperature_data) > 3
    threshold_check = int(max(temperature_data) < 300.0)
    
    result = temperature_data[1:4][::-1][0] * threshold_check
    print(f"Target result: {result}")

analyze_temperature_readings()