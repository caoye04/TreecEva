def analyze_agricultural_output():
    # Initialize crop production data
    crop_data = {
        'wheat': {
            'base_yield': 3.2,
            'area_planted': 1500,
            'yield': 2.8,
            'pest_incidence': 0.15
        },
        'corn': {
            'base_yield': 4.1,
            'area_planted': 1200,
            'yield': 3.9,
            'pest_incidence': 0.08
        },
        'barley': {
            'base_yield': 2.5,
            'area_planted': 800,
            'yield': 2.3,
            'pest_incidence': 0.2
        }
    }

    # Environmental and economic factors
    weather_index = 0.92
    soil_quality = 0.88
    market_demand = {'wheat': 1.05, 'corn': 0.97, 'barley': 1.02}
    subsidy_rate = 0.03

    # Calculate composite growth factor (mostly irrelevant for final yield)
    for crop in crop_data:
        base = crop_data[crop]['base_yield']
        area = crop_data[crop]['area_planted']
        pest_level = crop_data[crop]['pest_incidence']
        theoretical_max = base * (1 - pest_level) * weather_index * soil_quality
        normalized_yield = theoretical_max * market_demand[crop]
        crop_data[crop]['potential'] = round(normalized_yield, 3)

    # Focus on wheat analysis
    current_yield = crop_data['wheat']['yield']
    pest_ratio = crop_data['wheat']['pest_incidence']

    # Adjustment logic with conditional expression
    adjustment_factor = 1.1 if pest_ratio < 0.1 else 0.95

    # Simulate policy impact (irrelevant to core calculation but adds noise)
    total_area = sum(crop_data[crop]['area_planted'] for crop in crop_data)
    avg_pest = sum(crop_data[cr]['pest_incidence'] for cr in crop_data) / len(crop_data)
    national_risk_score = total_area * avg_pest * 0.001

    # Bonus offset based on performance tier
    performance_tier = 'A' if current_yield >= 2.7 else 'B'
    bonus_offset = 0.15 if performance_tier == 'A' else 0.05

    # Sorting crops by yield (distractor operation)
    sorted_crops = sorted(crop_data.keys(), key=lambda x: crop_data[x]['yield'], reverse=True)

    # Core computation step — this determines the answer
    final_yield = crop_data['wheat']['yield'] * adjustment_factor + bonus_offset

    # Irrelevant string manipulation (adds cognitive load)
    report_id = "AGRI-" + "WHEAT"[:3] + "-" + str(int(current_yield * 100))
    status_flag = report_id.lower().replace('-', '_') if national_risk_score < 1.0 else 'high_risk'

    # Print result as required
    print(f"Result: {final_yield}")

analyze_agricultural_output()