import itertools
import math
from dataclasses import dataclass
from typing import List, Tuple

def hexagon_moment_of_inertia(weights: List[float]) -> float:
    # Positions of vertices in a regular hexagon (unit radius)
    angles = [math.pi/3 * i for i in range(6)]
    positions = [(math.cos(a), math.sin(a)) for a in angles]
    
    min_moment = float('inf')
    
    # Try all permutations of weights
    for perm in itertools.permutations(weights):
        moment = 0.0
        for i in range(6):
            x, y = positions[i]
            distance_squared = x**2 + y**2
            moment += perm[i] * distance_squared
        min_moment = min(min_moment, moment)
    
    return round(min_moment, 2)

def greedy_initial_sort(weights: List[float]) -> List[float]:
    # Sort weights in descending order for initial arrangement
    return sorted(weights, reverse=True)

# Package weights in kilograms
package_weights = [2.5, 3.7, 1.2, 4.8, 2.1, 3.3]

# Apply greedy algorithm first
initial_arrangement = greedy_initial_sort(package_weights)

# Calculate optimized moment of inertia
optimized_moment = hexagon_moment_of_inertia(initial_arrangement)

print(f"Result: {optimized_moment}")