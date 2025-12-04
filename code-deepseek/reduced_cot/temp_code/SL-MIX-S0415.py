def calculate_warehouse_value():
    inventory_data = {"widgets": 45, "gadgets": 32, "tools": 67, "parts": 23}
    pricing_info = {"widgets": 12.5, "gadgets": 8.75, "tools": 15.25, "components": 9.99}
    
    # Distractor operations
    temp_calculation = sum(inventory_data.values()) * 2
    avg_price = sum(pricing_info.values()) / len(pricing_info)
    
    # Unused variables that appear relevant
    category_count = len(set(inventory_data.keys()) | set(pricing_info.keys()))
    processed_items = [item.upper() for item in inventory_data.keys()]
    
    # Key computation with list comprehension
    available_products = set(inventory_data.keys()) & set(pricing_info.keys())
    item_data = inventory_data
    prices = pricing_info
    
    # Final calculation
    total_inventory_value = sum([item_data[product] * prices.get(product, 0) for product in available_products])
    
    print(f"Total inventory value: {total_inventory_value}")
    return total_inventory_value

result = calculate_warehouse_value()