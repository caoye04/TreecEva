import itertools

ingredient_weights = [7, 3, 5, 10, 2, 8, 1]
valid_combinations = 0

for combo in itertools.combinations(ingredient_weights, 3):
    if sum(combo) % 5 == 0 and len(set(combo)) == 3:
        valid_combinations += 1

print(f"Result: {valid_combinations}")