import itertools
from dataclasses import dataclass
from typing import List, Tuple

dataclass
@dataclass
class Vehicle:
    capacity: int
    waypoints: List[int]

# Fleet configuration
fleet_manifest = [
    Vehicle(100, [15, 25, 35]),
    Vehicle(150, [20, 30, 40, 50]),
    Vehicle(120, [10, 20])
]

# Route efficiency calculation
waypoint_weights = {10: 2, 15: 3, 20: 4, 25: 3, 30: 5, 35: 4, 40: 6, 50: 7}
def calculate_route_efficiency(vehicle: Vehicle) -> int:
    total_weight = sum(waypoint_weights.get(wp, 1) for wp in vehicle.waypoints)
    utilization = min(total_weight / vehicle.capacity, 1.0)
    return int(utilization * 100)

# Optimization process
efficiency_scores = []
for vehicle in fleet_manifest:
    base_score = calculate_route_efficiency(vehicle)
    # Apply optimization if waypoints count is even
    if len(vehicle.waypoints) % 2 == 0 and not (base_score < 50):
        optimized_waypoints = list(itertools.combinations(vehicle.waypoints, 2))
        bonus = sum(min(pair) for pair in optimized_waypoints) % 10
        efficiency_scores.append(base_score + bonus)
    else:
        efficiency_scores.append(base_score)

# Final efficiency metric
efficiency_score = sum(score for score in efficiency_scores if score > 60)
print(f'Result: {efficiency_score}')