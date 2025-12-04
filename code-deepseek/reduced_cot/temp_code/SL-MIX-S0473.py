from collections import Counter

def analyze_inventory_system():
    # Initial inventory data
    warehouse_stock = [45, 32, 67, 89, 23, 54, 76, 31, 45, 67]
    
    # Process stock data (relevant processing)
    stock_counter = Counter(warehouse_stock)
    most_common_item = stock_counter.most_common(1)[0][0]
    
    # Calculate average stock (relevant for later use)
    average_stock = sum(warehouse_stock) / len(warehouse_stock)
    
    # Distractor calculations (not used in final result)
    total_items = len(warehouse_stock)
    stock_variance = sum((x - average_stock) ** 2 for x in warehouse_stock) / total_items
    
    # Process stock adjustments
    adjusted_stock = [item + 5 if item < average_stock else item - 3 for item in warehouse_stock]
    
    # More distractor operations
    max_stock = max(warehouse_stock)
    min_stock = min(warehouse_stock)
    stock_range = max_stock - min_stock
    
    # Key processing steps
    processed_data = {}
    processed_data["common"] = most_common_item
    processed_data["adjusted_avg"] = sum(adjusted_stock) / len(adjusted_stock)
    processed_data["target"] = (most_common_item * 2) - (int(average_stock) // 3)
    
    # Data mapping (critical for final result)
    data_map = {"common_key": "common", "avg_key": "adjusted_avg", "result_key": "target"}
    
    # Final output calculation
    final_output = processed_data[data_map["result_key"]]
    
    # Print the result
    print(f"Result: {final_output}")
    return final_output

# Execute the function
analyze_inventory_system()