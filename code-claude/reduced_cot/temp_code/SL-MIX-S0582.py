# Inventory analysis for an online store
# Analyzing product IDs and their corresponding quantities

product_ids = [102, 305, 208, 417, 506]
quantities = [8, 3, 12, 4, 9]

# Count discontinued items (those with odd IDs)
discontinued = sum(1 for pid in product_ids if pid % 2 != 0)

# Find average quantity across all products
avg_quantity = sum(quantities) / len(quantities)

# Count product pairs where ID is even and quantity exceeds 5
valid_pairs = sum(1 for i, j in zip(product_ids, quantities) if i % 2 == 0 and j > 5)

# Find products with quantity above average
above_avg = 0
for idx, qty in enumerate(quantities):
    if qty > avg_quantity:
        above_avg += 1

print(f"Result: {valid_pairs}")