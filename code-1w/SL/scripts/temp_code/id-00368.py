import math

def preprocess_sensor_array(arr):
    # Irrelevant preprocessing function (dead utility)
    return [x * 0.95 for x in arr if x > 0]

def validate_phase_stability(temp_seq):
    # Misleading validation logic (not used in final result)
    threshold = sum(temp_seq) / len(temp_seq)
    return all(t < threshold * 1.2 for t in temp_seq)

def calculate_thermal_capacity(matrix, offset):
    base_sum = 0
    adjustment = 0
    
    # Real logic starts here
    for row in matrix:
        for val in row:
            if val % 2 == 0:
                base_sum += int(math.sqrt(abs(val)) + 0.5)
            else:
                adjustment += val % 7
    
    # Distractor: complex but unused calculation
    coherence_score = sum(1 for r in matrix for v in r if v > 10) / (len(matrix) * len(matrix[0]))
    normalization_factor = math.log(coherence_score * 16 + 1) if coherence_score > 0 else 0
    
    # Another red herring variable
    diagnostic_trace = [math.atan(x) for x in range(1, len(matrix) + 1)]
    trace_magnitude = sum(diagnostic_trace)
    
    # Actual relevant transformation
    adjusted_base = base_sum * 2 + adjustment
    
    # Conditional expression with meaningful effect
    scaling_factor = 3 if adjusted_base > 50 else 5
    
    # Final computation chain
    raw_capacity = adjusted_base * scaling_factor
    thermal_capacity = raw_capacity - (offset ** 2)  # Key dependency on input
    
    # Dead code path (never executed due to fixed condition)
    if False:
        fallback = 0
        for i in range(len(matrix)):
            fallback += matrix[i][i] * 2
        thermal_capacity = fallback
    
    return thermal_capacity

# Main execution block
sensor_data = [18, 23, 41, 56]
fusion_matrix = [
    [16, 25, 36],
    [49, 50, 64],
    [81, 34, 27]
]

calibration_offset = 4

# Irrelevant data structure
status_registry = {
    'sensor_a': 'active',
    'sensor_b': 'standby',
    'checksum': sum(sensor_data) % 100
}

# Unused list comprehension (distractor)
processed_pairs = [(x, y) for x in sensor_data for y in sensor_data if x + y > 60]

# Trigger actual computation
thermal_capacity = calculate_thermal_capacity(fusion_matrix, calibration_offset)

# Additional misleading intermediate
entropy_metric = sum(math.log(abs(x) + 1) for x in sensor_data) / len(sensor_data)

# Print target result
print(f"Result: {thermal_capacity}")