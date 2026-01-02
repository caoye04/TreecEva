def analyze_soil_composition(elements):
    # Irrelevant analysis of soil elements (distractor)
    heavy_metals = ['lead', 'cadmium', 'arsenic']
    toxic_load = 0
    for elem, level in elements.items():
        if elem in heavy_metals:
            toxic_load += level * 1.5
    return max(toxic_load - 10, 0)  # Not used in final result


def calculate_harvest_efficiency(fields, limits):
    total_yield = 0
    efficiency_corrections = []
    
    # Real computation begins: process each field
    for idx, (field_id, data) in enumerate(fields.items()):
        base_yield = data['crop_yield']
        moisture = data['moisture_level']
        pests_present = data['pests']
        
        # Misleading intermediate: pest adjustment (partially irrelevant)
        pest_penalty = 0
        if pests_present:
            pest_penalty = base_yield * 0.15
        else:
            pest_penalty = -5  # Red herring
        
        # Actual logic: moisture-based tiered efficiency
        if moisture < limits['min_moisture']:
            adjusted_yield = base_yield * 0.6
        elif moisture > limits['max_moisture']:
            adjusted_yield = base_yield * 0.7
        else:
            adjusted_yield = base_yield * 1.1  # Optimal moisture
        
        # Accumulate real contribution
        total_yield += adjusted_yield
        
        # Distractor: tracking corrections that aren't used
        efficiency_corrections.append(adjusted_yield / base_yield)
        
    # Secondary distractor loop: unused statistical check
    avg_correction = sum(efficiency_corrections) / len(efficiency_corrections) if efficiency_corrections else 1.0
    fluctuation = max(efficiency_corrections) - min(efficiency_corrections)
    
    # Final calculation: apply bonus only if stable
    final_yield = total_yield
    if fluctuation < 0.2:
        final_yield += 20  # Stability bonus
    
    # Dead code branch (never reached due to above logic)
    if avg_correction < 0.8:
        final_yield *= 0.9  # This doesn't trigger
    
    return int(final_yield)

# Main execution
if __name__ == "__main__":
    field_data = {
        'field_A1': {'crop_yield': 80, 'moisture_level': 30, 'pests': False},
        'field_A2': {'crop_yield': 90, 'moisture_level': 55, 'pests': True},
        'field_B1': {'crop_yield': 100, 'moisture_level': 42, 'pests': False},
        'field_C3': {'crop_yield': 75, 'moisture_level': 65, 'pests': False}
    }
    
    thresholds = {
        'min_moisture': 40,
        'max_moisture': 60
    }
    
    # Irrelevant soil analysis call (distractor)
    soil_elements = {'nitrogen': 2.3, 'phosphorus': 1.1, 'lead': 0.05, 'potassium': 1.8}
    contamination_level = analyze_soil_composition(soil_elements)
    
    # Key statement
    final_yield = calculate_harvest_efficiency(field_data, thresholds)
    
    # Print result as required
    print(f"Result: {final_yield}")