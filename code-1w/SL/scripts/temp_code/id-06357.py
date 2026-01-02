import itertools

# Simulate agricultural yield optimization across climate and soil conditions
def preprocess_soil(ph_levels):
    normalized = [(p - 6.0) / 1.5 for p in ph_levels if 4.0 <= p <= 8.0]
    return [n for n in normalized if n > 0]

# Irrelevant function - decoy for nutrient analysis
def analyze_nutrients(data):
    total_n = sum(d.get('nitrogen', 0) for d in data)
    total_p = sum(d.get('phosphorus', 0) for d in data)
    return {'N_total': total_n, 'P_total': total_p}

# Unused helper - dead code path
def calculate_erosion_risk(slopes, veg_density):
    risk_score = 0
    for s, v in zip(slopes, veg_density):
        if s > 0.2:
            risk_score += (s * 100) / (v + 0.1)
    return risk_score

# Core logic disguised among distractors
def evaluate_resilience(rainfall, temp, ph_processed):
    base_yield = 0
    adjustments = []
    
    for r, t in itertools.product(rainfall[:3], temp[:3]):
        if r < 50:
            base_yield -= 10
        elif r > 120:
            base_yield -= 5
        else:
            base_yield += 8
            
        if t < 15:
            base_yield -= 7
        elif t > 35:
            base_yield -= 12
        else:
            base_yield += 5
            
        adjustments.append(base_yield)
    
    # Real computation happens here but obscured by noise
    resilience_factor = sum(adjustments) / len(adjustments)
    soil_bonus = sum(ph_processed[:4]) * 3.5
    
    return resilience_factor + soil_bonus

# Key function computing final result
def optimize_harvest(climate, soils):
    temps = climate['daily_temps']
    rain = climate['monthly_rain_mm']
    ph_values = soils['ph_readings']
    
    # Real processing chain
    processed_ph = preprocess_soil(ph_values)
    main_yield = evaluate_resilience(rain, temps, processed_ph)
    
    # Distractor computations with misleading intermediate values
    fake_index = 0
    for i in range(len(rain)):
        if rain[i] > 100:
            fake_index += (temps[i % len(temps)] // 5) * 2
    fake_index *= 0.1
    
    # More red herring: nutrient analysis not used in final result
    nutrient_data = [{'nitrogen': n, 'phosphorus': 15} for n in [8, 10, 12]]
    nutrients = analyze_nutrients(nutrient_data)
    bonus = nutrients['N_total'] * 0.01  # Not actually used
    
    # Final calculation (only this affects output)
    scaling = len(processed_ph) if processed_ph else 1
    final_yield = (main_yield * scaling) - 15.5
    
    # Critical execution point
    return final_yield

# Input data with mixed relevance
climate_data = {
    'daily_temps': [12, 16, 18, 22, 25, 28, 32, 30, 25, 20],
    'monthly_rain_mm': [40, 60, 130, 90, 45, 70, 110, 50, 85, 95],
    'humidity': [60, 65, 70, 80, 75, 68, 62, 78, 85, 82]  # Unused
}

soil_profiles = {
    'ph_readings': [4.2, 5.8, 6.3, 6.7, 7.1, 8.5, 5.5],
    'depth_cm': [20, 25, 30, 28, 35, 40, 22],  # Unused
    'organic_content': [3.2, 3.8, 4.1, 3.9, 4.5, 5.0, 3.6]  # Unused
}

# Execution with irrelevant setup
slopes = [0.05, 0.12, 0.30, 0.08]
vegetation = [0.8, 0.7, 0.2, 0.9]
calculate_erosion_risk(slopes, vegetation)  # Dead call

# Target result computation
final_yield = optimize_harvest(climate_data, soil_profiles)
print(f"Target result: {final_yield}")