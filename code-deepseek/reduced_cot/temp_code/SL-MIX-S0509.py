def process_inventory_data():
    inventory_levels = [45, 78, 23, 91, 34, 67, 12, 88, 56, 29]
    threshold = 50
    
    # Calculate average of high inventory items (distractor calculation)
    high_items = [item for item in inventory_levels if item > threshold]
    avg_high = sum(high_items) // len(high_items) if high_items else 0
    
    # Find the middle slice of data (relevant operation)
    middle_slice = inventory_levels[3:7]
    
    # Process the middle slice data
    processed_data = sum(middle_slice) - min(middle_slice)
    
    # Additional calculations that don't affect final result
    temp_calc = (avg_high * 3) % 17
    redundant_check = len(inventory_levels) * threshold
    
    # Dictionary operations for scaling factors
    scaling_factors = {'low': 2, 'medium': 3, 'high': 4}
    scaling_factor = scaling_factors['medium']
    
    # Final calculation
    final_result = processed_data * scaling_factor // 2
    
    print(f"Target result: {final_result}")

process_inventory_data()