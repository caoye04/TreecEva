import math

def analyze_efficiency(data, threshold=0.75):
    """Irrelevant helper function for distraction."""
    return sum(1 for x in data if x > threshold) / len(data)

def transform_value(x):
    """Apply non-linear transformation (used in one distractor)."""
    return math.log(1 + x) * 2.718

def evaluate_performance(metrics, weights):
    # Core logic starts here — relevant code path
    base = 0
    adjustment = 0
    
    # Distractor: complex-looking but unused calculation
    temp_data = [transform_value(x) for x in metrics.values()]
    irrelevant_ratio = analyze_efficiency(temp_data)
    
    # Real logic: conditional weighting with dictionary operations
    weighted_sum = sum(metrics[key] * weights[key] for key in weights)
    total_weight = sum(weights.values())
    average = weighted_sum / total_weight
    
    # Bitwise interference — misleading use of bit operations
    magic_flag = 0b1010 ^ 0b1100 & 0b0011
    if magic_flag == 1:
        average = average << 1  # This branch never executes
    
    # Conditional branches affecting final score
    if average > 80:
        base = 95
    elif average > 60:
        base = 75
    else:
        base = 50
    
    # Lambda-based dynamic bonus calculation — actually used
    bonus_calculator = lambda x: int(x * 0.1) if x < 100 else 10
    bonus = bonus_calculator(base)
    
    # State tracking with decoy list accumulation
    history = []
    for i in range(3):
        history.append({'step': i, 'value': base + i*2})  # Dead code — not used
    
    # Final adjustment based on composite condition
    compliance = metrics.get('accuracy', 0) >= 0.85
    activity = metrics.get('engagement', 0) > 0.5
    stability = metrics.get('variance', 1) < 0.2
    
    # Complex boolean logic with short-circuiting — affects adjustment
    if compliance and (activity or stability) and (stability or not activity):
        adjustment = 12
    elif compliance or activity:
        adjustment = 5
    else:
        adjustment = 0
    
    # Critical assignment — answer depends on this
    final_score = base + bonus + adjustment
    
    # Unused variables to increase interference
    dummy_mask = 0xFF & 0x0A | 0x3
    shadow_sum = sum(math.sin(i) for i in range(5))
    placeholder = {'temp': math.exp(1), 'flag': False}
    
    return final_score

# Main execution block
if __name__ == "__main__":
    # Input data
    metrics = {
        'accuracy': 0.88,
        'engagement': 0.62,
        'latency': 0.15,
        'throughput': 120.5,
        'variance': 0.18
    }
    
    weights = {
        'accuracy': 0.4,
        'engagement': 0.3,
        'latency': 0.2,
        'throughput': 0.1
    }
    
    # Distractor: unused transformed values
    processed_metrics = {k: transform_value(v) for k, v in metrics.items()}
    
    # Key statement: determines final_score
    final_score = evaluate_performance(metrics, weights)
    
    # Output result as required
    print(f"Result: {final_score}")