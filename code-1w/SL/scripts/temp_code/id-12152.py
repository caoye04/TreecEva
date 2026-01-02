def analyze_growth_patterns(data, threshold=0.75):
    high_yield_indices = set()
    for i, row in enumerate(data):
        if sum(1 for val in row if val > threshold) >= 2:
            high_yield_indices.add(i)
    return high_yield_indices

# Simulate agricultural yield prediction using environmental factors
soil_quality = [0.82, 0.65, 0.91, 0.73]
environmental_stress = [0.21, 0.54, 0.15, 0.48]
water_availability = [0.77, 0.69, 0.88, 0.76]
temperature_factor = [0.74, 0.83, 0.68, 0.79]

# Irrelevant intermediate calculations (distractors)
decay_rates = list(map(lambda x: x * 0.01 + 0.002, environmental_stress))
stress_adjusted = [max(0, s - w * 0.1) for s, w in zip(environmental_stress, water_availability)]
baseline_scores = [q * t for q, t in zip(soil_quality, temperature_factor)]

# Core data structure: land parcel with multi-factor growth potential
land_parcel = []
for i in range(4):
    factor_set = [
        soil_quality[i],
        1 - environmental_stress[i],
        water_availability[i],
        temperature_factor[i]
    ]
    land_parcel.append(factor_set)

# Misleading auxiliary analysis (dead computation path)
outlier_detection = []
for row in land_parcel:
    mean_val = sum(row) / len(row)
    variance = sum((x - mean_val) ** 2 for x in row) / len(row)
    if variance > 0.02:
        outlier_detection.append(True)
    else:
        outlier_detection.append(False)

# Growth models as nonlinear transformations
model_a = lambda x: x[0] * x[1] * 1.1
model_b = lambda x: (x[2] + x[3]) / 2 * 0.95
model_c = lambda x: (x[0] * 0.3) + (x[2] * 0.7)

growth_models = [model_a, model_b, model_c]

# Secondary distraction: unused model ranking
model_strengths = []
for model in growth_models:
    sample_output = [model(plot) for plot in land_parcel]
    model_strengths.append(sum(sample_output))

# Key function combining multiple reasoning types
def calculate_optimal_yield(parcel, models):
    yields = []
    for plot in parcel:
        model_outputs = [m(plot) for m in models]
        # Apply filtering based on minimum viability
        viable_outputs = [y for y in model_outputs if y > 0.5]
        if viable_outputs:
            yields.append(max(viable_outputs))
        else:
            yields.append(0.5)  # default baseline
    
    # Final aggregation with conditional logic
    total = sum(yields)
    count_viable = len([y for y in yields if y > 0.65])
    adjustment_factor = 1.05 if count_viable >= 2 else 0.98
    
    # Distractor: unused risk metric
    volatility = sum((y - total/len(yields))**2 for y in yields) / len(yields)
    
    return total * adjustment_factor

# Execute main logic
preliminary_mask = analyze_growth_patterns(land_parcel, 0.68)
interim_result = [land_parcel[i] for i in sorted(preliminary_mask)]

# Critical execution point
final_yield = calculate_optimal_yield(land_parcel, growth_models)

print(f"Result: {final_yield}")