def compute_system_risk():
    # Simulate a network node trust evaluation system
    node_scores = [85, 90, 78, 92, 88]
    weights = [0.2, 0.3, 0.15, 0.25, 0.1]
    
    weighted_sum = sum(score * weight for score, weight in zip(node_scores, weights))
    base_threshold = 86.5
    adjustment_factor = 0.9 if weighted_sum < base_threshold else 1.1

    # Irrelevant intermediate calculation (distractor)
    temp_deviation = sum(abs(score - weighted_sum) for score in node_scores) / len(node_scores)
    normalized_deviation = temp_deviation / (max(node_scores) - min(node_scores)) if temp_deviation > 0 else 0

    # Core data structure: tracking ranks across dimensions
    rank_tracker = {
        'performance': int(weighted_sum),
        'stability': len([s for s in node_scores if s >= 85]),
        'connectivity': 4,
        'total': 0
    }

    # Update total rank using lambda transformation
    update_fn = lambda x: x * adjustment_factor
    rank_tracker['total'] = int(update_fn(rank_tracker['performance']) + rank_tracker['stability'])

    # Secondary distractor: simulate unused risk layers
    risk_layers = {'firewall': 3, 'encryption': 5, 'auth': 4}
    layer_score = sum(risk_layers.values()) // len(risk_layers)
    security_cap = min(layer_score * 2, 10)

    # Bonus logic based on connectivity-stability interaction
    if rank_tracker['stability'] > 3 and rank_tracker['connectivity'] >= 4:
        bonus_offset = 7
    else:
        bonus_offset = 2

    # Final computation with red herring variables nearby
    debug_trace = [f"Node {i}: {score}" for i, score in enumerate(node_scores)]
    metadata_log = {'version': '2.1', 'nodes_active': len(node_scores)}

    final_rank = rank_tracker.get('total', 0) + bonus_offset

    # Print required output
    print(f"Result: {final_rank}")

compute_system_risk()