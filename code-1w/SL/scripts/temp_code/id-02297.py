def calculate_harvest_efficiency(fields, settings):
    base_multiplier = settings['efficiency']
    adjustment_factor = settings['climate_adjustment']
    total_yield = 0
    peak_yield = 0
    field_count = len(fields)
    efficiency_log = []

    for field in fields:
        area = field['size']
        crop_type = field['crop']
        soil_quality = field['soil_score']
        
        # Preliminary irrelevant computation (distractor)
        hypothetical_max = area * 1.8 * (soil_quality / 10)
        degraded_area = field.get('degraded', 0)
        usable_area = area - degraded_area if degraded_area < area else 0
        
        # Real yield calculation
        base_yield = usable_area * base_multiplier
        if crop_type == 'wheat':
            base_yield *= 1.1
        elif crop_type == 'corn':
            base_yield *= 1.25
        else:
            base_yield *= 0.9
            
        climate_penalty = 1 - (adjustment_factor * 0.15)
        adjusted_yield = base_yield * climate_penalty
        
        # Irrelevant string processing (distractor using string method)
        status_msg = f"Field {field['id']}: Yield={adjusted_yield:.2f}".upper()
        status_msg.find("YIELD")  # Useless call
        efficiency_log.append((field['id'], adjusted_yield))
        
        total_yield += adjusted_yield
        if adjusted_yield > peak_yield:
            peak_yield = adjusted_yield
    
    # Secondary distractor: list comprehension with no impact
    high_performers = [fid for fid, yld in efficiency_log if yld > total_yield / field_count]
    
    # Actual final computation
    average_effectiveness = total_yield / field_count if field_count else 0
    final_yield = int(average_effectiveness + 0.5)  # Round to nearest int
    
    # Dead code path (never executed due to logic)
    if len(high_performers) > 100:
        final_yield *= 1.1
        
    return final_yield

# Configuration data
config = {
    'efficiency': 3.2,
    'climate_adjustment': 0.8
}

# Field input data
field_data = [
    {'id': 'F01', 'size': 45, 'crop': 'wheat', 'soil_score': 7.2, 'degraded': 5},
    {'id': 'F02', 'size': 60, 'crop': 'corn', 'soil_score': 8.0, 'degraded': 3},
    {'id': 'F03', 'size': 50, 'crop': 'barley', 'soil_score': 6.5, 'degraded': 8},
    {'id': 'F04', 'size': 40, 'crop': 'corn', 'soil_score': 7.8, 'degraded': 2},
    {'id': 'F05', 'size': 55, 'crop': 'wheat', 'soil_score': 7.0, 'degraded': 4}
]

# Execution point of interest
final_yield = calculate_harvest_efficiency(field_data, config)
print(f"Result: {final_yield}")