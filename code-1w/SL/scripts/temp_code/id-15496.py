from itertools import combinations

def analyze_soil_variability(samples):
    # Irrelevant analysis - distractor
    avg_ph = sum(s[0] for s in samples) / len(samples)
    ph_variance = sum((s[0] - avg_ph) ** 2 for s in samples)
    return ph_variance

def compute_nutrient_score(samples):
    # Semi-relevant: used in intermediate step but not final
    base_score = 0
    for sample in samples:
        ph, nitrogen, potassium = sample
        if ph > 6.5:
            base_score += nitrogen * 0.3
        else:
            base_score += potassium * 0.2
    return round(base_score, 2)

def compute_harvest_efficiency(data):
    total_yield = 0
    efficiency_bonus = 0

    # Real logic begins: extract region samples
    for region_id, samples in data.items():
        if len(samples) < 3:
            continue

        # Use slicing to get middle samples (exclude first and last)
        mid_samples = samples[1:-1]

        # Compute base yield from nitrogen levels
        base_yield = sum(sample[1] for sample in samples)  # nitrogen contributes

        # Apply conditional bonus using boolean logic
        has_high_potassium = any(s[2] > 150 for s in mid_samples)
        is_balanced_ph = all(6.0 <= s[0] <= 7.0 for s in mid_samples)

        if has_high_potassium and is_balanced_ph:
            efficiency_bonus += 15

        # Use itertools to check nutrient pair consistency
        valid_pairs = 0
        for pair in combinations(mid_samples, 2):
            diff_n = abs(pair[0][1] - pair[1][1])
            diff_k = abs(pair[0][2] - pair[1][2])
            if diff_n <= 10 and diff_k <= 20:
                valid_pairs += 1

        if valid_pairs >= 2:
            total_yield += base_yield * 1.2
        else:
            total_yield += base_yield * 0.9

    # Final computation
    final_efficiency = total_yield + efficiency_bonus

    # Dead code - irrelevant transformation
    normalized = [round(max(0, min(100, total_yield * 0.05)), 1)]

    return int(final_efficiency)

# Simulated agricultural survey data
region_data = {
    'north_field': [
        (5.8, 120, 130),
        (6.2, 135, 160),
        (6.7, 140, 155),
        (6.9, 138, 170)
    ],
    'south_greenhouse': [
        (7.1, 110, 140),
        (7.3, 105, 135),
        (7.0, 112, 142)
    ],
    'east_plot': [
        (6.3, 160, 180),
        (6.5, 155, 175),
        (6.4, 158, 170),
        (6.6, 162, 185),
        (6.5, 160, 180)
    ]
}

# Irrelevant preprocessing - distractor
ph_levels = [s[0] for region in region_data.values() for s in region]
sorted_ph = sorted(ph_levels)
median_ph = sorted_ph[len(sorted_ph)//2]

# Key computation steps
soil_variability = analyze_soil_variability([s for region in region_data.values() for s in region])
nutrient_profile = compute_nutrient_score([s for region in region_data.values() for s in region])

# Core execution point
final_yield = compute_harvest_efficiency(region_data)

# Output result
print(f"Result: {final_yield}")