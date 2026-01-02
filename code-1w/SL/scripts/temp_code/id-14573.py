def analyze_growth_patterns(data):
    # Irrelevant analysis function (dead code path)
    return sum(x ** 0.5 for x in data if x > 20)

# Simulate agricultural yield prediction based on soil and climate
def calculate_harvest_yield(areas, conditions):
    base_yield = 0
    adjustment_factor = 0.85
    temp_boost = {}
    
    # Process each field's area with corresponding climate condition
    for i, (area, condition) in enumerate(zip(areas, conditions)):
        stress_level = 0
        if condition < 15:
            stress_level = 0.4
        elif condition > 30:
            stress_level = 0.6
        else:
            stress_level = 0.1
        
        # Compute effective growing index using lambda
        growth_index = (lambda a, s: a * (1 - s))(area, stress_level)
        base_yield += growth_index

        # Track temporary boost (semi-relevant but not used directly)
        temp_boost[i] = area * (condition / 100)

    # Secondary adjustment using dictionary operations
    boost_values = list(temp_boost.values())
    avg_boost = sum(boost_values) / len(boost_values) if boost_values else 0

    # Distractor computation: unused nutrient score
    nutrient_score = 0
    for val in areas:
        nutrient_score += (val % 7) * 1.5  # No impact on result

    # Final yield calculation depends only on base_yield and adjustment_factor
    final_yield = int(base_yield * adjustment_factor)
    
    # Additional red herring: complex but unused formula
    peak_area = max(areas)
    dummy_metric = (peak_area ** 2) / (sum(conditions) + 1e-5)
    
    return final_yield

# Input data
area_data = [120, 85, 200, 95, 150]
growth_conditions = [25, 32, 18, 14, 27]

# Execute main logic
final_yield = calculate_harvest_yield(area_data, growth_conditions)

# Print result as required
print(f"Target result: {final_yield}")