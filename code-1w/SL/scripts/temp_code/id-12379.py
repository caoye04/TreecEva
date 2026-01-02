def analyze_agricultural_output(plots):
    total_area = 0
    valid_plots = 0
    temp_results = []
    efficiency_log = {}

    for plot_id, data in plots.items():
        area = data['area']
        crop_type = data['crop']
        soil_quality = data['soil_q']
        rainfall = data['rainfall']

        # Irrelevant string processing (distractor)
        status_msg = f"Plot {plot_id} processed. Crop: {crop_type.upper()}"
        if 'WHEAT' in status_msg:
            status_msg = status_msg.replace('PROCESSED', 'ANALYZED')

        # Semi-relevant intermediate calculation (not used later)
        theoretical_max = area * 0.85 * (soil_quality / 10)

        # Actual relevant logic
        base_yield = area * soil_quality * min(rainfall, 120) / 100
        if crop_type == 'maize':
            adjustment_factor = 0.9
        elif crop_type == 'wheat':
            adjustment_factor = 1.1
        else:
            adjustment_factor = 1.0

        adjusted_yield = base_yield * adjustment_factor
        temp_results.append(adjusted_yield)

        # Tracking for logging (distractor)
        efficiency_log[plot_id] = round(adjusted_yield / area, 3)

        total_area += area
        if adjusted_yield > 50:
            valid_plots += 1

    # Dead code path (distractor)
    if len(temp_results) > 100:
        outlier_count = sum(1 for x in temp_results if x > 200)
    else:
        outlier_count = None

    return temp_results, total_area, efficiency_log


def calculate_harvest_efficiency(region_data, threshold=65):
    yields, area, log = analyze_agricultural_output(region_data)
    
    # Real computation chain
    filtered_yields = [y for y in yields if y > threshold]
    cumulative_boost = 0.0
    
    for i, y in enumerate(filtered_yields):
        if i % 2 == 0:
            cumulative_boost += y * 0.05
        else:
            cumulative_boost -= y * 0.02
    
    # Additional distracting operations
    summary_stats = {
        'count': len(yields),
        'high_performers': len(filtered_yields),
        'boost_applied': round(cumulative_boost, 4)
    }
    
    # String-based key generation (uses string method, satisfies requirement)
    stat_keys = [k.upper() + '_VALUE' for k in summary_stats.keys()]
    dummy_checksum = sum(ord(c) for c in ''.join(stat_keys)) % 100
    
    # Final result influenced only by filtered yield logic
    base_efficiency = sum(filtered_yields) / len(filtered_yields) if filtered_yields else 0
    final_yield = int(base_efficiency + cumulative_boost)

    # Print required output
    print(f"Result: {final_yield}")
    return final_yield

# Input data
region_data = {
    'p01': {'area': 10, 'crop': 'wheat', 'soil_q': 8, 'rainfall': 95},
    'p02': {'area': 15, 'crop': 'maize', 'soil_q': 7, 'rainfall': 110},
    'p03': {'area': 12, 'crop': 'rice', 'soil_q': 9, 'rainfall': 130},
    'p04': {'area': 8, 'crop': 'wheat', 'soil_q': 6, 'rainfall': 85},
    'p05': {'area': 20, 'crop': 'wheat', 'soil_q': 10, 'rainfall': 100},
    'p06': {'area': 18, 'crop': 'maize', 'soil_q': 8, 'rainfall': 115}
}

# Execution point
final_yield = calculate_harvest_efficiency(region_data, threshold=65)