def analyze_growth_factors(conditions):
    # Irrelevant processing of string metadata
    season_tag = conditions['season'].upper().replace('_', '')
    modifier = len(season_tag) if 'WET' in season_tag else -1

    # Distractor: temperature adjustments that aren't used later
    temp_adj = conditions['temp'] + (modifier * 0.5)
    adjusted_temp = max(10, min(temp_adj, 40))  # Clamped for safety

    # Real computation path begins
    base_rainfall = conditions['rainfall']
    normalized_rain = base_rainfall / 100.0
    return normalized_rain


def validate_soil_composition(profiles):
    # String-based classification with red herring logic
    valid_types = ['LOAM', 'SILT', 'CLAY']
    scores = {}
    total_valid = 0

    for pid, data in profiles.items():
        # Misleading complexity: case conversion and parsing
        soil_type = data['type'].strip().upper()
        ph_level = data['ph']

        # Distractor: unused quality score calculation
        quality_score = 100 - abs(ph_level - 6.5) * 10
        stability_index = data.get('density', 1.3) * 100

        # Actual decision logic
        if soil_type in valid_types and 5.5 <= ph_level <= 7.5:
            scores[pid] = True
            total_valid += 1
        else:
            scores[pid] = False

    # Return only boolean summary, making individual scores irrelevant
    return total_valid > 0


def calculate_harvest_potential(climate, soils):
    # Step 1: Extract and normalize rainfall
    rain_factor = analyze_growth_factors(climate)

    # Step 2: Check soil validity
    viable_soil = validate_soil_composition(soils)

    # Step 3: Base yield estimation
    base_yield = 5000 * rain_factor

    # Step 4: Apply conditional boost
    if viable_soil:
        base_yield *= 1.25

    # Step 5: Adjust with hidden rule — cap at 6250 if season has 'DRY'
    if 'DRY' in climate['season'].upper():
        base_yield = min(base_yield, 6250)

    # Step 6: Final micro-adjustment using string length (obscure but deterministic)
    tag_len = len(climate['season'].replace('-', ''))
    final_yield = base_yield + (tag_len * 2)

    return final_yield

# Main execution
climate_data = {
    'season': 'LATE-DRY',
    'temp': 32,
    'rainfall': 780
}

soil_profiles = {
    'plot_A': {'type': 'loam', 'ph': 6.2, 'density': 1.4},
    'plot_B': {'type': 'sand', 'ph': 8.0},
    'plot_C': {'type': 'silt', 'ph': 6.8}
}

final_yield = calculate_harvest_potential(climate_data, soil_profiles)
print(f"Target result: {final_yield}")