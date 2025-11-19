croissant_price = 2
muffin_price = 3
scone_base_prices = [4, 4]  # fib seq starts with two values

daily_sales = {'croissants': 10, 'muffins': 15, 'scones': 8}

for day in range(1, 6):  # Day 1 to Day 5
    if day > 1:
        croissant_price *= 2
        muffin_price += 2
        next_scone_price = scone_base_prices[-1] + scone_base_prices[-2]
        scone_base_prices.append(next_scone_price)
    
scone_price = scone_base_prices[-1]
total_revenue = (
    daily_sales['croissants'] * croissant_price +
    daily_sales['muffins'] * muffin_price +
    daily_sales['scones'] * scone_price
)
print(f"Result: {total_revenue}")