# Sales matrix: rows are products, columns are regions
sales_matrix = [
    [25, 30, 28, 35],
    [15, 20, 18, 22],
    [40, 35, 38, 42],
    [12, 15, 10, 14]
]

# Step 1: Find products with total sales > 100
high_sales_products = []
for product_sales in sales_matrix:
    total_sales = sum(product_sales)
    if total_sales > 100:
        high_sales_products.append(product_sales)

# Step 2: Calculate variance for each high-sales product
variances = []
for product_sales in high_sales_products:
    mean = sum(product_sales) / len(product_sales)
    squared_diffs = [(x - mean) ** 2 for x in product_sales]
    variance = sum(squared_diffs) / len(squared_diffs)
    variances.append(int(variance))

# Step 3: XOR operation
product_count = len(high_sales_products)
total_variance = sum(variances)
result_value = total_variance ^ product_count

print(f"Result: {result_value}")