import itertools

def analyze_inventory(supply_data):
    raw_items = ['widget_a', 'widget_b', 'widget_c', 'widget_a', 'widget_b', 'widget_d']
    processed_stock = []
    
    # Distractor: Process but don't use this list
    temp_sorted = sorted(raw_items)
    
    for item in raw_items:
        if item.startswith('widget_'):
            processed_stock.append(item)
    
    # Distractor: Calculate but don't use this value
    total_processed = len(processed_stock)
    
    # Key operation: Group by item type and count
    grouped_items = {}
    for key, group in itertools.groupby(sorted(processed_stock)):
        grouped_items[key] = len(list(group))
    
    # Distractor: Intermediate calculation
    max_quantity = max(grouped_items.values()) if grouped_items else 0
    
    # Main logic: Count items with quantity > 1
    final_count = 0
    for item, quantity in grouped_items.items():
        if quantity > 1:
            final_count += 1
    
    # Final assignment
    result = final_count
    print(f"Target result: {result}")

# Execute the analysis
analyze_inventory(['dummy_data'])