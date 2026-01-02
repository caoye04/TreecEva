from collections import defaultdict, Counter

# Simulated agricultural data processing with heavy interference

def preprocess_soil(ph_levels, nutrient_map):
    # Irrelevant transformation
    normalized = [max(0, min(14, p + 2)) for p in ph_levels]
    enriched = defaultdict(float)
    for key, val in nutrient_map.items():
        enriched[key] += val * 1.5
    return sorted(normalized), dict(enriched)


def assess_rainfall_pattern(precipitation):
    # Misleading function: looks important but unused in final calculation
    wet_days = sum(1 for p in precipitation if p > 5)
    dry_streak = max(
        len([p for p in chunk if p <= 1])
        for chunk in [precipitation[i:i+7] for i in range(len(precipitation)-6)]
    )
    return {'wet_days': wet_days, 'longest_dry': dry_streak}


def calculate_solar_efficiency(hours_list):
    # Dead code path — never called
    base = sum(hours_list) / len(hours_list)
    adjusted = base * (1.2 if base > 8 else 0.85)
    return round(adjusted, 2)


def evaluate_pest_pressure(plant_count, infestation_rate):
    # Decoy computation with plausible variables
    expected_loss = plant_count * infestation_rate * 0.3
    risk_factor = 'high' if expected_loss > 500 else 'moderate'
    return int(expected_loss), risk_factor


def filter_outliers(data, threshold=2):
    # Red herring utility: used on irrelevant data
    mean_val = sum(data) / len(data)
    stdev = (sum((x - mean_val)**2 for x in data) / len(data)) ** 0.5
    return [x for x in data if abs(x - mean_val) <= threshold * stdev]


def optimize_harvest(weather, soils):
    # Core logic embedded in noise
    
    # Irrelevant preprocessing steps
    temp_range = [t for t in weather['temps'] if 15 < t < 35]
    filtered_precip = filter_outliers(weather['precip'])
    
    # Distractor: complex but unused structure
    microclimate_map = defaultdict(dict)
    for zone, temp in enumerate(weather['temps']):
        microclimate_map[zone]['temp'] = temp
        microclimate_map[zone]['risk'] = 'heat' if temp > 30 else 'cold' if temp < 20 else 'optimal'
    
    # Actual relevant data extraction
    avg_temp = sum(weather['temps']) / len(weather['temps'])
    total_rain = sum(weather['precip'])
    
    # Soil scoring - only this part matters
    fertility_score = 0
    for profile in soils:
        # Only 'ph' and 'organic_content' are used; others are decoys
        ph = profile.get('ph', 7.0)
        nutrients = profile['nutrients']  # dict with N, P, K
        organic = profile.get('organic_content', 0)
        drainage = profile.get('drainage', 'moderate')  # unused
        salinity = profile.get('salinity', 0.0)  # unused
        
        # Real contribution to result
        base = (ph - 6.0) * 10
        bonus = nutrients['N'] * 0.5 + nutrients['P'] * 0.3 + nutrients['K'] * 0.2
        humus = organic ** 1.5
        fertility_score += base + bonus + humus
    
    # Key intermediate (misleading)
    raw_yield = avg_temp * (total_rain / 10) * (fertility_score / len(soils))
    
    # Final adjustment using conditional expression (required feature)
    stress_factor = 0.8 if any(t > 38 for t in weather['temps']) else 1.0
    pest_loss, _ = evaluate_pest_pressure(1000, 0.07)  # Computed but not used
    
    # Final yield depends only on raw_yield and stress_factor
    final_yield = raw_yield * stress_factor
    
    # Additional distraction
    summary = {
        'zones': len(soils),
        'peak_temp': max(weather['temps']),
        'yield_per_zone': final_yield / len(soils)
    }
    
    return final_yield  # This is what we care about

# Main execution with realistic domain data
if __name__ == '__main__':
    
    # Simulated climate data
    climate_data = {
        'temps': [22, 24, 26, 28, 30, 32, 31, 29, 27, 25, 23, 21],
        'precip': [12, 15, 8, 0, 0, 3, 18, 22, 5, 10, 14, 16],
        'humidity': [65, 68, 70, 72, 75, 76, 74, 70, 68, 66, 64, 63]  # unused
    }
    
    # Soil profiles - only 'ph', 'nutrients', 'organic_content' matter
    soil_profiles = [
        {
            'ph': 6.5,
            'nutrients': {'N': 8, 'P': 6, 'K': 7},
            'organic_content': 3.2,
            'drainage': 'good',
            'salinity': 0.1
        },
        {
            'ph': 6.8,
            'nutrients': {'N': 9, 'P': 5, 'K': 8},
            'organic_content': 2.9,
            'drainage': 'moderate',
            'salinity': 0.15
        },
        {
            'ph': 6.3,
            'nutrients': {'N': 7, 'P': 7, 'K': 6},
            'organic_content': 3.5,
            'drainage': 'poor',
            'salinity': 0.08
        }
    ]
    
    # Irrelevant counters
    nutrient_counter = Counter()
    for s in soil_profiles:
        for elem, val in s['nutrients'].items():
            nutrient_counter[elem] += val
    
    # Execution point of interest
    final_yield = optimize_harvest(climate_data, soil_profiles)
    
    # Print target result
    print(f"Target result: {final_yield}")