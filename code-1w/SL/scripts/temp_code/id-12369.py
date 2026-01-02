from collections import defaultdict

# Simulate sensor data aggregation for structural load analysis
def aggregate_sensor_data(raw_readings):
    aggregated = defaultdict(float)
    temp_offset = 0.0
    correction_factor = 1.05

    for sensor_id, readings in raw_readings.items():
        base_value = sum(readings) / len(readings)
        adjusted = base_value * correction_factor
        
        # Irrelevant smoothing step (not used later)
        smoothed = [r * 0.9 + temp_offset for r in readings]
        
        if 'A' in sensor_id:
            aggregated[sensor_id] += adjusted * 1.1
        elif 'B' in sensor_id:
            aggregated[sensor_id] += adjusted * 0.95
        else:
            aggregated[sensor_id] += adjusted
    
    return dict(aggregated)

# Determine threshold compliance with dummy metrics
def compute_threshold_metrics(data, baseline):
    above_count = 0
    below_count = 0
    compliance_log = []
    
    for val in data.values():
        deviation = abs(val - baseline)
        status = 'PASS' if deviation < 15 else 'FAIL'
        compliance_log.append((val, status))
        
        if val > baseline:
            above_count += 1
        else:
            below_count += 1
    
    # Dummy metric not used in final calculation
    redundancy_check = above_count > below_count
    
    return compliance_log

# Main stability calculation
def calculate_stability(profile, limits):
    total_weight = sum(profile.values())
    segment_count = len(profile)
    average_load = total_weight / segment_count
    
    # Simulate conditional adjustment based on limit ranges
    adjustment = 0.0
    for limit in limits:
        if average_load > limit * 1.2:
            adjustment -= 2.5
        elif average_load < limit * 0.8:
            adjustment += 1.8
    
    # Apply adjustment to stabilize
    stabilized = average_load + adjustment
    
    # Dead code: unused branch
    if stabilized < 0:
        stabilized = 0
    
    return int(stabilized)

# Input data
raw_sensors = {
    'A1': [12.5, 13.0, 12.8],
    'A2': [14.1, 13.9, 14.2],
    'B1': [11.7, 11.5, 11.8],
    'C1': [10.2, 10.4, 10.3]
}

thresholds = [12.0, 13.5, 11.0]

# Processing pipeline
aggregated_loads = aggregate_sensor_data(raw_sensors)
compliance = compute_threshold_metrics(aggregated_loads, 13.0)
final_load = calculate_stability(aggregated_loads, thresholds)

# Output result
print(f"Result: {final_load}")