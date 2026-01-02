def analyze_soil_quality(plots):
    quality_scores = {}
    for plot_id, data in plots.items():
        ph_level = data['soil']['ph']
        nutrient_level = sum(data['soil']['nutrients'].values())
        stability_index = data['topography']['slope'] * 0.3 + data['elevation'] * 0.001
        # Irrelevant intermediate calculation (distractor)
        dummy_score = (ph_level * nutrient_level) / (stability_index + 1e-5)
        quality_scores[plot_id] = ph_level * nutrient_level - abs(6.5 - ph_level) * 10
    return quality_scores


def filter_irrigation_zones(plots):
    zones = []
    for plot_id, data in plots.items():
        water_access = data['irrigation']['access_level']
        pipe_age = data['irrigation']['pipe_age']
        # Misleading computation with no impact on final result
        deprecated_flag = pipe_age > 15 and water_access < 3
        if water_access >= 2:
            zones.append(plot_id)
    return zones


def calculate_harvest_efficiency(plots, threshold):
    total_yield = 0
    efficiency_factors = []
    
    soil_qualities = analyze_soil_quality(plots)
    active_zones = filter_irrigation_zones(plots)
    
    for plot_id, data in plots.items():
        crop_type = data['crop']['type']
        area = data['dimensions']['area']
        base_yield_per_hectare = data['crop']['base_yield']
        
        # Simulate conditional yield adjustments
        quality_bonus = soil_qualities[plot_id] / 100.0
        
        if crop_type == 'wheat':
            adjustment = 1.1 if quality_bonus > 1.0 else 0.95
        elif crop_type == 'corn':
            adjustment = 1.15 if data['sunlight_hours'] > 7 else 0.85
        else:
            adjustment = 1.0
        
        # Apply multiple factors
        adjusted_yield = base_yield_per_hectare * adjustment * quality_bonus * area
        
        # String method used for state tracking (real usage)
        status_flag = f"{crop_type}_{data['status']}".upper()
        if 'QUARANTINE' in status_flag:
            adjusted_yield *= 0.1  # Severe penalty
        
        total_yield += adjusted_yield
        efficiency_factors.append(quality_bonus * adjustment)
    
    avg_efficiency = sum(efficiency_factors) / len(efficiency_factors) if efficiency_factors else 0
    
    # Dummy entropy-like measure (not used, distractor)
    import math
    if avg_efficiency > 0:
        entropy_noise = sum(math.log(f + 1e-5) for f in efficiency_factors)

    # Final logic: only plots above threshold contribute fully
    final_yield = 0
    for plot_id, data in plots.items():
        contribution = total_yield * (data['dimensions']['area'] / 100.0)
        if data['dimensions']['area'] >= threshold:
            final_yield += contribution * 0.3
        else:
            final_yield += contribution * 0.1

    # Additional red herring: unused transformation
    normalized_plots = {k: v for k, v in sorted(plots.items(), key=lambda x: x[1]['elevation'])}
    elevation_shift = sum(p['elevation'] for p in plots.values()) * 0.0001

    return int(final_yield + elevation_shift)

# Input data structure
plots = {
    'P01': {
        'crop': {'type': 'wheat', 'base_yield': 45},
        'dimensions': {'area': 12},
        'soil': {'ph': 6.8, 'nutrients': {'nitrogen': 3, 'phosphorus': 2, 'potassium': 4}},
        'topography': {'slope': 2},
        'elevation': 150,
        'irrigation': {'access_level': 3, 'pipe_age': 10},
        'sunlight_hours': 8,
        'status': 'active'
    },
    'P02': {
        'crop': {'type': 'corn', 'base_yield': 60},
        'dimensions': {'area': 8},
        'soil': {'ph': 5.9, 'nutrients': {'nitrogen': 4, 'phosphorus': 5, 'potassium': 3}},
        'topography': {'slope': 1},
        'elevation': 170,
        'irrigation': {'access_level': 1, 'pipe_age': 20},
        'sunlight_hours': 6,
        'status': 'quarantine_pending'
    },
    'P03': {
        'crop': {'type': 'wheat', 'base_yield': 50},
        'dimensions': {'area': 15},
        'soil': {'ph': 6.2, 'nutrients': {'nitrogen': 2, 'phosphorus': 3, 'potassium': 2}},
        'topography': {'slope': 3},
        'elevation': 140,
        'irrigation': {'access_level': 4, 'pipe_age': 5},
        'sunlight_hours': 9,
        'status': 'active'
    }
}

threshold = 10
final_yield = calculate_harvest_efficiency(plots, threshold)
print(f"Result: {final_yield}")