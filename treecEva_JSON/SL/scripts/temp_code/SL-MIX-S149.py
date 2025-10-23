def categorize_weight(wgt):
    if wgt <= 0:
        return 0
    elif wgt <= 5:
        return 1 + categorize_weight(wgt - 1)
    elif wgt <= 10:
        return 2 + categorize_weight(wgt - 2)
    else:
        return 3 + categorize_weight(wgt - 3)

package_weights = [7, 3, 12, 4]
category_map = {w: categorize_weight(w) for w in package_weights}

adjustment_factors = {
    1: 2,
    2: -1,
    3: 0
}

adjusted_map = {w: category_map[w] + adjustment_factors.get(category_map[w] % 3, 5) for w in category_map}

primary_set = {v for v in adjusted_map.values() if v > 10}
secondary_set = frozenset([11, 13, 16, 18])

common_values = primary_set & secondary_set
unique_to_primary = primary_set - secondary_set

loading_indices = [v * 2 for v in common_values]
loading_indices.extend([v + 3 for v in unique_to_primary])

final_loading_index = sum(loading_indices) if loading_indices else -1
print(f"Result: {final_loading_index}")