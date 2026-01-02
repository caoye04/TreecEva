def analyze_growth_patterns(temperatures, rainfall, soil_ph):
    # Irrelevant baseline metrics
    avg_temp = sum(temperatures) / len(temperatures)
    total_rain = sum(rainfall)
    ph_balance = abs(soil_ph - 6.5)  # Ideal pH is 6.5

    # Distractor: Compute unused stress indices
    heat_stress = 0
    for t in temperatures:
        if t > 35:
            heat_stress += (t - 35) * 0.3

    drought_days = 0
    for r in rainfall:
        if r < 2:
            drought_days += 1

    # Relevant growth window analysis using slicing
    peak_window = temperatures[10:20]  # Days 10-19 for peak growth phase
    effective_rain = rainfall[10:20]

    # Early return if conditions are too poor
    if min(peak_window) < 18 or max(peak_window) > 40:
        return 0

    # Simulate nutrient retention based on pH
    nutrient_efficiency = 0.9 - (ph_balance * 0.05)

    # Yield components
    base_yield = 0
    for i in range(len(peak_window)):
        temp_factor = max(0, 1 - abs(peak_window[i] - 25) / 15)  # Optimal at 25°C
        rain_factor = min(1, effective_rain[i] / 10)  # Saturates at 10mm
        base_yield += temp_factor * rain_factor

    # Adjust yield by nutrient efficiency
    adjusted_yield = base_yield * nutrient_efficiency

    # Secondary distraction: unused pest pressure index
    pest_index = 0
    for i, t in enumerate(temperatures):
        if 20 <= t <= 30 and rainfall[i] > 15:
            pest_index += 0.1

    # Final harvest potential with red herring computation
    buffer_zone = temperatures[::7]  # Weekly sampling - unused
    decay_correction = len(buffer_zone) * 0.02  # Simulated edge loss
    final_yield = adjusted_yield - decay_correction

    # Print result as required
    return final_yield

# Input data
temp_data = [22, 24, 26, 28, 30, 33, 35, 34, 30, 28, 26, 25, 24, 23, 22, 21, 23, 25, 27, 29, 31, 32, 30, 28, 26, 24, 23, 22, 21, 20]
rain_data = [5, 6, 8, 10, 12, 3, 1, 0, 2, 4, 5, 7, 9, 11, 13, 14, 10, 8, 6, 5, 4, 3, 2, 1, 0, 5, 7, 9, 11, 13]
pH_level = 5.8

result = analyze_growth_patterns(temp_data, rain_data, pH_level)
print(f"Result: {result}")