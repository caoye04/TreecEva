# Warehouse stock optimization analysis

# Initial stock levels for different product categories
electronics_stock = [15, 8, 22, 17, 9]
furniture_stock = [12, 25, 7, 18, 14]

# Calculate total stock for each category
electronics_total = sum([item for item in electronics_stock if item > 10])
furniture_total = sum([item for item in furniture_stock if item % 2 == 0])

# Intermediate calculation (distractor)
stock_difference = abs(electronics_total - furniture_total)

# Final result calculation
final_total = (electronics_total + furniture_total) // 2

# Store the target result
result = final_total

print(f"Result: {result}")