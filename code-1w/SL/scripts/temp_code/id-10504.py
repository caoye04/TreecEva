import itertools

# Simulated sensor data processing pipeline for environmental monitoring station
def analyze_readings(readings):
    filtered = [x for x in readings if 10 <= x <= 100]
    smoothed = [sum(filtered[i:i+3]) / 3 for i in range(len(filtered) - 2)]
    return smoothed if smoothed else [0]

# Irrelevant auxiliary function - dead code path
def compute_entropy(data):
    from math import log
    freq = {}
    for d in data:
        freq[d] = freq.get(d, 0) + 1
    total = len(data)
    entropy = -sum((count / total) * log(count / total) for count in freq.values())
    return round(entropy, 4)

# Data calibration with red herring transformations
def calibrate_sensor_data(raw_values):
    offset = 2.5
    calibrated = [v + offset for v in raw_values]
    # Distractor: complex but unused transformation
    transformed = list(itertools.accumulate(calibrated, lambda a, b: (a * b) % 17))
    scaled = [c * 0.98 for c in calibrated]
    normalized = [s / max(scaled) * 100 for s in scaled]
    return normalized

# Core logic with meaningful computation buried in distractions
def evaluate_stability(profiles):
    baseline = [78, 85, 76, 80, 88]
    deviations = []
    for p in profiles:
        diff = sum(abs(b - p[i]) for i, b in enumerate(baseline[:len(p)]))
        deviations.append(diff)
    avg_dev = sum(deviations) / len(deviations) if deviations else 0
    stability_index = 100 - avg_dev
    return round(stability_index, 2)

# Misleading combinatorics distraction
def generate_combinations(items):
    combos = []
    for r in range(1, len(items)+1):
        combos.extend(itertools.combinations(items, r))
    return [(sum(c), len(c)) for c in combos]  # Never used

# Main evaluation workflow with decoy variables and paths
def aggregate_performance(metrics, weights):
    # Critical path starts here
    weighted_sum = 0
    max_weight = 0
    
    # Decoy variables and misleading calculations
    temp_results = []
    cumulative_product = 1
    for m in metrics:
        temp_results.append(m ** 2)
        cumulative_product *= (m % 10 + 1)
    
    # Real logic mixed with noise
    for i, (metric, weight) in enumerate(zip(metrics, weights)):
        if i % 2 == 0:
            weighted_sum += metric * weight * 1.1  # Adjustment factor
        else:
            weighted_sum += metric * weight * 0.9
        max_weight = max(max_weight, weight)
    
    # Final adjustment using non-linear transformation
    adjustment_factor = (max_weight / len(metrics)) ** 0.5
    preliminary_score = weighted_sum * adjustment_factor
    
    # Secondary correction based on stability metric (buried dependency)
    stability_metric = evaluate_stability([metrics[:3], metrics[1:4]])
    final_correction = stability_metric / 100
    
    # Answer is determined here
    final_score = int(preliminary_score * final_correction)
    
    # More red herrings
    summary_stats = {
        'peak': max(temp_results, default=0),
        'product_trace': cumulative_product % 1000,
        'combo_count': len(generate_combinations(metrics))
    }
    
    return final_score

# Execution entry point with irrelevant setup
if __name__ == '__main__':
    raw_sensor_data = [75, 82, 79, 84, 81, 77, 83]
    processed = analyze_readings(raw_sensor_data)
    calibrated = calibrate_sensor_data(processed)
    
    # Decoy data structures
    entropy_data = [1, 1, 2, 2, 3, 3, 4]
    entropy_value = compute_entropy(entropy_data)
    
    # Actual input to target function
    metrics = [88.4, 76.2, 91.5, 83.7, 79.1]
    weights = [4, 3, 5, 2, 4]
    
    # Key statement
    final_score = aggregate_performance(metrics, weights)
    
    # Print result as required
    print(f"Result: {final_score}")