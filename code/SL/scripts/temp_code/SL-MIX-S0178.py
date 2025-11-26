def calculate_inventory_value(base_items, price_multiplier, bonus_threshold):
    # Initial inventory assessment
    initial_count = len(base_items)
    base_value = initial_count * price_multiplier
    
    # Quality adjustment
    quality_adjustment = 1.5 if initial_count > 10 else 0.8
    adjusted_value = base_value * quality_adjustment
    
    # Bonus calculation
    bonus = 25 if adjusted_value > bonus_threshold else 0
    
    # Final computation
    adjusted_total = int(adjusted_value)
    final_value = adjusted_total + bonus
    
    print(f"Result: {final_value}")
    return final_value

# Inventory data
items = ['widget_A', 'widget_B', 'widget_C', 'widget_D', 'widget_E', 'widget_F']
multiplier = 15
threshold = 100

# Execute the main calculation
calculate_inventory_value(items, multiplier, threshold)