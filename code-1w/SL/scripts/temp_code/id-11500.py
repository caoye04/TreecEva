def calculate_final_score(raw_data, importance_weights):
    # Initialize tracking variables
    temp_sum = 0
    normalization_factor = 0
    adjusted_values = {}
    
    # Irrelevant pre-processing: dummy scaling (not used in final logic)
    scaled_data = {k: v * 1.05 for k, v in raw_data.items()}
    outlier_buffer = []
    for key, value in raw_data.items():
        if value > 80:
            outlier_buffer.append(value * 0.9)  # Distractor: not used later
    
    # Core logic with dictionary and weighting
    for item, weight in importance_weights.items():
        if item in raw_data:
            contribution = raw_data[item] * weight
            temp_sum += contribution
            normalization_factor += weight
            adjusted_values[item] = contribution
    
    # Secondary adjustment with distractor condition (only some branches matter)
    bonus_applied = False
    total_base = sum(raw_data.values())
    if total_base > 200:
        temp_sum += 10  # Meaningful bonus
        bonus_applied = True
    
    # Red herring: complex but unused calculation
    entropy_proxy = 0
    for v in raw_data.values():
        if v > 0:
            entropy_proxy -= v * __import__('math').log(v)
    
    # Final aggregation
    average_contribution = temp_sum / normalization_factor if normalization_factor else 0
    final_score = int(round(average_contribution + (5 if bonus_applied else 0)))
    
    return final_score

# Main execution
sensor_readings = {'temp': 75, 'pressure': 85, 'humidity': 60}
feature_weights = {'temp': 0.4, 'pressure': 0.35, 'altitude': 0.25, 'humidity': 0.6}

# Dead code path: simulation of fallback (never triggered due to complete data)
if 'altitude' not in sensor_readings:
    feature_weights['altitude'] = 0.1

intermediate_total = sum(sensor_readings[k] for k in ['temp', 'pressure'])  # Distractor variable

final_score = calculate_final_score(sensor_readings, feature_weights)
print(f"Result: {final_score}")