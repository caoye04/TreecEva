ingredients_quantities = [12, 7, 23, 5, 18, 9, 15]
storage_limit = 30

# Greedy selection: sort descending and accumulate until limit
sorted_quantities = sorted(ingredients_quantities, reverse=True)
total_selected = 0
cumulative_sum = 0

for qty in sorted_quantities:
    if cumulative_sum + qty <= storage_limit:
        cumulative_sum += qty
        total_selected += qty
    else:
        break

print(f"Result: {total_selected}")