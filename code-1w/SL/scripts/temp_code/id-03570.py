def analyze_metallurgical_sample():
    base_elements = ['Fe', 'Ni', 'Cr', 'Mo', 'Ti']
    trace_contaminants = ['S', 'P', 'O', 'N', 'H']

    raw_readings = [18.2, 22.1, 15.6, 8.9, 43.3, 7.4, 31.8, 9.2]
    normalized_signals = [round(x ** 0.5, 3) for x in raw_readings if x > 10]

    # Irrelevant spectroscopy calibration (distractor)
    calibration_coefficients = list(map(lambda x: (x + 1.5) / 4.7, [3, 7, 2, 8]))
    adjusted_offsets = [calibration_coefficients[i % 4] * 0.87 for i in range(10)]

    # Simulate compound generation with slicing and transformations
    element_pool = base_elements + trace_contaminants[::-1]
    shifted_pool = element_pool[2:] + element_pool[:2]
    compound_templates = [
        shifted_pool[i:i+4] for i in range(0, len(shifted_pool), 3)
    ]

    # Generate metallurgical phases (some irrelevant)
    phase_codes = []
    for idx, template in enumerate(compound_templates):
        code = sum([len(elem) * (idx + 1) for elem in template])
        phase_codes.append(code * 2 if code % 2 == 0 else code * 3)

    # Decoy processing path (dead branch)
    if len(phase_codes) > 10:
        backup_analysis = [c >> 1 for c in phase_codes if c & 1]
    else:
        temp_mask = 0
        for p in phase_codes:
            temp_mask ^= p

    # Core logic disguised among distractions
    def compute_stability_factor(seq):
        return sum(ord(c) for c in str(seq)) % 17

    def evaluate_crystalline_form(formula_str):
        mid_section = formula_str[2:-2]
        score = 0
        for char in mid_section:
            if char in 'aeiou':
                score += 5
            elif char.isupper():
                score += 3
        return score * len(mid_section)

    def process_alloy_composition(compound):
        if isinstance(compound, list):
            # Real transformation path
            lengths = [len(item) for item in compound]
            total = sum(lengths)
            modifier = 1 if total % 2 == 0 else -1
            base_value = total * lengths[0] + modifier * lengths[-1]
            return abs(base_value - compute_stability_factor(compound))
        return 0

    # Construct actual compounds using slicing and manipulation
    final_compounds = []
    for i in range(len(normalized_signals)):
        if i % 2 == 0 and normalized_signals[i] > 3:
            segment = raw_readings[i:i+3]
            transformed = ''.join([
                chr(int(sum(segment) / len(segment)) + offset)
                for offset in [65, 70, 75]
            ])
            evaluated = evaluate_crystalline_form(transformed)
            if evaluated > 40:
                # This appends lists to final_compounds
                final_compounds.append(
                    [base_elements[j % 5] for j in range(evaluated % 7 + 3)]
                )

    # Red herring: unused filtering function
    def filter_artifacts(data):
        return [x for x in data if isinstance(x, float) and x.is_integer()]

    # Unused intermediate variables (distraction)
    aggregation_map = {i: phase_codes[i] for i in range(len(phase_codes))}
    cumulative_shift = sum(adjusted_offsets[:len(raw_readings)])

    # Key execution point
    filtration_score = process_alloy_composition(final_compounds[-1])

    # Output target result
    print(f"Result: {filtration_score}")

analyze_metallurgical_sample()