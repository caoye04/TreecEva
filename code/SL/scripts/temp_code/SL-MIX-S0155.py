def process_inventory_data():
    inventory_records = [45, 78, 23, 91, 56, 34, 67, 12, 89, 44]
    threshold = 50
    
    # Calculate valid items above threshold
    valid_items = [item for item in inventory_records if item > threshold]
    valid_sum = sum(valid_items)
    
    # Calculate items below threshold (distractor - not used in final result)
    low_items = [item for item in inventory_records if item <= threshold]
    low_count = len(low_items)
    
    # Process special categories (partial distractor)
    high_value = [item for item in inventory_records if item > 75]
    medium_value = [item for item in inventory_records if 40 <= item <= 75]
    
    # Calculate invalid sum from set operations
    all_items_set = set(inventory_records)
    processed_set = set(valid_items)
    invalid_items = all_items_set - processed_set
    invalid_sum = sum(invalid_items)
    
    # Final calculation
    final_result = valid_sum - invalid_sum
    
    print(f"Result: {final_result}")

process_inventory_data()