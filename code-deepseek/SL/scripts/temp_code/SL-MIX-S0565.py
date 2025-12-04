def process_inventory_data():
    # Distractor variables - misleading inventory calculations
    item_counts = [45, 23, 78, 91, 12, 67, 34, 56, 89, 14]
    price_fluctuations = [2.5, -1.8, 3.2, -0.5, 4.1, -2.3, 1.7, -3.9, 0.8, -1.2]
    
    # Relevant variables for actual calculation
    stock_levels = [120, 85, 200, 45, 300, 75, 180, 95, 250, 60]
    threshold_min = 80
    threshold_max = 220
    
    # Misleading intermediate calculation (dead code path)
    average_count = sum(item_counts) / len(item_counts) if item_counts else 0
    price_variance = max(price_fluctuations) - min(price_fluctuations)
    
    # Relevant filtering with list comprehension
    filtered_values = [level for level in stock_levels 
                     if threshold_min <= level <= threshold_max]
    
    # Distractor calculations that look important but aren't
    total_inventory = sum(stock_levels)
    excess_stock = sum(level for level in stock_levels if level > 250)
    
    # Final result calculation (this is what matters)
    fallback_result = (threshold_min + threshold_max) // 2
    final_result = max(filtered_values) if filtered_values else fallback_result
    
    # Print the result
    print(f"Result: {final_result}")

# Execute the function
process_inventory_data()