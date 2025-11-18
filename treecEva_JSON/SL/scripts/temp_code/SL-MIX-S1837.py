prices = [2.5, 3.0, 4.0]  # Base prices for croissant, muffin, scone
increments = [0.1, 0.15, 0.2]
weekly_sales = [20, 15, 10]
total_revenue = 0
for week in range(4):
    for i in range(len(prices)):
        total_revenue += prices[i] * weekly_sales[i]
        prices[i] += increments[i]
print(f"Result: {total_revenue}")