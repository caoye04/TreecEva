def optimize_distribution(capacity_list, rate_sequence):
    temp_buffer = [0] * len(capacity_list)
    cumulative_shift = 0
    
    # Irrelevant pre-processing: normalize rates (not actually used in final logic)
    normalized_rates = [round(r / sum(rate_sequence), 3) for r in rate_sequence]
    offset_adjustment = sum(normalized_rates) * 10  # Red herring computation

    # Actual logic begins: simulate load redistribution
    for i in range(len(capacity_list)):
        shift_factor = (i + 1) % 3
        if shift_factor == 0:
            temp_buffer[i] = capacity_list[i] * 0.9
        elif shift_factor == 1:
            temp_buffer[i] = capacity_list[i] * 1.1
        else:
            temp_buffer[i] = capacity_list[i] * 0.95

    # Secondary transformation using lambda and slicing
    transformer = lambda x: x ** 2 if x < 90 else x ** 0.5
    transformed = [transformer(val) for val in temp_buffer[::2]]  # Only even indices

    # Simulate feedback loop with dictionary tracking
    status_log = {}
    feedback_factor = 0.0
    for idx, val in enumerate(transformed):
        key = f"step_{idx}"
        adjusted = val * (1 + feedback_factor)
        status_log[key] = round(adjusted, 3)
        feedback_factor += 0.05  # Accumulates but only affects logging

    # Core result calculation
    base_total = sum(temp_buffer)
    penalty = len([x for x in capacity_list if x > 85]) * 2.5
    bonus = len([x for x in capacity_list if x < 40]) * 1.75
    
    # Final adjustment using tuple unpacking
    multiplier, threshold = (1.05, 100)
    if base_total > threshold:
        final_capacity = (base_total - penalty + bonus) * multiplier
    else:
        final_capacity = (base_total - penalty + bonus) * 0.95

    return final_capacity

# Input data
capacities = [88, 45, 67, 33, 91]
flow_rates = [23, 15, 37, 29, 41]

# Misleading preliminary calculation
initial_estimate = sum(capacities) * 0.8
placeholder_result = [x * 0.1 for x in flow_rates if x > 25]  # Dead-end list

final_capacity = optimize_distribution(capacities, flow_rates)
print(f"Result: {final_capacity}")