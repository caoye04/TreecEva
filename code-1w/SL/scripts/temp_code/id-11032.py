def analyze_soil_composition(elements):
    # Irrelevant analysis with misleading computations
    toxic_levels = 0
    trace_metals = {"Fe": 12, "Zn": 8, "Cu": 3, "Pb": 0.02}
    for metal, level in trace_metals.items():
        if level < 5:
            toxic_levels += level * 0.1
    return toxic_levels  # Not actually used in final result


def preprocess_field_data(raw_data):
    # Preprocess and normalize field sensor readings
    normalized = {}
    total_sensors = len(raw_data)
    for key, readings in raw_data.items():
        avg = sum(readings) / len(readings)
        normalized[key] = round(avg, 2)
    
    # Distractor: complex but unused transformation
    enhanced_data = {k.upper(): v * 1.05 for k, v in normalized.items() if v > 40}
    return normalized

# Helper function that contributes to final answer
def calculate_crop_health(index_log):
    base_health = 100
    for day, index in index_log.items():
        if index < 0.6:
            base_health -= 15
        elif index > 0.9:
            base_health += 5
    return max(base_health, 0)

# Main computation function
def calculate_optimal_yield(config):
    area = config['area_sqm']
    irrigation_efficiency = config['irrigation']
    sunlight_hours = config['sunlight']
    
    # Simulated yield baseline
    base_yield_per_sqm = 2.5 if sunlight_hours >= 6 else 1.8
    
    # Conditional expression for pest resistance
    pest_factor = 0.9 if config['crop_type'] in ['wheat', 'barley'] else 0.75
    
    # Dictionary-based nutrient adjustment
    nutrient_map = {'loam': 1.2, 'clay': 0.9, 'sandy': 0.8}
    soil_multiplier = nutrient_map.get(config['soil_type'], 0.7)
    
    # Primary yield calculation
    potential_yield = area * base_yield_per_sqm * soil_multiplier * pest_factor * irrigation_efficiency
    
    # Health adjustment from remote sensing log
    health_index = {"day1": 0.85, "day2": 0.72, "day3": 0.91, "day4": 0.88}
    health_score = calculate_crop_health(health_index) / 100.0
    adjusted_yield = potential_yield * health_score
    
    # Red herring: unused cost calculation
    fertilizer_cost = 0
    if config['soil_type'] == 'sandy':
        fertilizer_cost = area * 0.5
    elif config['soil_type'] == 'clay':
        fertilizer_cost = area * 0.3
    maintenance_fee = adjusted_yield * 0.01  # Dead code path
    
    # Final scaling based on economic factors (semi-relevant)
    market_conditions = {'demand': 'high', 'export': True}
    demand_boost = 1.1 if market_conditions['demand'] == 'high' else 1.0
    export_bonus = 0.05 if market_conditions['export'] else 0
    final_multiplier = demand_boost + export_bonus
    
    final_yield = adjusted_yield * final_multiplier
    return final_yield

# Entry point
if __name__ == "__main__":
    # Simulated input from farm management system
    field_data = {
        "temp": [22, 24, 23, 25, 26],
        "humidity": [60, 62, 58, 65, 70],
        "pressure": [1013, 1012, 1014, 1015, 1013]
    }
    
    processed = preprocess_field_data(field_data)
    dummy_analysis = analyze_soil_composition(["N", "P", "K"])
    
    # Actual configuration used in computation
    area_config = {
        'area_sqm': 450,
        'irrigation': 0.95,
        'sunlight': 7,
        'crop_type': 'wheat',
        'soil_type': 'loam'
    }
    
    final_yield = calculate_optimal_yield(area_config)
    print(f"Target result: {final_yield}")