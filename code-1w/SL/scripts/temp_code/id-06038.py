def analyze_growth_cycle(temperature_log, base_threshold=22):
    """Simulate crop growth phase analysis (distractor function)"""
    active_days = 0
    stress_events = 0
    for temp in temperature_log:
        if temp > base_threshold + 5:
            stress_events += 1
        if temp >= base_threshold:
            active_days += 1
    return active_days

# Simulated agricultural sensor readings (historical)
temperature_readings = [20, 23, 25, 21, 27, 24, 19, 26, 28, 22]

# Irrelevant yield prediction model output (distractor data)
baseline_forecast = {
    'wheat': 3.2,
    'corn': 4.1,
    'barley': 2.8
}

# Key input parameters
soil_nutrient_levels = [0.8, 0.9, 0.75, 0.85, 0.92]
moisture_index = [0.65, 0.71, 0.68, 0.73, 0.70]

# Distractor: unused transformation
normalized_nutrients = [round((val - 0.7) * 10, 2) for val in soil_nutrient_levels]

# Composite health score using slicing and zip
health_segments = list(zip(soil_nutrient_levels[1:4], moisture_index[1:4]))
segment_score = sum(n * m * 100 for n, m in health_segments)

# Adjustment factor derived from environmental data
adjustment_factor = (sum(moisture_index) / len(moisture_index)) ** 1.5

# Projection data with embedded logic
base_projection = [x * 120 for x in soil_nutrient_levels]
projection_data = {f'day_{i}': val for i, val in enumerate(base_projection)}

# Misleading intermediate calculation (dead code path)
if len(projection_data) > 10:
    fallback_mode = True
    segment_offset = 5
else:
    fallback_mode = False
    segment_offset = 0  # Not used elsewhere

# Core harvest calculation function
def calculate_harvest(data_dict, adj_factor):
    raw_values = [v for k, v in data_dict.items() if 'day_' in k]
    trimmed_values = raw_values[1:-1]  # Use slicing to exclude first and last
    
    # Apply adjustment and compute weighted contribution
    adjusted_contributions = []
    for i, value in enumerate(trimmed_values):
        weight = 1 + (i * 0.1)
        adjusted_value = value * adj_factor * weight
        adjusted_contributions.append(adjusted_value)
    
    # Secondary filtering based on threshold (simulates quality control)
    filtered_yields = [y for y in adjusted_contributions if y > 85]
    total_adjusted = sum(filtered_yields)
    
    # Final nonlinear scaling
    final_output = int(total_adjusted ** 0.5)
    
    # Red herring: this variable is not returned
    peak_yield = max(filtered_yields) if filtered_yields else 0
    
    return final_output

# Execute main computation
final_yield = calculate_harvest(projection_data, adjustment_factor)

# Log distractor metric
stress_days = analyze_growth_cycle(temperature_readings)

# Output target result
print(f"Result: {final_yield}")