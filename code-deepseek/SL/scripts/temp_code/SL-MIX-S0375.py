from collections import Counter

def analyze_product_data(sales_data):
    # Process initial sales data
    total_sales = sum(sales_data)
    average_sales = total_sales / len(sales_data)
    
    # Calculate some intermediate metrics (partially relevant)
    sales_counter = Counter(sales_data)
    most_common_sale = sales_counter.most_common(1)[0][0]
    
    # Perform operations with some distraction
    adjusted_values = [sale * 2 if sale > average_sales else sale // 2 for sale in sales_data]
    
    # More intermediate calculations (somewhat relevant)
    temp_sum = sum(adjusted_values)
    max_adjusted = max(adjusted_values)
    
    # Final processing with the key logic
    processed_values = [val % 100 + 15 for val in adjusted_values]
    
    # Distraction: unused calculation
    unused_metric = (total_sales + temp_sum) // len(sales_data)
    
    # Final assignment
    final_result = processed_values[-1]
    
    print(f"Target result: {final_result}")
    return final_result

# Test data
sales_records = [245, 189, 312, 278, 401, 156, 333]
analyze_product_data(sales_records)