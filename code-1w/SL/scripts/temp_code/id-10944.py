def monitor_pressure():
    baseline = 760
    raw_data = [745, 758, 762, 750, 770, 768, 740]
    pressure_readings = [val + 2 for val in raw_data if val < 765]
    
    # Irrelevant auxiliary calculation (minimal distraction)
    avg_reading = sum(pressure_readings) / len(pressure_readings)
    normal_range_count = len([r for r in pressure_readings if abs(r - baseline) <= 10])
    
    threshold_alert = []
    threshold_alert = list(filter(lambda x: x > baseline, pressure_readings))
    
    # Print final result as required
    print(f"Target result: {len(threshold_alert)}")

monitor_pressure()