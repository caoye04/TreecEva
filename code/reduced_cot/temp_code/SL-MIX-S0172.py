def process_data_quality(data_list, quality_thresholds):
    # Initialize tracking variables
    valid_count = 0
    total_processed = 0
    temp_buffer = []
    dummy_calc = 42  # Irrelevant computation
    
    # Process each item with zip and enumerate
    for idx, (item, threshold) in enumerate(zip(data_list, quality_thresholds)):
        # Dead code path - never executed due to condition
        if idx < -5:
            misleading_value = item * 3.14
        
        # Main processing logic
        item_quality = len(str(item)) if item > 0 else abs(item) % 7
        validation_flag = item_quality >= threshold
        
        # Conditional expression for processing
        processed_value = item * 2 if validation_flag else item // 3
        temp_buffer.append(processed_value)
        
        # Update counters based on validation
        valid_count += 1 if validation_flag else 0
        total_processed += 1
        
        # Misleading intermediate calculation
        fake_metric = (idx * processed_value) % 11
    
    # Unused operation - distractor
    unused_set = set(range(5, 15))
    
    # Calculate final metric with complex logic
    if valid_count > 0:
        base_value = sum(temp_buffer[:valid_count])
        adjustment = (base_value % 13) - (len(temp_buffer) % 5)
        final_result = base_value // valid_count + adjustment
    else:
        final_result = -1
    
    # More irrelevant computations
    red_herring = (dummy_calc * len(data_list)) // 2
    another_distractor = sum(quality_thresholds) * 3.14159
    
    return final_result

# Test data
items_data = [24, 17, 35, 42, 8, 51, 63]
thresholds = [2, 3, 2, 1, 1, 2, 2]

# Execute the key statement
final_metric = process_data_quality(items_data, thresholds)

# Print result
print(f"Target result: {final_metric}")