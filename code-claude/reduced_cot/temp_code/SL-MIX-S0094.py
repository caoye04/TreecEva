def analyze_inventory_status(warehouse_data, season_factor=1.2):
    # Extract inventory metrics
    current_stock = 145
    projected_increase = warehouse_data.get('projected_shipments', 50) * season_factor
    
    # Order processing metrics
    standard_orders = 35
    canceled_orders = 12
    priority_status = warehouse_data.get('priority', False)
    
    # Calculate potential waste based on product shelf life
    shelf_life_days = 120
    expected_turnover_days = 90
    waste_factor = max(0, 1 - (expected_turnover_days / shelf_life_days))
    potential_waste = current_stock * waste_factor
    
    # Historical data analysis
    historical_data = {45, 67, 89, 72, 58}
    recent_data = {58, 72, 91}
    relevant_history = historical_data.intersection(recent_data)
    historical_average = sum(relevant_history) / len(relevant_history) if relevant_history else 0
    
    # Tracking and monitoring variables
    monitoring_threshold = 150
    alert_needed = current_stock < monitoring_threshold
    adjustment_factor = 0.85 if alert_needed else 1.0
    
    # Calculate final stock level
    final_stock = current_stock + projected_increase - (canceled_orders if priority_status else standard_orders)
    
    # Apply inventory optimization strategy
    optimized_stock = final_stock * adjustment_factor
    
    # Display inventory status
    inventory_status = "Low" if final_stock < 150 else "Adequate" if final_stock < 200 else "Excess"
    
    print(f"Inventory Analysis Complete")
    print(f"Historical Average: {historical_average}")
    print(f"Potential Waste: {potential_waste}")
    print(f"Status: {inventory_status}")
    print(f"Result: {final_stock}")
    
    return optimized_stock

warehouse_info = {
    'location': 'Central',
    'projected_shipments': 42,
    'priority': False
}

analyze_inventory_status(warehouse_info)