def analyze_temperature_stability(readings):
    stable_count = 0
    temp_variance = [abs(readings[i] - readings[i-1]) for i in range(1, len(readings))]
    avg_variance = sum(temp_variance) / len(temp_variance) if temp_variance else 0
    for v in temp_variance:
        if v < 0.5:
            stable_count += 1
    return stable_count > len(temp_variance) * 0.7


def preprocess_sensor_data(raw_data):
    cleaned = [x for x in raw_data if isinstance(x, (int, float)) and -50 <= x <= 150]
    outliers = [x for x in cleaned if x > 100]
    filtered = [x for x in cleaned if x <= 100]
    sorted_vals = sorted(filtered)
    mid_point = len(sorted_vals) // 2
    median_val = (sorted_vals[mid_point] + sorted_vals[-(mid_point+1)]) / 2
    return {'data': filtered, 'median': median_val, 'outliers_removed': len(outliers)}


def calculate_optimal_yield(data_dict):
    base = data_dict['median']
    adjustment_factor = 0.8 if analyze_temperature_stability(data_dict['data']) else 1.2
    fluctuation_score = sum(abs(a - b) for a, b in zip(data_dict['data'], data_dict['data'][1:]))
    penalty = fluctuation_score * 0.05 if fluctuation_score > 20 else 0
    
    # Distractor variables - not used in final computation
    theoretical_max = max(data_dict['data']) * 1.5
    safety_margin = theoretical_max * 0.1
    normalized_score = (fluctuation_score + base) / (theoretical_max or 1)
    
    raw_yield = base * 10 * adjustment_factor
    final_yield = raw_yield - penalty
    
    return final_yield

# Simulated sensor input with minor noise
raw_input = [23, 24, 24, 23, 25, 26, 25, 24, 23, 105, 24, 23, 24, 25, 26, 27, 26, 25, 24, 23]

processed_data = preprocess_sensor_data(raw_input)
final_yield = calculate_optimal_yield(processed_data)
print(f"Result: {final_yield}")