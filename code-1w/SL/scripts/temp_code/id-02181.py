def analyze_growth_patterns(data, thresholds):
    growth_rates = []
    noise_filter = lambda x: x > thresholds['min_signal']
    filtered_data = list(filter(noise_filter, data))
    
    for val in filtered_data:
        if val > thresholds['optimal_range'][0]:
            growth_rates.append(val * 0.85)
        else:
            growth_rates.append(val * 0.67)
    
    return growth_rates


def calculate_stress_index(readings):
    baseline = sum(readings) / len(readings)
    variance = sum((x - baseline) ** 2 for x in readings) / len(readings)
    stress_score = baseline * (variance ** 0.5)
    
    # Distractor: irrelevant normalization
    normalized_scores = [(x - baseline) / (variance + 1e-5) for x in readings]
    avg_normalized = sum(normalized_scores) / len(normalized_scores)
    
    return stress_score  # Only this matters


def calculate_optimal_yield(env_conditions, stress_factors):
    base_yield = 0
    penalty_adjustment = 0
    
    # Real logic begins
    temperature_window = set(range(env_conditions['temp_low'], env_conditions['temp_high']))
    ideal_range = {t for t in temperature_window if t in range(22, 29)}
    suboptimal_penalty = len(temperature_window) - len(ideal_range)
    
    # Use of dictionary operations
    humidity_factor = env_conditions.get('humidity', 50) / 100.0
    light_exposure = env_conditions['light_hours']
    
    if light_exposure > 12:
        base_yield += 45 * humidity_factor
    else:
        base_yield += 30 * humidity_factor

    # Lambda used in aggregation
    multiplier_fn = lambda x: x * 1.1 if x > 0 else x
    adjusted_penalty = multiplier_fn(suboptimal_penalty)
    
    # Stress factor integration (only one component used)
    dummy_calc = calculate_stress_index(stress_factors)
    actual_influence = dummy_calc * 0.05  # Minor correction
    
    # Irrelevant branching
    if actual_influence > 10:
        penalty_adjustment += 5
    elif actual_influence < 5:
        penalty_adjustment -= 2  # Never reached due to input
    else:
        pass  # Dead code path

    final_yield = int(base_yield - adjusted_penalty + penalty_adjustment)
    return final_yield

# Main execution
conditions = {
    'temp_low': 18,
    'temp_high': 30,
    'humidity': 60,
    'light_hours': 14,
    'optimal_range': [22, 28]
}

stress_factors = [1.2, 0.9, 1.5, 1.1, 0.8, 1.3]

# Extraneous data processing
raw_sensor_data = [1.1, 0.8, 1.6, 2.0, 0.7, 1.4, 3.1]
thresh = {'min_signal': 0.75, 'optimal_range': [1.0, 2.0]}
growth_results = analyze_growth_patterns(raw_sensor_data, thresh)

# Actual target computation
final_yield = calculate_optimal_yield(conditions, stress_factors)

print(f"Result: {final_yield}")