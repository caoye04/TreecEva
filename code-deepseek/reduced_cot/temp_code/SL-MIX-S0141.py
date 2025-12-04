product_codes = [101, 102, 101, 103, 102, 104, 101, 105]
# Calculate total products
product_total = len(product_codes)
# Find unique product codes
unique_products = list(set(product_codes))
# Count unique products
final_count = len(unique_products)
print(f"Result: {final_count}")