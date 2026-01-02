from collections import defaultdict

# Sensor data aggregation and noise filtering
def process_sensor_data(raw_readings):
    reading_count = defaultdict(int)
    total_power = 0
    
    for val in raw_readings:
        reading_count[val] += 1
        total_power += val ** 2

    # Extract frequent readings (occur more than once)
    frequent_readings = [v for v, count in reading_count.items() if count > 1]
    
    # Simulate baseline adjustment (irrelevant to final result)
    baseline_offset = len(raw_readings) - len(frequent_readings)
    adjusted_offset = baseline_offset * 0.5
    
    # Filter out low-power readings
    filtered_readings = [r for r in frequent_readings if r > 50]
    
    # Correction factor based on system calibration
    correction_factor = 0.85
    
    # Critical computation point
    filtration_score = sum(filtered_readings) * correction_factor
    
    return filtration_score

# Input data
sensor_inputs = [60, 75, 60, 45, 80, 80, 90, 45, 30, 75]

result = process_sensor_data(sensor_inputs)
print(f"Target result: {result}")