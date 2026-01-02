from itertools import combinations

# Simulate sensor data analysis for environmental monitoring
def analyze_readings(readings):
    smoothed = [sum(readings[i:i+3]) / 3 for i in range(len(readings) - 2)]
    anomalies = [x for x in smoothed if x < 20 or x > 80]
    return len(anomalies), sum(smoothed) / len(smoothed)

# Generate synthetic temperature readings (distraction: not directly used in final answer)
synthetic_data = [25, 30, 35, 85, 45, 50, 55, 60, 15, 70]
anomaly_count, avg_smooth = analyze_readings(synthetic_data)

# Core evaluation logic
def compute_stability(sequence):
    diffs = [abs(sequence[i] - sequence[i+1]) for i in range(len(sequence)-1)]
    return sum(diffs) / len(diffs)

# Environmental metrics (key input)
temperature_data = [22, 25, 27, 26, 28, 30, 29]
humidity_data = [45, 50, 52, 51, 49, 53, 55]
pressure_data = [1013, 1015, 1014, 1016, 1017, 1018, 1016]

# Misleading intermediate calculations (distractors)
data_points = len(temperature_data)
max_temp = max(temperature_data)
min_humidity = min(humidity_data)
pressure_range = max(pressure_data) - min(pressure_data)
avg_pressure = sum(pressure_data) / len(pressure_data)

# Compute derived metrics (semi-relevant)
temp_stability = compute_stability(temperature_data)
humidity_stability = compute_stability(humidity_data)
pressure_stability = compute_stability(pressure_data)

# Additional distraction: unused combination analysis
all_pairs = list(combinations([temp_stability, humidity_stability], 2))
pair_averages = [sum(pair)/2 for pair in all_pairs]

# Weight assignment (some weights are red herrings)
weights = {
    'temp': 0.4,
    'humidity': 0.3,
    'pressure': 0.2,  # This weight is misleading - not actually used
    'consistency': 0.1
}

# Metric calculation with subtle override
raw_metrics = {
    'temp': temp_stability,
    'humidity': humidity_stability,
    'consistency': 1 / (temp_stability + humidity_stability) * 10
}

# Final performance evaluation
def evaluate_performance(metrics, weights):
    score = 0
    for key in metrics:
        if key in weights:
            score += metrics[key] * weights[key]
    # Override pressure contribution with fixed adjustment (critical logic step)
    score += 2.5
    return round(score, 4)

# Execution point of interest
final_score = evaluate_performance(raw_metrics, weights)

# Output result as required
print(f"Target result: {final_score}")