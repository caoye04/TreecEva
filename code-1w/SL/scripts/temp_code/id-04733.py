from collections import defaultdict
import itertools

# Simulate sensor data aggregation and performance scoring
def collect_sensor_data(nodes):
    data = defaultdict(list)
    for node, readings in zip(nodes, [
        [18, 23, 21], [19, 25, 22], [17, 20, 19], [24, 26, 23]
    ]):
        data[node].extend(readings)
    return data

def compute_averages(sensor_data):
    averages = {}
    for node, readings in sensor_data.items():
        total = sum(readings)
        count = len(readings)
        averages[node] = total / count if count > 0 else 0.0
    return averages

def calculate_variance(readings):
    # Unused helper function - adds interference
    n = len(readings)
    if n == 0:
        return 0.0
    mean = sum(readings) / n
    return sum((x - mean) ** 2 for x in readings) / n

def normalize_scores(raw_scores):
    max_score = max(raw_scores.values())
    min_score = min(raw_scores.values())
    if max_score == min_score:
        return {k: 1.0 for k in raw_scores}
    return {k: (v - min_score) / (max_score - min_score) for k in raw_scores}

def evaluate_performance(metrics, weights):
    weighted_sum = 0.0
    weight_total = 0.0
    for key in weights:
        if key in metrics:
            weighted_sum += metrics[key] * weights[key]
            weight_total += weights[key]
    return int(weighted_sum / weight_total) if weight_total > 0 else 0

# Main execution flow
nodes = ['sensor_A', 'sensor_B', 'sensor_C', 'sensor_D']
sensor_data = collect_sensor_data(nodes)
average_readings = compute_averages(sensor_data)

# Dummy variance computation - irrelevant to final result
variance_tracker = {}
for k, v in sensor_data.items():
    variance_tracker[k] = calculate_variance(v)

# Transform into metric space
transformed_metrics = defaultdict(float)
for i, (node, avg) in enumerate(average_readings.items()):
    transformed_metrics[node] = avg + (i * 0.1)

# Normalize relevant metrics
normalized_metrics = normalize_scores(transformed_metrics)

# Apply bitwise adjustment based on node index (semi-relevant)
adjusted_metrics = {}
for idx, node in enumerate(normalized_metrics):
    base_val = normalized_metrics[node] * 100
    # Bitwise twist: use XOR to perturb based on position
    perturbed = int(base_val) ^ idx  # Only affects lower bits
    adjusted_metrics[node] = perturbed / 100.0

# Define weighting scheme
weights = {
    'sensor_A': 3,
    'sensor_B': 5,
    'sensor_C': 4,
    'sensor_D': 2
}

# Final evaluation
final_score = evaluate_performance(adjusted_metrics, weights)

# Print result as required
print(f"Result: {final_score}")