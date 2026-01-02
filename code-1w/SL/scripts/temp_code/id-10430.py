from collections import defaultdict

# Simulate sensor data with noise and redundancy
def preprocess_sensor_data(raw_data):
    processed = []
    noise_offset = 0.1
    for item in raw_data:
        temp = item.get('temp', 0) + noise_offset
        humidity = item.get('humidity', 0) - noise_offset
        # Irrelevant transformation
        adjusted = (temp * 1.02) + (humidity * 0.01)
        processed.append({'temp': temp, 'humidity': humidity})
    return processed

# Filter out extreme values that might skew results
def filter_extremes(data, threshold=95):
    filtered = []
    high_temp_count = 0  # Distractor counter
    for entry in data:
        if entry['temp'] < threshold:
            filtered.append(entry)
        else:
            high_temp_count += 1
    # High temp count is never used again
    return filtered

# Calculate weighted performance score
def calculate_performance(metrics):
    base_score = 0
    multiplier = 1.0
    for m in metrics:
        # Semi-relevant logic: only temp contributes
        contribution = m['temp'] * 0.8
        if m['humidity'] > 60:
            multiplier *= 1.05  # Minor boost
        base_score += contribution
    return base_score * multiplier

# Misleading auxiliary function that's called but doesn't affect final result
def compute_reliability_index(data):
    reliability = defaultdict(int)
    for d in data:
        if d['temp'] > 80:
            reliability['high'] += 1
        elif d['temp'] > 60:
            reliability['medium'] += 1
        else:
            reliability['low'] += 1
    total = sum(reliability.values())
    return reliability['high'] / total if total > 0 else 0

# Core scoring logic
def calculate_final_score(data, weights):
    performance = calculate_performance(data)
    weight_sum = sum(weights.values())
    adjustment_factor = 0.95
    
    # Dead code path - never executed due to fixed condition
    debug_mode = False
    extra_penalty = 0
    if debug_mode:  # This block is never run
        extra_penalty = len(data) * 0.01
    
    # Actual computation
    score = performance * adjustment_factor * weight_sum
    scaling_offset = 5.5  # Computed but unused
    scaling_offset += weight_sum * 0.1
    
    # Final assignment
    final_score = int(round(score))
    return final_score

# Main execution flow
if __name__ == '__main__':
    raw_sensor_data = [
        {'temp': 70, 'humidity': 65},
        {'temp': 82, 'humidity': 70},
        {'temp': 67, 'humidity': 58},
        {'temp': 90, 'humidity': 75},  # Will be filtered out
        {'temp': 75, 'humidity': 63}
    ]

    weights = {'w1': 0.7, 'w2': 1.3}  # Sum = 2.0

    # Step 1: Preprocess
    cleaned_data = preprocess_sensor_data(raw_sensor_data)
    
    # Step 2: Filter extremes
    valid_data = filter_extremes(cleaned_data, threshold=90)
    
    # Step 3: Compute irrelevant reliability index (distractor call)
    _ = compute_reliability_index(valid_data)
    
    # Step 4: Calculate final score
    final_score = calculate_final_score(valid_data, weights)
    
    print(f"Result: {final_score}")