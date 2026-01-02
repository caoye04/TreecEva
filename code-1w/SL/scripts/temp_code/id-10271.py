def analyze_temperatures(temps):
    avg_temp = sum(temps) / len(temps)
    deviation = [abs(t - avg_temp) for t in temps]
    max_dev = max(deviation)
    normalized = [(t - min(temps)) / (max(temps) - min(temps)) * 100 for t in temps]
    return avg_temp, max_dev, normalized


def evaluate_stability(metrics, history):
    current_avg, peak_dev, norm_vals = metrics
    trend = 0
    for i, val in enumerate(history):
        if i > 0:
            trend += norm_vals[i % len(norm_vals)] * (val - history[i-1])
    stability_score = current_avg - (peak_dev / 2) + (trend / 100)
    adjustment = 0
    for idx, (h, n) in enumerate(zip(history, norm_vals)):
        if h > current_avg and idx % 2 == 0:
            adjustment += n * 0.1
    return stability_score + adjustment


def compute_entropy(data):
    from collections import Counter
    counts = Counter(data)
    total = len(data)
    entropy = 0
    for count in counts.values():
        prob = count / total
        entropy -= prob * (prob ** 0.5)  # simplified pseudo-entropy
    return entropy * 100


def process_metrics(raw_data, limits):
    filtered = [x for x in raw_data if x >= limits['min']]
    shifted = [x + 5 for x in filtered]
    reversed_data = shifted[::-1]
    paired = list(zip(filtered, reversed_data))
    products = [a * b for a, b in paired]
    base_metric = sum(products) / len(products) if products else 0
    
    # Irrelevant transformation chain
    temp_buffer = [x.upper() for x in ['a', 'b', 'c']]  # dead code path
    redundant_calc = [compute_entropy([1,2,2,3]) for _ in range(3)]
    dummy_sum = sum(redundant_calc) / len(redundant_calc)
    
    # Actual computation branch
    scaling_factor = 0.75
    if base_metric > limits['threshold']:
        scaling_factor += 0.2
    adjusted_metric = base_metric * scaling_factor
    
    # Secondary distraction: linear search with no impact
    target = 'X'
    found_index = -1
    search_space = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i, char in enumerate(search_space):
        if char == target:
            found_index = i
            break
    
    final_score = int(adjusted_metric + 17)  # key assignment
    return final_score

# Main execution
sensor_readings = [23.5, 19.1, 27.3, 21.8, 25.6, 29.4, 18.2]
access_logs = [102, 105, 103, 110, 115, 112, 118]
config = {'min': 20.0, 'threshold': 400}

temp_analysis = analyze_temperatures(sensor_readings)
stability = evaluate_stability(temp_analysis, access_logs)
data_stream = [int(x * 2) for x in sensor_readings if x > 20]
final_score = process_metrics(data_stream, config)
print(f"Result: {final_score}")