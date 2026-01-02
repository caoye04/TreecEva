from itertools import combinations

def analyze_trends(data, threshold=3):
    trends = []
    for i in range(1, len(data)):
        if data[i] - data[i-1] > threshold:
            trends.append((i-1, i))
    return trends

def calculate_entropy(values):
    total = sum(values)
    if total == 0:
        return 0.0
    probs = [v / total for v in values]
    entropy = -sum(p * __import__('math').log2(p) for p in probs if p > 0)
    return round(entropy, 4)

def evaluate_performance(metrics, weights):
    weighted_sum = sum(m * w for m, w in zip(metrics, weights))
    adjustment_factor = 1.0
    
    # Irrelevant entropy calculation (distractor)
    entropy = calculate_entropy(metrics)
    temp_data = [x * 2 for x in metrics if x > 5]  # Unused list comprehension
    
    # Misleading trend analysis on unrelated transformation
    scaled_metrics = [int(m * 10) for m in metrics]
    detected_trends = analyze_trends(scaled_metrics)
    if len(detected_trends) > 1:
        adjustment_factor *= 0.9
    
    # Core logic: apply weight normalization only if certain condition met
    norm_weights = [w / sum(weights) for w in weights]
    normalized_contribution = sum(m * nw for m, nw in zip(metrics, norm_weights))
    
    # Bitwise interference (semi-relevant but doesn't affect final path)
    flag = 0b1010
    if sum(metrics) & 1:  # Check if sum is odd
        flag ^= 0b1111
    
    # Final score computation — this is what matters
    base_score = weighted_sum * normalized_contribution
    final_score = int(base_score + 0.5)  # Round to nearest integer
    
    # Dead code branch (never executed due to fixed input properties)
    if False and any(w < 0 for w in weights):
        backup = max(metrics) * min(weights)
        final_score = backup
    
    return final_score

# Main execution
metrics = [8, 7, 9, 6]
weights = [0.4, 0.3, 0.2, 0.1]

# Preprocessing distraction: set operations with no impact
unique_metrics = set(metrics)
duplicated = {x for x in metrics if metrics.count(x) > 1}

# Generate unused combination pairs
metric_pairs = list(combinations(metrics, 2))

# Key statement
final_score = evaluate_performance(metrics, weights)
print(f"Result: {final_score}")