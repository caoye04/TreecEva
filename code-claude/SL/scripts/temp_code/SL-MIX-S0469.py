from itertools import groupby

# Inventory tracking system for a small electronics store
# Status codes: 1=in stock, 0=out of stock, 2=on order

inventory_status = [1, 1, 1, 0, 0, 1, 2, 2, 0, 1]

# Count number of items in each status category
status_names = {0: "Out of Stock", 1: "In Stock", 2: "On Order"}

# Calculate average status value
average_status = sum(inventory_status) / len(inventory_status)

# Find consecutive runs of the same status
product_count = sum(len(list(g)) for _, g in groupby(inventory_status, key=lambda x: x))

# Display number of distinct product runs
print(f"Total product runs: {product_count}")
