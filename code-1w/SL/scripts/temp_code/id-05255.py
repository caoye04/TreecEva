import math

def analyze_anomaly(data):
    # Irrelevant function: analyzes anomalies but not used in final calculation
    anomalies = [x for x in data if x < 0]
    return len(anomalies) > 0

def preprocess_sensor_data(raw):
    # Distractor function: looks important but unused
    cleaned = [max(0, x) for x in raw]
    normalized = [x / sum(cleaned) for x in cleaned]
    return normalized

def shift_window(sequence, offset=1):
    # Unused helper with red herring logic
    return sequence[offset:] + sequence[:offset]

def calculate_entropy(values):
    # Misleading intermediate computation
    total = sum(values)
    probs = [v / total for v in values if v > 0]
    return -sum(p * math.log(p) for p in probs)

def recursive_filter(seq, threshold):
    # Dead code path - never called
    if len(seq) <= 1:
        return seq
    mid = len(seq) // 2
    left = recursive_filter([x for x in seq[:mid] if x > threshold], threshold)
    right = recursive_filter([x for x in seq[mid:] if x > threshold], threshold)
    return left + right

def integrate_subsystems(a, b, c):
    # Complex-looking but irrelevant integration
    temp_a = [x * 1.05 for x in a]  # Simulate calibration
    temp_b = [y + 2 for y in b]
    zipped = zip(temp_a, temp_b, c)
    fused = [p[0] * p[1] / (p[2] + 1) for p in zipped]
    return sum(fused) / len(fused) if fused else 0

def calculate_optimal_flow(readings):
    # Core relevant function
    filtered = [x for x in readings if x >= 10]  # Only consider valid high-range readings
    
    # Simulate multi-stage processing
    stage1 = [x * 0.9 for x in filtered]
    stage2 = [math.sqrt(x) for x in stage1]
    
    # Weighted average using position-based coefficients
    weights = [math.exp(-i * 0.1) for i in range(len(stage2))]
    weighted_sum = sum(value * weight for value, weight in zip(stage2, weights))
    total_weight = sum(weights)
    
    flow_base = weighted_sum / total_weight if total_weight else 0
    
    # Apply environmental correction factor
    correction_factor = 1.23
    adjusted_flow = flow_base * correction_factor
    
    # Final transformation
    result = int(round(adjusted_flow ** 2))
    return result

# Main execution block
sensor_readings = [12, 15, 8, 23, 45, 7, 19, 11, 30, 25, 5, 18]

# Irrelevant variables and computations (distractors)
decoy_readings = [x * 2 + 1 for x in sensor_readings if x % 2 == 0]
analysis_report = {
    'total_sensors': len(sensor_readings),
    'out_of_range': len([x for x in sensor_readings if x > 40]),
    'stdev': (sum([x**2 for x in sensor_readings]) / len(sensor_readings))**0.5,
    'entropy': calculate_entropy(sensor_readings)
}

# Unused data structure with complex initialization
system_state = {
    'calibration': {'offset': 0.5, 'active': True},
    'history': [[x, x*0.95] for x in sensor_readings],
    'flags': [False, True, False]
}

# Key statement - answer depends on this
optimized_flow_rate = calculate_optimal_flow(sensor_readings)

# Print final target result
print(f"Target result: {optimized_flow_rate}")