def process_inventory(items):
    total_quantity = sum(items.values())
    low_stock_threshold = 5
    high_stock_threshold = 20
    
    # Distractor: unused tracking variables
    stock_categories = {'low': 0, 'medium': 0, 'high': 0}
    inventory_ratio = total_quantity / len(items) if items else 0
    
    # Misleading intermediate calculations
    temp_adjustment = (high_stock_threshold - low_stock_threshold) * 3
    redundancy_factor = temp_adjustment // 2
    
    # Main logic with bit operations
    adjustment_mask = 0b1101
    base_adjustment = (adjustment_mask & 0b1111) ^ 0b1010
    
    # Process items with enumerate
    primary_sum = 0
    for idx, (item_name, quantity) in enumerate(items.items()):
        if quantity < low_stock_threshold:
            category_modifier = (idx | 0x1) & 0xF
        elif quantity > high_stock_threshold:
            category_modifier = (idx ^ 0x3) % 8
        else:
            category_modifier = (idx + 2) & 0x7
        
        primary_sum += quantity * category_modifier
    
    # Dead code path that looks relevant
    if total_quantity > 100:
        emergency_adjust = primary_sum // 10
        # This path is never taken with given data
    
    # Final calculation chain
    adjustment_factor = base_adjustment + redundancy_factor
    final_result = primary_sum - adjustment_factor
    
    print(f"Target result: {final_result}")

# Execute with sample data
inventory_data = {'widgets': 8, 'gadgets': 15, 'tools': 3, 'parts': 22}
process_inventory(inventory_data)