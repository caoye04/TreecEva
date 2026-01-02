from collections import defaultdict, Counter

# Simulate sensor data analysis with noise filtering and anomaly detection
def collect_sensor_readings():
    raw_data = [101, 105, 98, 102, 205, 103, 97, 100, 104, 195, 102, 99]
    filtered_data = [x for x in raw_data if 90 <= x <= 110]  # Remove obvious outliers
    return filtered_data

def compute_moving_average(data, window=3):
    averages = []
    for i in range(len(data) - window + 1):
        averages.append(sum(data[i:i+window]) / window)
    return averages

def identify_trends(moving_averages):
    trend_changes = 0
    for i in range(1, len(moving_averages)):
        if moving_averages[i] > moving_averages[i-1]:
            trend_changes += 1
        elif moving_averages[i] < moving_averages[i-1]:
            trend_changes -= 1
    return abs(trend_changes)

def evaluate_performance(anomalies, metrics):
    base_score = metrics['stability'] * 10
    penalty = len(anomalies) * 5
    bonus = metrics['consistency'] // 2
    debug_factor = sum([i * 2 for i in range(3)])  # Irrelevant computation (evaluates to 6)
    adjustment = 0
    
    if metrics['reliability'] > 0.7:
        adjustment += 10
        temp_history = [1, 1, 2, 3, 5, 8]
        # Dead code path - Fibonacci values not used
        fib_sum = sum(temp_history)
        
    final_score = base_score - penalty + bonus + adjustment
    
    # Additional irrelevant variables
    snapshot_log = defaultdict(int)
    for val in ['a', 'b', 'a', 'c']:
        snapshot_log[val] += 1
    
    return final_score

# Main execution flow
data = collect_sensor_readings()
moving_avgs = compute_moving_average(data)
trend_index = identify_trends(moving_avgs)

# Construct metrics dictionary
base_metrics = {
    'stability': len(moving_avgs),
    'consistency': Counter(data).most_common(1)[0][1],
    'reliability': 0.85,
    'noise_level': 0.05
}

# Detect anomalies based on deviation
mean_val = sum(data) / len(data)
anomalies = [x for x in data if abs(x - mean_val) > 3]

# Key computational step
final_score = evaluate_performance(anomalies, base_metrics)
print(f"Result: {final_score}")