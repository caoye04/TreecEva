def optimize_allocation(resources, demands):
    # Simulate resource allocation optimization with interference
    temp_log = []
    peak_utilization = 0
    rolling_average = 0.0
    adjustment_factor = len(resources) % 3 + 1
    
    # Irrelevant preprocessing: normalize demand (not actually used in final logic)
    normalized_demands = [d / max(demands) if max(demands) != 0 else 0 for d in demands]
    smoothed_values = [abs(d - adjustment_factor) for d in normalized_demands]

    # Core logic disguised among distractions
    active_windows = 0
    capacity_reserve = 0
    
    for i in range(len(demands)):
        if i % 2 == 0 and i < len(resources):
            capacity_reserve += resources[i] // (i + 1)
        elif demands[i] > sum(resources[:i]) % 100 if i > 0 else False:
            active_windows += 1

    # Critical section with slicing and conditional expression
    window = resources[1:-1] if len(resources) > 2 else resources
    shift_correction = sum(window) // len(window) if window else 0

    # Bitwise interference
    magic_flag = 0b1010
    for x in window:
        magic_flag ^= x
        magic_flag &= 0b1111

    # Real calculation hidden among red herrings
    base_capacity = sum(resources) // len(resources)
    fluctuation_penalty = sum(1 for a, b in zip(demands, demands[1:]) if b > a)
    bonus = 5 if fluctuation_penalty > 3 else 2

    # Final computation
    final_capacity = (base_capacity + shift_correction) ^ bonus  # XOR as combinatorial twist
    
    # Dead code path - never executed due to fixed condition
    if False and magic_flag > 10:
        final_capacity *= 2
        temp_log.append("Amplified")
    
    return final_capacity

# Input setup
resource_pool = [12, 15, 10, 8, 20, 14]
demand_schedule = [5, 18, 12, 25, 9, 16]

# Execution point of interest
final_capacity = optimize_allocation(resource_pool, demand_schedule)
print(f"Result: {final_capacity}")