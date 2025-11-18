import numpy as np

# Sales data: rows=days, columns=items (croissants, muffins, scones)
sales_matrix = [
    [10, 15, 8],
    [12, 10, 10],
    [9, 18, 7],
    [11, 14, 9],
    [13, 12, 11],
    [8, 16, 6],
    [14, 11, 12]
]

prices = [2, 3, 4]  # Prices for croissants, muffins, scones

daily_revenues = []
for day_sales in sales_matrix:
    revenue = sum(qty * price for qty, price in zip(day_sales, prices))
    daily_revenues.append(revenue)

average_revenue = sum(daily_revenues) / len(daily_revenues)
print(f"Result: {average_revenue}")