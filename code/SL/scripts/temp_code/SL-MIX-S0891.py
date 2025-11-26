def process_inventory_data():
    # Initial inventory data
    items = ['book', 'pen', 'notebook', 'eraser', 'ruler', 'calculator', 'pencil']
    quantities = [15, 8, 12, 6, 9, 4, 11]
    
    # Distractor operations that don't affect final result
    total_items = sum(quantities)
    max_qty = max(quantities)
    avg_qty = total_items / len(quantities)
    
    # Filter items with quantities > 5
    filtered_items = list(filter(lambda x: x[1] > 5, zip(items, quantities)))
    filtered_data = [item[1] for item in filtered_items]
    
    # Additional irrelevant processing
    sorted_quantities = sorted(quantities)
    doubled_values = [q * 2 for q in quantities if q % 2 == 0]
    
    # Core logic with slicing and lambda
    processed_values = list(map(lambda x: x // 2 if x > 7 else x * 3, quantities[1:5]))
    
    # Final calculation - this is what matters
    final_count = filtered_data[2] * processed_values[-1]
    
    print(f"Result: {final_count}")
    return final_count

process_inventory_data()