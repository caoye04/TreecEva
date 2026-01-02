import math

# Irrelevant helper function (decoy)
def dummy_transform(x):
    return (x ** 2 + 3) % 7

# Unused mathematical mapping (distractor)
math_lookup = {i: round(math.sin(i) * 100, 2) for i in range(15)}

# Real data processing pipeline
def process_pipeline(data):
    temp_state = []
    accumulator = 0
    
    # Step 1: Filter valid entries using slicing and conditionals
    filtered_data = data[1:-1]  # Remove first and last elements
    
    # Misleading transformation (not used in final result)
    shadow_copy = [dummy_transform(x) for x in data]
    
    # Step 2: Process each element with conditional logic
    for val in filtered_data:
        if val <= 0:
            continue
        elif val % 4 == 0:
            accumulator += int(math.sqrt(abs(val)))
        elif val % 3 == 0:
            accumulator -= val // 3
        else:
            accumulator += val % 7
    
    # Step 3: Bit manipulation on accumulator (key step)
    accumulator ^= 0b101010
    accumulator &= ~0b1100  # Clear lower 4 bits except defined pattern
    
    # Step 4: Dictionary-based state transition (real logic)
    state_map = {
        'offset': 17,
        'multiplier': 3,
        'shift': len(filtered_data) % 5
    }
    
    # Dead code path (never executed due to logic)
    if len(shadow_copy) > 100:
        state_map['multiplier'] *= 2
        temp_state.append('unused_flag')
    
    # Step 5: Apply state transformations
    intermediate = (accumulator + state_map['offset']) * state_map['multiplier']
    intermediate >>= state_map['shift']  # Right shift based on data length
    
    # Step 6: Final adjustment using logical operations
    flag_check = (intermediate > 0) and (state_map['shift'] != 0) or False
    if flag_check:
        final_value = intermediate + 5
    else:
        final_value = intermediate - 2
    
    # Red herring: unused aggregation
    aggregate_stats = {
        'max_raw': max(data),
        'min_filtered': min(filtered_data),
        'sum_shadow': sum(shadow_copy)
    }
    
    return final_value

# Initial data chunk (meaningful structure)
data_chunk = [0, -4, 12, 9, 25, 16, 7, -3, 5]

# Spurious variable assignments (distractors)
baseline_ref = 12345
control_flag = False
temp_buffer = [0] * len(data_chunk)

# Key execution point
final_output = process_pipeline(data_chunk)

# Output result as required
print(f"Target result: {final_output}")