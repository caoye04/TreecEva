def analyze_sensor_data():
    # Sensor readings from two different monitoring periods
    set_a = {15, 22, 37, 42, 58, 63, 79, 84}
    set_b = {22, 37, 51, 63, 75, 84, 92, 106}
    
    # Find common readings between both monitoring periods
    common_readings = set_a.intersection(set_b)
    
    # Calculate average of common readings
    if common_readings:
        average_reading = sum(common_readings) / len(common_readings)
    else:
        average_reading = 0
    
    # Find final intersection using bitwise operator
    final_intersection = set_a & set_b
    
    print(f"Common sensor readings: {common_readings}")
    print(f"Average reading value: {average_reading}")
    print(f"Target result: {len(final_intersection)}")

analyze_sensor_data()