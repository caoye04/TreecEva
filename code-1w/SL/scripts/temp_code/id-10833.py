def calibrate_sensor_data():
    raw_values = {'temp': 23.5, 'humidity': 45.2, 'pressure': 1013.25}
    offsets = {'temp': -2.1, 'humidity': 3.8, 'pressure': -12.5}
    
    # Apply offset corrections
    corrected_pressure = raw_values['pressure'] + offsets['pressure']
    temperature_adj = raw_values['temp'] + offsets['temp']
    humidity_adj = raw_values['humidity'] + offsets['humidity']
    
    # Secondary validation check (not affecting pressure)
    if temperature_adj < 20:
        status = 'COOL'
    else:
        status = 'NORMAL'
    
    # Final calibrated reading
    pressure_reading = round(corrected_pressure, 2)
    
    # Unrelated telemetry log (distraction)
    telemetry_log = f'Status: {status}, Humidity Adj: {humidity_adj:.1f}'
    
    return pressure_reading

result = calibrate_sensor_data()
print(f"Result: {result}")