def process_warehouse_inventory():
    inventory_data = {
        'electronics': 45,
        'clothing': 78,
        'books': 32,
        'home_goods': 56
    }
    
    # Calculate total items and average
    total_items = sum(inventory_data.values())
    average_stock = total_items / len(inventory_data)
    
    # Process items (distractor: this doesn't affect final result)
    processed_electronics = inventory_data['electronics'] * 2
    
    # Create filtered inventory (distractor: not used in final calculation)
    high_stock_items = {k: v for k, v in inventory_data.items() if v > 40}
    
    # Calculate actual processed items
    processed_items = sum([items * 0.8 for items in inventory_data.values()])
    
    # Calculate remaining stock after processing
    remaining_stock = total_items - processed_items
    
    # Intermediate calculation (distractor: not used)
    theoretical_capacity = total_items * 1.5
    
    # Final inventory count
    final_inventory_count = processed_items + remaining_stock
    
    print(f"Target result: {final_inventory_count}")

process_warehouse_inventory()