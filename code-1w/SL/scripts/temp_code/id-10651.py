import itertools

# Simulated performance metrics from different subsystems
def collect_metrics():
    raw_data = [85, 90, 78, 92, 88, 76, 95, 89]
    adjustments = [0.98, 1.02, 0.95, 1.05, 0.99, 1.01, 0.97, 1.03]
    adjusted = [raw_data[i] * adjustments[i] for i in range(len(raw_data))]
    
    # Irrelevant transformation - red herring
    transformed = []
    for x in adjusted:
        if x > 90:
            transformed.append(x ** 0.5 * 2)
        else:
            transformed.append(x / 2)
    
    # Decoy function call with no effect
    def normalize(data):
        m = max(data)
        return [d / m for d in data]
    
    # Actual relevant processing
    filtered = [val for val in adjusted if val >= 80]
    averages = [sum(filtered) / len(filtered)] * len(filtered)
    
    # Misleading intermediate score
    phantom_score = sum(transformed) / len(transformed)
    
    return adjusted, filtered, averages

# Weight calculation with distractors
def compute_weights():
    base_weights = [1, 2, 3, 4]
    shift = 0.1
    
    # Complex but irrelevant weight shifting
    shifted = [(w + shift) ** 2 for w in base_weights]
    normalized_shifted = [s / sum(shifted) for s in shifted]
    
    # Dead code path - never used
    if len(normalized_shifted) > 5:
        scaled = [w * 10 for w in normalized_shifted]
    else:
        dummy = [w * 0 for w in normalized_shifted]  # Unused
    
    # Relevant weights computed via alternate route
    entropy_weights = [0.25, 0.25, 0.25, 0.25]  # Uniform importance
    noise = [0.01, -0.01, 0.02, -0.02]
    final_weights = [max(0.1, min(0.9, entropy_weights[i] + noise[i])) for i in range(len(entropy_weights))]
    
    return final_weights, normalized_shifted  # Only first is used

# Core aggregation logic with nested operations
def aggregate_performance(metrics, weights):
    extended_metrics = []
    
    # Use of enumerate and zip - required Python feature
    for idx, (m, w) in enumerate(zip(metrics, itertools.cycle(weights))):
        if idx % 2 == 0:
            extended_metrics.append(m * w * 1.1)
        else:
            extended_metrics.append(m * w * 0.9)
    
    # Redundant smoothing pass
    smoothed = []
    for i, val in enumerate(extended_metrics):
        if i == 0 or i == len(extended_metrics) - 1:
            smoothed.append(val)
        else:
            neighbor_avg = (extended_metrics[i-1] + extended_metrics[i+1]) / 2
            smoothed.append((val + neighbor_avg) / 2)
    
    # Key computation buried in distractions
    base_total = sum(smoothed)
    
    # Distractor: complex formula that isn't actually used
    def calculate_harmonic_score(vals):
        inv_sum = sum(1 / (v + 1e-8) for v in vals)
        return len(vals) / inv_sum
    
    # Another decoy metric
    peak_deviation = max(smoothed) - min(smoothed)
    adjustment_factor = 1.0
    if peak_deviation > 20:
        adjustment_factor = 0.95
    elif peak_deviation < 5:
        adjustment_factor = 1.05
    
    # Final score calculated here — this is the real answer
    final_score = base_total * adjustment_factor
    
    # Multiple print statements to obscure the target
    print(f'Debug - Phantom score: {calculate_harmonic_score(smoothed):.4f}')
    print(f'Tracking - Peak deviation: {peak_deviation:.2f}')
    print(f'Status - Adjustment factor applied: {adjustment_factor:.2f}')
    
    return final_score

# Main execution flow
if __name__ == '__main__':
    # Collect data
    all_metrics, valid_metrics, rolling_averages = collect_metrics()
    
    # Compute weighting scheme
    weights, decoy_weights = compute_weights()
    
    # Perform final aggregation
    # What is the value of variable 'final_score' after executing this statement?
    final_score = aggregate_performance(valid_metrics, weights)
    
    # Output result
    print(f'Result: {final_score}')