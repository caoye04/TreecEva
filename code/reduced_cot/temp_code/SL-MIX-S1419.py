from collections import defaultdict
import statistics

def calculate_revenue(prices, quantities):
    base_revenue = sum(prices[item] * qty for item, qty in zip(prices.keys(), quantities))
    avg_qty = statistics.mean(quantities)
    
    if any(qty > 2 * avg_qty for qty in quantities):
        adjustment_factor = 0.95
    else:
        adjustment_factor = 1.0
    
    return base_revenue * adjustment_factor

bakery_prices = {'croissant': 2.5, 'baguette': 3.0, 'muffin': 1.5}
sales_quantities = [20, 15, 50]
adjusted_revenue = calculate_revenue(bakery_prices, sales_quantities)
print(f'Result: {adjusted_revenue}')