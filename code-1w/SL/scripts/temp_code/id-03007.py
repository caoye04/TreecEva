from itertools import combinations

def evaluate_route_efficiency(route):
    base_score = 0
    for i in range(len(route) - 1):
        base_score += abs(route[i] - route[i + 1])
    return base_score

def generate_transport_windows(locations):
    windows = []
    for combo in combinations(locations, 2):
        windows.append((combo[0], combo[1]))
    return windows

def calculate_remaining_capacity(roster):
    total_load = 0
    max_capacity = 1500
    fluctuation_factor = 0.1
    
    # Irrelevant pre-processing: analyzing route efficiency (not used later)
    efficiency_scores = []
    for transport_route in roster['active_routes']:
        score = evaluate_route_efficiency(transport_route)
        efficiency_scores.append(score)
    
    # Real logic begins: summing actual loads
    temp_capacity_pool = []
    for entry in roster['loads']:
        load_id, weight, priority = entry
        if priority > 1:
            adjustment = 1.05 if load_id % 2 == 0 else 0.95
            adjusted_weight = weight * adjustment
            temp_capacity_pool.append(adjusted_weight)
    
    total_load = sum(temp_capacity_pool)
    
    # Distractor: unused sorting operation on transport windows
    location_set = [10, 25, 40, 60]
    unused_windows = generate_transport_windows(location_set)
    sorted_windows = sorted(unused_windows, key=lambda x: x[0])
    
    # Final capacity calculation — depends only on total_load
    final_capacity = max_capacity - total_load
    
    # Additional red herring: simulate fluctuation but don't apply
    projected_fluctuation = final_capacity * fluctuation_factor
    buffer_check = True if projected_fluctuation > 100 else False  # unused
    
    return int(final_capacity)

# Data setup
logistics_roster = {
    'active_routes': [
        [10, 20, 30],
        [15, 25, 35, 45]
    ],
    'loads': [
        (101, 200, 2),
        (102, 300, 3),
        (103, 150, 1),  # priority 1, so skipped
        (104, 350, 4),
        (105, 100, 2)
    ]
}

final_capacity = calculate_remaining_capacity(logistics_roster)
print(f"Result: {final_capacity}")