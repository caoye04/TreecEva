def analyze_inventory(products):
    stock_analysis = {}
    total_items = 0
    
    for product, details in products.items():
        current_stock = details['stock']
        price = details['price']
        
        # Calculate value but don't use it
        stock_value = current_stock * price
        
        # Distractor operation
        temp_check = current_stock % 3
        
        if current_stock > 15:
            status = 'High'
            adjustment = current_stock - 10
        elif current_stock > 5:
            status = 'Medium'
            adjustment = current_stock * 2
        else:
            status = 'Low'
            adjustment = current_stock + 8
            
        stock_analysis[product] = {
            'status': status,
            'adjusted': adjustment
        }
        total_items += current_stock
    
    # Find product with highest adjusted value
    target_key = max(stock_analysis.keys(), 
                    key=lambda x: stock_analysis[x]['adjusted'])
    
    processed_data = {}
    for product, analysis in stock_analysis.items():
        # Unused intermediate calculation
        score = len(product) * analysis['adjusted']
        
        if analysis['status'] == 'High':
            processed_data[product] = analysis['adjusted'] - 7
        elif analysis['status'] == 'Medium':
            processed_data[product] = analysis['adjusted'] + 3
        else:
            processed_data[product] = analysis['adjusted'] * 2
    
    final_result = processed_data[target_key]
    print(f"Result: {final_result}")

# Main execution
product_inventory = {
    'widget_A': {'stock': 25, 'price': 12.5},
    'widget_B': {'stock': 8, 'price': 18.0},
    'widget_C': {'stock': 3, 'price': 22.0},
    'widget_D': {'stock': 18, 'price': 15.5}
}

analyze_inventory(product_inventory)