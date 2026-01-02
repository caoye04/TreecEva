def main():
    # System for optimizing warehouse inventory distribution across zones
    base_inventory = [17, 23, 14, 38, 29, 31, 13]
    zone_thresholds = [15, 20, 25, 30]
    adjustment_factor = 1.25
    temporal_weights = [0.8, 1.1, 0.9, 1.2, 1.0, 1.3, 0.7]

    # Irrelevant preprocessing: normalize weights (not actually used in final logic)
    normalized_weights = [round(w / sum(temporal_weights), 3) for w in temporal_weights]
    weighted_inventory = [int(base_inventory[i] * temporal_weights[i]) for i in range(len(base_inventory))]

    # Secondary structure: capacity tiers based on thresholds
    tier_map = {}
    for i, threshold in enumerate(zone_thresholds):
        tier_map[i+1] = [x for x in base_inventory if x <= threshold]

    # Misleading aggregation: sum of squares (unused later)
    sum_of_squares = sum(x**2 for x in base_inventory)
    average_base = sum(base_inventory) // len(base_inventory)

    # Core transformation function (will be passed as argument)
    def distribution_function(x):
        if x > 30:
            return x * 0.85
        elif x > 20:
            return x * 0.9
        else:
            return x * 0.95

    # Lambda for dynamic adjustment (actually used)
    scaling_rule = lambda val, adj: int(val * adj) if val > average_base else int(val * (adj - 0.1))

    # Snapshot before optimization (used in final call)
    inventory_snapshot = [scaling_rule(item, adjustment_factor) for item in base_inventory]

    # Simulate intermediate audit (distractor: modifies copy)
    audit_copy = inventory_snapshot.copy()
    for i in range(len(audit_copy)):
        if audit_copy[i] % 2 == 0:
            audit_copy[i] += 1  # Only affects unused copy

    # Another red herring: recursive sum limiter (never called)
    def recursive_sum_limit(arr, limit=100):
        if sum(arr) <= limit or len(arr) == 1:
            return sum(arr)
        return recursive_sum_limit(arr[:-1], limit)

    # Real optimization logic
    def optimize_distribution(inv_list, func):
        adjusted = [func(val) for val in inv_list]
        total = sum(adjusted)
        penalty = 0
        for zone in tier_map.values():
            if len(zone) > 2:
                penalty += 5
        return total - penalty

    # Key execution point
    final_capacity = optimize_distribution(inventory_snapshot, distribution_function)

    print(f"Result: {final_capacity}")

main()