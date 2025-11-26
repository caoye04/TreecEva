def process_inventory(items):
    base_stock = 42
    temp_buffer = 15
    seasonal_factor = 3
    
    # Distractor calculations
    total_items = len(items) * seasonal_factor
    average_stock = (base_stock + temp_buffer) / 2
    max_capacity = base_stock * seasonal_factor
    
    # Relevant calculations
    base_value = base_stock - temp_buffer
    offset_multiplier = lambda x: x * 2
    offset_calc = offset_multiplier(seasonal_factor)
    temporary_adjustment = sum([ord(c) for c in 'test']) % 10
    
    # Final computation
    final_adjustment = base_value + offset_calc - temporary_adjustment
    
    print(f"Result: {final_adjustment}")

# Execute with sample data
process_inventory(['item_a', 'item_b', 'item_c'])