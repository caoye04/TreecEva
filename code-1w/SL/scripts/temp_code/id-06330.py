def calculate_harvest(regions, efficiency):
    base_yield = 100
    modifiers = {'coastal': 1.2, 'forest': 1.5, 'plains': 1.3, 'mountain': 0.8}
    terrain_bonus = 0
    total_yield = 0
    temp_results = []

    for region in regions:
        area_id, terrain, size = region
        if terrain in modifiers:
            base_mod = modifiers[terrain]
            eff = efficiency.get(area_id, 1.0)
            raw_yield = base_yield * size
            adjusted_yield = raw_yield * base_mod * eff
            
            # Distractor: tracking intermediate values not used in final logic
            temp_results.append((area_id, adjusted_yield))
            terrain_bonus += base_mod * 0.1
        else:
            adjusted_yield = base_yield * size * 0.5

        # Real accumulation
        total_yield += adjusted_yield

    # Irrelevant transformation
    reversed_results = temp_results[::-1]
    average_temp = sum(val for _, val in temp_results) / len(temp_results) if temp_results else 0

    # Final adjustment using only total_yield and fixed logic
    stabilization_factor = 0.95
    final_yield = int(total_yield * stabilization_factor - terrain_bonus * 10)

    # Dead code: never executed but adds cognitive load
    if False:
        fallback = sum(size for _, _, size in regions) * 50
        final_yield = fallback

    return final_yield

# Simulation setup
efficiency_map = {1: 1.1, 2: 0.95, 3: 1.05}
regions = [
    (1, 'coastal', 10),
    (2, 'forest', 8),
    (3, 'plains', 12)
]

# Key execution point
final_yield = calculate_harvest(regions, efficiency_map)
print(f"Result: {final_yield}")