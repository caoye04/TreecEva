def analyze_growth_factors(temperature, rainfall):
    # Analyze temperature stability
    temp_fluctuation = max(temperature) - min(temperature)
    avg_rainfall = sum(rainfall) / len(rainfall)
    
    # Irrelevant intermediate calculation (distractor)
    growth_index = (avg_rainfall * 0.7) + (30 - temp_fluctuation) * 0.3
    efficiency_factor = 1.0 if temp_fluctuation < 15 else 0.85
    
    return avg_rainfall, efficiency_factor

# Simulate seasonal climate data (in Celsius and mm)
climate_data = {
    'summer': {'temp': [25, 30, 35, 28, 32], 'rain': [80, 100, 60, 90, 110]},
    'autumn': {'temp': [18, 15, 12, 14, 16], 'rain': [50, 40, 60, 55, 45]}
}

soil_quality = {
    'ph': 6.5,
    'nitrogen': 28,
    'organic_matter': 3.2,
    'compaction': 2.1  # Lower is better
}

# Additional irrelevant metrics (distractors)
baseline_yields = [4500, 4700, 4600, 4800]
weather_variability_score = (max(climate_data['summer']['temp']) - min(climate_data['summer']['temp'])) * 2

# Lambda function to assess soil suitability (relevant)
soil_suitability = lambda n, om: (n * 0.6 + om * 10) / 100

# Set operations to determine favorable conditions (relevant)
ideal_temp_range = set(range(20, 33))
summer_temps = set(climate_data['summer']['temp'])
favorable_days = len(summer_temps & ideal_temp_range)

# Extract key climate metrics
avg_rain, efficiency = analyze_growth_factors(
    climate_data['summer']['temp'], 
    climate_data['summer']['rain']
)

# Calculate base potential yield (kg/ha)
base_yield = (avg_rain * 3) + (favorable_days * 100)

# Apply soil and efficiency adjustments
suitability_score = soil_suitability(soil_quality['nitrogen'], soil_quality['organic_matter'])
adjusted_yield = base_yield * suitability_score * efficiency

# Secondary adjustment based on conditional logic
if soil_quality['ph'] > 7 or soil_quality['compaction'] > 3:
    adjusted_yield *= 0.7
elif soil_quality['ph'] < 5.5:
    adjusted_yield *= 0.8
else:
    adjusted_yield *= 1.05  # Optimal pH range

# Final harvest potential with minor correction
final_correction = 0.98 if weather_variability_score > 30 else 1.0
final_yield = int(adjusted_yield * final_correction)

# Print result as required
print(f"Target result: {final_yield}")