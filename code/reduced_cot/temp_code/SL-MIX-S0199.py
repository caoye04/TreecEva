def process_inventory(items):
    # Initial inventory processing
    initial_count = len(items)
    temp_sum = sum(items)  # This appears relevant but isn't used later
    
    # Filter and process relevant items
    filtered_set = {item for item in items if item > 5}
    processing_multiplier = 7  # Distractor variable
    
    # Critical execution point
    processed_items = [x * 2 for x in filtered_set if x % 3 != 0]
    
    # Final calculation
    irrelevant_calc = len(filtered_set) * processing_multiplier  # Distractor calculation
    final_result = sum(processed_items) - len(filtered_set)
    
    print(f"Result: {final_result}")
    return final_result

# Test data
inventory_data = [2, 8, 5, 12, 7, 15, 3, 9, 11]
result = process_inventory(inventory_data)