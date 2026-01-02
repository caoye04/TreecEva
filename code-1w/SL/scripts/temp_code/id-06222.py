def analyze_trends(data_stream, thresholds):
    trend_strength = 0
    temp_buffer = []
    for i in range(len(data_stream)):
        if data_stream[i] > thresholds[0]:
            temp_buffer.append(data_stream[i])
            if len(temp_buffer) >= 3:
                trend_strength += 1
                temp_buffer = temp_buffer[-2:]
    return trend_strength


def filter_anomalies(raw_readings):
    clean_readings = []
    anomaly_count = 0
    for val in raw_readings:
        if abs(val - sum(clean_readings) / max(len(clean_readings), 1)) < 50 if clean_readings else True:
            clean_readings.append(val)
        else:
            anomaly_count += 1
    return clean_readings


def evaluate_performance(feedback, criteria):
    base_metric = 0
    adjustment_factor = 0.85
    history_log = [0] * len(feedback)
    
    # Irrelevant preprocessing (distractor)
    processed = filter_anomalies([x * 2 for x in feedback if x > 0])
    processed_sliced = processed[1::2]  # slicing operation (required feature)
    
    for idx, item in enumerate(feedback):
        if item in criteria['positive']:
            base_metric += 3
            history_log[idx] = 1
        elif item in criteria['negative']:
            base_metric -= 2
        else:
            base_metric += 1
    
    # Secondary logic with conditional expression
    volatility_index = sum(1 for i in range(1, len(feedback)) if abs(feedback[i] - feedback[i-1]) > 5)
    adjustment_factor = 0.9 if volatility_index < 4 else 0.7
    
    # Simulated auxiliary analysis (misleading computation)
    dummy_impact = 0
    for x in feedback[::3]:
        dummy_impact += (x % 7) * 0.1
    
    # Core result calculation
    final_score = int((base_metric * adjustment_factor) + 10)
    
    # Dead code path (distractor)
    if False:
        fallback = analyze_trends(feedback, [5, 10])
        final_score = max(final_score, fallback)
    
    return final_score

# Main execution
feedback_sequence = [8, 12, 3, 9, 1, 7, 14, 6]
criteria_config = {
    'positive': [7, 8, 9, 10, 11, 12],
    'negative': [1, 2, 3],
    'neutral': [4, 5, 6]
}

interim_result = analyze_trends(feedback_sequence, [5, 10])
final_score = evaluate_performance(feedback_sequence, criteria_config)
print(f"Result: {final_score}")