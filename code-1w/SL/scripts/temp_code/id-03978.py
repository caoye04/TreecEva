def analyze_soil_composition(elements):
    ratios = []
    for i, elem in enumerate(elements):
        if elem['level'] > 5:
            ratio = elem['carbon'] / (elem['nitrogen'] + 1)
            ratios.append(ratio)
    return ratios


def validate_sensor_readings(readings):
    valid_count = 0
    temp_buffer = []
    for r in readings:
        if r < 0 or r > 1024:
            continue
        temp_buffer.append(r * 0.95)  # calibration
        valid_count += 1
    return valid_count


def calculate_harvest_efficiency(plot_data, limits):
    efficiency_list = []
    total_area = 0
    cumulative_yield = 0
    
    for idx, plot in enumerate(plot_data):
        area = plot['dimensions']['length'] * plot['dimensions']['width']
        total_area += area
        
        # Simulated yield per square meter
        base_yield = plot['fertility_index'] * 12.5
        
        # Apply weather adjustment
        weather_factor = 1.0
        if plot['recent_rainfall'] < 20:
            weather_factor = 0.7
        elif plot['recent_rainfall'] > 80:
            weather_factor = 0.85
            
        adjusted_yield = base_yield * weather_factor
        
        # Distractor: Soil analysis not directly used in final yield
        soil_elements = [{'level': 6, 'carbon': 12, 'nitrogen': 3}] * 3
        _ = analyze_soil_composition(soil_elements)
        
        # Multiple assignments and slicing to increase complexity
        history = plot['yield_history'][-3:]  # last 3 seasons
        recent_avg = sum(history) / len(history) if history else 0
        
        # Efficiency score based on consistency
        variance = sum((x - recent_avg) ** 2 for x in history) / len(history) if history else 0
        stability_bonus = 1.1 if variance < 25 else 1.0
        
        final_plot_yield = adjusted_yield * stability_bonus
        efficiency_list.append(final_plot_yield)
        
        # Irrelevant aggregation
        buffer_sum = 0
        for val in [area, base_yield, recent_avg]:
            buffer_sum += val * 0.01  # negligible contribution

    # Use of zip and enumerate together
    indexed = list(enumerate(zip(efficiency_list, [p['fertility_index'] for p in plot_data])))
    weighted_total = 0
    weight_sum = 0
    
    for i, (eff, fert) in indexed:
        weight = fert * (i + 1)
        weighted_total += eff * weight
        weight_sum += weight
    
    overall_efficiency = weighted_total / weight_sum if weight_sum else 0
    
    # Final computation
    final_yield = int(overall_efficiency * total_area // 100)
    
    # Dead code path - never executed due to logic above
    if False and len(temp_buffer) > 100:
        final_yield *= 2
        
    return final_yield

# Main execution
plots = [
    {
        'dimensions': {'length': 10, 'width': 8},
        'fertility_index': 7,
        'recent_rainfall': 65,
        'yield_history': [85, 90, 88, 87, 89]
    },
    {
        'dimensions': {'length': 12, 'width': 6},
        'fertility_index': 9,
        'recent_rainfall': 15,
        'yield_history': [95, 92, 94]
    },
    {
        'dimensions': {'length': 9, 'width': 9},
        'fertility_index': 6,
        'recent_rainfall': 85,
        'yield_history': [70, 75, 73, 74]
    }
]

thresholds = {'min_rain': 20, 'max_rain': 80}

# Sensor data - irrelevant to final result but adds distraction
sensor_logs = [100, 205, 512, 1025, 700, -10, 900]
_ = validate_sensor_readings(sensor_logs)

final_yield = calculate_harvest_efficiency(plots, thresholds)
print(f"Target result: {final_yield}")