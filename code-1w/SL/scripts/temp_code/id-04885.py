def analyze_temperature_data():
    raw_samples = [68, 72, 74, 76, 80, 85, 65]
    offset = 2
    adjusted_temps = [temp + offset for temp in raw_samples]
    
    # Simulate sensor confidence weights (irrelevant to final result)
    confidence = [0.9, 0.95, 0.85, 0.99, 0.97, 0.88, 0.91]
    weighted_avg = sum(adjusted_temps[i] * confidence[i] for i in range(len(adjusted_temps)))

    temperature_readings = adjusted_temps
    
    # Key statement
    threshold_alert = list(filter(lambda x: x > 75, temperature_readings))
    
    # Additional unrelated tracking variable (minor distraction)
    sample_count = len(raw_samples)
    
    print(f"Result: {threshold_alert}")

analyze_temperature_data()