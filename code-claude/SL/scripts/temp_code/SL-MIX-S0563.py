def process_sensor_data(readings, calibration_factor=1.0):
    # Sensor readings are tuples of (timestamp, temperature, humidity, pressure)
    # Process readings to find key metrics
    
    # Calibrate readings based on sensor type
    sensor_types = {'A': 0.8, 'B': 1.2, 'C': 0.95, 'D': 1.05}
    selected_type = 'C'
    actual_calibration = sensor_types.get(selected_type, 1.0) * calibration_factor
    
    # Extract temperature readings and convert to Celsius
    # Formula: (temperature - 32) * 5/9
    daily_readings = []
    outlier_count = 0
    
    for i, reading in enumerate(readings):
        timestamp, temp_f, humidity, pressure = reading
        
        # Skip corrupted readings (indicated by negative humidity)
        if humidity < 0:
            outlier_count += 1
            continue
            
        # Convert Fahrenheit to Celsius with calibration
        temp_c = (temp_f - 32) * 5/9 * actual_calibration
        
        # Apply humidity correction factor for certain conditions
        if humidity > 80 and pressure < 1000:
            humidity_factor = 0.95
        elif humidity < 20 and pressure > 1020:
            humidity_factor = 1.05
        else:
            humidity_factor = 1.0
            
        # Calculate adjusted temperature
        adjusted_temp = temp_c * humidity_factor
        
        # Store timestamp and adjusted temperature
        daily_readings.append((timestamp, adjusted_temp))
    
    # Process alternative data for comparison (not used in final result)
    alt_data = [(r[0], r[1] + 273.15) for r in daily_readings]  # Convert to Kelvin
    kelvin_avg = sum(k for _, k in alt_data) / len(alt_data) if alt_data else 0
    
    # Find minimum temperature and its timestamp
    min_temp = float('inf')
    min_temp_idx = -1
    max_temp = float('-inf')
    max_temp_idx = -1
    
    for idx, (_, temp) in enumerate(daily_readings):
        if temp < min_temp:
            min_temp = temp
            min_temp_idx = idx
        if temp > max_temp:
            max_temp = temp
            max_temp_idx = idx
    
    # Calculate temperature range and average
    temp_range = max_temp - min_temp if daily_readings else 0
    temp_avg = sum(temp for _, temp in daily_readings) / len(daily_readings) if daily_readings else 0
    
    # Determine if we need to apply a weather pattern adjustment
    pattern_adjustment = 0
    if max_temp - min_temp > 15 and temp_avg > 25:
        pattern_adjustment = -2.5
    elif max_temp - min_temp < 5 and temp_avg < 10:
        pattern_adjustment = 1.8
    
    # These variables are for a different analysis and not used in the result
    forecast_temps = [t + pattern_adjustment for _, t in daily_readings]
    forecast_high = max(forecast_temps) if forecast_temps else 0
    forecast_low = min(forecast_temps) if forecast_temps else 0
    
    # Get the minimum temperature reading
    final_temperature = daily_readings[min_temp_idx][1] if min_temp_idx != -1 else 0
    
    # Prepare return values (only some are actually used)
    return {
        'min_temp': final_temperature,
        'max_temp': max_temp,
        'avg_temp': temp_avg,
        'kelvin_avg': kelvin_avg,
        'outliers': outlier_count,
        'forecast_high': forecast_high,
        'forecast_low': forecast_low
    }

# Sample sensor data: (timestamp, temperature_F, humidity%, pressure_hPa)
sensor_data = [
    (1634721600, 68, 65, 1013),  # Normal reading
    (1634725200, 70, -5, 1012),   # Corrupted humidity
    (1634728800, 73, 62, 1011),   # Normal reading
    (1634732400, 59, 70, 1010),   # Normal reading
    (1634736000, 64, 75, 1008)    # Normal reading
]

results = process_sensor_data(sensor_data, 1.1)
final_temperature = results['min_temp']
print(f"Result: {final_temperature}")