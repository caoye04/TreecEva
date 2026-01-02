def analyze_trends(data, threshold=0.5):
    trend_data = {}
    for key, values in data.items():
        avg_val = sum(values) / len(values)
        trend_data[key] = avg_val > threshold
    return trend_data

# Simulate sensor readings over time
sensor_readings = {
    'temp': [0.4, 0.5, 0.6, 0.7],
    'pressure': [0.3, 0.2, 0.4, 0.5],
    'humidity': [0.6, 0.7, 0.8, 0.9]
}

status_flags = analyze_trends(sensor_readings)

# Irrelevant transformation (distractor)
decay_weights = [0.9 ** i for i in range(4)]
weighted_decay = list(map(lambda x: round(x * 100) / 100, decay_weights))

# Core metrics for evaluation
metrics = {
    'stability': sum(sensor_readings['temp']) / len(sensor_readings['temp']),
    'consistency': len([x for x in sensor_readings['humidity'] if x > 0.6]),
    'response_time': (sensor_readings['pressure'][-1] - sensor_readings['pressure'][0]) * 10
}

# Weight configuration (some entries are red herrings)
weights = {
    'stability': 0.4,
    'consistency': 0.3,
    'response_time': 0.2,
    'redundant_metric': 0.1  # Unused in calculation
}

# Additional distraction: unused helper function
def normalize_values(vals):
    max_val = max(vals)
    return [v / max_val for v in vals] if max_val > 0 else vals

# Real computation begins here
effective_metrics = [
    metrics['stability'] * weights['stability'],
    metrics['consistency'] * weights['consistency'],
    abs(metrics['response_time']) * weights['response_time']
]

# Use of slicing and dictionary ops (required features)
temp_slice = sensor_readings['temp'][1:3]
interim = sum(temp_slice) / 2

# Conditional adjustment based on logical checks
if status_flags['temp'] and not status_flags.get('pressure'):
    interim *= 1.1

# Final performance score with distractors
final_score = sum(effective_metrics) + interim * 0.05

# Print result as required
Target result: {final_score}