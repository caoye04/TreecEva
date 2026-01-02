from itertools import permutations

# Simulate delivery route optimization with priority scoring
def calculate_priority(route):
    base_score = 0
    for i in range(len(route)):
        if route[i] % 2 == 0:
            base_score += route[i] * 1.5
        else:
            base_score += route[i] * 0.8
    return int(base_score)

# City zone identifiers (simulated as integers)
city_zones = [3, 7, 2, 8, 5]

# Irrelevant helper: computes unused distance metric
def euclidean_shift(a, b):
    return ((a - b) ** 2 + (b - a) ** 2) ** 0.5

# Track processed pairs (distraction)
processed_pairs = []
for z1 in city_zones:
    for z2 in city_zones:
        if z1 < z2:
            temp_dist = euclidean_shift(z1, z2)  # Computed but not used
            processed_pairs.append((z1, z2))

# Generate all possible routes (permutations)
all_routes = list(permutations(city_zones))

# Filter routes where sum of first three zones > 12
valid_routes = []
for r in all_routes:
    if sum(r[:3]) > 12:
        valid_routes.append(r)

# Find route with maximum middle element
max_middle_value = -1
optimal_route = None
for r in valid_routes:
    middle_element = r[2]  # Third zone in route
    if middle_element > max_middle_value:
        max_middle_value = middle_element
        optimal_route = r

# Dead code path: never executed due to condition
redundant_correction = False
if len(optimal_route) > 10:
    redundant_correction = True  # Unreachable

# Core computation: determine final priority score
final_priority = calculate_priority(optimal_route)

# Print result for verification
print(f"Result: {final_priority}")