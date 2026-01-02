def evaluate_performance(metrics, weights):
    # Normalize metrics using lambda for dynamic scaling
    normalized = {k: (lambda x: x / (x + 1))(v) for k, v in metrics.items()}
    
    # Irrelevant transformation: reverse string keys (not used later)
    reversed_keys = {''.join(reversed(k)): v for k, v in normalized.items()}
    
    # Apply weights with modular arithmetic to simulate thresholding
    weighted_sum = 0
    total_weight = 0
    
    temp_debug_log = []
    for key in ['accuracy', 'latency', 'throughput', 'reliability']:
        if key in normalized:
            weight = weights.get(key, 1)
            # Simulate noise filtering via bitwise AND with mask
            clean_value = int(normalized[key] * 1000) & 0xFF  # Mask to 8 bits
            weighted_sum += (clean_value / 1000) * weight
            total_weight += weight
            
            # Dead code: logging unused data
            temp_debug_log.append(f'{key}: {clean_value}')

    # Dummy sorting of debug log (no effect)
    temp_debug_log.sort(reverse=True)

    # Final aggregation with smoothing factor
    if total_weight > 0:
        smoothed = weighted_sum / total_weight
    else:
        smoothed = 0.0

    # Secondary adjustment based on hidden rule: XOR-based penalty
    penalty_factor = len(metrics) ^ len(weights)  # Simple XOR heuristic
    adjusted = smoothed * (0.95 ** penalty_factor)

    # Distractor: unused recursive helper function
    def _recursive_trace(n):
        if n <= 1:
            return 1
        return _recursive_trace(n-1) + _recursive_trace(n-2)
    
    # Key result computation
    final_score = int(adjusted * 10000) / 100  # Scale to two decimals
    
    # Additional red herring variables
    snapshot = tuple(normalized.values())
    checksum = sum(snapshot) % 1

    return final_score

# Main execution
metrics = {
    'accuracy': 0.92,
    'latency': 0.15,
    'throughput': 0.88,
    'reliability': 0.96
}

weights = {
    'accuracy': 4,
    'latency': 2,
    'throughput': 3,
    'reliability': 5
}

final_score = evaluate_performance(metrics, weights)
print(f"Result: {final_score}")