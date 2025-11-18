from itertools import combinations, permutations
from collections import defaultdict

genetic_markers = {'A1C', 'B2D', 'C3F', 'D4G', 'E5H', 'F6I'}
constraint_set = frozenset(['A1C', 'C3F', 'E5H'])
threshold_map = {'A1C': 3, 'B2D': 7, 'C3F': 2, 'D4G': 5, 'E5H': 4, 'F6I': 6}

filtered_permutations_count = 0
marker_frequency = defaultdict(int)

for size in range(2, 5):
    for combo in combinations(genetic_markers, size):
        combo_set = set(combo)
        if combo_set & constraint_set and not (len(combo_set) > 3 and sum(threshold_map[m] for m in combo if m in threshold_map) < 15):
            for perm in permutations(combo):
                valid_perm = True
                cumulative_threshold = 0
                for i, marker in enumerate(perm):
                    if i > 0 and ((marker_frequency[perm[i-1]] > 2) or (perm[i-1] == 'B2D' and marker == 'D4G')):
                        valid_perm = False
                        break
                    cumulative_threshold += threshold_map.get(marker, 0)
                    if cumulative_threshold > 12:  
                        break
                if valid_perm and (cumulative_threshold <= 12 or len(perm) <= 3):
                    filtered_permutations_count += 1
                    for marker in perm:
                        marker_frequency[marker] += 1

filtered_combinations_count = sum(1 for v in marker_frequency.values() if v > 10)
print(f"Result: {filtered_combinations_count}")