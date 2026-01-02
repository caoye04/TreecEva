def analyze_composition(raw_data, thresholds):
    base_elements = {x for x in raw_data if x % 3 == 0}
    extended_profile = set()
    temp_sum = 0
    decoy_value = 0

    for i in range(1, 12):
        if i in base_elements:
            temp_sum += i * 2
        elif i % 4 == 0:
            decoy_value += i ** 2  # irrelevant path
        extended_profile.add(i * 3)

    filtered_extended = {x for x in extended_profile if x < 25}
    secondary_mask = {x for x in filtered_extended if x % 2 == 1}

    adjustment_factor = 0
    for val in secondary_mask:
        adjustment_factor += val % 7

    # Dead code path - never used
    def deprecated_transform(x):
        return (x + 5) // 2

    processed_elements = []
    for item in sorted(base_elements):
        transformed = item * 3 + adjustment_factor
        processed_elements.append(transformed)

    # Irrelevant dictionary construction
    metadata_log = {}
    for idx, val in enumerate(processed_elements):
        metadata_log[f'entry_{idx}'] = {
            'raw': val,
            'offset': val + 100,
            'flagged': False
        }

    # Another red herring: complex but unused calculation
    outlier_candidates = []
    for x in raw_data:
        if x > 20:
            outlier_candidates.append(x ^ 7)
    outlier_score = sum(outlier_candidates) // 2 if outlier_candidates else 0

    def evaluate_purity(elements):
        if not elements:
            return 0
        total = 0
        for e in elements:
            if e % 4 == 0:
                total += e // 4
            else:
                total += e % 5
        return total + len(elements)

    # Key computation with distractors around
    filtration_score = evaluate_purity(processed_elements)

    # Unused nested structure
    diagnostics = {
        'levels': [
            {'depth': 1, 'value': adjustment_factor},
            {'depth': 2, 'value': temp_sum},
            {'depth': 3, 'value': decoy_value}
        ]
    }

    # Print required result
    print(f"Result: {filtration_score}")
    return filtration_score

# Input data
input_stream = [3, 6, 9, 12, 15, 18, 21]
config_thresholds = {'min_val': 5, 'max_val': 20}

# Execute function
result = analyze_composition(input_stream, config_thresholds)