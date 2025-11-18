from collections import namedtuple

# Define named tuple for bakery items
Item = namedtuple('Item', ['name', 'price', 'quantity'])

# Daily sales data
croissant = Item('croissant', 2.5, 20)
muffin = Item('muffin', 3.0, 15)
scone = Item('scone', 2.0, 25)

# Calculate revenue for each item
revenue_croissant = croissant.price * croissant.quantity
revenue_muffin = muffin.price * muffin.quantity
revenue_scone = scone.price * scone.quantity

# Total revenue
total_revenue = revenue_croissant + revenue_muffin + revenue_scone

# Check if the day was successful
successful_day = total_revenue > 100

print(f"Result: {int(successful_day)}")