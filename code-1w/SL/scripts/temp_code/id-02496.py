import math

# Simulate sensor readings and health monitoring system
def analyze_sensor_data(readings, baseline):
    trend_score = 0
    fluctuation_index = 0
    stable_count = 0
    total_deviation = 0.0

    for reading in readings:
        deviation = abs(reading - baseline)
        total_deviation += deviation

        if deviation < 5:
            stable_count += 1
            trend_score += 2
        elif deviation < 15:
            trend_score += 1
        else:
            trend_score -= 1

        # Irrelevant fluctuation metric (distractor)
        if deviation > 10:
            fluctuation_index += deviation * 0.5

    avg_deviation = total_deviation / len(readings) if readings else 0
    return trend_score, avg_deviation, stable_count


# Data transformation pipeline
transform_data = lambda raw: [round(x * 1.08 - 2.3, 1) for x in raw if x > 0]

# Auxiliary function with partial relevance
def compute_resilience_factor(metrics, weights):
    weighted_sum = sum(m * w for m, w in zip(metrics, weights))
    normalization = math.sqrt(sum(w ** 2 for w in weights))
    return weighted_sum / normalization if normalization else 0


# Main processing logic
def process_results(raw_input, criteria):
    # Step 1: Preprocess raw data
    cleaned_data = transform_data(raw_input)
    
    # Step 2: Analyze core behavior
    score, deviation, stability = analyze_sensor_data(cleaned_data, baseline=18.5)
    
    # Step 3: Compute auxiliary metrics (some irrelevant)
    outlier_count = sum(1 for x in cleaned_data if x > 30 or x < 10)
    range_spread = max(cleaned_data) - min(cleaned_data) if cleaned_data else 0
    
    # Distractor dictionary operations (semi-relevant)
    stats_summary = {
        'count': len(cleaned_data),
        'high_deviation': deviation > 8.0,
        'outliers': outlier_count,
        'spread': range_spread
    }
    
    # Extract flags using string methods (artificial complexity)
    flag_keys = [k for k in stats_summary.keys() if 'i' in k]
    flag_count = len(flag_keys)
    
    # Core calculation path
    resilience_metrics = [score, stability, deviation]
    weights = [0.6, 0.3, -0.1]  # More stable = better; high deviation = penalty
    resilience = compute_resilience_factor(resilience_metrics, weights)
    
    # Decision logic with conditional override
    if criteria['min_stability'] > stability:
        resilience *= 0.7
    
    if deviation < 6.0 and stability >= 4:
        resilience += 2.5
    
    # Final adjustment using dict.get() and default (minor impact)
    bonus = stats_summary.get('bonus_flag', 0)
    final_value = int(round(resilience * 17.3 + flag_count * 1.1 + bonus))
    
    return final_value


# Input data and configuration
raw_sensor_readings = [20, -1, 15, 18, 25, 17, 19, 0, 22, 16]
thresholds = {
    'min_stability': 5,
    'max_deviation': 10
}

# Execute main logic
final_output = process_results(raw_sensor_readings, thresholds)
print(f"Result: {final_output}")