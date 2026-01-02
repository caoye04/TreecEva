from collections import defaultdict

# Simulate system performance metrics over time
def collect_metrics():
    raw_data = [120, 135, 140, 128, 155, 160, 145]
    timestamps = [1, 2, 3, 4, 5, 6, 7]
    
    # Irrelevant transformation
    normalized = [x / max(raw_data) for x in raw_data]
    
    metrics = defaultdict(float)
    metrics['peak'] = max(raw_data)
    metrics['baseline'] = raw_data[0]
    metrics['trend'] = sum(raw_data[i] - raw_data[i-1] for i in range(1, len(raw_data)))
    metrics['stability'] = sum(1 for x in raw_data if x > 130)
    metrics['jitter'] = sum(abs(raw_data[i] - raw_data[i-1]) for i in range(1, len(raw_data)))
    
    # Distractor computation - not used later
    avg_normalized = sum(normalized) / len(normalized)
    penalty_factor = 0.9 if avg_normalized < 0.9 else 1.0
    
    return metrics

# Weight assignment with red herring alternatives
def define_weights():
    weight_map = {}
    weight_map['peak'] = 0.3
    weight_map['baseline'] = 0.1
    weight_map['trend'] = 0.25
    weight_map['stability'] = 0.2
    weight_map['jitter'] = -0.15  # Negative weight: higher jitter reduces score
    
    # Unused alternative schemes (dead code path)
    alt_scheme_a = {'peak': 0.4, 'trend': 0.3, 'stability': 0.3}
    alt_scheme_b = defaultdict(lambda: 0.2)
    
    return weight_map

# Core evaluation logic
def evaluate_performance(metrs, wts):
    score = 0.0
    debug_values = []
    
    # Apply weighted sum using only specific keys
    for key in ['peak', 'trend', 'stability', 'jitter']:
        if key in wts:
            contribution = metrs[key] * wts[key]
            score += contribution
            debug_values.append(contribution)
    
    # Secondary adjustment based on threshold logic
    if metrs['peak'] > 150:
        bonus = 5.0
        # Misleading unused bonus types
        conditional_bonus = 3.0 if metrs['stability'] > 4 else 0
        tiered_bonus = 10.0 if metrs['trend'] > 50 else 5.0
        score += bonus
    
    # Extra noise calculation (irrelevant)
    efficiency_ratio = metrs['stability'] / len(debug_values) if debug_values else 0
    
    return int(score)  # Final discretization

# Main execution flow
if __name__ == "__main__":
    # Collect observed behavior
    collected = collect_metrics()
    
    # Configure weighting strategy
    weights = define_weights()
    
    # Compute final composite score
    final_score = evaluate_performance(collected, weights)
    
    # Print result as required
    print(f"Target result: {final_score}")