def preprocess_signal(raw_data, factor=0.85):
    # Irrelevant preprocessing step with decoy computation
    normalized = [x * factor for x in raw_data]
    offset = sum(normalized) % 7
    return [int(x + offset) for x in normalized]


def generate_mask(length, seed=3):
    # Dead code path - never used in actual logic
    mask = [0] * length
    for i in range(length):
        mask[i] = (seed * i) % 5
    return mask


def evaluate_health_status(diag_code):
    # Distractor function: looks important but unused
    if diag_code < 0:
        return 'CRITICAL'
    elif diag_code == 0:
        return 'STABLE'
    else:
        return 'WARNING'


def compute_checksum(sequence):
    # Relevant but indirect: used in final analysis
    checksum = 0
    for val in sequence:
        checksum ^= val  # Bitwise XOR accumulation
    return checksum + 100


def analyze_pattern(seq, limit):
    # Core logic with conditional expressions and nesting
    temp_result = 0
    history = []
    adjustment = 5 if len(seq) > limit else -3
    
    for i in range(len(seq)):
        if i % 4 == 0:
            if seq[i] % 2 == 1:
                temp_result += seq[i] * 2
            else:
                temp_result -= seq[i] // 2
        elif i % 3 == 1:
            nested_offset = 7 if seq[i] > 50 else 2
            temp_result += (seq[i] + nested_offset) % 13
        else:
            temp_result += abs(seq[i] - adjustment)
        
        # Conditional expression update to history
        status_flag = 'HIGH' if temp_result > 200 else 'LOW'
        history.append((i, temp_result, status_flag))
    
    # Final transformation using dictionary lookup
    modifier_map = {0: 4, 1: -2, 2: 6, 3: 1, 4: 0}
    index_key = len(seq) % 5
    modifier = modifier_map.get(index_key, 3)
    
    # Key calculation
    base_value = temp_result
    checksum_influence = compute_checksum(seq) // 10
    final_score = base_value + checksum_influence * modifier
    
    # Red herring: complex-looking but unused compound expression
    hypothetical = (base_value ** 0.5) * (modifier or 1) if modifier != 0 else 999
    
    # Critical assignment
    final_diagnostic = final_score - 17  # This is the answer
    return final_diagnostic

# Main execution flow
if __name__ == '__main__':
    # Input data with meaningful naming
    sensor_readings = [12, 45, 67, 23, 89, 34, 56, 78, 91, 104]
    
    # Irrelevant transformations
    processed_data = preprocess_signal(sensor_readings)
    unused_mask = generate_mask(len(processed_data))
    
    # Decoy variables with misleading names
    system_integrity = sum(x ** 2 for x in processed_data) % 1000
    anomaly_flag = system_integrity > 500
    
    # Threshold used in actual logic
    threshold = 6
    
    # Actual core logic input
    logic_sequence = [x % 89 for x in sensor_readings]  # Transformed input
    
    # Execution point of interest
    final_diagnostic = analyze_pattern(logic_sequence, threshold)
    
    # Output result as required
    print(f"Result: {final_diagnostic}")