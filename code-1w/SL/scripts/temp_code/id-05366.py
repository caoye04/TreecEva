from collections import defaultdict
import math

# Simulate system performance metrics over time
def collect_metrics():
    data = [120, 85, 90, 75, 110]
    timestamps = [1, 2, 3, 4, 5]
    
    # Misleading intermediate processing
    avg_latency = sum(data) / len(data)
    peak = max(data)
    normalized = [(x - min(data)) / (max(data) - min(data)) * 100 for x in data]
    
    metrics = defaultdict(float)
    metrics['response_time'] = sum(data) / len(data)
    metrics['stability'] = len([x for x in zip(data, data[1:]) if abs(x[0] - x[1]) < 10])
    metrics['trend'] = sum(normalized[:3]) - sum(normalized[3:])
    
    # Unused distractor values
    temp_correction = 0.987
    baseline_offset = 5.2
    debug_trace = [math.sin(i) for i in range(len(data))]
    
    return metrics

# Weighting logic with red herring components
def generate_weights():
    base_weights = {'response_time': 0.5, 'stability': 0.3}
    
    # Irrelevant computation path
    adjustment_factor = 1.0
    for i in range(2):
        adjustment_factor *= 0.99 + (i * 0.01)
    
    # Distractor variables
    legacy_scale = 0.88
    deprecated_flag = True
    temp_map = {k: v * adjustment_factor for k, v in base_weights.items()}
    
    weights = defaultdict(float)
    weights['response_time'] = base_weights['response_time']
    weights['stability'] = base_weights['stability']
    weights['trend'] = 0.2  # New metric added
    
    # Unused normalization
    total = sum(weights.values())
    normalized_weights = {k: v / total for k, v in weights.items()}
    
    return weights

# Core evaluation function
def evaluate_performance(metrics, weights):
    score = 0.0
    
    # Main scoring logic
    for key in weights:
        if key == 'response_time':
            # Inverse relationship: lower response time → higher score
            score += (100 / metrics[key]) * weights[key]
        elif key == 'stability':
            score += metrics[key] * 10 * weights[key]
        elif key == 'trend':
            # Positive trend improves score
            adjusted_trend = max(0, metrics[key] + 50)  # Shift baseline
            score += (adjusted_trend / 100) * 100 * weights[key]
    
    # Dead code branch - never executed due to current inputs
    if 'reliability' in metrics:
        score += metrics['reliability'] * weights['reliability']
    
    # Final transformation
    final_adjustment = lambda x: round(x, 2)
    return final_adjustment(score)

# Execution flow
if __name__ == "__main__":
    metrics = collect_metrics()
    weights = generate_weights()
    
    # Key statement
    final_score = evaluate_performance(metrics, weights)
    
    # Print result as required
    print(f"Result: {final_score}")