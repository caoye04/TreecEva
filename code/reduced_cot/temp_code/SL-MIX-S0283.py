def process_inventory_counts(items, prices):
    total_count = sum(items.values())
    max_price = max(prices.values())  # Distractor - not used in final calculation
    
    # Distractor operations that don't affect final result
    avg_price = sum(prices.values()) / len(prices)
    price_variance = [(p - avg_price) ** 2 for p in prices.values()]
    
    # Core logic
    inventory_value = 0
    for item, count in items.items():
        if item in prices:
            inventory_value += count * prices[item]
    
    # More distractor calculations
    item_ratio = len(items) / len(prices)
    adjusted_count = total_count * 0.8  # Unused variable
    
    return inventory_value

# Main execution
item_counts = {'widget_a': 15, 'widget_b': 8, 'widget_c': 12, 'widget_d': 5}
price_mapping = {'widget_a': 25.5, 'widget_b': 18.0, 'widget_c': 32.75, 'widget_d': 9.5}

inventory_analysis = process_inventory_counts(item_counts, price_mapping)
final_inventory_value = inventory_analysis

# Additional distractor operations
temp_adjustment = final_inventory_value * 0.1  # Never used
count_sum = sum(item_counts.values())  # Redundant calculation

print(f"Result: {final_inventory_value}")