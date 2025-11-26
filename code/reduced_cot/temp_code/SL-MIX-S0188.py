def process_warehouse_operations():
    # Initial inventory data
    warehouse_data = {
        'electronics': {'stock': 150, 'category': 'A'},
        'furniture': {'stock': 75, 'category': 'B'},
        'appliances': {'stock': 200, 'category': 'A'}
    }
    
    # Distractor operations that don't affect final result
    total_initial = sum(item['stock'] for item in warehouse_data.values())
    category_a_count = sum(1 for item in warehouse_data.values() if item['category'] == 'A')
    
    # Core inventory processing
    inventory_tracker = {}
    adjustments = {}
    
    # Process inventory with some irrelevant calculations
    temp_processing = []
    for item_name, item_data in warehouse_data.items():
        processed_stock = item_data['stock'] * 0.9  # 10% processing loss
        temp_processing.append(processed_stock)
        
    # This calculation is used but partially irrelevant
    avg_processing = sum(temp_processing) / len(temp_processing)
    
    # Key dictionary operations - these matter
    inventory_tracker['processed'] = int(sum(temp_processing))
    adjustments['damaged'] = 25
    
    # Another distractor that looks important
    quality_check = [stock * 1.05 for stock in temp_processing]
    
    # Final target statement
    final_inventory = inventory_tracker['processed'] - adjustments['damaged']
    
    print(f"Result: {final_inventory}")
    return final_inventory

# Execute the function
result = process_warehouse_operations()