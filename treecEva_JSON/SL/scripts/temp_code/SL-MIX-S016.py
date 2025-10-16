from collections import namedtuple

# Define item sales record
SalesRecord = namedtuple('SalesRecord', ['sourdough_count', 'croissant_count', 'day_code'])

# Sales data
bakery_sales = SalesRecord(sourdough_count=15, croissant_count=8, day_code=6)

# Pricing logic using lambda
get_prices = lambda day: (12, 5) if day in [5, 6] else (10, 4)

# Get prices based on day
sourdough_price, croissant_price = get_prices(bakery_sales.day_code)

# Calculate initial revenue
initial_revenue = (bakery_sales.sourdough_count * sourdough_price) + \
                  (bakery_sales.croissant_count * croissant_price)

# Apply discount if total items > 20
total_items = bakery_sales.sourdough_count + bakery_sales.croissant_count
total_revenue = initial_revenue * 0.9 if total_items > 20 else initial_revenue

print(f"Result: {total_revenue}")