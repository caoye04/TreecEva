from functools import reduce

# Daily sales: pastry name -> (quantity, price per item)
daily_sales = {
    'croissant': (10, 2.50),
    'muffin': (20, 1.75),
    'danish': (15, 3.00)
}

def apply_bulk_discount(quantity, price):
    if quantity >= 20:
        return quantity * price * 0.90  # 10% discount
    return quantity * price

# Calculate total revenue
revenues = map(lambda item: apply_bulk_discount(item[1][0], item[1][1]), daily_sales.items())
total_revenue = reduce(lambda x, y: x + y, revenues, 0)

print(f'Total revenue: {total_revenue}')