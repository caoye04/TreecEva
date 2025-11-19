from itertools import permutations
from functools import reduce

def transform_molecule(seq):
    return ''.join(sorted(set(seq)))

def count_unique_permutations(seq):
    perms = set(permutations(seq))
    return len(perms)

molecular_sequences = ['CNOH', 'HCNO', 'OHNC']
transformed_sequences = [transform_molecule(seq) for seq in molecular_sequences]
sorted_transformed = sorted(transformed_sequences, key=lambda x: len(x))
unique_perm_counts = [count_unique_permutations(seq) for seq in sorted_transformed]
normalized_count = reduce(lambda x, y: x + y if y % 2 == 0 else x * y, unique_perm_counts, 1)
print(f"Result: {normalized_count}")