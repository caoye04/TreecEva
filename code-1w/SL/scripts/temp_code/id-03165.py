def analyze_component(reading, threshold=75):
    """Irrelevant analysis function (decoy)"""
    if reading > threshold:
        return (reading - threshold) * 1.5
    return reading * 0.8

def preprocess_entry(data_list):
    """Another decoy function that isn't used in critical path"""
    return [x * 0.9 + 10 for x in data_list if x > 0]

def calculate_entropy(values):
    """Unused scientific calculation to mislead"""
    import math
    total = sum(values)
    entropy = 0.0
    for v in values:
        p = v / total
        if p > 0:
            entropy -= p * math.log(p)
    return entropy

def transform_sequence(seq):
    """Bit manipulation red herring"""
    result = []
    for i, val in enumerate(seq):
        if i % 2 == 0:
            result.append(val ^ 255)  # XOR with mask
        else:
            result.append(val & 127)
    return result

def validate_stability(readings):
    """Unused validation logic"""
    return all(abs(readings[i] - readings[i-1]) < 20 for i in range(1, len(readings)))

def compute_aggregate(weights, values):
    """Distraction: weighted sum not used in final answer"""
    return sum(w * v for w, v in zip(weights, values))

def filter_outliers(data, cutoff=50):
    """Dead code path - never called"""
    return [x for x in data if x >= cutoff]

def evaluate_performance(metrics, reference):
    score = 0
    temp_offset = 0
    
    # Real logic begins here - nested and interwoven with distractors
    for idx, (m, r) in enumerate(zip(metrics, reference)):
        if m < 40:
            temp_offset += 5
        elif m >= 80:
            temp_offset -= 2
        else:
            temp_offset += 1
        
        # Critical branching mixed with irrelevant operations
        adjustment = 0
        for bit_pos in range(4):  # Bit-level distraction
            if (r >> bit_pos) & 1:
                adjustment += 1
        
        if idx % 3 == 0:
            score += (m + adjustment) // 3
        elif idx % 3 == 1:
            score += (m - temp_offset) % 7
        else:
            score += adjustment * 2
    
    # Final transformation using tuple unpacking (real)
    multiplier, offset = (3, -15)
    final_value = score * multiplier + offset
    
    # Decoy variables that look important
    diagnostic_flag = score > 100
    calibration_factor = 1.05
    baseline_delta = sum(reference) / len(reference) - 65
    
    return final_value

# Main execution block
if __name__ == '__main__':
    # Irrelevant dataset initialization
    sensor_readings = [85, 60, 90, 30, 70, 88, 40]
    weights_config = [0.1, 0.2, 0.1, 0.3, 0.05, 0.15, 0.1]
    
    # Distractor: unused preprocessed data
    cleaned_data = preprocess_entry(sensor_readings)
    entropy_metric = calculate_entropy(sensor_readings)
    transformed_bits = transform_sequence(sensor_readings)
    
    # Real inputs for the actual computation
    metrics = [45, 82, 38, 91, 67, 55, 73]
    benchmark_data = [60, 75, 44, 88, 62, 50, 70]
    
    # Unused intermediate results to mislead
    stability_status = validate_stability(sensor_readings)
    aggregate_score = compute_aggregate(weights_config, sensor_readings)
    
    # Actual key computation
    final_score = evaluate_performance(metrics, benchmark_data)
    
    # Print required output
    print(f"Result: {final_score}")