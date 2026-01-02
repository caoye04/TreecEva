def analyze_soil_quality(plots):
    quality_scores = []
    for p in plots:
        base_score = p['nutrients'] * 0.4 + p['moisture'] * 0.6
        adjusted = base_score * (1 + 0.1 * p['shading'])
        quality_scores.append(round(adjusted, 2))
    return quality_scores

# Irrelevant soil analysis function (dead path)
def assess_pest_risk(plots):
    risk_levels = []
    for p in plots:
        if p['crop_type'] == 'wheat':
            risk = p['humidity'] * 0.3 + sum(p['insects']) * 0.7
        else:
            risk = p['humidity'] * 0.5
        risk_levels.append(int(risk))
    return risk_levels

# Distractor: unused crop mapping
crop_yield_map = {
    'wheat': lambda x: x * 1.2,
    'corn': lambda x: x * 1.5,
    'barley': lambda x: x * 0.9
}

def calculate_harvest(plots, weather):
    total_yield = 0
    bonus_trigger = False
    threshold_met_count = 0

    # Real logic begins
    for i, plot in enumerate(plots):
        # Extract relevant features with distractors
        base_productivity = plot['nutrients'] + plot['moisture']
        
        # Weather impact
        temp_factor = 1.0
        if weather['temperature'] > 30:
            temp_factor = 0.8
        elif weather['temperature'] < 15:
            temp_factor = 0.6

        # Rain boost
        rain_boost = 1.1 if weather['rainfall'] > 50 else 1.0
        
        # Light efficiency using string-based condition (idiom)
        light_efficiency = 0.9 if plot.get('exposure', '').lower() == 'full' else 0.6

        # Core yield calculation
        plot_yield = base_productivity * temp_factor * rain_boost * light_efficiency
        
        # Conditional bonus logic
        if plot_yield > 80 and plot['soil_type'] != 'sandy':
            threshold_met_count += 1

        total_yield += plot_yield

    # Bonus application (only if at least 3 plots meet criteria)
    if threshold_met_count >= 3:
        total_yield *= 1.15

    # Secondary adjustment based on wind
    if weather['wind_speed'] > 20:
        total_yield *= 0.92

    # Final transformation using zip and enumerate (python idiom)
    modifiers = [0.95, 1.05, 1.02, 0.98, 1.01]
    for idx, (plot, mod) in enumerate(zip(plots, modifiers)):
        if idx % 2 == 0:
            total_yield += mod * 0.5  # Minor incremental tweak

    # Final yield computed here
    final_yield = int(round(total_yield, 0))

    # Dead code: logging irrelevant stats
    avg_modifier = sum(modifiers) / len(modifiers) if modifiers else 1.0
    status_flag = 'OPTIMAL' if avg_modifier > 0.9 else 'SUBOPTIMAL'

    return final_yield

# Simulated farm data (real input)
land_plots = [
    {'nutrients': 30, 'moisture': 45, 'crop_type': 'wheat', 'soil_type': 'loamy', 'exposure': 'Full', 'shading': 2, 'humidity': 60, 'insects': [1, 0, 2]},
    {'nutrients': 35, 'moisture': 50, 'crop_type': 'corn', 'soil_type': 'clay', 'exposure': 'partial', 'shading': 1, 'humidity': 40, 'insects': [0, 1]},
    {'nutrients': 40, 'moisture': 60, 'crop_type': 'barley', 'soil_type': 'loamy', 'exposure': 'Full', 'shading': 0, 'humidity': 55, 'insects': [1, 1, 1]},
    {'nutrients': 25, 'moisture': 40, 'crop_type': 'wheat', 'soil_type': 'sandy', 'exposure': 'Full', 'shading': 3, 'humidity': 65, 'insects': [2, 2]},
    {'nutrients': 45, 'moisture': 55, 'crop_type': 'corn', 'soil_type': 'loamy', 'exposure': 'Full', 'shading': 1, 'humidity': 35, 'insects': [0, 0]}
]

weather_conditions = {
    'temperature': 25,
    'rainfall': 60,
    'wind_speed': 18,
    'humidity': 50
}

# Misleading preliminary analyses (distractors)
soil_analysis = analyze_soil_quality(land_plots)
pest_risk = assess_pest_risk(land_plots)

# Actual target computation
final_yield = calculate_harvest(land_plots, weather_conditions)

# Output result as required
print(f"Result: {final_yield}")