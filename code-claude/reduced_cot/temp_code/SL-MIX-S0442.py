# Soil Quality Analysis for Agricultural Plots

def calculate_moisture_index(readings):
    # Calculate moisture index (not used in final calculation)
    return sum(readings) / len(readings) * 0.8

# Soil sample readings from different plots
soil_ph_values = [6.2, 5.8, 7.1, 6.5, 6.9, 7.3, 5.5]
soil_nitrogen = [34, 28, 45, 39, 41, 47, 30]
soil_phosphorus = [12, 15, 9, 14, 11, 8, 16]

# Additional measurements (some will be used, some won't)
sunlight_hours = [8.5, 7.2, 9.1, 8.3, 7.8, 9.4, 6.5]
moisture_readings = [42, 38, 29, 35, 40, 27, 45]
organic_matter = [3.2, 2.8, 4.1, 3.7, 3.5, 4.3, 2.5]

# Process data
quality_scores = []
weighted_qualities = []
plot_anomalies = 0

# Calculate moisture index (not directly used in final result)
moisture_index = calculate_moisture_index(moisture_readings)
print(f"Moisture index: {moisture_index:.2f}")

# Process each plot's data
for i, (ph, nitrogen, phosphorus, sunlight, organic) in enumerate(zip(soil_ph_values, 
                                                                   soil_nitrogen, 
                                                                   soil_phosphorus,
                                                                   sunlight_hours,
                                                                   organic_matter)):
    # Baseline quality calculation
    if 6.0 <= ph <= 7.0:
        base_quality = 100
    else:
        base_quality = 85
        plot_anomalies += 1
    
    # Apply nitrogen and phosphorus adjustments
    nutrient_factor = (nitrogen / 40) + (phosphorus / 10)
    
    # Calculate plot quality (the sunlight factor isn't actually used)
    sunlight_factor = sunlight / 8.0
    
    # Calculate organic matter bonus (this will be used)
    organic_bonus = organic * 5 if organic > 3.0 else organic * 2
    
    # Final plot quality calculation
    plot_quality = (base_quality + organic_bonus) * (nutrient_factor / 2)
    
    # Round to nearest integer
    plot_quality = int(plot_quality)
    quality_scores.append(plot_quality)
    
    # Apply weight based on plot index (even plots get higher weight)
    weight = 1.5 if i % 2 == 0 else 1.0
    weighted_qualities.append(plot_quality * weight)

# Calculate statistics (not all used in final result)
average_quality = sum(quality_scores) / len(quality_scores)
max_quality = max(quality_scores)
min_quality = min(quality_scores)

# The key calculation
final_soil_quality = sum(weighted_qualities)

# Print results
print(f"Quality scores by plot: {quality_scores}")
print(f"Weighted qualities: {[round(w, 2) for w in weighted_qualities]}")
print(f"Plot anomalies detected: {plot_anomalies}")
print(f"Average quality: {average_quality:.2f}")
print(f"Result: {final_soil_quality}")