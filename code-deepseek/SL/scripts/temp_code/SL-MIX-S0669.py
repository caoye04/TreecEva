def process_inventory():
    inventory_data = {
        'item_a': {'quantity': 15, 'price': 24.5},
        'item_b': {'quantity': 8, 'price': 32.0},
        'item_c': {'quantity': 12, 'price': 18.75},
        'item_d': {'quantity': 6, 'price': 45.25}
    }
    
    processed_items = []
    total_items = 0
    price_summary = 0
    irrelevant_counter = 0
    
    for item_name, item_info in inventory_data.items():
        quantity = item_info['quantity']
        price = item_info['price']
        calculated_value = quantity * price
        
        # This intermediate calculation doesn't affect final result
        irrelevant_counter += quantity - 2
        
        if quantity > 7:
            processed_items.append(calculated_value)
            total_items += quantity
            
    # Distractor operation that seems relevant but isn't used
    temp_adjustment = total_items * 1.1
    
    final_result = sum(processed_items)
    print(f"Target result: {final_result}")

process_inventory()