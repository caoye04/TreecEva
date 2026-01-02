def analyze_trend(values):
    trend_scores = [values[i+1] - values[i] for i in range(len(values)-1)]
    avg_change = sum(trend_scores) / len(trend_scores)
    return avg_change

# Simulate agricultural yield optimization under varying conditions
def optimize_harvest(climate, soil):
    base_yield = 0
    adjustment_factor = 1.0
    
    # Irrelevant intermediate calculation (distractor)
    temp_anomalies = [abs(t - 22) for t in climate['temps']]
    avg_anomaly = sum(temp_anomalies) / len(temp_anomalies)
    
    # Relevant growth index computation
    growth_index = 0
    for moisture, ph in zip(soil['moisture_levels'], soil['ph_values']):
        if moisture > 30 and 6.0 <= ph <= 7.5:
            growth_index += 1.5
        elif moisture > 20:
            growth_index += 0.8
        else:
            growth_index += 0.2

    # Misleading secondary loop (semi-relevant but not used directly)
    potential_yield = 0
    for i, precip in enumerate(climate['precipitation']):
        potential_yield += precip * (0.1 + 0.01 * climate['temps'][i])
    
    # Distractor: unused function call simulation
    _ = analyze_trend(climate['temps'])
    
    # Core logic: combine filtered climate suitability with soil response
    suitable_days = sum(1 for t, p in zip(climate['temps'], climate['precipitation']) if 18 <= t <= 30 and p > 5)
    base_yield = suitable_days * 2.5
    
    # Apply growth index as multiplicative factor
    final_yield = base_yield * (1 + growth_index / 10)
    
    # Dead code path (never executed - distractor)
    if False:
        final_yield *= adjustment_factor
        buffer = [0] * 100
        for b in buffer:
            b += 1
    
    return int(final_yield)

# Input data
climate_data = {
    'temps': [20, 25, 18, 32, 27, 23, 19],
    'precipitation': [10, 0, 40, 5, 15, 20, 30]
}

soil_conditions = {
    'moisture_levels': [35, 25, 40, 15, 30, 33, 28],
    'ph_values': [6.8, 5.9, 7.2, 4.5, 6.1, 6.9, 7.0]
}

# Execute main logic
final_yield = optimize_harvest(climate_data, soil_conditions)
print(f"Result: {final_yield}")