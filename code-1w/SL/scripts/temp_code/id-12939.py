from itertools import combinations

# Simulate sensor data with noise and valid readings
def fetch_sensor_data():
    raw_readings = [104, 98, 110, 102, 99, 105, 101, 97]
    noise_filter = [x for x in raw_readings if x % 2 == 0]
    return noise_filter

# Process data through multiple validation layers
def validate_chunks(data):
    validated = []
    temp_buffer = []
    for i, val in enumerate(data):
        if i % 2 == 0:
            temp_buffer.append(val + 3)
        else:
            temp_buffer.append(val - 1)
    # Irrelevant transformation (distractor)
    squared_temp = [x**2 for x in temp_buffer if x > 100]
    # Only every third element is actually used
    for j in range(0, len(temp_buffer), 3):
        if j < len(temp_buffer):
            validated.append(temp_buffer[j])
    return validated

# Extract feature patterns using pairwise combinations
def extract_features(validated_data):
    pairs = list(combinations(validated_data, 2))
    xor_sum = 0
    for a, b in pairs:
        xor_sum += a ^ b  # Bitwise XOR across all pairs
    feature_metric = xor_sum % 1000
    return feature_metric

# Apply threshold logic and calculate final score
def compute_final_score(metrics):
    base = metrics[0] if isinstance(metrics, list) else metrics
    adjustment = 0
    
    # Conditional logic with red herring branches
    if base > 500:
        adjustment += 25
    elif base < 300:
        adjustment -= 10
    else:
        adjustment += 15
    
    # Distractor: complex slicing that isn't used
    unused_slice = [base:base+5 for base in range(3)]
    
    # Real computation path
    intermediate = (base * 1.75) + adjustment
    
    # Extra state tracking (only one matters)
    history_log = {'step1': base, 'step2': intermediate}
    final_score = int(intermediate - 18)  # Final deterministic transformation
    
    # Dead code path (never executed but looks relevant)
    if len(unused_slice) > 10:
        final_score *= 2
        
    return final_score

# Main execution flow
sensor_data = fetch_sensor_data()
processed_data = validate_chunks(sensor_data)
feature_vector = extract_features(processed_data)
final_score = compute_final_score(feature_vector)
print(f"Result: {final_score}")