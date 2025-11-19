from statistics import mean

def track_bakery_sales():
    prices = {'croissant': 2.50, 'baguette': 3.00, 'muffin': 1.75}
    inventory = {'croissant': 20, 'baguette': 15, 'muffin': 25}
    sales_log = [
        {'croissant': 3, 'baguette': 2, 'muffin': 5},
        {'croissant': 2, 'baguette': 4, 'muffin': 3},
        {'croissant': 1, 'baguette': 1, 'muffin': 7},
        {'croissant': 4, 'baguette': 3, 'muffin': 2}
    ]
    
    total_revenue = 0.0
    
    for day_sales in sales_log:
        for item, quantity in day_sales.items():
            inventory[item] -= quantity
            total_revenue += quantity * prices[item]
        
        # Greedy check: restock if any item drops below 10
        if any(count < 10 for count in inventory.values()):
            break
    
    return total_revenue

result = track_bakery_sales()
print(f"Result: {result}")