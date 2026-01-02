from collections import defaultdict
from itertools import combinations

# Simulate system performance metrics across different modules
def collect_diagnostics():
    raw_data = [120, 85, 90, 77, 110, 95]
    diagnostics = defaultdict(int)
    
    for i, val in enumerate(raw_data):
        diagnostics[f'module_{i}'] = val * 0.8 if val > 80 else val * 0.9
    
    # Irrelevant transformation (distractor)
    temp_adjustment = sum(diagnostics.values()) / len(diagnostics) * 0.05
    
    return dict(diagnostics)

# Weighting strategy based on module criticality
def get_weight_profile():
    base_weights = {'module_0': 1.2, 'module_1': 0.9, 'module_2': 1.1, 'module_3': 0.8,
                    'module_4': 1.3, 'module_5': 1.0}
    
    # Generate unused combination set (distractor)
    unused_pairs = list(combinations(base_weights.keys(), 2))
    
    adjusted_weights = {k: w * 1.05 for k, w in base_weights.items()}
    return adjusted_weights

# Evaluate overall system performance
def evaluate_performance(metrics, weights):
    weighted_sum = 0.0
    total_weight = 0.0
    
    # Secondary tracking variables (some not used)
    peak_value = max(metrics.values())
    normalized_metrics = {k: v / peak_value for k, v in metrics.items()}
    
    for key in metrics:
        if key in weights:
            contribution = normalized_metrics[key] * weights[key]
            weighted_sum += contribution
            total_weight += weights[key]
    
    # Compute final score using weighted average
    final_score = weighted_sum / total_weight if total_weight > 0 else 0
    
    # Dead code path (distractor)
    if False:
        fallback = sum(normalized_metrics.values()) / len(normalized_metrics)
        final_score = fallback
    
    return final_score

# Main execution flow
def main():
    metrics = collect_diagnostics()
    weights = get_weight_profile()
    
    # Intermediate diagnostic calculation (not used in final result)
    avg_metric = sum(metrics.values()) / len(metrics)
    adjusted_avg = avg_metric * 0.95
    
    final_score = evaluate_performance(metrics, weights)
    print(f"Result: {final_score}")

if __name__ == "__main__":
    main()