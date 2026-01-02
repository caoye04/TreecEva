from itertools import combinations
from functools import reduce

# System parameters for resource allocation
capacity_pool = [8, 15, 22, 34, 45, 50]
demand_sequence = [12, 18, 25, 30]
threshold = 40

# Irrelevant helper: calculates average (not used in final logic)
def calculate_efficiency(data):
    return sum(data) / len(data) if data else 0

# Misleading metric: looks important but unused later
efficiency_score = calculate_efficiency(capacity_pool)

# Core logic: find optimal subset matching demand under threshold
def evaluate_fit(unit_set, demands):
    total_used = 0
    for d in demands:
        if d <= unit_set[-1]:  # Only consider if largest unit fits demand
            total_used += d
    return total_used

# Secondary distraction: dead-end optimization path
def deprecated_method():
    temp_result = 0
    for i in range(len(demand_sequence)):
        temp_result += demand_sequence[i] * (i + 1)
    return temp_result  # Never called

# Main optimization function with lambda and set operations
optimize_allocation = lambda units, limit: reduce(
    lambda acc, pair: acc + pair[0],
    filter(
        lambda pair: pair[0] > pair[1],
        zip(
            [evaluate_fit(c, demand_sequence) for c in combinations(sorted(units), 3) if sum(c) < limit],
            [threshold // 2] * 10
        )
    ),
    0
)

# Tracking state that seems relevant but isn't critical
candidate_combinations = []
for combo in combinations(capacity_pool, 3):
    if sum(combo) < threshold:
        candidate_combinations.append(combo)

# Actual execution point
final_capacity = optimize_allocation(capacity_pool, threshold)

# Additional red herring: unrelated bitwise analysis
bit_analysis = 0
for x in capacity_pool:
    bit_analysis ^= x & 7

print(f"Result: {final_capacity}")