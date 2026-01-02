def analyze_temperature_fluctuations():
    temperature_readings = [23.5, 24.1, 22.9, 25.6, 26.3, 21.8, 27.0]
    temperature_baseline = 25.0
    reading_count = len(temperature_readings)
    average_temperature = sum(temperature_readings) / reading_count
    
    # Key computational step with lambda and filtering
    threshold_alert = list(filter(lambda x: x > temperature_baseline, temperature_readings))
    
    # Auxiliary operations (minimal interference)
    sorted_readings = sorted(temperature_readings)
    deviation_from_baseline = [abs(temp - temperature_baseline) for temp in temperature_readings]
    
    # Final output
    Result: {len(threshold_alert)}
    return len(threshold_alert)

result = analyze_temperature_fluctuations()
print(f"Result: {result}")