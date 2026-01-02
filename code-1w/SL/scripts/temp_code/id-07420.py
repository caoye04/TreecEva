def analyze_phase_contribution(elements, threshold=3):
    relevant = set()
    for idx, val in enumerate(elements):
        if val % 2 == 0 and idx < threshold:
            relevant.add(val)
    return relevant


def compute_dynamic_offset(seq):
    offset = 0
    for i in range(len(seq)):
        if i % 3 == 0:
            offset += seq[i] * 2
        elif i % 3 == 1:
            offset -= seq[i]
    return offset

# Simulate multi-phase industrial production cycles
production_cycles = [5, 8, 12, 3, 9, 6, 11]
baseline_reference = sum(production_cycles) // len(production_cycles)

# Irrelevant intermediate: phase efficiency scores (not used in final yield)
efficiency_scores = []
for cycle in production_cycles:
    if cycle > baseline_reference:
        efficiency_scores.append(cycle * 0.85)
    else:
        efficiency_scores.append(cycle * 0.65)

# Misleading computation: total theoretical capacity (unused)
theoretical_capacity = sum([x**2 for x in production_cycles if x > 7]) // 2

# Key data transformation: shift-based adjustment using slicing
adjusted_cycles = production_cycles[1:] + [production_cycles[0]]
decay_factor = 0.9

# Apply decay over three iterations (simulates degradation)
for _ in range(3):
    adjusted_cycles = [int(x * decay_factor) for x in adjusted_cycles]
    decay_factor *= 0.95

# Extract core components using set operations
core_elements = set(production_cycles)
side_elements = set(adjusted_cycles)
common_flow = core_elements.intersection(side_elements)

# Red herring: unused string processing involving cycle labels
labels = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
label_mapping = {k: v for k, v in zip(production_cycles, labels)}
encoded_sequence = ''.join([label_mapping.get(x, 'X') for x in production_cycles])
rotated_labels = encoded_sequence[2:] + encoded_sequence[:2]  # Dead code path

# Compute dynamic offset from modified sequence
tracking_offset = compute_dynamic_offset(list(common_flow))

# Harvest function combines multiple concepts
def harvest_results(cycles):
    base_yield = 0
    peak = max(cycles)
    
    # Nested logic with conditional increments
    for i, val in enumerate(cycles):
        if val >= baseline_reference:
            contribution = val // 2
            if i % 2 == 1:
                contribution += tracking_offset
            base_yield += contribution
    
    # Additional adjustment via string-derived weight (fake dependency)
    temp_str = f"{sum(cycles)}"
    digit_sum = sum(int(d) for d in temp_str)
    fake_weight = len(rotated_labels) - digit_sum  # Computation with no real impact
    
    # Final composition
    final_component = base_yield + len(common_flow)
    return final_component

# Critical execution point
final_yield = harvest_results(production_cycles)
print(f"Result: {final_yield}")