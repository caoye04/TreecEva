def calculate_performance_metrics(sales_data):
    # Process sales data with list comprehension (distractor - not used in final result)
    processed_sales = [sale * 1.15 for sale in sales_data if sale > 100]
    
    # Calculate base performance score
    base_score = sum(sales_data) * 0.85
    
    # Distractor calculations that don't affect final result
    bonus_calc = len(sales_data) * 25
    adjustment_factor = max(sales_data) / min(sales_data) if min(sales_data) > 0 else 1.0
    
    # Apply conditional bonus based on performance
    if base_score > 500:
        performance_bonus = 75
        # Additional distractor operation
        temp_adjustment = performance_bonus * 0.3
    elif base_score > 300:
        performance_bonus = 45
    else:
        performance_bonus = 15
    
    # Final score calculation
    final_score = base_score + performance_bonus
    
    # More distractor operations
    final_adjustment = final_score * 0.1
    quality_metric = (sum(sales_data) / len(sales_data)) * 2
    
    result = final_score
    print(f"Result: {result}")

# Test data
sales_figures = [120, 85, 210, 180, 95, 250, 110]
calculate_performance_metrics(sales_figures)