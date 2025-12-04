# Set operations for inventory management
inventory_a = {101, 203, 305, 407, 509}
inventory_b = {203, 407, 612, 814, 916}

# Calculate various set operations
union_set = inventory_a | inventory_b
intersection_set = inventory_a & inventory_b
diff_a_b = inventory_a - inventory_b
diff_b_a = inventory_b - inventory_a

# Some intermediate calculations that don't affect final result
temp_calc = len(inventory_a) * len(inventory_b)
redundant_sum = sum(inventory_a) + sum(inventory_b)

# Symmetric difference (items in either set but not both)
symmetric_diff_set = inventory_a ^ inventory_b

# Distractor operation that seems relevant but isn't used
potential_items = {x for x in range(100, 1000, 100)}

# Final calculation combining multiple set operations
final_solution = union_set - symmetric_diff_set

print(f"Result: {len(final_solution)}")