from itertools import combinations

# Simulate sensor data quality assessment in an environmental monitoring system
def analyze_sensor_readings(readings):
    base_quality = 0
    temp_sum = 0
    spike_count = 0
    for i, val in enumerate(readings):
        temp_sum += val
        if i > 0 and abs(val - readings[i-1]) > 15:
            spike_count += 1
    avg = temp_sum / len(readings) if readings else 0
    noise_ratio = spike_count / len(readings) if readings else 0
    return max(0, 100 - (avg * 0.3) - (noise_ratio * 50))

# Assess geographic coverage efficiency
def calculate_coverage_efficiency(locations):
    total_pairs = 0
    close_pairs = 0
    for i, j in combinations(range(len(locations)), 2):
        x1, y1 = locations[i]
        x2, y2 = locations[j]
        distance = ((x1 - x2)**2 + (y1 - y2)**2)**0.5
        total_pairs += 1
        if distance < 10:
            close_pairs += 1
    coverage_score = (total_pairs - close_pairs) * 2 if total_pairs else 0
    redundancy_penalty = close_pairs * 1.5
    return max(0, coverage_score - redundancy_penalty)

# Main evaluation function with multiple factors
def evaluate_performance(metrics, weights):
    raw_product = 1
    adjusted_metrics = []
    
    # Irrelevant transformation (distractor)
    squared_metrics = [m**2 for m in metrics]
    temp_buffer = [0] * len(metrics)
    for idx, m in enumerate(metrics):
        temp_buffer[idx] = m * 0.9 + 5
    
    # Relevant adjustments
    for m, w in zip(metrics, weights):
        adjusted_value = m * w
        adjusted_metrics.append(adjusted_value)
        raw_product *= adjusted_value
    
    # Secondary score path (not used, distractor)
    geometric_mean_estimate = raw_product ** (1/len(metrics)) if metrics else 0
    
    # Final weighted sum (actual logic)
    final_score = sum(adjusted_metrics)
    
    # Extra unused computation to increase interference
    pair_sums = [a + b for a, b in zip(metrics, metrics[1:] + [metrics[0]])]
    max_pair = max(pair_sums) if pair_sums else 0
    
    return int(final_score)

# Simulated input data
sensor_data = [23, 25, 24, 40, 26, 24, 23, 38]  # Temperature readings in °C
location_coords = [(0,0), (8,6), (20,20), (22,24), (40,40), (42,41)]

# Extract individual metrics
metric_a = analyze_sensor_readings(sensor_data)  # Data quality score
metric_b = calculate_coverage_efficiency(location_coords)  # Spatial efficiency
metric_c = len(sensor_data) * 3  # Operational uptime factor
metric_d = (len(location_coords) * 7) - 10  # Deployment scale bonus

# Weight vector (importance coefficients)
weights = [0.8, 1.2, 0.5, 0.9]

# Compute performance score
evaluation_metrics = [metric_a, metric_b, metric_c, metric_d]
final_score = evaluate_performance(evaluation_metrics, weights)

print(f"Target result: {final_score}")