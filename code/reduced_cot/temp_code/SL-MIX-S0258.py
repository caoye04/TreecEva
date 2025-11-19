from itertools import combinations

class Palette:
    def __init__(self, hues):
        self.hues = hues
        self.length = len(hues)
    
    def compute_harmony(self, subset_indices):
        if not subset_indices:
            return 0
        product = 1
        for idx in subset_indices:
            product *= (idx + 1) * self.hues[idx]
        return product + sum(subset_indices)

# Initialize palette with specific hue values
artistic_hues = [2, -1, 3, 0, 4]
creative_palette = Palette(artistic_hues)

# Dynamic programming table for storing max harmony up to index i
harmony_table = [float('-inf')] * creative_palette.length
harmony_table[0] = creative_palette.compute_harmony([0])

# Combinatorial exploration with dynamic programming
for idx in range(1, creative_palette.length):
    # Calculate all combinations including current index
    current_max = float('-inf')
    for r in range(1, idx+2):  # r is the size of combination
        for combo in combinations(range(idx+1), r):
            if idx in combo:  # Only consider combos that include current index
                score = creative_palette.compute_harmony(list(combo))
                if score > current_max:
                    current_max = score
    harmony_table[idx] = max(harmony_table[idx-1], current_max)

max_harmony_score = harmony_table[-1]
print(f"Result: {max_harmony_score}")