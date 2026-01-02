def analyze_growth_potential(area, rainfall):
    # Irrelevant analysis with decoy logic
    if area <= 0:
        return 0
    growth_index = (rainfall * 0.3) / (area ** 0.5 + 1)
    adjustment_factor = 1.2 if growth_index > 5 else 0.8
    return growth_index * adjustment_factor

# Unused but plausible function to mislead
def estimate_water_loss(evaporation_rate, duration):
    total_loss = 0
    for day in range(duration):
        total_loss += evaporation_rate * (1.05 ** day)  # Compounding distraction
    return total_loss

# Distractor variables
soil_pH = 6.8
microbe_count = 125000
optimal_temperature = True

# Real input data
land_plots = [25, 18, 30, 12]
soil_quality = [0.9, 0.65, 0.8, 0.4]
rainfall_data = [120, 95, 140, 60]

# Fake transformation path
transformed_scores = []
for i in range(len(land_plots)):
    score = land_plots[i] * soil_quality[i] ** 2
    normalized = (score - 10) / (score + 5) if score > 10 else 0
    transformed_scores.append(round(normalized, 3))

# Dummy filter that does nothing critical
valid_plots = []
for idx, sq in enumerate(soil_quality):
    if sq >= 0.45:
        valid_plots.append(idx)

# Core logic buried under noise
def calculate_harvest_efficiency(plots, quality):
    base_yield = 0
    bonus_applied = False
    
    for i in range(len(plots)):
        # Relevant computation mixed with red herrings
        plot_yield = plots[i] * quality[i] * 100
        
        # Early termination red herring
        if plot_yield < 500 and not bonus_applied:
            continue  # Simulates skipping poor plots
            
        # Actual key conditional expression
        penalty = 0.1 if quality[i] < 0.7 else 0.0
        adjusted_yield = plot_yield * (1 - penalty)
        
        # Accumulate only if above threshold
        if adjusted_yield > 600:
            base_yield += adjusted_yield
        elif adjusted_yield > 400 and len(valid_plots) > 2:
            base_yield += adjusted_yield * 0.5

        # Decoy bit manipulation
        temp_flag = i ^ 3
        if temp_flag & 1:
            base_yield -= 5  # Minor noise

    # Final adjustment using tuple unpacking (relevant)
    multiplier, offset = (1.1, 10) if sum(quality) > 2.5 else (0.9, -5)
    final_calc = (base_yield * multiplier) + offset
    
    # Linear search for highest quality index (distractor)
    best_idx = 0
    for j in range(1, len(quality)):
        if quality[j] > quality[best_idx]:
            best_idx = j
    
    # Redundant correction based on rainfall (unused)
    correction_term = 0
    for r in rainfall_data:
        if r > 100:
            correction_term += r * 0.02
    
    return int(final_calc)  # Deterministic integer result

# Execution point of interest
final_yield = calculate_harvest_efficiency(land_plots, soil_quality)

# Print required output
print(f"Result: {final_yield}")