def analyze_trends(values):
    trend_summary = {}
    increasing = 0
    decreasing = 0
    for i in range(1, len(values)):
        if values[i] > values[i-1]:
            increasing += 1
        elif values[i] < values[i-1]:
            decreasing += 1
    trend_summary['up'] = increasing
    trend_summary['down'] = decreasing
    return trend_summary

# Simulate sensor data fluctuations
temperature_readings = [20, 22, 21, 23, 25, 24, 26, 28, 27, 29]

# Misleading computation - not used later
drift_estimate = sum([abs(temperature_readings[i] - temperature_readings[i-1]) for i in range(1, len(temperature_readings))]) // len(temperature_readings)

# Analyze trend but only use part of it
trend_metrics = analyze_trends(temperature_readings)

# Secondary data stream
response_times = [0.45, 0.52, 0.48, 0.55, 0.51, 0.49, 0.53, 0.50, 0.47, 0.54]

# Compute auxiliary stats (some irrelevant)
avg_response = sum(response_times) / len(response_times)
variance = sum((x - avg_response) ** 2 for x in response_times) / len(response_times)
std_dev = variance ** 0.5

# Build metric dictionary with red herrings
metric_data = {
    'trend_up': trend_metrics['up'],
    'trend_down': trend_metrics['down'],
    'base_temp': temperature_readings[0],
    'peak_response': max(response_times),
    'noise_floor': 0.05,
    'drift': drift_estimate,  # unused in final logic
    'consistency': std_dev  # also unused
}

# Evaluate performance based only on directional trends
# This function ignores most fields in metric_data
def evaluate_performance(metrics):
    upward = metrics['trend_up']
    downward = metrics['trend_down']
    net_trend = upward - downward
    
    # Apply non-linear weighting
    if net_trend > 0:
        score = net_trend * 17
    else:
        score = abs(net_trend) * 5
    
    # Artificial cap
    if score > 50:
        score = 50
    
    # Inject distraction: modify local copy (no effect)
    metrics['temp_score'] = score + 10  # dead assignment
    
    # Final adjustment based on arbitrary rule
    if upward >= 5:
        score += 3
    
    return score

# Key execution point
trend_analysis_result = analyze_trends(temperature_readings)
final_score = evaluate_performance(metric_data)

print(f"Result: {final_score}")