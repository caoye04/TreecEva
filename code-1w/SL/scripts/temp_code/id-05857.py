def analyze_performance(metrics):
    # Irrelevant transformation
    normalized = {k: v / 100.0 for k, v in metrics.items()}
    adjusted = {}
    for key, value in normalized.items():
        if value < 0.5:
            adjusted[key] = value * 1.2
        else:
            adjusted[key] = value * 0.9
    return adjusted

# Simulate sensor readings (distractor data)
sensor_data = {'temp': 45, 'pressure': 88, 'humidity': 30}
sensor_metrics = {k: v / 100.0 for k, v in sensor_data.items() if v > 25}

# Core problem data
results = {
    'accuracy': 85,
    'latency': 60,
    'throughput': 75,
    'memory_usage': 40
}

weights = {
    'accuracy': 0.4,
    'latency': 0.1,
    'throughput': 0.3,
    'memory_usage': 0.2
}

# Distractor: unused weight combination
aux_weights = {k: v + 0.05 for k, v in weights.items()}
dropped_metrics = [k for k in results.keys() if results[k] < 50]

# Preprocessing with red herring computation
scaled_results = {k: (v / 100.0) * 50 for k, v in results.items()}
penalty_factor = 1.0
for metric, score in results.items():
    if score < 60:
        penalty_factor *= 0.95  # Minor adjustment not used later

# Actual calculation chain
def calculate_weighted_sum(data, w):
    total = 0.0
    for key in data:
        total += data[key] * w[key]
    return total

# Secondary helper with list comprehension distraction
def get_high_performers(data, threshold=70):
    return [k.upper() for k, v in data.items() if v >= threshold]

high_perf = get_high_performers(results)

# Main scoring logic
def calculate_final_score(data, w):
    base_score = calculate_weighted_sum(data, w)
    bonus = 0.0
    if 'accuracy' in data and data['accuracy'] >= 80:
        bonus += 5
    if len(get_high_performers(data)) >= 2:
        bonus += 3
    return int(base_score + bonus)

# Intermediate irrelevant function call
_ = analyze_performance(results)

# Key execution point
final_score = calculate_final_score(results, weights)
print(f"Target result: {final_score}")