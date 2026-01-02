def analyze_system_readings(readings):
    threshold = 75.5
    filtered_data = [r for r in readings if r > threshold]
    
    # Irrelevant auxiliary calculation (minor distraction)
    avg_temp = sum(readings) / len(readings) if readings else 0
    temp_variance = sum((x - avg_temp) ** 2 for x in readings) / len(readings) if readings else 0

    # Core logic step 1: Check if high-temperature events are significant
    temperature_alert = len([x for x in filtered_data if x > 85]) >= 2
    
    # Core logic step 2: Apply string-based status filter (using string method)
    system_status = "critical,standby,active"
    status_parts = system_status.split(',')
    active_systems = [s for s in status_parts if s.startswith('a')]
    
    # Core logic step 3: Determine flag based on string and list conditions
    temperature_flag = temperature_alert or 'active' in active_systems
    
    # Core logic step 4: Final boolean score based on data size and flag
    filtration_score = temperature_flag and len(filtered_data) > 3
    
    return filtration_score

# Input data
sensor_readings = [70.1, 76.3, 82.4, 88.9, 77.2, 91.5, 86.0]

result = analyze_system_readings(sensor_readings)
print(f"Result: {result}")