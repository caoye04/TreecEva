def analyze_growth_cycle(temperature, moisture_levels):
    """Irrelevant function analyzing plant growth (distraction)"""
    base_rate = 0.5
    stress_factor = 0
    for temp in temperature:
        if temp > 35:
            stress_factor += 0.1
    return [moisture * (base_rate - stress_factor) for moisture in moisture_levels]


def calculate_water_retention(texture_array):
    """Dead-end function for soil water retention (decoy)"""
    retention = 0
    for i, val in enumerate(texture_array):
        retention += val * (i % 3 + 1)
    return retention // 2


def optimize_harvest(climate, soils):
    # Core logic embedded within distractions
    cumulative_yield = 0
    adjustment_factor = 1.75
    
    # Irrelevant preprocessing block (red herring)
    shadow_correction = 0
    for entry in climate:
        if 'humidity' in entry and entry['humidity'] > 60:
            shadow_correction += 0.05
    
    # Distractor: unused transformation
    transformed_soils = [soil * 0.89 for soil in soils if soil > 20]
    
    # Key data processing with slicing and zip
    growing_periods = climate[1:6]  # Critical slice
    efficiency_map = [1.2, 0.9, 1.4, 0.7, 1.1]
    
    # Real computation begins here
    for period, soil, eff in zip(growing_periods, soils, efficiency_map):
        temp_avg = sum(period['temps']) / len(period['temps'])
        rain_total = period['rainfall']
        base_yield = temp_avg * (rain_total ** 0.5) * eff
        cumulative_yield += base_yield
    
    # Secondary adjustment using lambda (meaningful use)
    decay_curve = lambda x: x * 0.98 ** (x / 10)
    cumulative_yield = decay_curve(cumulative_yield)
    
    # Final adjustment with integer division and rounding
    final_adjustment = len([p for p in growing_periods if p['rainfall'] > 50])
    cumulative_yield //= (final_adjustment or 1)
    
    # Misleading normalization (not actually used in answer path)
    normalized = round(cumulative_yield / adjustment_factor, 4)
    
    # Actual result
    return int(round(cumulative_yield))

# Simulated environmental data (real input)
climate_data = [
    {'temps': [22, 24, 26, 23], 'humidity': 45, 'rainfall': 30},
    {'temps': [25, 27, 29, 28], 'humidity': 52, 'rainfall': 75},
    {'temps': [28, 30, 31, 29], 'humidity': 65, 'rainfall': 40},
    {'temps': [26, 25, 27, 28], 'humidity': 70, 'rainfall': 95},
    {'temps': [24, 23, 25, 26], 'humidity': 58, 'rainfall': 55},
    {'temps': [22, 21, 20, 23], 'humidity': 40, 'rainfall': 35}
]

soil_profiles = [25, 30, 35, 40, 45]  # cm depth readings

# Unused variables (distractors)
data_checksum = sum(len(str(val)) for val in [climate_data, soil_profiles])
baseline_index = calculate_water_retention([12, 18, 22, 15, 30])
predicted_growth = analyze_growth_cycle(
    [25, 27, 29, 28, 26], 
    [30, 35, 40, 45, 50]
)

# Key execution point
final_yield = optimize_harvest(climate_data, soil_profiles)

print(f"Result: {final_yield}")