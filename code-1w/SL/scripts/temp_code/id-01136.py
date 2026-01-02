def calculate_harvest_efficiency(plots, quality_map):
    base_multiplier = 1.5
    penalty_factor = 0.9
    bonus_threshold = 75
    efficiency_ratings = []
    
    # Precompute auxiliary statistics (some irrelevant)
    total_area = sum([p[1] for p in plots])
    avg_size = total_area / len(plots) if plots else 0
    size_variance = sum([(p[1] - avg_size)**2 for p in plots]) / len(plots) if plots else 0

    dummy_correction = 0.05 * size_variance

    for i, (crop_type, area) in enumerate(plots):
        base_yield = area * base_multiplier
        
        # Soil quality adjustment
        soil_score = quality_map.get(i, 50)
        adjusted_yield = base_yield * (soil_score / 100.0)
        
        # Apply conditional bonus using lambda for dynamic thresholding
        is_high_quality = (lambda x: x > bonus_threshold)(soil_score)
        
        if is_high_quality and crop_type in ['wheat', 'corn']:
            adjusted_yield *= 1.2
        elif soil_score < 40:
            adjusted_yield *= penalty_factor

        # Irrelevant transformation
        normalized = adjusted_yield / (area + 1e-8)
        efficiency_ratings.append(adjusted_yield)

    # Summation with distractor logic
    raw_sum = sum(efficiency_ratings)
    count_correction = len(efficiency_ratings) * dummy_correction
    final_yield = int(raw_sum - count_correction)  # Final answer is deterministic

    # Unused diagnostic variables
    max_single_yield = max(efficiency_ratings) if efficiency_ratings else 0
    yield_per_unit = [ry/area for (crop_type, area), ry in zip(plots, efficiency_ratings) if area > 0]

    return final_yield

# Input data
plots_data = [
    ('wheat', 20),
    ('corn', 30),
    ('barley', 25),
    ('wheat', 15)
]

soil_conditions = {
    0: 80,
    1: 90,
    2: 60,
    3: 45
}

# Execution point
final_yield = calculate_harvest_efficiency(plots_data, soil_conditions)
print(f"Result: {final_yield}")