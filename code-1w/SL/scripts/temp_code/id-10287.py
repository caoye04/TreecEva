def analyze_trends(data_points):
    trend_scores = []
    for i in range(1, len(data_points)):
        if data_points[i] > data_points[i-1]:
            trend_scores.append(1)
        elif data_points[i] < data_points[i-1]:
            trend_scores.append(-1)
        else:
            trend_scores.append(0)
    return trend_scores

# Simulate sensor stability adjustments (distractor function)
def calculate_stability(signal_log):
    base_stability = 100
    for val in signal_log:
        if val % 7 == 0:
            base_stability -= 3
        elif val % 5 == 0:
            base_stability += 2
    return base_stability  # Not used in final result

def aggregate_performance(weights, metrics):
    weighted_sum = 0
    normalization = sum(weights)
    for w, m in zip(weights, metrics):
        weighted_sum += w * m
    return int(weighted_sum / normalization) if normalization != 0 else 0

# Main execution
sensor_readings = [12, 15, 15, 18, 20, 19, 25]
adjustment_factor = 0.9
offset_correction = 4

# Distractor: unused transformation
corrected_readings = [int(x * adjustment_factor) + offset_correction for x in sensor_readings]

# Real processing path
trend_analysis = analyze_trends(sensor_readings)
performance_metrics = [t + 2 for t in trend_analysis]  # Boost baseline

# Weight configuration (simulates feedback importance)
feedback_weights = [3, 1, 4, 1, 5, 9]  # Pi digits for distraction

# Dead code: irrelevant filtering
valid_weights = [w for w in feedback_weights if w > 2]

# Unused stability check
stability_score = calculate_stability(sensor_readings)

# Key computation
final_score = aggregate_performance(feedback_weights, performance_metrics)

# Print result as required
print(f"Target result: {final_score}")