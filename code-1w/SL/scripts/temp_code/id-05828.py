from itertools import combinations

# Simulate warehouse inventory optimization with combinatorial load balancing
def evaluate_stability(config):
    weight = sum(config)
    spread = max(config) - min(config)
    return weight - spread

# Irrelevant helper: calculates unused metric
def compute_redundancy_score(items):
    return len(set(items)) / len(items) if items else 0

# Misleading function that looks important but isn't used in final logic
def legacy_balance_check(arr):
    total = 0
    for i in range(len(arr)):
        if i % 2 == 0:
            total += arr[i] * 1.5
        else:
            total -= arr[i] * 0.5
    return total

# Core algorithm: find optimal subset matching target demand pattern
def optimize_distribution(stocks, demands):
    target_load = sum(demands) // 2  # Ideal split for dual distribution centers
    best_match = None
    best_diff = float('inf')
    
    # Track auxiliary metrics (semi-relevant)
    eval_count = 0
    total_evaluated = 0
    
    for r in range(1, len(stocks) + 1):
        for combo in combinations(stocks, r):
            eval_count += 1
            total_evaluated += sum(combo)
            diff = abs(sum(combo) - target_load)
            if diff < best_diff:
                best_diff = diff
                best_match = combo
    
    # Dead code path: never executed due to logic above, adds distraction
    if not best_match and len(stocks) == 0:
        return -999
    
    # Auxiliary variable (not used in answer)
    avg_eval = total_evaluated / eval_count if eval_count else 0
    
    # Final capacity is the sum of optimally selected inventory
    final_capacity = sum(best_match) if best_match else 0
    
    # Red herring computation
    phantom_risk = compute_redundancy_score(list(str(final_capacity)))
    
    return final_capacity

# Input data
inventory_levels = [12, 7, 23, 15, 8, 19]
demand_stream = [34, 18, 21, 9]

# Execution point of interest
final_capacity = optimize_distribution(inventory_levels, demand_stream)
print(f"Result: {final_capacity}")