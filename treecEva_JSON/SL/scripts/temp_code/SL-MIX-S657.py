import itertools

flavors = ['chocolate', 'vanilla', 'strawberry', 'lemon', 'caramel']
combinations = list(itertools.combinations(sorted(flavors), 3))
sorted_combinations = sorted(combinations)
target_combination = ('chocolate', 'strawberry', 'vanilla')
position = sorted_combinations.index(target_combination) + 1
print(f'Result: {position}')