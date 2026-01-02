import math

# Simulated system metrics from a distributed computing environment
def collect_metrics():
    raw_data = [89.5, 76.3, 92.1, 65.4, 80.0, 94.7, 73.2]
    normalization_factor = 1.05
    adjusted = [min(x * normalization_factor, 100) for x in raw_data]  # List comprehension

    # Irrelevant transformations (distractors)
    inverted = [100 - val for val in adjusted]
    squared_devs = [(x - 85)**2 for x in adjusted]
    avg_inverted = sum(inverted) / len(inverted)
    penalty_offset = math.sin(avg_inverted / 10)  # Red herring

    return adjusted

# Weighting strategy based on component criticality
def calculate_weights(n):
    base_weights = [0.1, 0.2, 0.15, 0.25, 0.1, 0.05, 0.1]
    decay_factor = 0.95
    time_decay = [base_weights[i] * (decay_factor ** i) for i in range(n)]
    total = sum(time_decay)
    normalized = [w / total for w in time_decay]

    # Dead code path - never used
    if total < 0:
        normalized = [w * 2 for w in normalized]

    # Irrelevant alternate weighting
    uniform = [1/n] * n
    priority_boost = normalized[3] * 1.5  # Misleading focus on index 3

    return normalized

# Legacy function - not used but looks important
def legacy_aggregate(data):
    weighted_sum = 0
    for i in range(len(data)):
        weighted_sum += data[i] * (0.1 + i * 0.01)
    return weighted_sum / len(data) * 1.2

# Core logic with distractors
def validate_inputs(metrics, weights):
    if len(metrics) != len(weights):
        raise ValueError("Mismatched dimensions")
    if any(w < 0 for w in weights):
        return False
    if sum(weights) < 0.8:  # Irrelevant threshold check
        pass  # Dead logic
    return True

# Aggregation with red herrings
def aggregate_performance(metrics, weights):
    # Pre-validation
    if not validate_inputs(metrics, weights):
        return -1
    
    # Key computation
    weighted_sum = sum(m * w for m, w in zip(metrics, weights))
    
    # Distracting transformations
    max_metric = max(metrics)
    min_metric = min(metrics)
    range_penalty = (max_metric - min_metric) * 0.05
    
    # Multiple intermediate variables to obscure flow
    temp_result = weighted_sum - range_penalty
    adjustment_factor = math.log(1 + weighted_sum / 100)  # Looks important
    boosted = temp_result * adjustment_factor
    
    # Conditional dead end
    if temp_result > 100:
        boosted = 100 + math.sqrt(temp_result - 100)
    
    # Final clamping (not actually needed due to input bounds)
    final_value = max(0, min(boosted, 100))
    
    # Critical result stored here
    final_score = int(round(final_value))
    
    # Decoy output variables
    auxiliary_score = sum(metrics) / len(metrics) * 0.95
    normalized_peak = max_metric * weights[metrics.index(max_metric)]
    
    return final_score

# Orchestration with irrelevant setup
def main():
    # Simulate system telemetry collection
    system_uptime = 145.6  # hours
    node_count = 7
    failure_rate = 0.023
    
    # Real data path
    metrics = collect_metrics()
    weights = calculate_weights(len(metrics))
    
    # Fake diagnostic trace
    diagnostics = []
    for i, m in enumerate(metrics):
        if m < 70:
            diagnostics.append(f"Node {i} degraded")
    
    # Key execution point
    final_score = aggregate_performance(metrics, weights)
    
    # Unused complex structure
    report = {
        'summary': {
            'nodes': node_count,
            'avg_health': sum(metrics)/len(metrics),
            'critical_nodes': len([m for m in metrics if m < 70])
        },
        'weights_applied': weights[:],
        'timestamp': "2023-11-05T14:30:00Z"
    }
    
    # Only this line matters
    print(f"Result: {final_score}")

if __name__ == "__main__":
    main()