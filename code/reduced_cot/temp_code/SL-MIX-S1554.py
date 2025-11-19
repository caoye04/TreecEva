from itertools import combinations
from functools import reduce

def color_intensity(tag):
    return len(tag) * sum(ord(c) for c in tag)

primary_hues = {'red': 255, 'green': 180, 'blue': 120}
modifier_tags = ['bright', 'dark', 'vibrant']

# Compute intensity values for each modifier
intensity_map = {tag: color_intensity(tag) for tag in modifier_tags}

# Generate all 2-element combinations of modifiers
modifier_pairs = list(combinations(modifier_tags, 2))

# Calculate combined intensities for each pair
combined_scores = [intensity_map[a] + intensity_map[b] for a, b in modifier_pairs]

# Reduce to get total modifier effect
modifier_effect = reduce(lambda x, y: x ^ y, combined_scores, 0)

# Apply to base hue values
base_sum = sum(primary_hues.values())
palette_score = base_sum + modifier_effect

print(f"Result: {palette_score}")