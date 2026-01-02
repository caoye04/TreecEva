def analyze_trends(data, threshold):
    trend_count = 0
    temp_sum = 0
    for val in data:
        if val > threshold:
            trend_count += 1
            temp_sum += val
    normalized = temp_sum / len(data) if data else 0
    return trend_count

# Simulate system diagnostics
def run_diagnostics():
    sensor_data = [12, 15, 18, 21, 9, 7, 24]
    avg_load = sum(sensor_data) / len(sensor_data)
    high_load_count = 0
    for load in sensor_data:
        if load > 15:
            high_load_count += 1
    # Irrelevant diagnostic flag
    system_stable = high_load_count < 4
    return avg_load

# Main evaluation logic
def evaluate_performance(feedback, multiplier):
    base_points = 0
    penalty_adjustment = 0
    
    # Real processing with dictionary
    for category, score in feedback.items():
        if category == 'usability':
            base_points += score * 1.5
        elif category == 'performance':
            base_points += score * 2.0
        elif category == 'security':
            base_points += max(score - 2, 0)
        else:
            penalty_adjustment -= 1  # Minor penalty for unknown
    
    # Distractor: complex but unused calculation
    inverted_weights = {k: (10 - v) / 10 for k, v in feedback.items()}
    total_inverted = sum(inverted_weights.values())
    adjustment_factor = total_inverted / len(inverted_weights) if inverted_weights else 0
    
    # Actual computation path
    final_value = base_points * multiplier
    
    # Extra distraction: bitwise manipulation not affecting result
    masked_value = int(final_value) & 0xFF
    xor_shift = masked_value ^ 15
    
    return int(final_value)

# Setup inputs
diag_result = run_diagnostics()
data_trend = [3, 5, 6, 8, 10]
trend_output = analyze_trends(data_trend, 5)

# Feedback dictionary with meaningful structure
feedback_dict = {
    'usability': 7,
    'performance': 6,
    'security': 8,
    'documentation': 5
}

base_multiplier = 3

# Key statement
final_score = evaluate_performance(feedback_dict, base_multiplier)

print(f"Result: {final_score}")