def process_final_data(data_sequence):
    # Main processing function with nested operations
    temp_sum = 0
    counter = 0
    irrelevant_accumulator = 1  # Distractor variable
    
    for idx, (x_val, y_val) in enumerate(zip(data_sequence, data_sequence[1:])):
        # Primary logic: process adjacent pairs
        if idx % 3 == 0:
            temp_sum += (x_val ^ y_val) * (idx + 1)  # XOR and scaling
        elif idx % 3 == 1:
            temp_sum -= (x_val | y_val) << 1  # OR and bit shift
        else:
            temp_sum += (x_val & y_val) * 3  # AND operation
            
        counter += 1
        irrelevant_accumulator *= (idx + 2)  # Misleading computation
    
    # Dead code path - never executed
    if counter > 100:
        misleading_result = irrelevant_accumulator // 10
        temp_sum = misleading_result  # This never happens
    
    # Final adjustment using modular arithmetic
    if temp_sum % 7 == 0:
        final_value = temp_sum // 3
    elif temp_sum % 7 == 1:
        final_value = temp_sum * 2 - 5
    else:
        final_value = temp_sum + 8
    
    return final_value

# Main execution with data preparation
input_data = [12, 7, 9, 15, 3, 11, 8]

# Irrelevant data processing
secondary_data = [x * 2 for x in input_data if x > 5]  # Never used
misleading_array = [x % 4 for x in input_data]  # Distractor

# Core data transformation
processed_values = []
for i, val in enumerate(input_data):
    if i % 2 == 0:
        processed_values.append(val + 3)
    else:
        processed_values.append(val - 2)

# More irrelevant operations
unused_result = sum(misleading_array) * 2  # Dead variable

# Key execution point
transformed_data = [x % 13 for x in processed_values]
final_aggregate = process_final_data(transformed_data)

print(f"Target result: {final_aggregate}")