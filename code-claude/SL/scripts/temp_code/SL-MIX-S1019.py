def calculate_environmental_impact(emissions, factors, thresholds):
    # Environmental impact calculator for industrial emissions
    # Calculates actual impact after filtering by thresholds
    
    # Initialize tracking variables
    total_raw_emissions = sum(emissions)
    max_factor = max(factors)
    min_factor = min(factors)
    
    # Normalize factors for fair comparison
    normalized_factors = [f / max_factor for f in factors]
    
    # Calculate potential impacts
    potential_impacts = []
    weighted_values = []
    for i in range(len(emissions)):
        # Calculate raw impact
        raw_impact = emissions[i] * normalized_factors[i]
        
        # Apply logarithmic scaling for certain high emissions
        if emissions[i] > 500:
            scaled_impact = raw_impact * (1 + 0.1 * (emissions[i] // 100))
        else:
            scaled_impact = raw_impact
            
        # Track potential impact
        potential_impacts.append(scaled_impact)
        
        # Calculate weighted values for reporting
        weight = 1.5 if normalized_factors[i] > 0.7 else 0.8
        weighted_value = scaled_impact * weight
        weighted_values.append(weighted_value)
    
    # Threshold processing (critical for actual impact)
    threshold_multipliers = [1.2, 0.9, 1.1, 0.85, 1.05]
    adjusted_thresholds = [thresholds[i % len(thresholds)] * 
                          threshold_multipliers[i % len(threshold_multipliers)]
                          for i in range(len(emissions))]
    
    # Filter impacts based on thresholds
    filtered_impacts = [potential_impacts[i] for i in range(len(potential_impacts)) 
                       if potential_impacts[i] > adjusted_thresholds[i]]
    
    # Calculate secondary metrics (not used in final calculation)
    average_impact = sum(potential_impacts) / len(potential_impacts) if potential_impacts else 0
    impact_variance = sum((x - average_impact) ** 2 for x in potential_impacts) / len(potential_impacts) if potential_impacts else 0
    risk_score = average_impact * (1 + impact_variance / 10000)
    
    # Determine actual impact from filtered values
    actual_impact = sum(filtered_impacts)
    
    # Calculate alternative impact (not used in final result)
    alternative_impact = sum(weighted_values) / len(weighted_values) * len(filtered_impacts)
    combined_impact = (actual_impact + alternative_impact) / 2
    
    # For reporting only
    if risk_score > 1000:
        risk_category = "High"
    elif risk_score > 500:
        risk_category = "Medium"
    else:
        risk_category = "Low"
    
    return {
        "total_emissions": total_raw_emissions,
        "actual_impact": actual_impact,
        "risk_score": risk_score,
        "risk_category": risk_category
    }

# Test data
emissions = [420, 380, 510, 290, 650]
factors = [1.2, 0.8, 1.5, 0.9, 1.7]
thresholds = [400, 350, 450]

result = calculate_environmental_impact(emissions, factors, thresholds)
print(f"Result: {result['actual_impact']}")