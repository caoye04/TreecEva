from itertools import combinations

class BakeryInventory:
    def __init__(self, cookie_types):
        self.cookie_types = cookie_types
        
inventory = BakeryInventory(['chocolate_chip', 'oatmeal_raisin', 'sugar', 'snickerdoodle', 'peanut_butter'])

# Calculate all unique pairs of different cookie types
cookie_pairs = list(combinations(inventory.cookie_types, 2))

pair_count = len(cookie_pairs)

print(f'Result: {pair_count}')