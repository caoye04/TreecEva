def calculate_inventory():
    initial_stock = 150
    daily_sales = [12, 8, 15, 10, 9]
    restock_threshold = 20
    storage_factor = 3
    
    # Calculate total sales (relevant but not used in final answer)
    total_sales = sum(daily_sales)
    
    # Calculate remaining items
    remaining_items = initial_stock - total_sales
    
    # Check if restocking is needed (distractor operation)
    needs_restock = remaining_items < restock_threshold
    
    # Calculate storage capacity (distractor variable)
    max_capacity = 200
    current_utilization = (remaining_items / max_capacity) * 100
    
    # Final calculation
    final_inventory_count = remaining_items * storage_factor
    
    # Print result
    print(f"Result: {final_inventory_count}")

calculate_inventory()