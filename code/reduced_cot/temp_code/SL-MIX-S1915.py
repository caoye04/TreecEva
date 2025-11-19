from contextlib import contextmanager

def calculate_revenue(prices, quantities):
    return sum(prices[item] * quantities.get(item, 0) for item in prices)

@contextmanager
def apply_bonus_multiplier(factor):
    try:
        yield lambda price: price * factor
    finally:
        pass

# Prices and quantities
bakery_prices = {'croissant': 3.5, 'muffin': 2.0, 'scone': 2.5}
daily_quantities = {'croissant': 20, 'muffin': 30, 'scone': 10}

# Calculate initial revenue
initial_revenue = calculate_revenue(bakery_prices, daily_quantities)

if initial_revenue <= 100:
    final_revenue = initial_revenue
else:
    with apply_bonus_multiplier(1.1) as multiplier:
        adjusted_prices = {item: multiplier(price) for item, price in bakery_prices.items()}
        final_revenue = calculate_revenue(adjusted_prices, daily_quantities)

print(f"Result: {final_revenue}")