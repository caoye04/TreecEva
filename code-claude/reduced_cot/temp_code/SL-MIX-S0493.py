# Analyzing gene sequence overlap between two species

sequence_a = [4, 8, 15, 16, 23, 42, 56, 61, 78, 92]
sequence_b = [7, 15, 23, 35, 42, 61, 77, 92, 99]

# Calculate potential binding sites (numbers divisible by both 3 and 5)
binding_sites = [i for i in range(10, 100) if i % 3 == 0 and i % 5 == 0]

# Find sequence elements present in both species
overlap = [x for x in sequence_a if x in sequence_b]

# Calculate mutation factors (not relevant for final calculation)
mutation_weights = {n: n**0.5 for n in range(5, 10)}
variation_index = sum(mutation_weights.values()) / len(mutation_weights)

# Process sequence data with some transformations
transformed_a = [x + 2 if x % 2 == 0 else x - 1 for x in sequence_a[:6]]
transformed_b = [x * 1.5 if x < 50 else x for x in sequence_b[2:7]]

# Find elements that exceed the variation threshold
exceeding = []
for idx, val in enumerate(overlap):
    if idx > 0 and val > 40:
        exceeding.append(val)

# Apply weighting to overlapping elements
overlap_values = []
for elem in overlap:
    # Check if element is in binding sites (distraction)
    is_binding = elem in binding_sites
    
    # Apply different weights based on value properties
    if elem < 30:
        overlap_values.append(elem * 2)
    elif elem > 70:
        overlap_values.append(elem // 2)
    else:
        overlap_values.append(elem)

# Calculate total overlap score
filtered_overlap = sum(overlap_values)

# Some additional calculations that don't affect the result
density_metric = len(overlap) / (len(sequence_a) + len(sequence_b))
combined_length = len(sequence_a) + len(sequence_b) - len(overlap)

print(f"Result: {filtered_overlap}")