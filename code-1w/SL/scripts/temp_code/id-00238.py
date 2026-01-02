from itertools import combinations

def calculate_entropy(seq):
    if not seq:
        return 0.0
    length = len(seq)
    entropy = 0.0
    for s in seq:
        if sum(s) % 2 == 0:
            entropy += 1
    return entropy

items = [1, 2, 3, 4]
combination_pairs = list(combinations(items, 2))
total_entropy = calculate_entropy(combination_pairs)
print(f"Result: {total_entropy}")