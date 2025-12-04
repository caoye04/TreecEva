def analyze_soil_quality(soil_samples):
    # Analyze soil samples for quality rating
    if not soil_samples:
        return 0
    
    mineral_content = sum(sample[0] for sample in soil_samples if len(sample) > 0)
    acidity_level = sum(sample[1] for sample in soil_samples if len(sample) > 0) / len(soil_samples)
    
    # Higher mineral content is better, optimal acidity is 7
    quality_score = mineral_content - 2 * abs(acidity_level - 7)
    return quality_score

def calculate_growth_factor(temperature_data):
    # Calculate growth factor based on temperature data
    if not temperature_data:
        return 1.0
    
    avg_temp = sum(temperature_data) / len(temperature_data)
    # Optimal temperature is 25°C
    if avg_temp < 15:
        return 0.8
    elif avg_temp > 35:
        return 0.7
    else:
        return 1.0 + (25 - abs(avg_temp - 25)) / 50

def calculate_final_yield(field_data, rainfall_data):
    # Extract field information
    field_size = field_data["size"]
    crop_type = field_data["crop_type"]
    soil_samples = field_data["soil_samples"]
    temperature_data = field_data["temperature"]
    
    # These crop types aren't used in final calculation
    crop_multipliers = {
        "wheat": 1.0,
        "corn": 1.2,
        "rice": 1.4,
        "barley": 0.9,
        "soybeans": 1.1
    }
    
    # Base yield calculation
    base_yield = field_size * 10
    
    # Calculate soil quality impact
    soil_quality = analyze_soil_quality(soil_samples)
    quality_factor = max(0.5, min(1.5, soil_quality / 10))
    
    # Rainfall impact - only use the rainfall from day 10 to day 30
    relevant_rainfall = rainfall_data[10:30]
    total_rainfall = sum(relevant_rainfall)
    
    # Optimal rainfall is between 100 and 200 units
    if total_rainfall < 50:
        rainfall_factor = 0.6
    elif total_rainfall < 100:
        rainfall_factor = 0.8
    elif total_rainfall <= 200:
        rainfall_factor = 1.2
    else:
        rainfall_factor = 0.9
    
    # Calculate growth factor based on temperature
    growth_factor = calculate_growth_factor(temperature_data)
    
    # Calculate raw yield
    raw_yield = base_yield * quality_factor * rainfall_factor * growth_factor
    
    # Apply crop-specific multiplier (wheat is the default)
    crop_multiplier = crop_multipliers.get(crop_type, 1.0)
    
    # Final yield calculation (rounded to nearest whole number)
    final_yield = round(raw_yield)
    
    return final_yield

# Field data
field_data = {
    "size": 25,  # hectares
    "crop_type": "wheat",
    "soil_samples": [(12, 6.8), (15, 7.2), (11, 6.5), (14, 7.0)],
    "temperature": [22, 24, 26, 25, 23]
}

# Rainfall data for 40 days (in mm)
rainfall_data = [5, 0, 2, 8, 12, 3, 0, 0, 5, 7,
                10, 12, 8, 5, 7, 15, 20, 12, 8, 5,
                3, 0, 0, 5, 8, 12, 15, 10, 5, 2,
                0, 0, 3, 5, 8, 10, 7, 5, 3, 0]

# Calculate crop yield
crop_yield = calculate_final_yield(field_data, rainfall_data)

# For testing other scenarios (not affecting the final result)
test_field = {
    "size": 15,
    "crop_type": "corn",
    "soil_samples": [(10, 6.5), (12, 7.0)],
    "temperature": [28, 30, 27, 29]
}

# These calculations don't affect our target variable
test_yield = field_data["size"] * 8
test_quality = analyze_soil_quality(test_field["soil_samples"])

print(f"Result: {crop_yield}")