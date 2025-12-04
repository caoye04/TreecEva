def analyze_inventory_metrics(product_data, min_threshold):
    # Distractor: unused variables and misleading calculations
    total_products = len(product_data)
    max_capacity = 1000
    buffer_space = max_capacity - total_products
    
    # Misleading intermediate calculations
    estimated_demand = sum(p['initial_stock'] for p in product_data) * 1.2
    safety_margin = estimated_demand * 0.15
    
    # Dead code path that doesn't affect result
    if buffer_space < 0:
        emergency_order = True
        order_quantity = abs(buffer_space) + 50
    
    # Actual logic with conditional expressions
    critical_items = [p for p in product_data if p['current_stock'] <= min_threshold]
    reorder_priority = len(critical_items) * 2 if critical_items else 0
    
    # Bitwise operations as distraction
    status_flags = 0b1101
    alert_level = (status_flags & 0b0100) >> 2
    
    # Main calculation with tuple unpacking
    stock_levels = tuple(p['current_stock'] for p in product_data)
    avg_stock = sum(stock_levels) / len(stock_levels)
    
    # Conditional expression for final decision
    action_score = (avg_stock - min_threshold) * 3 if avg_stock > min_threshold else min_threshold - avg_stock
    
    # More irrelevant computations
    quality_metrics = {'score': 85, 'rating': 'good'}
    inspection_count = quality_metrics['score'] // 10
    
    # Final result calculation
    inventory_health = action_score + reorder_priority - alert_level
    return inventory_health

# Main execution
product_catalog = [
    {'name': 'widget_a', 'current_stock': 25, 'initial_stock': 50},
    {'name': 'widget_b', 'current_stock': 12, 'initial_stock': 30},
    {'name': 'widget_c', 'current_stock': 45, 'initial_stock': 60},
    {'name': 'widget_d', 'current_stock': 8, 'initial_stock': 25}
]

# Distractor variables
threshold_value = 15
backup_supplier = True
warehouse_capacity = 200
emergency_funds = 5000

# Key execution point
result = analyze_inventory_metrics(product_catalog, threshold_value)
final_output = result + 2  # Final adjustment

# More irrelevant operations that don't affect final_output
performance_bonus = warehouse_capacity * 0.1
optimization_factor = emergency_funds // 1000

print(f"Target result: {final_output}")