def analyze_signal(value, mode):
    if mode == 'A':
        return (value ** 2) % 17
    elif mode == 'B':
        return (value + 5) * 3
    else:
        return value // 2


def validate_sequence(seq):
    checksum = 0
    for item in seq:
        checksum += item % 11
    return checksum > 50


def transform_item(x, flag):
    temp_offset = 13
    base = x + temp_offset if x < 100 else x - temp_offset
    adjusted = base * 2 if flag else base // 2
    # Irrelevant transformation
    dummy_calc = (adjusted ^ 7) | 3
    return adjusted


def process_flow(data, limit):
    intermediate_values = []
    secondary_accum = 0
    index_state = 0
    
    for i, val in enumerate(data):
        # Primary logic branch
        if val > limit:
            processed = analyze_signal(val, 'A')
        else:
            processed = analyze_signal(val, 'C')
        
        # Semi-relevant state tracking
        secondary_accum += i * (processed % 4)
        
        # Transform with conditional flag
        flag_decision = processed > 25
        transformed = transform_item(processed, flag_decision)
        intermediate_values.append(transformed)
        
        # Dead code path - never alters final result
        if i == len(data) // 2:
            snapshot = [transformed, i, limit]
            # This list is created but never used

    # Core computation
    filtered = [v for v in intermediate_values if v % 3 == 0]
    aggregate = sum(filtered) if filtered else 0
    
    # Red herring variable
    phantom_sum = sum([x ^ 5 for x in intermediate_values])
    
    # Final decision using conditional expression
    scaling_factor = 1.5 if validate_sequence(intermediate_values) else 0.8
    final_output = int(aggregate * scaling_factor) if aggregate > 0 else -1
    
    # Output required format
    print(f"Result: {final_output}")
    return final_output

# Input setup
sensor_data = [12, 18, 24, 30, 6, 42]
threshold = 20

# Execution entry point
final_output = process_flow(sensor_data, threshold)