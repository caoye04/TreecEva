import itertools

# Simulate agricultural yield optimization under varying conditions
def calculate_base_yield(variety, moisture, temp):
    # Core calculation - only this path contributes to final answer
    base = (moisture * 0.6) + (temp * 0.4)
    if variety == 'drought_resistant':
        base *= 1.25
    return base

def analyze_rainfall_pattern(precip_data):
    # Irrelevant function: analyzes rainfall but not used in final computation
    moving_avg = []
    for i in range(2, len(precip_data)):
        avg = (precip_data[i-2] + precip_data[i-1] + precip_data[i]) / 3
        moving_avg.append(avg)
    return [x * 0.1 for x in moving_avg]  # Distractor transformation

def assess_pest_risk(temperature, humidity):
    # Dead code path - never called in execution
    risk_score = 0
    if temperature > 30:
        risk_score += humidity * 0.3
    if humidity > 70:
        risk_score += temperature * 0.2
    return risk_score  # Unused result

def compute_soil_nutrient_depletion(nutrients, crop_rotation):
    # Decoy logic with complex data structure manipulation
    depletion_map = {key: 0 for key in nutrients}
    for rotation in crop_rotation:
        for crop, impact in rotation.items():
            for nut, factor in impact.items():
                if nut in depletion_map:
                    depletion_map[nut] += factor * 0.15
    return depletion_map  # Computed but irrelevant

def optimize_harvest(climate, soils):
    # Key function containing relevant and irrelevant operations
    
    # Irrelevant pre-processing
    smoothed_temps = [sum(climate['temps'][i:i+3])/3 for i in range(0, len(climate['temps']), 3) if i+2 < len(climate['temps'])]
    adjusted_humidity = [(h - 10) * 1.1 for h in climate['humidity'] if h > 15]
    
    # Relevant parameters
    temp_trend = sum(climate['temps']) / len(climate['temps'])
    total_rainfall = sum(climate['rainfall'])
    moisture_index = total_rainfall / (temp_trend + 10)
    
    # Distractor: complex dictionary restructuring
    soil_health = {}
    for zone, properties in soils.items():
        ph_factor = 1.0
        if properties['ph'] < 6.0:
            ph_factor = 0.8
        elif properties['ph'] > 7.5:
            ph_factor = 0.7
        soil_health[zone] = {
            'nutrient_level': properties['nitrogen'] * 0.3 + properties['phosphorus'] * 0.2,
            'moisture_retention': properties['clay_content'] * 0.01,
            'ph_factor': ph_factor
        }
    
    # Irrelevant combinatorics using itertools
    combinations_tested = 0
    for combo in itertools.combinations_with_replacement(['wheat', 'corn', 'soy'], 2):
        if combo[0] != combo[1]:
            combinations_tested += 1
    
    # Core logic buried among distractions
    candidate_yields = []
    for region, s in soils.items():
        # Only drought_resistant variety is actually planted
        yield_val = calculate_base_yield('drought_resistant', moisture_index, temp_trend)
        
        # Multiple layers of adjustments - only one path matters
        if s['sand_content'] < 40 and moisture_index > 80:
            yield_val *= 1.15
        elif temp_trend > 25:
            yield_val *= 0.95
        else:
            yield_val *= 1.05  # This branch is taken
        
        candidate_yields.append(yield_val)
    
    # Final aggregation
    raw_average = sum(candidate_yields) / len(candidate_yields)
    adjustment_factor = 0.98
    
    # One final correction based on climate trend
    if climate['temps'][-1] > climate['temps'][0]:
        adjustment_factor = 1.02
    
    final_yield = raw_average * adjustment_factor
    return final_yield

# Main execution block
if __name__ == '__main__':
    # Input data structures
    climate_data = {
        'temps': [22, 24, 26, 28, 27, 25, 24],
        'humidity': [65, 68, 72, 75, 70, 64, 60, 55, 50],
        'rainfall': [75, 80, 85, 90, 95, 100, 110]
    }
    
    soil_profiles = {
        'north_field': {
            'ph': 6.8,
            'nitrogen': 25,
            'phosphorus': 18,
            'clay_content': 28,
            'sand_content': 35
        },
        'south_field': {
            'ph': 7.2,
            'nitrogen': 22,
            'phosphorus': 20,
            'clay_content': 32,
            'sand_content': 45
        },
        'east_field': {
            'ph': 6.5,
            'nitrogen': 28,
            'phosphorus': 15,
            'clay_content': 25,
            'sand_content': 38
        }
    }
    
    # Spurious variables and computations
    dummy_matrix = [[i*j for j in range(5)] for i in range(5)]
    outlier_detection = [x for x in climate_data['humidity'] if x > 70]
    growth_potential = {}
    for fld, props in soil_profiles.items():
        cap = props['nitrogen'] * 0.4 + props['phosphorus'] * 0.3
        growth_potential[fld] = cap
    
    # Critical execution point
    final_yield = optimize_harvest(climate_data, soil_profiles)
    
    # Output result
    print(f"Target result: {final_yield}")