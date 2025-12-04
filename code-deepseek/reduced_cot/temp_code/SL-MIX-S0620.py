def process_inventory():
    # Inventory tracking system
    items = {'widget_a': 25, 'widget_b': 18, 'component_c': 42}
    
    # Distractor operations
    total_count = sum(items.values())
    average_count = total_count / len(items)
    
    # Key processing with lambda
    processed_key = (lambda x: x.replace('_', '').upper())('widget_a')
    
    # Result mapping with conditional expressions
    result_map = {
        'WIDGETA': (items['widget_a'] // 5) if items['widget_a'] > 20 else items['widget_a'] * 2,
        'WIDGETB': (items['widget_b'] * 3) if items['widget_b'] < 20 else items['widget_b'],
        'COMPONENTC': items['component_c'] - 10
    }
    
    # Unused intermediate calculation
    max_item = max(items.values())
    min_item = min(items.values())
    
    # Main calculation
    base_value = 8
    multiplier = 3 if total_count > 70 else 2
    
    # Final result determination
    final_result = result_map.get(processed_key, base_value) * multiplier
    
    print(f"Target result: {final_result}")

process_inventory()