def analyze_inventory():
    product_codes = ['A001', 'B002', 'C003', 'D004', 'E005']
    stock_levels = [45, 120, 78, 33, 210]
    
    # Calculate total stock (distractor - not used in final result)
    total_stock = sum(stock_levels)
    
    # Process inventory using enumerate and zip
    processed_sum = 0
    valid_count = 0
    temp_calc = 0  # Distractor variable
    
    for idx, (code, stock) in enumerate(zip(product_codes, stock_levels)):
        if stock > 50:
            processed_sum += stock * (idx + 1)
            valid_count += 1
        else:
            temp_calc += stock  # This doesn't affect final result
    
    # Intermediate calculation (distractor)
    average_stock = total_stock / len(stock_levels)
    
    # Final ratio calculation
    final_ratio = processed_sum / valid_count
    
    print(f"Result: {final_ratio}")
    return final_ratio

# Execute the analysis
analyze_inventory()