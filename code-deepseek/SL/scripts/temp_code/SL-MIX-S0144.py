def process_orders(orders, threshold):
    # Calculate total for orders above threshold with 15% discount
    eligible_orders = list(filter(lambda x: x > threshold, orders))
    discounted_total = sum(map(lambda x: x * 0.85, eligible_orders))
    
    # Regular orders below threshold
    regular_orders = list(filter(lambda x: x <= threshold, orders))
    regular_total = sum(regular_orders)
    
    final_result = discounted_total + regular_total
    print(f"Result: {final_result}")
    return final_result

orders = [120, 85, 200, 65, 180, 95]
discount_threshold = 100
final_result = process_orders(orders, discount_threshold)