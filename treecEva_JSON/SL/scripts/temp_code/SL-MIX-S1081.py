pastry_prices = {'croissant': 2.5, 'muffin': 1.8, 'danish': 3.0}
quantities_sold = {'croissant': 40, 'muffin': 30, 'danish': 20}

revenues_per_type = {pastry: price * quantities_sold[pastry] for pastry, price in pastry_prices.items()}
total_revenue = sum(revenues_per_type.values())

print(f"Result: {total_revenue}")