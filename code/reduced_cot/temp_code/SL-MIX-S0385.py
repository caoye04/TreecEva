from collections import Counter

# Process sales data analysis
def analyze_sales_patterns(sales_records):
    product_counts = Counter(sales_records)
    
    # Calculate product metrics (some are distractors)
    total_sales = len(sales_records)
    unique_products = len(product_counts)
    average_sales = total_sales / unique_products if unique_products > 0 else 0
    
    # Relevant calculations for final result
    product_values = [count * price for price, count in product_counts.items()]
    sorted_products = sorted(product_values)
    
    # Intermediate calculations (partially relevant)
    sales_range = max(sales_records) - min(sales_records) if sales_records else 0
    base_offset = sales_range // 2 if sales_range > 0 else 5
    
    # Final calculation
    final_metric = sorted_products[-1] - base_offset
    
    # Print irrelevant intermediate values (distraction)
    print(f"Total sales: {total_sales}")
    print(f"Unique products: {unique_products}")
    
    return final_metric

# Main execution
sales_data = [45, 23, 45, 67, 23, 89, 45, 89, 12, 67, 89]
prices_mapping = {12: 150, 23: 200, 45: 175, 67: 300, 89: 250}

result = analyze_sales_patterns(sales_data)
print(f"Target result: {result}")