def analyze_data_chunk(chunk):
    # Irrelevant analysis function that's never actually used
    temp_sum = sum(chunk)
    avg_factor = len(chunk) * 2.5
    return temp_sum / avg_factor if len(chunk) > 0 else 0

def process_sensor_data(values):
    # Distractor function with misleading computations
    base_offset = 17
    scaling_factor = 3.14159
    processed = []
    
    for i, val in enumerate(values):
        # Dead branch - condition never met
        if i > 100 and val < -50:
            processed.append(val * scaling_factor + base_offset)
        elif i % 2 == 0:
            processed.append(val + base_offset)
        else:
            processed.append(val - base_offset)
    
    return processed

def compute_final_score(data_stream):
    # Core logic with multiple inference steps
    threshold_map = {0: 5, 1: 3, 2: 7, 3: 2, 4: 8}
    running_total = 0
    valid_count = 0
    
    for idx, value in enumerate(data_stream):
        # Complex conditional logic with dictionary lookup
        threshold = threshold_map.get(idx % 5, 4)
        
        # Red herring - this condition is misleading
        if value > 100 or value < -100:
            adjustment = threshold * 2
        else:
            adjustment = threshold
        
        # Actual relevant condition
        if value % 2 == 0 and value > 0:
            running_total += value + adjustment
            valid_count += 1
        
        # Irrelevant computation that doesn't affect final result
        dummy_var = (value * 3.14) if idx % 3 == 0 else (value / 2.0)
    
    # Key computation - final result depends on this
    final_score = running_total // valid_count if valid_count > 0 else 0
    
    # More distractors that don't change the answer
    redundant_check = final_score * 2 - final_score
    verification_sum = sum(data_stream[:3]) if len(data_stream) >= 3 else 0
    
    return final_score

# Main execution with mixed data
sensor_readings = [24, 45, 18, 33, 52, 67, 14, 89, 26, 41]
preliminary_data = process_sensor_data(sensor_readings)
final_metric = compute_final_score(sensor_readings)

# Print the result
print(f"Result: {final_metric}")