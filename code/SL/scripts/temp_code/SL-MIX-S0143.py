def process_inventory_data():
    inventory_counts = {'A': 45, 'B': 67, 'C': 89, 'D': 23, 'E': 56}
    adjustment_factors = {'X': 15, 'Y': 28, 'Z': 42}
    
    # Relevant processing
    primary_key = 'C'
    base_value = inventory_counts[primary_key]
    
    # Semi-relevant calculations (not used in final result)
    total_items = sum(inventory_counts.values())
    average_count = total_items // len(inventory_counts)
    
    # Bitwise operations
    adjustment_mask = adjustment_factors['Y'] & 0b1111
    processed_data = {}
    for key, value in inventory_counts.items():
        processed_data[key] = value | 0x10
    
    # Distractor operations
    temp_sum = sum(adjustment_factors.values())
    adjusted_average = average_count + (temp_sum % 5)
    
    # Critical statement
    final_output = processed_data[primary_key] ^ adjustment_mask
    
    print(f"Result: {final_output}")
    return final_output

process_inventory_data()