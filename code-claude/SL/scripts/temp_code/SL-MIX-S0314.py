# Gene inheritance simulator
# Tracking unique genes in offspring

parent_a = [1, 3, 5, 7, 9]
parent_b = [2, 4, 6, 8, 10]

# Offspring inherit genes with some mutations
offspring_a = [gene for gene in parent_a if gene % 2 != 0]  # Only odd genes
offspring_a.extend([4, 6])  # Mutations from environment

offspring_b = [gene for gene in parent_b if gene % 3 != 0]  # Genes not divisible by 3
offspring_b.append(5)  # Mutation from environment

# Calculate genetic diversity between offspring
unique_genes = len(set(offspring_a).symmetric_difference(set(offspring_b)))

# Count total genetic material for research purposes
total_genes = sum(offspring_a) + sum(offspring_b)

print(f"Result: {unique_genes}")