def analyze_environmental_conditions():
    # Sensor data: temperatures in Celsius from region A
    temperature_readings = {23, 24, 25, 26, 27, 28, 30, 31, 33, 35}
    
    # High pressure zones identified (in arbitrary units)
    pressure_zones = {25, 26, 27, 28, 29, 30, 32, 35}
    
    # Critical thresholds exceeded in certain areas
    extreme_events = {23, 24, 33, 35}  # Areas with either heat or pressure spikes
    
    # Filter temperatures above threshold
    high_temp_threshold = 25
    filtered_temps = {t for t in temperature_readings if t >= high_temp_threshold}
    
    # Define high pressure zones as those above median value
    median_pressure = sum(pressure_zones) // len(pressure_zones)
    high_pressure_zones = {p for p in pressure_zones if p > median_pressure}
    
    # Identify zones where critical thresholds were exceeded
    critical_threshold_exceedances = extreme_events.intersection(temperature_readings)
    
    # Key computation step
    result_set = filtered_temps.intersection(high_pressure_zones).difference(critical_threshold_exceedances)
    result_set_size = len(result_set)
    
    # Output result
    print(f"Result: {result_set_size}")

analyze_environmental_conditions()