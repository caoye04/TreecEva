def analyze_growth_potential(temperature, rainfall):
    # Assess base growth potential from climate factors
    base_index = (temperature - 15) * (rainfall / 100)
    adjusted_index = base_index * 0.8 if temperature > 30 else base_index * 1.1
    return adjusted_index

# Simulate agricultural yield optimization under varying conditions
def optimize_harvest(climate_data, soil_conditions):
    total_segments = len(climate_data)
    fertility_map = {}
    temp_offsets = []

    # Initialize soil fertility mapping with pH and nutrient data
    for i, (ph, nutrients) in enumerate(soil_conditions):
        fertility_score = (7.0 - abs(ph - 6.5)) + (nutrients / 10)
        fertility_map[i] = max(fertility_score, 0)

    # Misleading computation: calculate average temperature deviation (not used later)
    all_temps = [data[0] for data in climate_data]
    mean_temp = sum(all_temps) / len(all_temps)
    for t in all_temps:
        temp_offsets.append((t - mean_temp) ** 2)

    cumulative_yield = 0
    peak_adjustment_factor = 0

    # Main processing loop: evaluate each field segment
    for idx in range(total_segments):
        temp = climate_data[idx][0]
        rain = climate_data[idx][1]
        
        # Compute growth index using temperature and rainfall
        growth_index = analyze_growth_potential(temp, rain)
        
        # Retrieve corresponding soil fertility
        soil_fertility = fertility_map[idx]
        
        # Apply combined model for expected yield
        raw_yield = growth_index * soil_fertility
        
        # Correction based on extreme heat
        if temp > 35:
            raw_yield *= 0.6
        
        # Accumulate weighted contribution
        cumulative_yield += raw_yield * (1 + 0.1 * (idx % 3))

        # Track peak adjustment (distractor, not directly used)
        if raw_yield > 20:
            peak_adjustment_factor += 1.5

    # Final aggregation with scaling
    baseline_total = cumulative_yield * 0.9
    penalty_reduction = len([x for x in all_temps if x > 35]) * 3.5
    final_yield = int(baseline_total - penalty_reduction)

    # Irrelevant slicing operation (distractor)
    mid_climate = climate_data[1:-1]
    temp_slice_avg = sum([c[0] for c in mid_climate]) / len(mid_climate) if mid_climate else 0

    return final_yield

# Input data setup
climate_readings = [(25, 120), (30, 95), (36, 88), (28, 110), (32, 90)]
soil_profiles = [(6.2, 8), (6.8, 12), (5.9, 6), (7.1, 10), (6.4, 9)]

# Execute main logic
crop_model_output = optimize_harvest(climate_readings, soil_profiles)
Result: crop_model_output