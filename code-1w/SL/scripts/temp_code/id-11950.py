def analyze_sensor_data():
    readings = [23.5, 24.1, 22.8, 25.6, 26.3, 24.9]
    valid_readings = [r for r in readings if r > 23.0]
    
    # Irrelevant buffer variable (minimal distraction)
    buffer_size = len(valid_readings) * 2
    
    temperatures = valid_readings[:5]
    
    # Key computation with slicing and conditional expression
    result = max(temperatures[-3:]) if len(temperatures) > 3 else temperatures[0]
    
    # Additional benign operation
    status = 'OK' if result < 27.0 else 'HIGH'
    
    print(f"Result: {result}")

analyze_sensor_data()