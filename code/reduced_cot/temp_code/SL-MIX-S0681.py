def process_data(items):
    # Filter items where value > 15 and apply transformation
    filtered = list(filter(lambda x: x > 15, items))
    
    # Distractor: calculate average but don't use it
    avg_val = sum(items) / len(items) if items else 0
    
    # Apply transformation using lambda
    processed = list(map(lambda x: x * 2 - 5, filtered))
    
    # Distractor: reverse processing that doesn't affect result
    reversed_proc = list(reversed(processed))
    
    # Final computation - only this matters
    target_output = sum(processed) + len(filtered)
    
    # Distractor: unused calculation
    temp_check = max(items) - min(items)
    
    return target_output

# Main execution
inventory_values = [8, 22, 15, 30, 12, 25, 18]
sorted_items = sorted(inventory_values, reverse=True)

# Distractor: unnecessary intermediate step
middle_value = sorted_items[len(sorted_items) // 2]

final_calculation = process_data(sorted_items)
print(f"Target result: {final_calculation}")