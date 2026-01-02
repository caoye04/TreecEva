def analyze_temperature_trends(temp_readings):
    trend_data = []
    increasing_count = 0
    decreasing_count = 0
    stable_count = 0

    for i, temp in enumerate(temp_readings):
        if i == 0:
            trend_data.append(0)
        else:
            diff = temp - temp_readings[i-1]
            if diff > 0.5:
                increasing_count += 1
                trend_data.append(1)
            elif diff < -0.5:
                decreasing_count += 1
                trend_data.append(-1)
            else:
                stable_count += 1
                trend_data.append(0)
    
    # Irrelevant transformation
    scaled_trends = [x * 2 for x in trend_data]
    reversed_scaled = scaled_trends[::-1]
    average_trend = sum(trend_data) / len(trend_data) if trend_data else 0

    return trend_data, average_trend, increasing_count


def calculate_outlier_threshold(data):
    mean_val = sum(data) / len(data)
    variance = sum((x - mean_val) ** 2 for x in data) / len(data)
    std_dev = variance ** 0.5
    return mean_val + 2 * std_dev


def preprocess_readings(raw_data, threshold_override=None):
    cleaned = [round(x, 1) for x in raw_data if isinstance(x, (int, float)) and not (x != x)]  # Remove NaNs and round
    
    # Dead code path - never executed under normal input
    if threshold_override and threshold_override > 100:
        cleaned = [x for x in cleaned if x <= threshold_override]
    
    # Extra processing with no impact on final result
    magnitude_levels = []
    for val in cleaned:
        if val < 10:
            magnitude_levels.append('low')
        elif val < 50:
            magnitude_levels.append('medium')
        else:
            magnitude_levels.append('high')
    
    return cleaned


def calculate_adjusted_score(dataset):
    base_scores = []
    adjustment_factor = 0.0

    for idx, value in enumerate(dataset):
        score = 0
        if value > 20:
            score += 10
        else:
            score += 5
            
        # Apply index-based bonus only if even position
        if idx % 2 == 0:
            score += 2
        
        # Conditional penalty based on neighboring values (if exist)
        if idx > 0 and dataset[idx-1] > value:
            score -= 1
        
        base_scores.append(score)
    
    # Distractor: unused intermediate calculation
    total_magnitude_weight = sum(len(str(int(x))) for x in dataset)
    normalized_weights = [w / max(base_scores) for w in base_scores] if base_scores else [0]
    
    raw_total = sum(base_scores)
    count_bonus = len(dataset) // 5
    adjustment_factor = len(set(round(x) for x in dataset)) * 0.5
    
    final = raw_total + count_bonus + adjustment_factor
    return int(final)

# Main execution
sensor_log = [23.4, 19.1, 25.6, 18.9, 20.0, 27.3, 15.8, 22.1]
processed_data = preprocess_readings(sensor_log)
trends, avg_trend, up_periods = analyze_temperature_trends(processed_data)

# Key statement
final_score = calculate_adjusted_score(processed_data)

print(f"Result: {final_score}")