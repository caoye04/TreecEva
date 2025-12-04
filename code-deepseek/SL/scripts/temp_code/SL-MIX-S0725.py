def calculate_inventory_status():
    base_stock = 150
    daily_demand = 25
    safety_stock = 40
    current_level = base_stock - daily_demand
    
    # Check if restocking is needed
    reorder_threshold = 80
    needs_restock = current_level <= reorder_threshold
    
    # Calculate final output based on inventory status
    buffer_multiplier = 2 if needs_restock else 1
    final_output = (current_level + safety_stock) * buffer_multiplier
    
    result = final_output
    print(f"Result: {result}")

calculate_inventory_status()