def process_inventory(items):
    # Initialize tracking variables
    total_items = len(items)
    irrelevant_count = total_items * 2  # Distractor computation
    
    # Process items with enumeration
    valid_items = []
    temp_storage = []
    
    for idx, item in enumerate(items):
        # Some items are processed, some are skipped
        if idx % 3 == 0:
            valid_items.append(item)
        elif idx % 5 == 0:
            temp_storage.append(item * 2)  # Never used
        else:
            # Dead code path - misleading operation
            misleading_value = item + 100
    
    # Set operations to find unique processed items
    processed_set = set(valid_items)
    backup_set = set(items)  # Distractor - not used in final calculation
    
    # Slicing operations on the processed set
    slice_start = len(processed_set) // 3
    slice_end = 2 * len(processed_set) // 3
    relevant_slice = list(processed_set)[slice_start:slice_end]
    
    # Calculate relevant total
    relevant_total = sum(relevant_slice)
    
    # Distractor calculations that look important
    offset_calc = (total_items - len(processed_set)) * 25
    adjustment = len(relevant_slice) * 7
    
    # Final calculation
    final_sum = relevant_total + adjustment
    
    # Print result
    print(f"Result: {final_sum}")

# Execute with sample data
inventory_items = [12, 45, 78, 23, 56, 89, 34, 67, 90, 13, 46, 79]
process_inventory(inventory_items)