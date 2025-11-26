def calculate_score(items):
    base_multiplier = 2
    processing_fee = 15
    
    # Calculate base score with multiplier
    base_score = sum(item * base_multiplier for item in items)
    
    # Apply processing adjustments
    processing_bonus = processing_fee // 3
    temp_adjustment = processing_fee * 2 - 10  # Distractor calculation
    
    # Filter and process items
    filtered_items = [item for item in items if item > 3]
    bonus_score = len(filtered_items) * 5
    
    # Final operation with lambda
    final_operation = lambda x: x + processing_bonus
    target_value = final_operation(base_score + bonus_score)
    
    # Distractor operations that don't affect target_value
    unused_calculation = temp_adjustment * len(items)
    redundant_check = sum(items) // base_multiplier
    
    print(f"Target result: {target_value}")

# Test with sample data
items_list = [2, 5, 3, 7, 4]
calculate_score(items_list)