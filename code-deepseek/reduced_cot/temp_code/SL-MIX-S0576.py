def process_inventory_data():
    inventory_items = ['widget-A', 'GADGET-B', 'part-C', 'COMPONENT-d']
    base_quantities = [15, 8, 22, 11]
    
    processed_items = []
    quantity_total = 0
    
    for item, qty in zip(inventory_items, base_quantities):
        processed_item = item.upper()
        processed_items.append(processed_item)
        quantity_total += qty
    
    # Distractor calculations
    temp_sum = sum(len(item) for item in inventory_items)
    average_length = temp_sum / len(inventory_items) if inventory_items else 0
    
    # Main processing logic
    item_count = len(processed_items)
    processed_total = quantity_total % 20
    
    # More distraction
    offset_calc = (item_count * 3) - 5
    offset_adjustment = offset_calc % 7
    
    # Final calculation
    processed_total = processed_total + offset_adjustment
    
    print(f"Result: {processed_total}")
    return processed_total

process_inventory_data()