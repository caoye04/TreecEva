def analyze_temperature_readings():
    temperature_data = [78, 65, 89, 54, 91, 47, 63, 70]
    offset = 3
    precision_factor = 4
    
    # Extract every second reading starting from index 0
    filtered_readings = temperature_data[::2]  # [78, 89, 91, 63]
    
    # Calculate midpoint index using integer division
    mid_index = len(filtered_readings) // 2 - 1  # 4//2 - 1 = 1
    
    # Perform scaled-down computation using floor division
    result = temperature_data[::2][mid_index] // precision_factor
    
    # Irrelevant auxiliary variable (minor distraction)
    average_noise_level = sum(temperature_data[:offset]) / offset
    
    print(f"Result: {result}")

analyze_temperature_readings()