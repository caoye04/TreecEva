from contextlib import contextmanager

@contextmanager
def sales_log():
    sales_data = [12, 8, 20]  # croissants, baguettes, muffins sold
    try:
        yield sales_data
    finally:
        pass

prices = [2, 3, 2]  # croissant, baguette, muffin prices
revenue_calc = lambda sales, price: sales * price

total_revenue = 0
with sales_log() as daily_sales:
    for i in range(len(daily_sales)):
        if daily_sales[i] == 0:
            break
        total_revenue += revenue_calc(daily_sales[i], prices[i])

print(f"Result: {total_revenue}")