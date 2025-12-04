def process_inventory_data():
    inventory_data = ['A:12', 'B:8', 'C:15', 'D:invalid', 'E:7', 'F:0', 'G:11']
    
    # Extract numeric values with validation
    quantities = []
    for item in inventory_data:
        if ':' in item:
            parts = item.split(':')
            if len(parts) == 2 and parts[1].isdigit():
                quantities.append(int(parts[1]))
    
    # Distractor operations that don't affect final result
    temp_max = max(quantities) if quantities else 0
    temp_min = min(quantities) if quantities else 0
    range_diff = temp_max - temp_min
    
    # Filter valid quantities (non-zero and even)
    valid_quantities = [q for q in quantities if q > 0 and q % 2 == 0]
    valid_count = len(valid_quantities)
    
    # More distractor operations
    partial_sum = sum(quantities[:3])
    average_temp = sum(quantities) / len(quantities) if quantities else 0
    
    # Core calculation
    processed_sum = sum(valid_quantities)
    final_output = processed_sum / valid_count
    
    # Additional unused calculation
    weighted_avg = (processed_sum * 2 + valid_count) / (valid_count + 1) if valid_count > 0 else 0
    
    print(f"Result: {final_output}")
    return final_output

process_inventory_data()