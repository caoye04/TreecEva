def process_inventory():
    inventory_data = {'items': [25, 42, 18, 67, 33], 'threshold': 30}
    
    # Process items above threshold
    high_value_items = {item for item in inventory_data['items'] if item > inventory_data['threshold']}
    
    # Calculate statistics
    item_count = len(high_value_items)
    max_item = max(high_value_items) if high_value_items else 0
    
    # Create result set with calculated values
    result_set = {item_count * 10, max_item // 2}
    
    # Final computation
    final_result = result_set.pop() if result_set else 0
    
    print(f"Target result: {final_result}")
    return final_result

# Execute the function
process_inventory()