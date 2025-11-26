def process_inventory(items):
    # Process warehouse inventory data
    initial_count = len(items)
    
    # Filter out items with length less than 5
    filtered_items = list(filter(lambda x: len(x) >= 5, items))
    
    # Calculate some intermediate metrics (distractor)
    temp_sum = sum(len(item) for item in items)
    avg_length = temp_sum / initial_count if initial_count > 0 else 0
    
    # Process relevant data
    processed_count = len(filtered_items)
    
    # More intermediate calculations (distractor)
    char_counts = [len(item) * 2 for item in filtered_items]
    total_chars = sum(char_counts)
    
    # Key calculations
    processed_data = processed_count * 3
    scaling_factor = 4
    
    # Final ratio calculation
    final_ratio = processed_data / scaling_factor
    
    # Print result
    print(f"Result: {final_ratio}")
    return final_ratio

# Test data
inventory_items = ['apple', 'banana', 'kiwi', 'orange', 'pear', 'grapefruit']
process_inventory(inventory_items)