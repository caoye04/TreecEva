import math

def analyze_signal(samples):
    # Irrelevant signal processing function (dead end)
    fft_magnitude = [abs(s) ** 2 for s in samples]
    return sum(fft_magnitude) / len(fft_magnitude)

def compute_entropy(data):
    # Distractor: computes entropy but not used in final path
    total = sum(data)
    probs = [d / total for d in data if d > 0]
    return -sum(p * math.log2(p) for p in probs)

def transform_coordinates(coords):
    # Complex but irrelevant transformation
    result = []
    for i, (x, y) in enumerate(coords):
        rotated_x = x * math.cos(math.pi / 4) - y * math.sin(math.pi / 4)
        rotated_y = x * math.sin(math.pi / 4) + y * math.cos(math.pi / 4)
        result.append((rotated_x + i, rotated_y - i))
    return result

def simulate_propagation(network, delay=0.15):
    # Unused simulation with decoy parameters
    for _ in range(3):
        network = [(n[0] * 0.9, n[1] * 1.1) for n in network]
    return network

def normalize_vector(v):
    norm = math.sqrt(sum(x * x for x in v))
    return [x / norm for x in v] if norm != 0 else v

def evaluate_metric(value, threshold, weight):
    return weight * (1 if value >= threshold else 0.5)

def evaluate_performance(weights, data):
    # Core logic buried in distractions
    base_metrics = []
    
    # Real computation begins here
    throughput = data['throughput']
    latency = data['latency']
    errors = data['errors']
    
    # Actual conditions affecting final score
    metric_1 = evaluate_metric(throughput, 850, weights[0])
    metric_2 = evaluate_metric(latency, 120, weights[1])
    metric_3 = evaluate_metric(errors, 5, weights[2])
    
    # Hidden logical dependency
    adjustment_factor = 1.0
    if latency < 100:
        adjustment_factor *= 1.1
    if errors <= 3:
        adjustment_factor *= 1.05
    
    raw_score = metric_1 + metric_2 + metric_3
    
    # Red herring: entropy-based penalty (never actually applied)
    dummy_penalty = compute_entropy([int(throughput), int(latency)])
    
    # Another distraction: coordinate shift (computed but unused)
    temp_coords = [(throughput / 100, latency / 10), (errors, 1)]
    transformed = transform_coordinates(temp_coords)
    
    # Final calculation
    final_score = raw_score * adjustment_factor
    
    # Dead branch: looks important but never reached due to logic
    if False and analyze_signal([1, 0, 1, 1]) > 0.5:
        final_score *= 0.9
        
    return final_score

# Main execution
if __name__ == '__main__':
    # Irrelevant initial data
    sensor_readings = [0.1, 0.4, 0.9, 0.2, 0.8]
    coordinate_grid = [(1, 2), (3, 4), (5, 6)]
    propagation_network = [(1.0, 2.0), (0.5, 1.5)]
    
    # Unused intermediate results
    _ = analyze_signal(sensor_readings)
    _ = simulate_propagation(propagation_network)
    _ = transform_coordinates(coordinate_grid)
    
    # Key data structure
    system_data = {
        'throughput': 920,
        'latency': 95,
        'errors': 2
    }
    
    # Weight vector - critical input
    metric_weights = [2.0, 3.0, 4.0]
    
    # Normalize weights using lambda and zip (required features)
    normalized_weights = list(map(lambda w: w / sum(metric_weights), metric_weights))
    weight_map = dict(zip(['t', 'l', 'e'], normalized_weights))
    
    # Enumerate over something irrelevant
    labels = ['A', 'B', 'C']
    for idx, label in enumerate(labels):
        weight_map[label.lower()] = idx * 0.1
    
    # Normalize main data (actual relevant preprocessing)
    total_tle = system_data['throughput'] + system_data['latency'] + system_data['errors']
    normalized_data = {k: v / total_tle for k, v in system_data.items()}
    
    # This normalization doesn't affect final result - red herring
    normalized_data['throughput'] = normalize_vector([system_data['throughput'], 100])[0]
    
    # Critical statement
    final_score = evaluate_performance(metric_weights, system_data)
    
    # Print result
    print(f"Target result: {final_score}")