import itertools
from collections import deque

def calculate_route_efficiency(route_data):
    # Initialize queue with route segments
    segment_queue = deque(route_data)
    total_distance = 0
    weight_multiplier = 1
    
    # Process each segment
    while segment_queue:
        segment = segment_queue.popleft()
        distance, weight, time_deviation = segment
        
        # Calculate weighted distance
        weighted_dist = distance * (1.5 if weight > 50 else 1.0)
        total_distance += weighted_dist
        
        # Update weight multiplier using ternary logic
        weight_multiplier = weight_multiplier * 2 if time_deviation > 0 else weight_multiplier
    
    # Apply penalty matrix based on total distance
    penalty_matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    
    row_index = min(2, int(total_distance // 100))
    col_index = min(2, weight_multiplier - 1)
    penalty_factor = penalty_matrix[row_index][col_index] if row_index < 3 and col_index < 3 else 1
    
    # Final efficiency calculation
    base_score = 1000 - total_distance
    efficiency_score = base_score - (penalty_factor * sum([x[2] for x in route_data]))
    
    return efficiency_score

# Route data: (distance_km, weight_kg, time_deviation_minutes)
routes = [
    (45, 30, 5),
    (75, 65, -2),
    (120, 45, 10),
    (30, 75, 0)
]

# Calculate using functional approach
route_permutations = list(itertools.permutations(routes))
best_score = float('-inf')

for perm in route_permutations[:10]:  # Only check first 10 permutations for efficiency
    score = calculate_route_efficiency(perm)
    best_score = score if score > best_score else best_score

final_efficiency_score = best_score
print(f"Result: {int(final_efficiency_score)}")