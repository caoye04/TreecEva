import itertools

# Bakery's signature pastries
pastries = ['Croissant', 'Eclair', 'Tart', 'Muffin', 'Danish', 'Scone']

# Calculate all unique combinations of 3 pastries
combinations = list(itertools.combinations(pastries, 3))

# Price per special package
package_price = 15

# Calculate total revenue from all combinations
total_revenue = len(combinations) * package_price

print(f"Result: {total_revenue}")