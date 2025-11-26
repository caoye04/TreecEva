def inventory_analysis():
    raw_items = [45, 67, 23, 89, 12, 56, 34, 78, 91, 15]
    threshold = 40
    
    # Process items above threshold
    filtered_items = [item for item in raw_items if item > threshold]
    
    # Calculate some intermediate metrics (distractor operations)
    total_sum = sum(raw_items)
    average_value = total_sum / len(raw_items)
    max_item = max(raw_items)
    
    # Process items with enumerate and slicing
    processed_items = []
    for idx, item in enumerate(filtered_items):
        if idx % 2 == 0:
            processed_items.append(item * 2)
        else:
            processed_items.append(item - 10)
    
    # More intermediate calculations (not used in final result)
    temp_calc = (max_item * average_value) // 10
    
    # Final inventory calculation
    remaining_stock = len([item for item in raw_items if item <= threshold])
    final_inventory_count = processed_items[-1] + remaining_stock
    
    print(f"Result: {final_inventory_count}")
    return final_inventory_count

# Execute the function
final_result = inventory_analysis()