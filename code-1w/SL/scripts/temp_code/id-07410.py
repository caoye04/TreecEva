from itertools import permutations

def analyze_resource_efficiency(resources):
    efficiency = {}
    total_utilized = sum(resources.values())
    for k, v in resources.items():
        efficiency[k] = round(v / total_utilized, 4) if total_utilized else 0
    return efficiency

def validate_allocation(seq, constraints):
    for i in range(len(seq) - 1):
        if abs(seq[i] - seq[i+1]) > constraints['jump_limit']:
            return False
    return True

def calculate_system_capacity(resource_config, sequence_plan):
    base_capacity = 0
    adjustment_factor = 0.0
    temp_storage = []

    # Simulate multi-phase capacity calculation
    for key in sorted(resource_config.keys()):
        val = resource_config[key]
        if val > 10:
            base_capacity += val * 1.5
        elif val > 5:
            base_capacity += val * 2
        else:
            base_capacity += val

    # Apply sequence-dependent modulation (only valid sequences contribute)
    valid_perms = 0
    for perm in permutations(sequence_plan):
        if validate_allocation(perm, {'jump_limit': 3}):
            valid_perms += 1

    # Irrelevant intermediate: track max permutation sum (not used in final result)
    max_sum = sum(max(p) for p in permutations(sequence_plan[:2])) if sequence_plan else 0

    # Actual adjustment based on valid configuration paths
    if valid_perms > 10:
        adjustment_factor = 1.25
    elif valid_perms > 5:
        adjustment_factor = 1.15
    else:
        adjustment_factor = 0.9

    # Introduce distractor state tracking
    state_log = {}
    for idx, val in enumerate(sequence_plan):
        state_log[f'step_{idx}'] = val * (idx + 1)
    cumulative_state = sum(state_log.values())  # Unused but plausible distraction

    # Final capacity with controlled interference
    final_capacity = int(base_capacity * adjustment_factor)

    # Print required output
    print(f"Result: {final_capacity}")
    return final_capacity

# Main execution context
resource_map = {
    'node_a': 12,
    'node_b': 8,
    'node_c': 15,
    'node_d': 4,
    'node_e': 6
}

allocation_sequence = [2, 1, 4, 3, 5]

# Trigger function call
final_capacity = calculate_system_capacity(resource_map, allocation_sequence)