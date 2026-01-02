from collections import defaultdict
import math

def analyze_trend(data, threshold=0.1):
    trend_changes = 0
    for i in range(1, len(data)):
        if abs(data[i] - data[i-1]) > threshold:
            trend_changes += 1
    return trend_changes

def compute_entropy(values):
    total = sum(values)
    if total == 0:
        return 0.0
    probabilities = [v / total for v in values if v > 0]
    entropy = -sum(p * math.log(p) for p in probabilities)
    return round(entropy, 4)

def evaluate_performance(weights, outcomes):
    weighted_sum = 0.0
    normalization = 0.0
    temp_debug = defaultdict(int)
    
    # Irrelevant tracking (distractor)
    for k in weights:
        temp_debug[k] += 1
    
    adjustment_factor = 1.0
    if len(outcomes) > 3:
        adjustment_factor = 0.95  # Minor distortion
    
    # Core logic
    for key in weights:
        if key in outcomes:
            contribution = weights[key] * outcomes[key]
            weighted_sum += contribution
            normalization += weights[key]
    
    # Dead code path (misleading)
    fallback_mode = False
    if normalization < 0.5:
        fallback_mode = True
        weighted_sum = 10  # Never reached due to data
    
    base_score = weighted_sum / normalization if normalization != 0 else 0
    
    # Apply irrelevant transformation
    squared_chain = [base_score]
    for _ in range(2):
        squared_chain.append(squared_chain[-1] ** 2)
    
    # Final computation
    entropy_proxy = compute_entropy(list(outcomes.values()))
    final_score = int(base_score * adjustment_factor + entropy_proxy)
    
    return final_score

# Simulated input data
metric_weights = {
    'precision': 0.4,
    'recall': 0.3,
    'latency': 0.2,
    'throughput': 0.1
}

raw_outcomes = {
    'precision': 0.85,
    'recall': 0.75,
    'latency': 0.6,
    'throughput': 0.9
}

# Extraneous list processing (distractor)
data_series = [0.1, 0.12, 0.2, 0.25, 0.3]
trend_count = analyze_trend(data_series, threshold=0.05)

# Key execution point
final_score = evaluate_performance(metric_weights, raw_outcomes)

# Output result
print(f"Result: {final_score}")