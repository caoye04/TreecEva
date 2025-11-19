import math

terrain_elevations = [120, 145, 110, 180, 95, 210, 165]
candidate_locations = [(2, 3), (5, 7), (1, 8), (8, 2), (4, 5), (9, 1), (3, 9)]
base_station_coords = (0, 0)
earth_curvature_factor = 0.000125
def calculate_signal_strength(distance, elevation_diff):
    effective_height = elevation_diff - (earth_curvature_factor * distance**2)
    return math.log(max(1, effective_height)) if effective_height > 0 else 0

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

visibility_scores = []
for i, (loc, elev) in enumerate(zip(candidate_locations, terrain_elevations)):
    dist = euclidean_distance(base_station_coords, loc)
    height_diff = elev - 100  # Base station height is 100m
    signal = calculate_signal_strength(dist, height_diff)
    obstruction_count = sum(1 for j, other_loc in enumerate(candidate_locations) 
                           if i != j and euclidean_distance(loc, other_loc) < 3)
    adjusted_score = signal - (0.5 * obstruction_count)
    visibility_scores.append(adjusted_score)

# Compute optimal placement considering both signal and clustering
score_threshold = sum(visibility_scores) / len(visibility_scores)
qualified_indices = {i for i, score in enumerate(visibility_scores) if score >= score_threshold}
location_set = {candidate_locations[i] for i in qualified_indices}
clustered_groups = []
visited = set()

for idx in qualified_indices:
    if idx not in visited:
        group = {idx}
        visited.add(idx)
        for j in qualified_indices:
            if j not in visited and euclidean_distance(candidate_locations[idx], candidate_locations[j]) < 4:
                group.add(j)
                visited.add(j)
        clustered_groups.append(group)

max_group_size = max(len(g) for g in clustered_groups) if clustered_groups else 0
optimal_candidates = [g for g in clustered_groups if len(g) == max_group_size]

if len(optimal_candidates) == 1 and len(optimal_candidates[0]) == 1:
    optimal_tower_index = next(iter(optimal_candidates[0]))
elif len(optimal_candidates) > 1:
    # Tie-breaker: highest individual visibility score
    tie_break_scores = [(idx, visibility_scores[idx]) for group in optimal_candidates for idx in group]
    optimal_tower_index = max(tie_break_scores, key=lambda x: x[1])[0]
else:
    # Fallback to highest score
    optimal_tower_index = max(qualified_indices, key=lambda x: visibility_scores[x])

# <-- ANSWER
print(f"Result: {optimal_tower_index}")