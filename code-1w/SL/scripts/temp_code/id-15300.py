from itertools import compress

def analyze_sensor_readings(readings):
    baseline = sum(readings) / len(readings)
    above_baseline = list(map(lambda x: x > baseline, readings))
    filtered_data = list(compress(readings, above_baseline))
    
    # Irrelevant tracking variables (low interference)
    total_updates = 0
    system_status = 'NORMAL'
    
    if len(filtered_data) > 3:
        system_status = 'MONITORING'
        total_updates += 1
    
    filtration_score = sum(filtered_data)
    return filtration_score

# Sensor input data (simulated)
sensor_readings = [12, 8, 15, 7, 23, 14, 6]

result = analyze_sensor_readings(sensor_readings)
print(f"Target result: {result}")