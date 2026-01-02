from collections import defaultdict

# Simulate system metrics over time
def collect_metrics():
    raw_data = [78, 85, 90, 65, 88, 92, 75]
    adjustments = [1.05, 0.98, 1.02, 0.94, 1.01, 1.03, 0.97]
    adjusted = [raw_data[i] * adjustments[i] for i in range(len(raw_data))]
    
    # Irrelevant transformation (distractor)
    squared_deltas = [(adjusted[i] - raw_data[i])**2 for i in range(len(raw_data))]
    avg_square_delta = sum(squared_deltas) / len(squared_deltas)
    
    metric_dict = defaultdict(float)
    metric_dict['avg_adjusted'] = sum(adjusted) / len(adjusted)
    metric_dict['peak'] = max(adjusted)
    metric_dict['volatility'] = sum(abs(adjusted[i] - adjusted[i-1]) for i in range(1, len(adjusted)))
    
    return metric_dict

# Weighting logic with conditional expressions
def define_weights(volatility_factor):
    base_weights = {'avg_adjusted': 0.6, 'peak': 0.3}
    extra_weight = 0.1 if volatility_factor < 10 else 0.05
    bonus_shift = 0.02 * (1 if base_weights['peak'] > 0.25 else 0)
    
    # Dead code path (distractor)
    if bonus_shift > 0.1:
        scaling_factor = 1.1
    else:
        scaling_factor = 1.0  # Never actually used
    
    base_weights['volatility_penalty'] = extra_weight - bonus_shift
    return base_weights

# Evaluation using lambda and complex logic
evaluate_performance = lambda m, w: (
    w['avg_adjusted'] * m['avg_adjusted'] + 
    w['peak'] * m['peak'] - 
    w['volatility_penalty'] * m['volatility']
)

# Main execution flow
metrics = collect_metrics()

# Intermediate irrelevant calculation (distractor)
temp_normalization = sum(metrics[k] for k in ['avg_adjusted', 'peak']) / 2
offset_correction = (temp_normalization * 0.01) ** 2

weights = define_weights(metrics['volatility'])

# Key statement
final_score = evaluate_performance(metrics, weights)

print(f"Result: {final_score}")