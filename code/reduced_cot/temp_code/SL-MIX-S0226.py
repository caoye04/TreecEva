def analyze_inventory_patterns(inventory_data):
    # Helper function that won't be used in final calculation
    def calculate_discounted_prices(items):
        discounts = [0.1, 0.15, 0.2]
        return [price * (1 - disc) for price, disc in zip(items, discounts)]
    
    # Main inventory data processing
    stock_levels = [45, 78, 92, 63, 21, 87, 34, 56, 79, 41]
    reorder_thresholds = [30, 25, 40, 35, 20, 45, 25, 30, 40, 30]
    
    # Irrelevant calculations with misleading intermediate results
    total_stock = sum(stock_levels)
    avg_stock = total_stock / len(stock_levels)
    max_stock = max(stock_levels)
    
    # Dead code path - never executed
    if total_stock > 1000:
        emergency_order = [x * 2 for x in stock_levels]
    
    # Relevant processing with enumerate and slicing
    low_stock_items = []
    for idx, (current_stock, threshold) in enumerate(zip(stock_levels, reorder_thresholds)):
        if current_stock <= threshold:
            low_stock_items.append((idx, current_stock, threshold))
    
    # More distractions - unused calculations
    stock_ratios = [stock / thresh for stock, thresh in zip(stock_levels, reorder_thresholds)]
    median_ratio = sorted(stock_ratios)[len(stock_ratios) // 2]
    
    # Key logic chain with multiple steps
    processed_data = []
    for item_idx, stock, reorder in low_stock_items:
        # Calculate reorder quantity using modular arithmetic
        reorder_qty = (reorder * 2 - stock) % 50
        
        # Apply bitwise operations (irrelevant but looks important)
        encoded_qty = reorder_qty ^ 0b101010
        
        # Actual relevant calculation with arithmetic operations
        priority_score = (stock_levels[item_idx] * 3 + reorder_qty * 2) // 5
        processed_data.append(priority_score)
    
    # Final processing with slicing operations
    if len(processed_data) > 0:
        processed_data = processed_data[-3:] + processed_data[:-3]
        final_solution = processed_data[-1]
    else:
        final_solution = -1
    
    # Print result for verification
    print(f"Target result: {final_solution}")
    return final_solution

# Execute the main function
analyze_inventory_patterns([])