from functools import reduce
from collections import defaultdict

def calculate_path_cost(path):
    costs = {'N': 3, 'S': 2, 'E': 1, 'W': 4}
    return sum(costs[move] for move in path)

def optimize_delivery(routes):
    memo = {}
    def dp(route_idx, visited_mask):
        if route_idx == len(routes):
            return 0
        if (route_idx, visited_mask) in memo:
            return memo[(route_idx, visited_mask)]
        min_cost = float('inf')
        for i in range(len(routes)):
            if not (visited_mask & (1 << i)):
                cost = calculate_path_cost(routes[i]) + dp(route_idx + 1, visited_mask | (1 << i))
                min_cost = min(min_cost, cost)
        memo[(route_idx, visited_mask)] = min_cost
        return min_cost
    return dp(0, 0)

# Drone movement tracking
movement_sequences = [
    ['N', 'E', 'N', 'W'],
    ['S', 'S', 'E'],
    ['W', 'N', 'E', 'S', 'S']
]

path_costs_map = {i: calculate_path_cost(seq) for i, seq in enumerate(movement_sequences)}
drone_energy_consumption = reduce(lambda x, y: x + (y ** 2 if y % 2 == 0 else y * 2), path_costs_map.values(), 0)

optimized_cost = optimize_delivery(movement_sequences)
is_feasible_operation = optimized_cost < 50 and drone_energy_consumption > 100

delivery_efficiency_index = (optimized_cost * 3 if is_feasible_operation else optimized_cost // 2) \
                           + (len(movement_sequences) ** 2 if any(len(s) > 4 for s in movement_sequences) else 0)

print(f"Result: {delivery_efficiency_index}")