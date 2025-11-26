# Inventory optimization calculation
base_inventory = [45, 23, 67, 89, 12, 34, 56, 78, 91, 15]
threshold = 50

# Filter high-value items using list comprehension
high_value_items = [item for item in base_inventory if item > threshold]

# Calculate optimized total
optimized_total = sum(high_value_items)

# Apply adjustment factor
adjustment_factor = 25
final_solution = optimized_total + adjustment_factor

print(f"Result: {final_solution}")