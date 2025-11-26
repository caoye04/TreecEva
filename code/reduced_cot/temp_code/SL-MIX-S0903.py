def data_processor(records):
    # Initialize tracking variables
    temp_sum = 0
    processed_count = 0
    validation_flag = True
    debug_counter = 0
    
    # Distractor operations
    batch_size = len(records) // 2
    capacity_check = batch_size * 3 + 7
    
    # Main processing loop
    for record in records:
        # Validation check (distractor)
        if record % 2 == 0:
            validation_flag = validation_flag and (record > 0)
        else:
            debug_counter += record
            
        # Core calculation with bitwise operations
        if record >= 10 and record <= 50:
            processed_value = (record ^ 15) & 31
            temp_sum += processed_value
            processed_count += 1
            
        # Unused calculation path
        elif record > 50:
            overflow_check = (record << 2) % 17
            capacity_check -= overflow_check
    
    # Final computation with slicing and set operations
    transaction_set = set(records)
    filtered_transactions = [x for x in records if x in range(10, 51)]
    
    if filtered_transactions:
        slice_avg = sum(filtered_transactions[::2]) / len(filtered_transactions[::2])
        base_adjustment = int(slice_avg) % 8
    else:
        base_adjustment = 7
    
    # Misleading intermediate calculation
    intermediate_result = (temp_sum * 3) - (processed_count * 2) + debug_counter
    
    # Actual final computation
    final_result = (temp_sum + base_adjustment) ^ (processed_count * 2)
    
    # Dead code path
    if validation_flag and capacity_check > 100:
        emergency_override = final_result + 50
        return emergency_override
    
    return final_result

# Input data
transaction_data = [8, 15, 22, 37, 45, 12, 29, 51, 18, 33, 26, 41]

# Processing call
final_output = data_processor(transaction_data)

# Output result
print(f"Result: {final_output}")