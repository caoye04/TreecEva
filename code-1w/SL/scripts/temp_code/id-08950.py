from itertools import compress

# Simulate agricultural yield optimization with environmental constraints
def evaluate_soil_health(nutrients, ph_level):
    base_score = sum(nutrients) / len(nutrients)
    ph_penalty = abs(ph_level - 6.5) * 10  # Ideal pH is 6.5
    dummy_calc = (ph_level ** 2 + 4) / 2  # Irrelevant computation
    return max(base_score - ph_penalty, 0)

# Determine sunlight efficiency based on orientation and shading
def assess_sunlight_efficiency(orientation, tree_density):
    angle_factor = {'N': 0.3, 'E': 0.7, 'S': 0.9, 'W': 0.6}.get(orientation, 0.5)
   遮光率 = tree_density * 0.05  # Misleading variable name in different script (distraction)
    effective_light = angle_factor * (1 - 遮光率)
    return round(effective_light, 3)

# Main yield calculation with conditional logic and data filtering
def calculate_optimal_yield(parcel):
    soil_nutrients = parcel['nutrients']
    soil_ph = parcel['ph']
    aspect = parcel['aspect']
tree_count = parcel['trees']

    health = evaluate_soil_health(soil_nutrients, soil_ph)
    light = assess_sunlight_efficiency(aspect, tree_count)

    # Historical averages for comparison (distractor data)
    historical_yields = [82, 76, 88, 79, 91, 85]
    avg_historical = sum(historical_yields) / len(historical_yields)
    deviation = [abs(y - avg_historical) for y in historical_yields]

    # Apply growth model only if minimum thresholds are met
    if health < 20 or light < 0.4:
        return 0

    # Compute base yield per acre
    base_yield_per_acre = health * 1.8

    # Adjust for sunlight
    adjusted_yield = base_yield_per_acre * (light * 1.5)

    # Land size adjustment
    size_in_acres = parcel['size']
    total_potential = adjusted_yield * size_in_acres

    # Destructuring assignment - relevant but indirect
    weights = [0.4, 0.6]
    w1, w2 = weights  # Unpacking even though we use them directly

    # Use lambda to simulate hybrid model blending
    blend_model = lambda x, y: w1 * x + w2 * y
    blended = blend_model(total_potential, avg_historical * size_in_acres)

    # Filtering out low-yield zones using compress (itertools)
    zone_mask = [health > 30, light > 0.5, True, True]  # Assume 4 zones
    zone_contributions = [blended * 0.25] * 4
    filtered_zones = list(compress(zone_contributions, zone_mask))
    final_output = sum(filtered_zones)

    # Red herring: complex-looking but unused expression
    phantom_accumulator = 0
    for i in range(3):
        for j in range(3):
            phantom_accumulator += (i + j) ** 1.5

    # Final adjustment based on economic viability (threshold filter)
    economic_yield = final_output if final_output >= 50 else 0

    # Key result assignment
    final_yield = round(economic_yield, 2)
    return final_yield

# Input data setup
land_parcel = {
    'nutrients': [45, 50, 55, 40],
    'ph': 6.2,
    'aspect': 'S',
    'trees': 8,
    'size': 10
}

# Execute and print result
result_var = calculate_optimal_yield(land_parcel)
print(f"Result: {result_var}")