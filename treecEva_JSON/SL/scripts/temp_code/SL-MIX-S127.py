import itertools

def calculate_priority_combinations(packages, max_cost):
    n = len(packages)
    dp = [[0] * (max_cost + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        priority, cost = packages[i-1]
        for j in range(max_cost + 1):
            dp[i][j] = dp[i-1][j]  # Don't take the item
            if cost <= j:
                dp[i][j] = max(dp[i][j], dp[i-1][j-cost] + priority)
    return dp[n][max_cost]

def recursive_package_selector(packages, index, current_cost, max_cost, selected):
    if current_cost > max_cost:
        return -1, []
    if index == len(packages):
        total_priority = sum(p[0] for p in selected)
        return total_priority, selected[:]
    
    # Try including the current package
    selected.append(packages[index])
    inc_priority, inc_selected = recursive_package_selector(packages, index + 1, current_cost + packages[index][1], max_cost, selected)
    selected.pop()
    
    # Try excluding the current package
    exc_priority, exc_selected = recursive_package_selector(packages, index + 1, current_cost, max_cost, selected)
    
    if inc_priority > exc_priority:
        return inc_priority, inc_selected
    else:
        return exc_priority, exc_selected

# Package data: (priority, cost)
shipment_manifest = [
    (10, 5),
    (40, 4),
    (30, 6),
    (50, 3),
    (20, 2)
]

budget_limit = 10
optimal_priority = 0
selected_packages = []

# Apply dynamic programming approach
optimal_priority_dp = calculate_priority_combinations(shipment_manifest, budget_limit)

# Apply recursive approach with early termination
optimal_priority_recursive, selected_packages = recursive_package_selector(shipment_manifest, 0, 0, budget_limit, [])

# Use itertools to generate combinations and find the best
best_priority_itertools = 0
for r in range(1, len(shipment_manifest) + 1):
    for combination in itertools.combinations(shipment_manifest, r):
        total_cost = sum(pkg[1] for pkg in combination)
        if total_cost <= budget_limit:
            total_priority = sum(pkg[0] for pkg in combination)
            if total_priority > best_priority_itertools:
                best_priority_itertools = total_priority

# Bitwise encoding of package statuses
package_status = 0
for i, pkg in enumerate(shipment_manifest):
    if pkg in selected_packages:
        package_status |= (1 << i)

# Final decision based on multiple approaches
if optimal_priority_dp >= optimal_priority_recursive and optimal_priority_dp >= best_priority_itertools:
    optimal_priority = optimal_priority_dp
elif optimal_priority_recursive >= best_priority_itertools:
    optimal_priority = optimal_priority_recursive
else:
    optimal_priority = best_priority_itertools

# Apply short-circuit evaluation
if package_status & 0b10100 and optimal_priority > 50:
    optimal_priority += 10

print(f"Result: {optimal_priority}")