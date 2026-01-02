def analyze_soil_composition(ph_levels, nutrient_map):
    # Irrelevant analysis function (dead code path)
    composite_index = 0
    for ph in ph_levels:
        if ph > 7:
            composite_index += 0.3
        elif ph < 6:
            composite_index -= 0.1
    return composite_index

ph_readings = [5.4, 6.1, 6.8, 7.2, 5.9]
nutrients = {'N': 12, 'P': 8, 'K': 15}

# Distractor: unused transformation
tiled_grids = [[x * 1.5 for x in ph_readings if x < 6.5]]


def compute_microclimate_influence(temp_data, humidity_data):
    # Another red herring function with misleading intermediate calculations
    base_score = 0
    adjustment_factor = 1.0
    for t, h in zip(temp_data, humidity_data):
        if t > 25 and h < 60:
            base_score += 2
        elif t < 20:
            adjustment_factor *= 0.95
    refined_score = base_score * adjustment_factor
    return refined_score

# Unused sensor data
temperatures = [22, 26, 19, 28, 24]
humidity = [55, 45, 70, 40, 60]

# Real computation begins — nested within irrelevant context
cluster_data = [
    {'nodes': [1, 2, 3], 'active': True, 'weight': 0.8},
    {'nodes': [4, 5], 'active': False, 'weight': 1.2},
    {'nodes': [6, 7, 8, 9], 'active': True, 'weight': 0.9}
]

# Simulate growth cycles using list comprehension and enumerate
growth_cycles = []
for idx, cluster in enumerate(cluster_data):
    cycle_entry = {}
    if cluster['active']:
        node_count = len(cluster['nodes'])
        # Relevant calculation embedded in complex logic
        efficiency_mod = sum([i % 3 for i in cluster['nodes']]) / float(node_count)
        cycle_entry['cycle_id'] = idx
        cycle_entry['yield_potential'] = node_count * 12.5
        cycle_entry['modifier'] = efficiency_mod
        growth_cycles.append(cycle_entry)

# Misleading conditional branch that doesn't affect final result
if len(growth_cycles) > 5:
    growth_cycles = growth_cycles[:3]

# Core algorithm hidden among distractors
def calculate_harvest_efficiency(scores, cycles):
    total_yield = 0.0
    peak_adjustment = 0

    # Use of enumerate and zip in meaningful way
    for i, cycle in enumerate(cycles):
        raw_yield = cycle['yield_potential']
        mod = cycle['modifier']
        contribution = raw_yield * mod

        # Conditional branching with early continue (not all paths matter)
        if i % 2 == 0:
            contribution *= 1.1
        else:
            temp_var = contribution / 2  # Dead computation
            temp_var += 5  # Unused

        total_yield += contribution

        # Bitwise distraction
        peak_adjustment |= (i + 1) << 1

    # Final adjustment using set operations (some elements are red herrings)
    indices = {c['cycle_id'] for c in cycles}
    extras = {0, 2, 4, 6}
    overlap = indices & extras  # Only overlaps on 0 and 2
    bonus = len(overlap) * 7.5

    total_yield += bonus

    # One last decoy operation
    _ = [x for x in range(len(cycles)) if x not in indices]  # Unused list comp

    return total_yield

# Auxiliary scoring system (mostly irrelevant)
base_scores = [85, 90, 78]
weights = [0.2, 0.3, 0.5]
weighted_avg = sum(a*b for a,b in zip(base_scores, weights))  # Distractor

# Real input to target function
cluster_scores = {'method': 'adaptive', 'version': '2.1'}  # Partially ignored

# Key execution point
final_yield = calculate_harvest_efficiency(cluster_scores, growth_cycles)

print(f"Result: {final_yield}")