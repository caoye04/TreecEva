import itertools

def analyze_growth_cycle(plots):
    # Irrelevant analysis function (dead code path)
    peak_phases = []
    for p in plots:
        if sum(p) > 50:
            peak_phases.append(max(p))
    return sorted(peak_phases, reverse=True)

def preprocess_soil_samples(samples):
    # Distractor: unused preprocessing logic
    processed = []
    for s in samples:
        adjusted = [val * 0.95 + 2.1 for val in s]
        processed.append([round(x, 1) for x in adjusted])
    return processed

def calculate_harvest_efficiency(fields, cfg):
    base_multiplier = cfg['multiplier']
    threshold = cfg['threshold']
    total_yield = 0
    bonus_applied = False

    # Real logic begins: extract valid field rows using itertools
    filtered_fields = list(itertools.filterfalse(lambda f: len(f) < 4, fields))

    temp_aggregate = 0
    for i, field in enumerate(filtered_fields):
        # Misleading intermediate transformation
        shifted = [(x << 1) >> 1 for x in field]  # No-op bit manipulation (distractor)

        row_sum = sum(shifted)
        temp_aggregate += row_sum

        # Actual key computation
        if row_sum > threshold:
            adjustment_factor = 1.2 if i % 2 == 0 else 0.9
            total_yield += row_sum * adjustment_factor

        # Red herring: complex condition that never triggers
        if all(x > 15 for x in shifted) and any(x % 7 == 0 for x in shifted):
            total_yield -= 100  # Dead logic branch (never reached in input)

    # Decoy aggregation with no effect
    outlier_count = 0
    for f in filtered_fields:
        avg = sum(f) / len(f)
        outlier_count += len([x for x in f if abs(x - avg) > 2 * avg])

    # Core calculation affected by configuration
    if temp_aggregate > 300:
        base_multiplier *= 1.1

    final_calc = total_yield * base_multiplier

    # Unused lambda — misleading functional style
    transform = lambda x: x * 0.99 if x > 100 else x * 1.01

    # Critical assignment
    final_yield = int(round(final_calc / len(filtered_fields)))

    # More red herrings
    status_flags = [True, False, True]
    flag_result = all(status_flags) or not (status_flags[1] and len(filtered_fields) < 5)

    return final_yield

# Simulated sensor data from agricultural zones (some invalid entries)
field_data = [
    [12, 15, 18, 23],
    [8, 10],           # Will be filtered out (length < 4)
    [20, 22, 19, 24, 21],
    [16, 14, 17, 15],
    [9, 11, 13, 10, 12]
]

# Soil sample readings — irrelevant to final result
soil_samples = [
    [4.2, 5.1, 4.8],
    [5.5, 4.9, 5.3],
    [4.7, 5.0, 4.6]
]

# Configuration dictionary with meaningful parameters
config = {
    'multiplier': 1.5,
    'threshold': 60,
    'debug_mode': False,
    'max_iter': 100
}

# Execute irrelevant preprocessing (distractor)
processed_samples = preprocess_soil_samples(soil_samples)

# Call analysis function that doesn't affect outcome
growth_phases = analyze_growth_cycle(field_data)

# Key statement: produces the target variable
final_yield = calculate_harvest_efficiency(field_data, config)

# Output result as required
print(f"Result: {final_yield}")