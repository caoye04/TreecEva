import itertools

def analyze_soil_nutrients(sample):
    # Simulate nutrient analysis with complex calculations
    nitrogen = (sample % 7) * 3.5 + 2
    phosphorus = (sample // 4) * 2.1
    potassium = (sample ^ 3) % 10
    
    # Misleading calculation that isn't used
    organic_matter = ((sample * 2) % 9) * 4.7
    
    return nitrogen + phosphorus + potassium

def calculate_rainfall_impact(moisture_levels):
    # This function creates a distraction with complex rainfall calculations
    rainfall_factors = []
    for level in moisture_levels:
        if level > 50:
            rainfall_factors.append(level * 0.8)
        elif level > 30:
            rainfall_factors.append(level * 1.2)
        else:
            rainfall_factors.append(level * 1.5)
    
    # This value is never actually used
    return sum(rainfall_factors) / len(rainfall_factors) if rainfall_factors else 0

def calculate_soil_composition(soil_samples, moisture_threshold):
    # Extract sample values - only odd indices matter
    relevant_samples = [sample for i, sample in enumerate(soil_samples) if i % 2 == 1]
    
    # Misleading calculation with full sample set
    all_samples_avg = sum(soil_samples) / len(soil_samples) if soil_samples else 0
    
    # Process each relevant sample
    nutrient_values = []
    for sample in relevant_samples:
        # Only samples divisible by 3 are actually used
        if sample % 3 == 0:
            nutrient_values.append(analyze_soil_nutrients(sample))
    
    # Create misleading moisture analysis that doesn't affect final result
    moisture_levels = [s * 1.5 for s in soil_samples if s > moisture_threshold]
    rainfall_impact = calculate_rainfall_impact(moisture_levels)
    
    # Calculate product of nutrient values that are above 15
    filtered_product = 1
    for value in nutrient_values:
        # Only values above 15 contribute to product
        if value > 15:
            filtered_product *= value
    
    # More distraction calculations that aren't used
    soil_quality_index = all_samples_avg * rainfall_impact / 100
    potential_yield = filtered_product * 0.75 - soil_quality_index
    
    # Additional misleading variable
    final_recommendation = "high" if potential_yield > 200 else "medium" if potential_yield > 100 else "low"
    
    return filtered_product

# Sample data
soil_samples = [12, 18, 27, 9, 36, 15, 42, 21]
moisture_threshold = 20

# Calculate results
filtered_product = calculate_soil_composition(soil_samples, moisture_threshold)

# Display result
print(f"Result: {filtered_product}")