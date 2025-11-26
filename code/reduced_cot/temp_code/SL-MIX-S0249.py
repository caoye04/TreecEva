def process_customer_orders(orders_data):
    # Initial data processing with some distractions
    raw_orders = [25, 42, 18, 56, 31, 29, 48, 15]
    temp_calc = sum(raw_orders) * 2  # Distraction - not used in final result
    
    # Filter orders above threshold using list comprehension
    threshold = 30
    filtered_orders = [order for order in raw_orders if order > threshold]
    
    # Calculate total with adjustment for high-value orders
    base_total = sum(filtered_orders)
    high_value_bonus = len([order for order in filtered_orders if order > 40]) * 10
    
    # Some intermediate calculations that don't affect final result
    processed_count = len(filtered_orders)
    average_order = base_total / processed_count if processed_count > 0 else 0
    
    # Set operations to find unique order values (distraction)
    unique_orders = set(filtered_orders)
    unique_sum = sum(unique_orders) if unique_orders else 0
    
    # Core logic with conditional expressions
    target_value = base_total if processed_count >= 3 else base_total // 2
    adjustment = high_value_bonus if target_value > 100 else high_value_bonus // 2
    
    final_result = target_value + adjustment
    print(f"Result: {final_result}")

process_customer_orders([])