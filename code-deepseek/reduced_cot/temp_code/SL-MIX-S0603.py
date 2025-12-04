def analyze_sales_data(sales_records):
    # Distractor: irrelevant customer analysis
    customer_ids = [1001, 1002, 1003, 1004, 1005]
    customer_ratings = [4.2, 3.8, 4.5, 4.1, 3.9]
    avg_rating = sum(customer_ratings) / len(customer_ratings)
    
    # Main logic with zip for pairing sales with regions
    regions = ['north', 'south', 'east', 'west', 'central']
    sales_figures = [12500, 9800, 14200, 7600, 11800]
    
    # Distractor: unused regional analysis
    regional_weights = [1.1, 0.9, 1.2, 0.8, 1.0]
    weighted_sales = [sales * weight for sales, weight in zip(sales_figures, regional_weights)]
    
    # Relevant processing with enumerate
    processed_data = []
    for idx, (region, sales) in enumerate(zip(regions, sales_figures)):
        # Distractor: misleading seasonal adjustment
        seasonal_factor = 1.05 if idx % 2 == 0 else 0.95
        adjusted_sales = sales * seasonal_factor
        
        # Relevant logic: apply discount tier
        if sales > 12000:
            discount_tier = 0.85
        elif sales > 10000:
            discount_tier = 0.90
        else:
            discount_tier = 0.95
        
        final_amount = adjusted_sales * discount_tier
        processed_data.append(final_amount)
    
    # More distractors: unnecessary calculations
    total_weighted = sum(weighted_sales)
    max_customer_rating = max(customer_ratings)
    
    # Key assignment
    final_sales_total = processed_data[-1]
    print(f"Result: {final_sales_total}")

# Execute the analysis
analyze_sales_data([])