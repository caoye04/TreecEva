def analyze_material_composition(elements):
    atomic_weights = {'Fe': 55.85, 'O': 16.00, 'C': 12.01, 'H': 1.01, 'N': 14.01}
    total_weight = 0.0
    processed_elements = []
    
    # Irrelevant tracking variables (distractors)
    element_count_log = []
    cumulative_sum_tracker = 0
    redundant_flag = False

    for idx, elem in enumerate(elements):
        if elem in atomic_weights:
            weight = atomic_weights[elem]
            total_weight += weight
            processed_elements.append((idx, elem, weight))
            
            # Distractor computation: logs index but isn't used later
            element_count_log.append(idx * 2 + 1)
            cumulative_sum_tracker += idx % 3
            
            if weight > 50 and not redundant_flag:
                redundant_flag = True  # Never actually used

    # Semi-relevant transformation using zip and enumerate
    indexed_weights = [w for _, _, w in processed_elements]
    paired_shifts = list(zip(indexed_weights, [w * 0.1 for w in indexed_weights]))
    adjusted_weights = [a + b for a, b in paired_shifts]

    # Dummy set operations for interference
    unique_weights = set(indexed_weights)
    shifted_set = set([round(w * 0.1, 2) for w in unique_weights])
    overlap = unique_weights.intersection(shifted_set)  # Unused

    return processed_elements, total_weight


def calculate_thermal_output(processed_elements):
    base_multiplier = 2.5
    decay_factor = 0.95
    thermal_capacity = 0

    # Additional distraction: early loop with dead condition
    temp_storage = []
    for i, (pos, el, wt) in enumerate(processed_elements):
        if i > len(processed_elements):  # Dead code path
            break
        temp_storage.append(wt * i)

    # Actual logic: accumulate thermal capacity using positional decay
    for i, (pos, el, wt) in enumerate(processed_elements):
        contribution = wt * base_multiplier * (decay_factor ** i)
        if el in ['O', 'H']:
            contribution *= 0.8  # Reduced impact for light elements
        thermal_capacity += contribution
    
    # Irrelevant post-processing
    final_list = [thermal_capacity / (j + 1) for j in range(3)]
    scalar_projection = sum(final_list) / len(final_list)

    return thermal_capacity  # Only this matters

# Main execution
input_elements = ['Fe', 'O', 'C', 'Fe', 'H', 'N']
processed_data, total_mass = analyze_material_composition(input_elements)
thermal_capacity = calculate_thermal_output(processed_elements)
print(f"Result: {thermal_capacity}")