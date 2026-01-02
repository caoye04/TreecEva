def calculate_harvest(plots):
    base_multiplier = 1.5
    bonus_factor = 0.0
    total_yield = 0.0
    peak_adjustment = 0.0
    
    # Irrelevant tracking variables (distractors)
    days_monitored = len(plots) * 7
    avg_moisture = sum([p['moisture'] for p in plots]) / len(plots) if plots else 0
    
    for idx, plot in enumerate(plots):
        crop_age = plot['age']
        soil_health = plot['health']
        moisture_level = plot['moisture']
        
        # Real computation branch
        if crop_age > 30:
            base_yield = crop_age * 0.8
            if soil_health >= 7:
                base_yield *= 1.4
                if moisture_level > 50:
                    base_yield += 12.5
            else:
                base_yield *= 0.7
        else:
            base_yield = crop_age * 0.5

        # Red herring adjustment (not actually used)
        if moisture_level < 30:
            bonus_factor = 1.1  # Never applied
        
        # Actual contribution to result
        total_yield += base_yield
        
        # Fake peak detection with unused logic
        if base_yield > 40:
            peak_adjustment += 5.0  # Accumulates but not used

    # Secondary loop: processing plot names (irrelevant string manipulation)
    all_names = [p['name'] for p in plots]
    processed_names = [name.upper().replace(' ', '_') for name in all_names]
    name_length_sum = sum(len(name) for name in processed_names)

    # Final calculation - only depends on total_yield
    final_yield = int(total_yield + 0.5)  # Round to nearest integer
    
    # Dead code path (never reached in normal execution)
    if False:
        final_yield *= base_multiplier
        final_yield += int(bonus_factor * 10)

    return final_yield

# Main execution
plots_data = [
    {'name': 'North Field', 'age': 35, 'health': 8, 'moisture': 60},
    {'name': 'South Ridge', 'age': 25, 'health': 9, 'moisture': 45},
    {'name': 'East Slope', 'age': 40, 'health': 6, 'moisture': 55},
    {'name': 'West Plot', 'age': 32, 'health': 7, 'moisture': 70}
]

final_yield = calculate_harvest(plots_data)
print(f"Result: {final_yield}")