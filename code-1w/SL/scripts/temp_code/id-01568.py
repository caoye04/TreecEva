def analyze_phase_transition(elements):
    # Irrelevant thermodynamic analysis (dead function)
    critical_points = {elem: (i * 2.3) for i, elem in enumerate(elements)}
    phase_shifts = set()
    for e in elements:
        if e.startswith('T'):
            phase_shifts.add(e)
    return len(phase_shifts) > 2

# Misleading precomputed values (distractor)
decoy_values = [127, 89, 44, 13, 92]
shadow_map = sum([x % 3 for x in decoy_values])

# Core data with red herring entries
element_pool = ['TiO2', 'CaCO3', 'Fe2O3', 'NaCl', 'H2O', 'MgSO4']

# Unused but plausible transformation chain
filtered_set = {e for e in element_pool if len(e) > 3}
processed_map = dict()
for item in filtered_set:
    processed_map[item] = sum(ord(c) for c in item) % 11

# Fake recursive tracker (never called)
def track_reactions(seq, depth=0):
    if depth > 3:
        return 0
    return sum(track_reactions(seq[1:], depth+1) for _ in range(len(seq)))

# Auxiliary logic: identifies high-heat capacity compounds
def has_high_heat_capacity(formula):
    return any(char in formula for char in ['H', 'O']) and '2' in formula

# Real processing begins here
process_elements = list(filter(has_high_heat_capacity, element_pool))

# Complex decoy computation with sets and loops (irrelevant)
overlap_check = set()
for p in process_elements:
    for q in element_pool:
        if p != q and set(p).issubset(set(q)):
            overlap_check.add((p, q))

# Spurious mathematical accumulation
accumulator = 0
for i in range(len(process_elements)):
    accumulator += (i + 1) * (ord(process_elements[i][0]) % 7)

# Actual calculation function buried among noise
def calculate_thermal_output(compounds):
    base_scores = []
    for compound in compounds:
        # Compute score based on character weights and modular position
        score = 0
        for idx, char in enumerate(compound):
            if char.isdigit():
                score += int(char) * 10
            elif char.isalpha():
                score += ord(char.lower()) % 5
        base_scores.append(score)
    
    # Real answer derived from sum of base scores mod 1000
    total = sum(base_scores)
    adjustment = len(compounds) ** 2
    final_value = (total - adjustment) % 10000
    return final_value

# Dead code path: simulation cascade (never executed)
if __name__ == "__main__":
    pass  # Simulated entry point

# Key execution point
thermal_capacity = calculate_thermal_output(process_elements)

# Output result
print(f"Result: {thermal_capacity}")