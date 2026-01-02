def analyze_data_sets():
    # Initial data parameters
    a = 45
    b = 12
    
    # Two sets representing sensor readings
    sensor_set_1 = {a, a+3, b, b*2, 15, 20}
    sensor_set_2 = {b, b+5, a-10, 15, 25, 30}
    
    # Irrelevant auxiliary variable (minor distraction)
    temp_threshold = 18
    
    # Find overlapping readings between sensors
    common_items = sensor_set_1.intersection(sensor_set_2)
    
    # Compute modular component based on primary input
    mod_value = a % 7
    
    # Final result computation
    result = mod_value + len(common_items)
    
    # Output result as required
    print(f"Result: {result}")

analyze_data_sets()