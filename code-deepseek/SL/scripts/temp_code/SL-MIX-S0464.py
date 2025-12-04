def analyze_product_inventory():
    inventory_data = {
        'product_a': {'units': 45, 'price': 12.75},
        'product_b': {'units': 83, 'price': 8.50},
        'product_c': {'units': 29, 'price': 15.25},
        'product_d': {'units': 67, 'price': 9.99}
    }
    
    # Calculate total values and process data
    processed_data = {}
    for product, details in inventory_data.items():
        total_value = details['units'] * details['price']
        processed_data[product] = round(total_value, 2)
    
    # Find product with maximum value (not directly used in final answer)
    max_key = max(processed_data, key=processed_data.get)
    max_value = processed_data[max_key]
    
    # Some intermediate calculations (distractor)
    temp_calc = sum(processed_data.values()) * 0.15
    adjustment = int(temp_calc)
    
    # Additional processing (semi-relevant)
    product_names_upper = [name.upper() for name in inventory_data.keys()]
    name_lengths = [len(name) for name in product_names_upper]
    
    # Key calculations for final answer
    multiplier = 2
    base_adjustment = 25  # This gets overridden
    base_adjustment = 10  # This is the actual value used
    
    final_total = processed_data[max_key] * multiplier - adjustment
    
    print(f"Target result: {final_total}")

analyze_product_inventory()