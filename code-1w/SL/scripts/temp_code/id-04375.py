from itertools import compress, cycle

def analyze_soil_quality(readings):
    # Irrelevant helper: computes average but not used in final logic
    averages = [sum(sensor) / len(sensor) for sensor in readings]
    valid = [any(x > 70 for x in sensor) for sensor in readings]
    return list(compress(readings, valid))

def calculate_harvest_efficiency(plot_data, sensor_flags):
    total_yield = 0
    efficiency_bonus = 0
    
    # Distractor variables
    temp_calibration = 0.0
    calibration_records = []
    
    for i, (plot, flag_list) in enumerate(zip(plot_data, sensor_flags)):
        base_yield = plot['size'] * plot['fertility']
        
        # Simulate sensor-based adjustment (only odd-indexed flags matter)
        active_sensors = sum(1 for j, f in enumerate(flag_list) if f and j % 2 == 1)
        
        # Real logic path
        if active_sensors >= 2:
            yield_boost = base_yield * 0.15
        else:
            yield_boost = base_yield * 0.05
        
        # Dead code path - looks relevant but unused
        if plot['size'] > 10:
            temp_calibration += base_yield * 0.02
            calibration_records.append(temp_calibration)
        
        total_yield += base_yield + yield_boost
        efficiency_bonus += yield_boost
    
    # Secondary distractor: complex but unused computation
    seasonal_cycle = cycle([1.05, 0.98, 1.02])
    adjusted_yield = sum(total_yield / (1.1 - 0.01 * i) for i in range(3))
    
    # Final result depends only on total_yield and bonus
    final_yield = int(total_yield + efficiency_bonus * 0.8)  # Key assignment point
    return final_yield

# Main data setup
plots = [
    {'size': 8, 'fertility': 6},
    {'size': 12, 'fertility': 5},
    {'size': 5, 'fertility': 9}
]

sensors = [
    [True, False, True, True],
    [False, True, False, True],
    [True, True, False, False]
]

# Analyze but don't use result (distractor call)
discarded_analysis = analyze_soil_quality(sensors)

# Critical execution point
final_yield = calculate_harvest_efficiency(plots, sensors)

print(f"Target result: {final_yield}")