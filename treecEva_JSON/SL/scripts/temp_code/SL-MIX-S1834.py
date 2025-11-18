import math
from collections import defaultdict

def calculate_triangle_influence(areas):
    influences = []
    for i in range(len(areas) - 1):
        current_area = areas[i]
        next_area = areas[i + 1]
        if current_area > 0 and next_area > 0:
            log_ratio = math.log(next_area) / math.log(current_area)
            influence_score = (current_area ** 0.5) * log_ratio
            influences.append(influence_score)
        else:
            influences.append(0)
    return influences

triangular_areas = [4, 16, 64, 256, 1024]
influence_scores = calculate_triangle_influence(triangular_areas)

adjacency_map = defaultdict(list)
for idx in range(len(influence_scores) - 1):
    adjacency_map[idx].append(idx + 1)

valid_pairs_count = 0
for node, neighbors in adjacency_map.items():
    for neighbor in neighbors:
        base_value = influence_scores[node]
        comp_value = influence_scores[neighbor]
        if base_value > 0 and comp_value > 0:
            exponent_check = math.exp(comp_value) > math.exp(base_value) * 2
            if exponent_check and (int(comp_value) & int(base_value)) != 0:
                valid_pairs_count += 1

print(f"Result: {valid_pairs_count}")