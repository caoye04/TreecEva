from itertools import permutations

# Inventory management scenario
initial_items = {'widget_a': 15, 'widget_b': 8, 'widget_c': 22, 'widget_d': 7}
restock_threshold = 10

# Calculate which items need restocking
restock_needed = [item for item, quantity in initial_items.items() if quantity <= restock_threshold]
restock_count = len(restock_needed)

# Process permutations (distractor - not used in final calculation)
permutation_samples = list(permutations(['x', 'y', 'z'], 2))
permutation_total = len(permutation_samples)

# Calculate adjusted quantities based on restocking needs
adjusted_quantities = {}
for item, quantity in initial_items.items():
    if item in restock_needed:
        adjusted_quantities[item] = quantity + 25
    else:
        adjusted_quantities[item] = quantity - 5

# Create list of processed quantities
processed_quantities = list(adjusted_quantities.values())

# Calculate adjustment factor (key computation)
adjustment_factor = (restock_count * 3) - 7

# Redundant calculation (distractor)
redundant_sum = sum(processed_quantities) // len(processed_quantities)

# Final output calculation
final_output = processed_quantities[2] + adjustment_factor

print(f"Result: {final_output}")