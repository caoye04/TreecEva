from collections import defaultdict

# Prices of bakery items
prices = {'croissant': 3, 'muffin': 2.5, 'scone': 2}

# Monday's sales quantities
sales_quantities = {'croissant': 20, 'muffin': 15, 'scone': 10}

# Lambda to compute total revenue
compute_revenue = lambda quantities, price_dict: sum(qty * price_dict[item] for item, qty in quantities.items())

# Compute initial revenue
initial_revenue = compute_revenue(sales_quantities, prices)

# Apply bonus if revenue exceeds threshold using short-circuit evaluation
bonus = 10 if initial_revenue > 100 else 0
final_revenue = initial_revenue + bonus

print(f'Result: {final_revenue}')