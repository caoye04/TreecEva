def analyze_growth_potential(temperature, rainfall):
    # Auxiliary calculation with partial relevance
    base_index = (temperature - 20) * 0.8
    if rainfall > 100:
        base_index += 15
    elif rainfall > 50:
        base_index += 8
    return base_index

# Simulate seasonal crop behavior under varying conditions
def optimize_harvest(climate_data, soil_quality):
    total_rainfall = sum([day[1] for day in climate_data])
    avg_temp = sum([day[0] for day in climate_data]) / len(climate_data)
    
    # Distractor: unused growth phases
    phase_one = climate_data[:3]
    phase_two = climate_data[3:6]
    phase_three = climate_data[6:]
    
    # Red herring variables
    peak_heat = max([day[0] for day in climate_data])
    dry_days = len([day for day in climate_data if day[1] < 5])
    moisture_stress = dry_days > 2
    
    # Semi-relevant transformation
    adjusted_soil = soil_quality + (5 if moisture_stress else 0)
    
    # Core logic begins
    yield_contributions = []
    for temp, rain in climate_data:
        index = analyze_growth_potential(temp, rain)
        efficiency = 0.7 if temp > 30 else 0.9
        # Apply conditional scaling using lambda
        scaler = (lambda x: x * 1.2) if rain > 15 else (lambda x: x * 0.85)
        index = scaler(index)
        yield_contributions.append(index * efficiency)
    
    # Use set operations to filter anomalies
    valid_yields = set(yield_contributions)
    filtered_yields = valid_yields - {x for x in valid_yields if x < 5}
    
    # Final computation chain
    raw_total = sum(filtered_yields)
    adjustment_factor = 0.95 if len(filtered_yields) < len(yield_contributions) else 1.0
    preliminary_yield = raw_total * adjustment_factor
    
    # Secondary adjustment based on soil
    soil_boost = (adjusted_soil / 10) * 3.5
    final_yield = int(preliminary_yield + soil_boost)
    
    # Dead code path - misleading branch
    if peak_heat > 40 and dry_days == 0:
        final_yield = int(final_yield * 0.75)  # Never reached in this data
    
    return final_yield

# Input data
climate_readings = [(25, 12), (27, 8), (32, 4), (29, 16), (26, 10), (31, 6), (28, 14)]
base_soil_score = 7

# Key execution point
final_yield = optimize_harvest(climate_readings, base_soil_score)
print(f"Target result: {final_yield}")