def calculate_productivity(temps, humids):
    base_multiplier = 1.2
    stress_factor = 0.0
    cumulative_index = 0.0
    adjustment_log = []

    # Irrelevant pre-processing: normalize humidity to unused scale
    normalized_humidity = [h / 100.0 for h in humids]
    inverted_temps = [100.0 / (t + 1) for t in temps]  # Unused computation

    productivity_map = {}
    for i, temp in enumerate(temps):
        if temp < 20 or temp > 35:
            stress_factor += 0.1
        else:
            adjusted_value = (temp - 20) * 1.5
            humidity_influence = humids[i] * 0.01
            
            # Real calculation branch
            efficiency_score = adjusted_value - humidity_influence
            
            # Dead code path (never taken due to data)
            if efficiency_score < 0:
                efficiency_score = 0.0
                adjustment_log.append(f'Clamped at index {i}')
            
            productivity_map[f'hour_{i}'] = round(efficiency_score, 2)
    
    # Lambda-based transformation (semi-relevant)
    apply_bonus = lambda x: x * 1.1 if x > 8.0 else x
    bonus_applied = [apply_bonus(v) for v in productivity_map.values()]
    
    # Core accumulation that determines final result
    total_productivity = sum(bonus_applied)
    
    # Distractor: complex dictionary filtering with no impact
    filtered_high = {k: v for k, v in productivity_map.items() if v > 7.5}
    peak_hours = len(filtered_high)
    dummy_aggregate = sum([len(k) for k in filtered_high.keys()])  # Irrelevant

    # Final computation chain
    base_integral = total_productivity * base_multiplier
    stress_penalty = stress_factor * 5
    net_yield = base_integral - stress_penalty
    
    # Final adjustment using unused intermediate
    decay_correction = 0.98 ** len(inverted_temps)  # Computed but not impactful
    final_yield = int(round(net_yield))  # Critical assignment point
    
    return final_yield

# Input data
temperature_data = [18, 22, 26, 30, 34, 28, 24]
humidity_levels = [40, 45, 50, 55, 60, 52, 48]

# Execution
final_yield = calculate_productivity(temperature_data, humidity_levels)
print(f"Result: {final_yield}")