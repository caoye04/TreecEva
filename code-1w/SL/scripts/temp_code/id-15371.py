def analyze_growth_cycles(data_points):
    cumulative_phase = 0
    for i, point in enumerate(data_points):
        if i % 2 == 0:
            cumulative_phase += point * 0.85
        else:
            cumulative_phase -= point * 0.15
    return int(cumulative_phase)

# Simulate sensor noise correction (distractor function - not used in final result)
def correct_sensor_noise(raw_readings):
    corrected = []
    for val in raw_readings:
        adjusted = val * 0.98 + 2.1
        if adjusted > 100:
            adjusted = 100
        corrected.append(round(adjusted, 2))
    return corrected

# Main agricultural yield computation
def calculate_harvest_efficiency(plots, sensors):
    base_yield = 0
    adjustment_factor = 0.0
    stability_scores = []
    
    for idx, (plot, sensor) in enumerate(zip(plots, sensors)):
        size = plot['area']
        soil_q = plot['soil_quality']
        readouts = sensor['readings']
        
        # Real contribution to yield
        raw_productivity = size * soil_q
        
        # Noise-corrupted data that must be filtered (semi-relevant)
        valid_readings = [r for r in readouts if 10 <= r <= 90]
        
        # Distractor: irrelevant average calculation
        avg_reading = sum(readouts) / len(readouts) if readouts else 0
        _ = avg_reading * 0.97  # Dead computation
        
        # Signal integrity score (not actually used later - misleading)
        signal_score = len(valid_readings) / len(readouts) if readouts else 0
        stability_scores.append(signal_score * 100)
        
        # Actual efficiency logic
        if soil_q >= 7:
            adjustment_factor += 0.2
        elif soil_q >= 4:
            adjustment_factor += 0.1
        else:
            adjustment_factor -= 0.05
        
        base_yield += raw_productivity
    
    # Secondary distractor loop: computes unused diagnostic
    diagnostics = []
    for score in stability_scores:
        if score > 80:
            diagnostics.append('OPTIMAL')
        elif score > 60:
            diagnostics.append('ACCEPTABLE')
        else:
            diagnostics.append('POOR')
    
    # Final efficiency model
    normalized_base = base_yield / 10.0
    applied_adjustment = normalized_base * (1 + adjustment_factor)
    
    # Final clipping and rounding
    clipped = max(50, min(applied_adjustment, 950))
    final_yield = int(round(clipped))
    
    return final_yield

# Input data setup
plots_data = [
    {'area': 12, 'soil_quality': 8},
    {'area': 15, 'soil_quality': 6},
    {'area': 10, 'soil_quality': 9},
    {'area': 20, 'soil_quality': 3}
]

sensors_data = [
    {'readings': [85, 92, 78, 15, 88]},
    {'readings': [80, 45, 95, 70]},
    {'readings': [88, 82, 79, 91]},
    {'readings': [105, 30, 25, 12]}
]

# Execute main logic
interim_analysis = analyze_growth_cycles([12, 15, 10, 20])  # Distractor call

final_yield = calculate_harvest_efficiency(plots_data, sensors_data)
print(f"Result: {final_yield}")