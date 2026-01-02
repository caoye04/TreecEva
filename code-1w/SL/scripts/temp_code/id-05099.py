from itertools import combinations

def analyze_soil_stability(terrain_risk):
    stability_score = 0
    for risk in terrain_risk:
        if risk < 2:
            stability_score += 3
        elif risk < 5:
            stability_score += 1
        else:
            stability_score -= 2  # High risk zones
    return max(stability_score, 0)

def calculate_harvest_potential(zones):
    base_yield = 100
    penalty_factor = 0.0
    bonus_tracker = []
    volatility_log = []
    
    for i, zone in enumerate(zones):
        climate_score = zone['temp_avg'] - zone['humidity'] * 0.3
        if climate_score > 25:
            penalty_factor += 0.1
        elif climate_score < 15:
            penalty_factor += 0.05
        
        # Track extreme fluctuations (distraction)
        fluctuation = abs(zone['temp_avg'] - zone.get('prev_temp', zone['temp_avg']))
        volatility_log.append(fluctuation)
        
        if zone['fertility'] >= 8:
            bonus_tracker.append(i)

    # Irrelevant combinatorics on fertility levels (distractor)
    fertile_indices = [i for i, z in enumerate(zones) if z['fertility'] > 7]
    redundant_combinations = list(combinations(fertile_indices, 2)) if len(fertile_indices) >= 2 else []
    combination_impact = len(redundant_combinations) * 0.01  # Negligible effect

    # Real computation path
    total_adjustment = 0
    for zone in zones:
        if zone['temp_avg'] < 18 or zone['temp_avg'] > 30:
            total_adjustment -= 8
        if zone['fertility'] > 9:
            total_adjustment += 12
        elif zone['fertility'] > 6:
            total_adjustment += 5

    # Simulated market demand interaction (semi-relevant but not used directly)
    projected_demand = sum([z['fertility'] * 1.5 for z in zones])
    demand_modifier = 1.0 + (min(projected_demand, 100) / 500)  # Small boost

    # Final yield calculation (core logic)
    adjusted_base = base_yield + total_adjustment
    applied_penalty = adjusted_base * (1 - penalty_factor)
    final_yield = int(applied_penalty * demand_modifier + combination_impact)
    
    # Dead code: logging unused statistics
    avg_volatility = sum(volatility_log) / len(volatility_log) if volatility_log else 0
    high_risk_count = len([v for v in volatility_log if v > 5])
    
    return final_yield

# Environmental data for agricultural planning
climate_zones = [
    {'temp_avg': 32, 'humidity': 60, 'fertility': 10, 'prev_temp': 34},
    {'temp_avg': 22, 'humidity': 45, 'fertility': 7, 'prev_temp': 20},
    {'temp_avg': 16, 'humidity': 50, 'fertility': 9, 'prev_temp': 15},
    {'temp_avg': 28, 'humidity': 70, 'fertility': 5, 'prev_temp': 29}
]

# Distraction: terrain analysis with no impact on harvest
terrain_risk = [3, 1, 6, 2]
stability_rating = analyze_soil_stability(terrain_risk)

# Key execution point
final_yield = calculate_harvest_potential(climate_zones)
print(f"Result: {final_yield}")