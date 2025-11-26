def calculate_sensor_readings():
    sensor_data = {
        'temp_sensor': [22.5, 23.1, 21.8, 24.2, 22.9],
        'humidity_sensor': [45, 47, 43, 49, 46],
        'pressure_sensor': [1013, 1015, 1012, 1016, 1014]
    }
    
    # Process temperature readings (not used in final result)
    temp_sum = sum(sensor_data['temp_sensor'])
    temp_avg = temp_sum / len(sensor_data['temp_sensor'])
    
    # Process humidity readings (not used in final result)
    humidity_max = max(sensor_data['humidity_sensor'])
    humidity_min = min(sensor_data['humidity_sensor'])
    humidity_range = humidity_max - humidity_min
    
    # Main calculation - pressure readings
    pressure_readings = sensor_data['pressure_sensor']
    pressure_sum = sum(pressure_readings)
    pressure_count = len(pressure_readings)
    
    # Some intermediate calculations that don't affect final result
    normalized_temp = (temp_avg - 20) / 5
    humidity_variance = (humidity_range ** 2) / 10
    
    # Core logic for result
    base_pressure = 1010
    adjustment_factor = (pressure_sum / pressure_count - base_pressure) * 2
    calibrated_pressure = base_pressure + adjustment_factor
    
    # Create result mapping
    result_map = {
        'calibrated': round(calibrated_pressure, 1),
        'raw_avg': pressure_sum / pressure_count,
        'normalized': (pressure_sum / pressure_count) / 10
    }
    
    target_key = 'calibrated'
    default_value = 0
    
    # Final assignment
    final_result = result_map.get(target_key, default_value)
    
    print(f"Target result: {final_result}")

calculate_sensor_readings()