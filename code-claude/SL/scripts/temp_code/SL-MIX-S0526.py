def inventory_analysis(items, prices):
    # Calculate potential profit for each item
    profit_margin = lambda price: price * 0.3 if price < 50 else price * 0.25
    potential_profits = {item: profit_margin(price) for item, price in zip(items, prices)}
    
    # Track inventory stats - not directly relevant to final answer
    avg_price = sum(prices) / len(prices) if prices else 0
    premium_items = [item for item, price in zip(items, prices) if price > 75]
    
    # Create inventory dictionary
    inventory = {}
    for i, item in enumerate(items):
        if i % 2 == 0:  # Distractor condition
            inventory[item] = {'price': prices[i], 'category': 'A' if prices[i] < 50 else 'B'}
        else:
            inventory[item] = {'price': prices[i], 'category': 'C' if prices[i] < 30 else 'D'}
    
    # Calculate valid combinations function
    def calculate_valid_combinations(inv, threshold):
        result = 0
        processed_items = set()  # Track processed items to avoid duplicates
        
        for item1, details1 in inv.items():
            for item2, details2 in inv.items():
                if item1 != item2:  # Don't pair an item with itself
                    # Create unique pair identifier regardless of order
                    pair = tuple(sorted([item1, item2]))
                    
                    if pair not in processed_items:
                        combined_price = details1['price'] + details2['price']
                        # Distractor calculation
                        category_bonus = 5 if details1['category'] == details2['category'] else 0
                        
                        if combined_price <= threshold:
                            result += 1
                        processed_items.add(pair)
        
        # Distractor calculation that doesn't affect the result
        unused_metric = sum(detail['price'] for detail in inv.values()) / len(inv)
        return result
    
    # Find combinations under price threshold
    price_threshold = 100
    valid_combinations = calculate_valid_combinations(inventory, price_threshold)
    
    # Distractor calculation
    efficiency_score = valid_combinations / len(inventory) if inventory else 0
    
    print(f"Result: {valid_combinations}")
    return valid_combinations

# Test with sample data
items = ['Keyboard', 'Mouse', 'Monitor', 'Headphones', 'Webcam']
prices = [45, 25, 120, 60, 35]
result = inventory_analysis(items, prices)