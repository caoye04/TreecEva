def main():
    # Simulate agricultural field data with moisture, nutrient levels, and area
    field_data = [
        {'moisture': 0.68, 'nutrients': 78, 'area': 12.5},
        {'moisture': 0.54, 'nutrients': 65, 'area': 8.0},
        {'moisture': 0.82, 'nutrients': 90, 'area': 15.3},
        {'moisture': 0.39, 'nutrients': 45, 'area': 5.7},
        {'moisture': 0.71, 'nutrients': 83, 'area': 10.2}
    ]

    # Irrelevant baseline metrics (distractor)
    baseline_moisture = 0.6
    ideal_nutrient_range = (70, 100)
    adjustment_factor = 1.15

    # Misleading transformation (not used in final calculation)
    adjusted_fields = []
    for f in field_data:
        adjusted = f.copy()
        adjusted['moisture'] *= adjustment_factor
        adjusted['adjusted_flag'] = True
        adjusted_fields.append(adjusted)

    # Red herring: unused helper function
    def predict_rainfall_impact(moisture_val):
        return moisture_val * 0.9 if moisture_val > 0.7 else moisture_val * 1.2

    # Actual threshold logic for viable fields
    threshold_fn = lambda x: x['moisture'] >= 0.6 and x['nutrients'] >= 70

    # Secondary distractor: grouping by size (unused)
    small_fields = [f for f in field_data if f['area'] < 10]
    large_fields = [f for f in field_data if f['area'] >= 10]

    # Track cumulative stats (some irrelevant)
    total_area = sum(f['area'] for f in field_data)
    viable_count = 0
    total_efficiency_score = 0.0
    efficiency_contributions = []

    # Core logic with nested conditions and dictionary operations
    for field in field_data:
        if threshold_fn(field):
            viability_score = field['moisture'] * field['nutrients']
            normalized_score = viability_score / 100.0
            weighted_yield = normalized_score * field['area']
            efficiency_contributions.append(weighted_yield)
            total_efficiency_score += weighted_yield
            viable_count += 1

    # Dead code path: never executed due to logic
    if len(small_fields) > 10:
        fallback_yield = sum(efficiency_contributions) * 0.8
    else:
        fallback_yield = 0  # Unused

    # Final computation
    base_yield = total_efficiency_score * 0.85
    penalty_reduction = viable_count * 0.5 if viable_count < 3 else 0
    final_yield = base_yield - penalty_reduction

    print(f"Result: {final_yield}")

main()