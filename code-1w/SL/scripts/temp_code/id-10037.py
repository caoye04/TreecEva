def analyze_soil_composition(terrain):
    # Irrelevant soil analysis with decoy computations
    ph_levels = {k: (v * 0.73 + 1.2) for k, v in terrain.items()}
    nutrient_score = sum(ph_levels.values()) / len(ph_levels)
    texture_profile = {k: v % 0.5 for k, v in ph_levels.items()}
    return nutrient_score  # Dead end return, not used

def preprocess_irrigation(flow_rates):
    # Distractor function: looks important but unused
    adjusted = [x * 1.15 for x in flow_rates if x > 0]
    normalized = [a / max(adjusted) for a in adjusted]
    return [round(n, 3) for n in normalized]

def compute_root_depth(elevation_map):
    # Misleading intermediate calculation
    depths = {}
    for zone, elev in elevation_map.items():
        if elev < 100:
            depths[zone] = 1.2
        elif elev < 300:
            depths[zone] = 0.8
        else:
            depths[zone] = 0.4
    avg_depth = sum(depths.values()) / len(depths)
    scaling_factor = 2.1
    adjusted_avg = avg_depth * scaling_factor  # Looks useful, never used
    return depths

def calculate_harvest_efficiency(fields, cycles):
    # Core logic embedded in noise
    efficiency_map = {}
    base_multiplier = 0.95
    
    # Real computation begins
    for name, data in fields.items():
        temp_efficiency = 0
        for cycle in cycles:
            # Actual signal: yield depends on moisture and seed_grade only
            moisture = data['moisture']
            grade = data['seed_grade']
            
            # Real formula path
            if moisture > 60 and grade in ['A', 'B']:
                temp_efficiency += 12.5
            elif moisture > 40 and grade in ['A', 'B', 'C']:
                temp_efficiency += 8.2
            else:
                temp_efficiency += 3.1
        efficiency_map[name] = temp_efficiency * base_multiplier
    
    # Irrelevant aggregation distractions
    total_fields = len(efficiency_map)
    aggregate_stress = sum([d['stress_index'] for d in fields.values()])
    dummy_ratio = aggregate_stress / (total_fields or 1)
    
    # Decoy conditional that doesn't affect output
    if dummy_ratio > 5.0:
        for key in efficiency_map:
            efficiency_map[key] *= 0.9

    # Real final step: sum efficiencies and apply fixed bonus
    raw_total = sum(efficiency_map.values())
    season_bonus = 17.3
    final_yield = raw_total + season_bonus  # This is the target variable
    
    # More red herrings
    outlier_check = {k: v for k, v in efficiency_map.items() if v > 50}
    if len(outlier_check) > 2:
        final_yield *= 0.95  # Never triggers
        
    return final_yield

# Main execution block
if __name__ == '__main__':
    # Real input data
    field_data = {
        'alpha': {'moisture': 68, 'seed_grade': 'A', 'stress_index': 4.2},
        'beta': {'moisture': 55, 'seed_grade': 'B', 'stress_index': 6.1},
        'gamma': {'moisture': 72, 'seed_grade': 'A', 'stress_index': 3.8},
        'delta': {'moisture': 44, 'seed_grade': 'C', 'stress_index': 7.3}
    }
    
    growth_cycles = [1, 2, 3]  # Three growing phases
    
    # Unused variables - red herrings
    terrain_analysis = {'north': 88, 'south': 105, 'east': 203, 'west': 310}
    irrigation_flow = [0.4, 0.65, 0.58, 0.0, 0.72]
    elevation_zones = {'alpha': 89, 'beta': 156, 'gamma': 220, 'delta': 305}
    
    # Irrelevant preprocessing calls
    _ = analyze_soil_composition(terrain_analysis)
    _ = preprocess_irrigation(irrigation_flow)
    _ = compute_root_depth(elevation_zones)
    
    # Critical statement
    final_yield = calculate_harvest_efficiency(field_data, growth_cycles)
    
    # Print result as required
    print(f"Target result: {final_yield}")