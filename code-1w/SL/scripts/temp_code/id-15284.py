def analyze_crop_quality(quality_readings):
    avg = sum(quality_readings) / len(quality_readings)
    deviation = sum((x - avg) ** 2 for x in quality_readings)
    consistency_score = deviation / len(quality_readings) if avg > 0 else 0
    return consistency_score


def calculate_harvest_efficiency(fields, min_threshold):
    total_yield = 0
    penalty_adjustment = 0
    quality_log = {}
    
    for field_id, data in fields.items():
        # Extract relevant metrics
        base_yield = data['yield']
        soil_health = data['soil_health']
        pest_level = data['pests']
        recent_rainfall = data['rainfall']

        # Irrelevant intermediate calculation (distractor)
        normalized_rainfall = max(0, min(1, recent_rainfall / 100))
        
        # Core logic: efficiency depends on thresholds
        if soil_health < min_threshold:
            adjustment_factor = 0.6
            penalty_adjustment += 10
        elif pest_level > 75:
            adjustment_factor = 0.75
            penalty_adjustment += 5
        else:
            adjustment_factor = 1.0

        # Apply adjustment
        adjusted_yield = base_yield * adjustment_factor
        total_yield += adjusted_yield

        # Log quality (semi-relevant, not used later)
        quality_flag = 'high' if adjusted_yield > 80 else 'moderate'
        quality_log[field_id] = quality_flag

    # Secondary processing: sort keys alphabetically (irrelevant but adds complexity)
    sorted_fields = sorted(fields.keys())
    temp_sum = 0
    for key in sorted_fields:
        temp_sum += len(key)  # Dead computation
    
    # Final efficiency with phantom dependency
    final_efficiency = total_yield - (penalty_adjustment * 0.5)
    return round(final_efficiency, 4)

# Main execution
field_data = {
    'north_field': {'yield': 95, 'soil_health': 68, 'pests': 30, 'rainfall': 88},
    'east_field': {'yield': 87, 'soil_health': 72, 'pests': 82, 'rainfall': 105},
    'west_field': {'yield': 90, 'soil_health': 58, 'pests': 20, 'rainfall': 70},
    'south_field': {'yield': 94, 'soil_health': 75, 'pests': 60, 'rainfall': 120}
}

threshold = 60

# Dummy string processing to incorporate string methods (required feature)
field_names = [name.upper().replace('_', ' ') for name in field_data.keys()]
delimiter = ' | '
combined_name = delimiter.join(field_names)
char_count = len(combined_name.replace(' ', ''))

# Call main logic
final_yield = calculate_harvest_efficiency(field_data, threshold)

# Print result as required
print(f"Target result: {final_yield}")