from itertools import combinations

genetic_markers = ['BRCA1', 'TP53', 'EGFR', 'KRAS', 'MYC', 'PIK3CA']
marker_positions = {marker: idx+1 for idx, marker in enumerate(genetic_markers)}

scoring_function = lambda combo: sum(marker_positions[m] for m in combo) + sum(1 for m in combo if marker_positions[m] % 2 == 0)

combinations_of_3 = list(combinations(genetic_markers, 3))
total_score = sum(scoring_function(combo) for combo in combinations_of_3)

print(f"Result: {total_score}")