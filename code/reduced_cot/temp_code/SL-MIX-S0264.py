def process_data(inventory_data):
    # Distractor: Calculate total items (not used in final result)
    total_count = sum(len(items) for items in inventory_data.values())
    
    # Main logic: Find maximum value items
    max_values = {}
    for location, items in inventory_data.items():
        if items:
            # Distractor: Calculate average (not used)
            avg_value = sum(items) / len(items)
            
            max_values[location] = max(items)
    
    # Process max values to find final result
    sorted_max = sorted(max_values.values())
    
    # Distractor: Create intermediate calculation (not directly used)
    temp_sum = sum(sorted_max[:-1]) * 2
    
    # Key calculation: Final result is the difference between largest and second largest
    if len(sorted_max) >= 2:
        result = sorted_max[-1] - sorted_max[-2]
    else:
        result = sorted_max[0] if sorted_max else 0
    
    # Another distractor: Unused variable
    unused_metric = total_count * 10
    
    return result

# Main execution
inventory_records = {
    'warehouse_a': [150, 200, 180, 210],
    'warehouse_b': [300, 250, 320],
    'warehouse_c': [400, 380]
}

# Additional distractor calculation
preliminary_total = sum(sum(items) for items in inventory_records.values())

final_result = process_data(inventory_records)
print(f"Target result: {final_result}")