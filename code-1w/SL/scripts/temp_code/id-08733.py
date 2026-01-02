from collections import defaultdict
import math

# Simulate system health metrics from distributed nodes
def collect_metrics():
    raw_data = [120, 85, 90, 75, 110]
    processed = defaultdict(float)
    for i, val in enumerate(raw_data):
        processed[f'node_{i}'] = val * 0.95 if val > 80 else val * 0.85
    return dict(processed)

# Weighting strategy based on node criticality
def get_weights():
    base_weights = {'node_0': 0.1, 'node_1': 0.2, 'node_2': 0.3, 'node_3': 0.25}
    # Redundant computation (distractor)
    temp_sum = sum(base_weights.values())
    adjusted = {k: v + 0.01 for k, v in base_weights.items()}
    normalized = {k: v / sum(adjusted.values()) for k, v in adjusted.items()}
    return normalized  # Note: normalization has minor effect

# Core evaluation logic
def evaluate_performance(metrics, weights):
    total = 0.0
    penalty_factor = 1.0
    
    # Apply weighted scoring
    for node, score in metrics.items():
        if node in weights:
            total += score * weights[node]
    
    # Secondary adjustment based on stability threshold
    stability_ref = list(metrics.values())[0]
    if stability_ref > 100:
        penalty_factor = 0.95
    
    # Distractor: unused transformation
    transformed_scores = list(map(lambda x: math.sqrt(x) * 1.1, metrics.values()))
    avg_transformed = sum(transformed_scores) / len(transformed_scores)
    
    # Another distractor: bitwise check with no real impact
    flag_state = 0b1010 ^ 0b1100
    if flag_state == 0b0110:
        pass  # Intentional noop

    # Final score with penalty applied
    final = total * penalty_factor
    
    # Irrelevant sorting (dead code path)
    sorted_items = sorted(metrics.items(), key=lambda x: x[1], reverse=True)
    top_nodes = [item[0] for item in sorted_items[:2]]
    
    return final

# Execution flow
if __name__ == "__main__":
    # Collect performance data
    metrics = collect_metrics()
    
    # Retrieve weighting scheme
    weights = get_weights()
    
    # Compute final performance score
    final_score = evaluate_performance(metrics, weights)
    
    # Output result
    print(f"Result: {final_score}")