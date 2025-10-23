prices = {'croissant': 2, 'muffin': 3, 'scone': 4}
quantities_sold = [5, 3, 2]

revenue_per_item = [prices[item] * qty for item, qty in zip(prices.keys(), quantities_sold)]
total_revenue = sum(revenue_per_item)

print(f'Result: {total_revenue}')