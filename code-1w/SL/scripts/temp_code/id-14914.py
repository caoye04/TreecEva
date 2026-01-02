def analyze_growth_cycle():
    # Simulate agricultural plot analysis with mixed computational logic
    plots = [
        {'id': 'A1', 'size': 120, 'crop': 'wheat', 'soil_q': 85, 'irrigated': True},
        {'id': 'B2', 'size': 95, 'crop': 'corn', 'soil_q': 70, 'irrigated': False},
        {'id': 'C3', 'size': 150, 'crop': 'barley', 'soil_q': 90, 'irrigated': True},
        {'id': 'D4', 'size': 80, 'crop': 'oats', 'soil_q': 60, 'irrigated': True}
    ]

    conditions = {
        'temperature_avg': 22.5,
        'rainfall_mm': 89,
        'optimal_temp_range': (18, 26),
        'min_rainfall': 50
    }

    # Irrelevant preprocessing: normalize crop names (not used later)
    normalized_crops = []
    for plot in plots:
        name = plot['crop'].upper()
        cleaned = ''.join([c for c in name if c.isalpha()])
        normalized_crops.append(cleaned[:3])

    # Misleading intermediate calculations
    total_size = sum(p['size'] for p in plots)
    avg_soil = sum(p['soil_q'] for p in plots) / len(plots)
    irrigated_count = len([p for p in plots if p['irrigated']])

    baseline_efficiency = 0.78
    temp_factor = 1.0
    if conditions['temperature_avg'] >= conditions['optimal_temp_range'][0]:
        if conditions['temperature_avg'] <= conditions['optimal_temp_range'][1]:
            temp_factor = 1.15
        else:
            temp_factor = 0.95
    else:
        temp_factor = 0.85

    rainfall_factor = 1.1 if conditions['rainfall_mm'] >= conditions['min_rainfall'] else 0.7

    # Distractor: unused yield prediction model
    def predict_yield(size, soil, irrigated):
        base = size * (soil / 100) * 0.5
        return base * 1.3 if irrigated else base * 0.9

    # Another distractor loop: compute per-plot theoretical output (unused)
    theoretical_yields = []
    for idx, plot in enumerate(plots):
        yield_val = predict_yield(plot['size'], plot['soil_q'], plot['irrigated'])
        theoretical_yields.append((idx, yield_val))

    # Real computation begins: efficiency based on weighted factors
    weights = {'size': 0.3, 'soil': 0.5, 'irrigation': 0.2}
    adjusted_scores = []

    for i, p in enumerate(plots):
        size_score = p['size'] / 100
        soil_score = p['soil_q'] / 100
        irrigation_bonus = 1.2 if p['irrigated'] else 1.0
        score = (
            size_score * weights['size'] + 
            soil_score * weights['soil']
        ) * irrigation_bonus
        adjusted_scores.append((i, score))

    # Use enumerate and zip as required
    indexed_results = []
    for idx, score in enumerate(adjusted_scores):
        indexed_results.append((idx, score[1] * temp_factor))

    # Combine with another dummy list using zip
    dummy_padding = [0.1 * (i+1) for i in range(len(indexed_results))]
    combined = []
    for res, pad in zip(indexed_results, dummy_padding):
        combined.append(res[1] + pad)  # padding has minimal effect

    # Final aggregation
    aggregate = sum(combined) * rainfall_factor * baseline_efficiency

    # Key variable assignment
    final_yield = int(round(aggregate * 100))  # scale and discretize

    # Print result for verification
    print(f"Target result: {final_yield}")

    return final_yield

# Execute function
def calculate_harvest_efficiency(plots, conditions):
    return analyze_growth_cycle()

result = analyze_growth_cycle()