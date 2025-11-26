def analyze_inventory_counts():
    inventory_data = {
        'north': {'widgets': 42, 'gadgets': 18, 'spares': 7},
        'south': {'widgets': 35, 'gadgets': 22, 'spares': 9},
        'east': {'widgets': 28, 'gadgets': 31, 'spares': 5},
        'west': {'widgets': 39, 'gadgets': 15, 'spares': 11}
    }
    
    threshold = 20
    valid_pairs = {}
    
    # Calculate valid item pairs per region (distraction - not used in final result)
    for region, items in inventory_data.items():
        above_threshold = [item for item, count in items.items() if count > threshold]
        if len(above_threshold) >= 2:
            valid_pairs[region] = len(above_threshold)
    
    # Calculate average widgets (distraction - computed but not used)
    widget_counts = [data['widgets'] for data in inventory_data.values()]
    avg_widgets = sum(widget_counts) / len(widget_counts)
    
    # Main logic - find maximum gadget count
    key_region = max(inventory_data.keys(), 
                    key=lambda r: inventory_data[r]['gadgets'])
    
    # Final result extraction
    final_count = valid_pairs[key_region]
    print(f"Result: {final_count}")

analyze_inventory_counts()