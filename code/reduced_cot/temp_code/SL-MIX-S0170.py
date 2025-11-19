from collections import namedtuple

# Define item prices
Item = namedtuple('Item', ['name', 'price'])
croissant = Item('croissant', 2.5)
muffin = Item('muffin', 3.0)
scone = Item('scone', 2.0)

# Daily sales quantities
sales_quantities = [40, 25, 30]  # croissants, muffins, scones

# Calculate total revenue using list comprehension
prices = [croissant.price, muffin.price, scone.price]
revenues = [qty * price for qty, price in zip(sales_quantities, prices)]
total_revenue = sum(revenues) if all(revenues) else 0

print(f'Total revenue: {total_revenue}')