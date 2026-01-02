from itertools import combinations


def analyze_trends(values, window_size):
    trend_scores = []
    for i in range(len(values) - window_size + 1):
        window = values[i:i + window_size]
        avg = sum(window) / len(window)
        variance = sum((x - avg) ** 2 for x in window) / len(window)
        trend_scores.append(avg - variance * 0.1)
    return max(trend_scores) if trend_scores else 0


def compute_entropy(data):
    from collections import Counter
    counts = Counter(data)
    total = len(data)
    entropy = 0
    for count in counts.values():
        p = count / total
        if p > 0:
            entropy -= p * (p ** 0.5)  # Simplified pseudo-entropy
    return round(entropy, 4)


def evaluate_performance(metrics, threshold):
    adjusted_metrics = [m * 1.1 for m in metrics if m > threshold]
    
    # Distractor: entropy calculation on scaled integer parts
    int_parts = [int(m * 2) for m in adjusted_metrics]
    _ = compute_entropy(int_parts)  # Unused result
    
    # Distractor: generate all pairs above a secondary threshold
    high_pairs = list(combinations([m for m in adjusted_metrics if m > threshold + 5], 2))
    pair_boost = len(high_pairs) * 0.05
    
    # Real logic path
    base_score = sum(adjusted_metrics)
    
    # Secondary adjustment based on trend analysis
    smoothed = [metrics[i] for i in range(0, len(metrics), 2)]  # Every other metric
    trend_component = analyze_trends(smoothed, 3) if len(smoothed) >= 3 else 0
    
    # Final score with distractor inclusion but non-dominant effect
    final_score = base_score + pair_boost + trend_component
    
    # Dead code branch (never reached due to structure)
    if False:
        fallback = sum(metrics) / len(metrics)
        final_score = fallback
        
    return final_score

# Main execution
raw_inputs = [85, 90, 78, 92, 88, 76, 95]
base_threshold = 80

# Irrelevant transformation chain
shifted_vals = [x + 2 for x in raw_inputs]
doubled_vals = [x * 2 for x in shifted_vals]
_ = [x - 1 for x in doubled_vals]  # Unused list

metric_data = [x - 70 for x in raw_inputs]  # Normalize baseline

# Key statement
final_score = evaluate_performance(metric_data, base_threshold)

print(f"Result: {final_score}")