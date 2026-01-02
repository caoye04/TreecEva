from collections import defaultdict

# Simulate sensor data aggregation and weighted anomaly scoring
def process_sensor_readings(raw_readings):
    aggregated = defaultdict(float)
    counts = defaultdict(int)
    
    for sensor_id, temp in raw_readings:
        if temp < -50 or temp > 150:  # Invalid range
            continue
        aggregated[sensor_id] += temp
        counts[sensor_id] += 1

    normalized = {}
    for key in aggregated:
        normalized[key] = aggregated[key] / counts[key]
    
    return normalized

# Misleading auxiliary function (not used in final path)
def compute_thermal_drift(readings):
    base = sum(readings) / len(readings)
    drift = 0
    for val in readings:
        drift += abs(val - base) * 0.05
    return drift

# Core logic
def calculate_anomaly_vector(values):
    anomalies = []
    avg = sum(values) / len(values)
    for v in values:
        if abs(v - avg) > 15:
            anomalies.append(v * 0.75)
    return anomalies

# Weight adjustment with red herring logic
def adjust_weights(wts, factor=1.0):
    temp_store = {}
    adjusted = []
    for i, w in enumerate(wts):
        temp_store[f'w_{i}'] = w * factor
        adjusted.append(w * 0.9 if i % 2 == 0 else w * 1.1)
    # Only the list `adjusted` matters; temp_store is distraction
    return adjusted

# Final score computation
def calculate_final_score(data_dict, weight_list):
    values = list(data_dict.values())
    
    # Step 1: Compute base average
    base_avg = sum(values) / len(values)
    
    # Step 2: Detect anomalies
    anomalies = calculate_anomaly_vector(values)
    anomaly_count = len(anomalies)
    
    # Step 3: Apply weights (reweighted)
    reweighted = adjust_weights(weight_list, factor=1.2)
    weighted_sum = 0
    for i, val in enumerate(values):
        weighted_sum += val * reweighted[i % len(reweighted)]
    
    # Step 4: Combine metrics into final score
    penalty = anomaly_count * 10
    intermediate_result = weighted_sum - penalty
    
    # Irrelevant debug computation (distraction)
    debug_info = {}
    for idx, v in enumerate(values):
        debug_info[idx] = v ** 2 + (v % 7)
    
    # Final transformation
    final_score = int(intermediate_result - base_avg + 5)
    
    return final_score

# Main execution
if __name__ == '__main__':
    # Raw sensor data: (sensor_id, temperature)
    raw_data = [
        ('A1', 23), ('B2', 45), ('A1', 25), ('C3', -60), ('B2', 40),
        ('D4', 180), ('A1', 100), ('B2', 42), ('C3', 38), ('D4', 170),
        ('A1', 24), ('B2', 160), ('C3', 40), ('D4', 190), ('A1', 26)
    ]

    # Weights for score calculation
    weights = [0.8, 1.2, 0.9, 1.1]

    # Process data
    processed = process_sensor_readings(raw_data)
    
    # Misleading standalone calculation (dead code path)
    sample_temps = [23, 25, 24, 26]
    drift_value = compute_thermal_drift(sample_temps)  # Unused
    
    # Key execution point
    final_score = calculate_final_score(processed, weights)
    
    print(f"Result: {final_score}")