from collections import defaultdict
import math

# Simulate system health metrics over time
def collect_metrics():
    raw_data = [120, 85, 90, 95, 110, 130, 100]
    timestamps = list(range(len(raw_data)))
    
    # Irrelevant transformation (distractor)
    normalized = [round((x - min(raw_data)) / (max(raw_data) - min(raw_data)) * 100) for x in raw_data]
    
    metrics = defaultdict(float)
    metrics['peak'] = max(raw_data)
    metrics['baseline'] = sum(raw_data) / len(raw_data)
    metrics['volatility'] = sum(abs(raw_data[i] - raw_data[i-1]) for i in range(1, len(raw_data))) / len(raw_data)
    metrics['trend'] = (raw_data[-1] - raw_data[0]) / len(raw_data)
    
    # Unused metric (dead code path)
    if metrics['trend'] > 0:
        metrics['growth_potential'] = 1.5
    else:
        metrics['growth_potential'] = 0.5
    
    return metrics

# Weighting strategy with historical bias adjustment
def get_weights(metrics):
    base_weights = {'peak': 0.2, 'baseline': 0.4, 'volatility': -0.3, 'trend': 0.1}
    adjustment_factor = 0.1 if metrics['peak'] > 100 else 0
    
    # Complex but partially irrelevant adjustment
    temp_shift = [abs(math.sin(i * 0.1)) for i in range(5)]
    decay = sum(temp_shift) / 5
    
    adjusted = defaultdict(float)
    for k, v in base_weights.items():
        adjusted[k] = v + adjustment_factor * 0.5 if k in ['baseline', 'trend'] else v
    
    # Dead computation: unused lambda
    transform = lambda x: x ** 2 if x > 0 else 0
    _ = [transform(x) for x in temp_shift]
    
    return adjusted

# Core evaluation logic
def evaluate_performance(metrics, weights):
    score = 0.0
    components = []
    
    for k in weights:
        if k == 'volatility':
            # Invert volatility impact
            contribution = -abs(metrics[k]) * abs(weights[k])
        else:
            contribution = metrics[k] * weights[k]
        components.append(round(contribution, 4))
    
    # Real logic: sum only specific contributions
    score += sum(components)
    
    # Distractor: slicing operation on intermediate result
    mid_results = components[1:3]
    _ = sum(mid_results) * 0.5  # Not used
    
    # Additional red herring calculation
    outlier_check = [c for c in components if c > 10]
    if outlier_check:
        score -= 0.5
    
    return round(score, 4)

# Execution flow
metrics = collect_metrics()
weights = get_weights(metrics)
final_score = evaluate_performance(metrics, weights)

# Target result output
print(f"Result: {final_score}")