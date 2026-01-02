from itertools import cycle

def calculate_remaining(capacities, usage_log):
    total_initial = sum(capacities)
    temp_buffer = [0] * len(capacities)
    overflow_flags = [False] * len(capacities)
    adjustment_factor = 0.95

    # Simulate cyclic usage over multiple phases
    for i, (device_id, usage) in enumerate(usage_log):
        normalized_index = device_id % len(capacities)
        temp_buffer[normalized_index] += usage

        # Irrelevant intermediate calculation (distractor)
        if i % 3 == 0:
            dummy_shift = (i * 2 + 1) % 7
            _ = dummy_shift ** 2  # Dead computation

        # Actual capacity reduction logic
        if temp_buffer[normalized_index] > capacities[normalized_index] * 0.8:
            overflow_flags[normalized_index] = True

    # Secondary processing with zip and enumerate
    reductions = []
    for idx, (cap, used) in enumerate(zip(capacities, temp_buffer)):
        utilization = used / cap if cap > 0 else 0
        penalty = 0.1 if overflow_flags[idx] else 0.05
        net_reduction = cap * (utilization + penalty)
        reductions.append(net_reduction)

    # Final adjustment using conditional expression
    base_remaining = sum(capacities) - sum(reductions)
    final_capacity = base_remaining if base_remaining > 10 else base_remaining * adjustment_factor
    
    # Extra unrelated tracking (distractor)
    status_cycle = cycle(['active', 'standby'])
    for _ in range(len(capacities)):
        next(status_cycle)  # No effect on result

    return final_capacity

def main():
    capacities = [100, 200, 150, 180]
    usage_log = [
        (0, 45), (1, 90), (2, 70), (3, 85),
        (0, 30), (1, 120), (2, 60), (3, 75)
    ]
    
    # Misleading pre-computation
    avg_load = sum([u for _, u in usage_log]) / len(capacities)
    threshold_check = avg_load > 50
    
    # Key statement
    final_capacity = calculate_remaining(capacities, usage_log)
    
    print(f"Result: {final_capacity}")

if __name__ == "__main__":
    main()