import itertools

def process_data(input_data):
    # Distractor: unused lambda function
    process_lambda = lambda x: x * 2 + 7
    
    # Main processing chain
    temp_values = []
    counter = 0
    
    # Misleading intermediate calculation
    offset_calc = (15 << 2) & 0xFF  # 60 & 255 = 60
    
    for item in input_data:
        # Dead code path that never executes
        if item < -1000:
            unused_var = item * 3.14159
            
        # Actual processing logic
        if item % 3 == 0:
            transformed = (item * 2) - 5
            temp_values.append(transformed)
        elif item % 5 == 0:
            transformed = (item + 8) // 2
            temp_values.append(transformed)
        else:
            transformed = item + 1
            temp_values.append(transformed)
            
        counter += 1
        
    # Red herring calculation
    misleading_sum = sum(range(10, 20)) + offset_calc
    
    # Core logic with itertools
    filtered_data = list(itertools.filterfalse(lambda x: x % 4 == 0, temp_values))
    
    if len(filtered_data) > 0:
        base_value = filtered_data[0] * 3
        adjustment = sum(filtered_data[1:]) if len(filtered_data) > 1 else 0
        
        # Final computation chain
        intermediate = base_value - adjustment
        result_value = intermediate + (counter * 2)
        
        # Distractor: unused string manipulation
        unused_string = "result_" + str(result_value).replace('5', 'X')
        
        return result_value
    else:
        return misleading_sum

# Main execution
input_stream = [12, 7, 25, 18, 4, 30]

# Misleading variable assignments
preliminary_calc = (8 | 3) ^ 5  # 11 ^ 5 = 14
unused_array = [x * preliminary_calc for x in range(5)]

# Key execution point
result = process_data(input_stream)

# Final assignment with distractor operations
final_offset = (result & 0x0F) << 2
final_output = result - final_offset

print(f"Target result: {final_output}")