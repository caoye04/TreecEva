from itertools import compress, cycle

# Simulate sensor data reliability assessment for an environmental monitoring system
def analyze_reliability(readings):
    avg = sum(readings) / len(readings)
    variance = sum((x - avg) ** 2 for x in readings) / len(readings)
    threshold = 5.0
    return variance < threshold

# Filter valid sensors based on historical performance
def filter_sensors(sensors, history):
    valid_flags = [analyze_reliability(his) for his in history]
    filtered = list(compress(sensors, valid_flags))
    
    # Distractor: unused transformation
    scaled = [s * 1.05 for s in sensors]
    offset = sum(scaled) / len(scaled) - 2.1
    
    return filtered

# Compute weighted performance score
def calculate_stability(values, window=3):
    if len(values) < window:
        return 0.0
    
    trends = []
    for i in range(len(values) - window + 1):
        segment = values[i:i+window]
        trend = sum(segment[i+1] - segment[i] for i in range(len(segment)-1))
        trends.append(trend)
    
    # Distractor: complex but unused pattern matching
    pattern_cycle = cycle([1, -1])
    _ = [next(pattern_cycle) * t for t in trends]
    
    return sum(abs(t) for t in trends) / len(trends)

# Main evaluation logic
def evaluate_performance(metrics, weights):
    stability_scores = []    
    for m in metrics:
        score = calculate_stability(m)
        stability_scores.append(score)
    
    # Apply weights (only some are actually used)
    total = 0.0
    for i in range(min(len(stability_scores), len(weights))):
        if i % 2 == 0:  # Only even-indexed weights contribute
            total += stability_scores[i] * weights[i]
    
    # Irrelevant normalization path (never taken)
    if False:
        total = total / (sum(weights) or 1)
    
    return int(total * 10)  # Final discretization

# Simulated input data
sensor_ids = [101, 102, 103, 104]
historical_data = [
    [20.1, 19.8, 20.3, 20.0, 19.9],  # Low variance → reliable
    [15.2, 18.7, 12.1, 25.3, 10.2],  # High variance → unreliable
    [30.0, 30.2, 29.8, 30.1, 29.9],  # Reliable
    [40.5, 45.1, 38.9, 50.2, 42.3]   # Unreliable
]

active_sensors = filter_sensors(sensor_ids, historical_data)

# Metrics: each sublist represents time-series data from a remaining sensor
metric_data = [
    [100, 102, 105, 103, 107, 110],  # Sensor 101
    [300, 295, 298, 302, 305, 300]   # Sensor 103
]

weights_list = [2.0, 1.5, 2.5, 1.0]  # Only indices 0 and 2 will be used

final_score = evaluate_performance(metric_data, weights_list)
print(f"Result: {final_score}")