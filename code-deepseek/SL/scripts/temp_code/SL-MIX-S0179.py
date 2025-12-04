def analyze_pattern(sequence):
    # Irrelevant analysis that doesn't affect final result
    temp_sum = sum(x * 2 for x in sequence if x % 3 == 0)
    pattern_mask = [x & 0b1111 for x in sequence]
    return len([x for x in pattern_mask if x > 8])

def validate_input(input_data):
    # Misleading validation that returns constant
    if len(input_data) > 5:
        return True
    elif input_data and input_data[0] > 0:
        return False
    return True

def process_sequence(data):
    # Core logic with distractions
    threshold = 7
    accumulator = 0
    
    # Dead code path - never executes
    if len(data) < 2:
        backup_val = data[0] * 3 + 5
        return backup_val
    
    # Main processing with slicing
    relevant_slice = data[1:-1] if len(data) > 3 else data
    
    # Distractor calculations
    noise_factor = sum(x for x in data[::2]) % 10
    shadow_count = len([x for x in data if x % 4 == 0])
    
    # Actual logic
    for value in relevant_slice:
        if value > threshold:
            accumulator += (value - threshold) * 2
        elif value < threshold // 2:
            accumulator -= 1
    
    # More distractions
    unused_flag = accumulator > 20
    dummy_array = [x * x for x in data[:3]]
    
    return accumulator

# Main execution with interference
data_stream = [12, 5, 8, 3, 15, 9, 6, 11]

# Irrelevant function calls
pattern_result = analyze_pattern(data_stream)
validation_check = validate_input(data_stream)

# Distractor variables
intermediate_sum = sum(data_stream[2:5])
filtered_values = [x for x in data_stream if x % 2 == 1]

# Key computation
final_count = process_sequence(data_stream)

# Print the result
print(f"Result: {final_count}")