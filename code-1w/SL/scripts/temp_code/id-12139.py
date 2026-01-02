def analyze_soil_quality(plots):
    # Irrelevant analysis with misleading intermediate values
    poor_count = 0
    moderate_count = 0
    rich_count = 0
    for p in plots:
        if p['nutrients'] < 3:
            poor_count += 1
        elif p['nutrients'] < 7:
            moderate_count += 1
        else:
            rich_count += 1
    compliance_score = (rich_count * 10) + (moderate_count * 5)  # Unused metric
    return {"poor": poor_count, "moderate": moderate_count, "rich": rich_count}


def filter_irrigation_zones(zones):
    # Dead code path - never used in final calculation
    valid_zones = []
    for z in zones:
        if z['water_flow'] > 0.5 and z['pressure'] in range(3,8):
            status = "optimal" if z['minerals'] < 0.7 else "monitored"
            valid_zones.append({"id": z['id'], "status": status})
    return valid_zones


def transform_coordinates(coords):
    # Distractor function: looks important but unused
    transformed = []
    for x, y in coords:
        lat = (x * 0.001) + 37.0
        lon = (y * 0.001) - 120.0
        transformed.append((round(lat,6), round(lon,6)))
    return transformed


def calculate_stress_factors(data):
    # Decoy computation with plausible but irrelevant math
    stress_values = []
    for d in data:
        heat_factor = max(0, d['temp'] - 30) * 1.5
        humidity_impact = d['humidity'] * 0.01
        combined = heat_factor - humidity_impact
        stress_values.append(round(combined, 4))
    avg_stress = sum(stress_values) / len(stress_values) if stress_values else 0
    threshold_alert = avg_stress > 5.0  # Unused boolean
    return stress_values


def calculate_optimal_yield(plots):
    # Core logic embedded within distractions
    base_yield_per_plot = 12.5
    total_area = sum(p['area'] for p in plots)
    total_nutrients = sum(p['area'] * p['nutrients'] for p in plots)
    avg_nutrients = total_nutrients / total_area if total_area > 0 else 0
    
    # Conditional logic with red herring variables
    bonus_multiplier = 1.0
    penalty_applied = False  # Misleading flag
    overworked_land = [p for p in plots if p['last_harvest'] < 30]  # Not actually used
    if any(p['slope'] > 15 for p in plots):
        bonus_multiplier *= 0.9  # Penalty disguised as multiplier
    
    # Real adjustment based on exposure (hidden among noise)
    shade_ratio = len([p for p in plots if p['exposure'] == 'shaded']) / len(plots)
    if shade_ratio > 0.4:
        base_yield_per_plot *= (1 - shade_ratio * 0.5)
    
    # Key calculation using average nutrients and area
    yield_potential = base_yield_per_plot * total_area * (0.5 + avg_nutrients * 0.1)
    
    # Final adjustment via list comprehension (required feature)
    quality_flags = [1 if p['nutrients'] >= 5 else 0 for p in plots]
    success_rate = sum(quality_flags) / len(quality_flags) if quality_flags else 0
    adjusted_yield = yield_potential * (0.8 + success_rate * 0.25)
    
    # Use of set operations to filter unique conditions (required feature)
    unique_exposures = set(p['exposure'] for p in plots)
    if 'full_shade' in unique_exposures and len(unique_exposures) > 2:
        adjusted_yield *= 0.95
    
    return int(round(adjusted_yield))

# Main execution block
if __name__ == '__main__':
    land_plots = [
        {'area': 10, 'nutrients': 8, 'slope': 5, 'exposure': 'sunny', 'last_harvest': 45},
        {'area': 15, 'nutrients': 6, 'slope': 12, 'exposure': 'partial_shade', 'last_harvest': 60},
        {'area': 8, 'nutrients': 4, 'slope': 18, 'exposure': 'partial_shade', 'last_harvest': 25},
        {'area': 12, 'nutrients': 7, 'slope': 7, 'exposure': 'sunny', 'last_harvest': 40},
        {'area': 5, 'nutrients': 3, 'slope': 10, 'exposure': 'shaded', 'last_harvest': 70}
    ]
    
    # Irrelevant preprocessing steps
    coordinates = [(1234, 5678), (2345, 6789), (3456, 7890), (4567, 8901), (5678, 9012)]
    geo_refs = transform_coordinates(coordinates)
    
    soil_analysis = analyze_soil_quality(land_plots)
    irrigation_zones = [
        {'id': 'Z1', 'water_flow': 0.7, 'pressure': 5, 'minerals': 0.6},
        {'id': 'Z2', 'water_flow': 0.4, 'pressure': 6, 'minerals': 0.8}
    ]
    filtered_zones = filter_irrigation_zones(irrigation_zones)
    
    environmental_data = [
        {'temp': 32, 'humidity': 45},
        {'temp': 35, 'humidity': 50},
        {'temp': 29, 'humidity': 60}
    ]
    stresses = calculate_stress_factors(environmental_data)
    
    # Critical statement
    final_yield = calculate_optimal_yield(land_plots)
    
    # Output result
    print(f"Result: {final_yield}")