from collections import defaultdict
import math

# Simulate sensor fusion from multiple sources with noise filtering and priority weighting
def preprocess_readings(raw_readings):
    filtered = []
    noise_floor = 0.1
    for r in raw_readings:
        if abs(r - 0.5) < noise_floor:  # Filter near-neutral readings
            continue
        adjusted = r * 1.05 if r > 0 else r * 0.95
        filtered.append(adjusted)
    return filtered

# Misleading helper: appears useful but not used in final computation
def legacy_normalization(x):
    return x / (1 + abs(x))

# Core scoring logic
def calculate_confidence(level, age_days):
    decay = math.exp(-age_days / 30)
    base_conf = max(0.1, min(0.9, level * 0.2))
    return round(base_conf * decay, 4)

# Weighted aggregation with redundancy checks
def calculate_final_score(sensor_data, importance_weights):
    aggregated = defaultdict(float)
    redundancy_count = defaultdict(int)
    
    for sensor_id, readings in sensor_data.items():
        weight = importance_weights.get(sensor_id, 1.0)
        total = 0
        count = 0
        
        for reading in readings:
            # Simulate preprocessing step
            processed = reading * 0.8 + 0.2
            if processed > 0.3:  # Threshold filter
                total += processed
                count += 1
                redundancy_count[sensor_id] += 1  # Track redundancy
        
        if count > 0:
            avg = total / count
            aggregated[sensor_id] = avg * weight
    
    # Compute composite score
    composite = sum(aggregated.values())
    
    # Red herring: unused intermediate calculation
    lambda_offset = lambda x: x ** 0.5
    dummy_adjustment = sum(lambda_offset(v) for v in aggregated.values() if v > 0.5)
    
    # Apply non-linear boost if high redundancy
    safety_factor = 1.0
    for sid, cnt in redundancy_count.items():
        if cnt >= 3:
            safety_factor *= 1.1
    
    boosted = composite * safety_factor
    final_score = int(round(boosted * 100))
    
    # Dead code path: never executed under normal inputs
    if False and 'debug' in aggregated:
        print("Debug mode active")
    
    return final_score

# Main execution
if __name__ == "__main__":
    # Raw data from 4 sensor clusters
    raw_sensor_input = [
        0.61, 0.05, 0.63, 0.21, 0.62  # One noisy entry will be filtered
    ]
    
    cleaned = preprocess_readings(raw_sensor_input)
    
    # Organize into structured sensor data
    data = {
        's1': [0.62, 0.63],
        's2': [0.45, 0.47, 0.44],  # Below threshold after processing
        's3': [0.71, 0.73, 0.72, 0.70],
        's4': [0.55]  # Single reading
    }
    
    weights = {'s1': 1.0, 's2': 0.8, 's3': 1.3, 's4': 1.1}
    
    # Unused variables - distractions
    calibration_matrix = [[1.0, 0.1], [0.05, 0.9]]
    baseline_drift = 0.0034
    temp_buffer = set()
    
    # Key execution point
    final_score = calculate_final_score(data, weights)
    
    # Additional red herring computation
    bitwise_diagnostic = (hash('s3') ^ hash('s1')) & 0xFF
    
    Result: {final_score}