def analyze_crop_performance(data):
    # Irrelevant preprocessing: character counting in crop names
    name_chars = sum(len(crop['name']) for crop in data if 'root' in crop['name'])
    dummy_score = name_chars * 0.5 if name_chars > 10 else 0

    total_yield = 0
    total_rainfall = 0
    drought_count = 0

    for entry in data:
        yield_per_hectare = entry['yield'] / entry['area']
        normalized_rain = max(entry['rainfall'], 10)  # prevent division by zero
        efficiency = yield_per_hectare / normalized_rain

        if efficiency < 0.3:
            drought_count += 1

        total_yield += entry['yield']
        total_rainfall += entry['rainfall']

    avg_rainfall = total_rainfall / len(data)
    stress_factor = 0.9 if drought_count >= 2 else 1.0

    return total_yield, avg_rainfall, stress_factor


def calculate_harvest_efficiency(area, labor_hours):
    # Simulate non-linear efficiency curve with diminishing returns
    base_efficiency = (area ** 0.6) / (labor_hours ** 0.4)
    adjustment = 1.1 if area > 50 else 0.95
    
    # Use conditional expression and string method as required
    region_code = 'Z7'.strip().lower()
    bonus = 0.05 if region_code.startswith('z') else 0.0
    
    final_efficiency = base_efficiency * adjustment * (1 + bonus)
    
    # Dead code: unused helper calculation
    peak_hour_ratio = max(labor_hours / 8, 1) if labor_hours else 1
    _ = [x for x in range(3) if x % 2 == 0]  # irrelevant list comprehension

    return round(final_efficiency, 4)

# Main execution block
farm_data = [
    {'name': 'carrot_field', 'yield': 240, 'area': 30, 'rainfall': 45},
    {'name': 'beet_root', 'yield': 180, 'area': 25, 'rainfall': 38},
    {'name': 'sweet_root', 'yield': 320, 'area': 40, 'rainfall': 52}
]

# Preliminary analysis (partially relevant)
overall_yield, mean_rain, factor = analyze_crop_performance(farm_data)

# Key parameters derived from data
total_area = sum(plot['area'] for plot in farm_data)
labor_input = len(farm_data) * 6.5  # 6.5 hours per plot

# Red herring variables
unused_buffer = [0] * int(mean_rain)
effective_drainage = sorted([plot['rainfall'] - 40 for plot in farm_data])
phantom_threshold = sum(1 for x in effective_drainage if x > 0) * 10

# Critical computation
final_yield = calculate_harvest_efficiency(total_area, labor_input)

print(f"Result: {final_yield}")