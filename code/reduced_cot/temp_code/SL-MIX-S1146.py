from collections import defaultdict

def calculate_optimal_loading(truck_capacity, packages):
    # packages is list of (weight, priority)
    n = len(packages)
    # dp[i][w] = maximum priority sum using first i packages with weight <= w
    dp = [[0] * (truck_capacity + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        weight, priority = packages[i-1]
        for w in range(truck_capacity + 1):
            # Don't take package i
            dp[i][w] = dp[i-1][w]
            # Take package i if it fits
            if weight <= w:
                dp[i][w] = max(dp[i][w], dp[i-1][w-weight] + priority)
    
    return dp[n][truck_capacity]

# Package data: (weight, priority)
shipment_manifest = [
    (3, 7), (5, 12), (2, 5), (8, 19), (4, 9), (6, 14), (1, 3)
]
max_load = 15
schedule_cycle = 7

day_counter = 3
priority_boost = defaultdict(int)
priority_boost[day_counter % schedule_cycle] = 5

# Apply priority adjustments using modular arithmetic
adjusted_packages = []
for i, (weight, base_priority) in enumerate(shipment_manifest):
    boost = priority_boost[(day_counter + i) % schedule_cycle]
    adjusted_priority = base_priority + boost
    adjusted_packages.append((weight, adjusted_priority))

# Short-circuit evaluation for special handling
has_high_value = any(priority > 15 for _, priority in adjusted_packages)
special_handling = True if has_high_value and max_load > 10 else False

# Ternary operator for capacity adjustment
final_capacity = max_load + 5 if special_handling else max_load

# Greedy pre-selection for heavy items
heavy_items = [(w, p) for w, p in adjusted_packages if w > 6]
greedy_selection = []
remaining_capacity = final_capacity

# Sort by priority-to-weight ratio (greedy approach)
heavy_items.sort(key=lambda x: x[1]/x[0], reverse=True)
for weight, priority in heavy_items:
    if weight <= remaining_capacity:
        greedy_selection.append((weight, priority))
        remaining_capacity -= weight

# Calculate optimal solution for remaining space
remaining_packages = [p for p in adjusted_packages if p not in greedy_selection]
optimal_priority_sum = sum(p for _, p in greedy_selection)
if remaining_packages and remaining_capacity > 0:
    additional_priority = calculate_optimal_loading(remaining_capacity, remaining_packages)
    optimal_priority_sum += additional_priority

print(f"Result: {optimal_priority_sum}")