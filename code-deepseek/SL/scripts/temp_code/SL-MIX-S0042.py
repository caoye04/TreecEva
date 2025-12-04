inventory_a = {"widgets": 45, "gadgets": 32, "tools": 18}
inventory_b = {"widgets": 28, "gadgets": 19, "tools": 12}

# Calculate total items in each inventory
total_a = sum(inventory_a.values())
total_b = sum(inventory_b.values())

# Compute remaining items after transfer
total_remaining = total_a - total_b

# Print result
print(f"Result: {total_remaining}")