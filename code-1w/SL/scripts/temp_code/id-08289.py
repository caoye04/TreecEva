def normalize(data):
    min_val, max_val = min(data), max(data)
    return [(x - min_val) / (max_val - min_val + 1e-8) for x in data]


def apply_penalty(x, threshold=0.5):
    # Irrelevant helper function - not used in final path
    return x * 0.9 if x < threshold else x

def case_convert(text_list):
    # Distractor: operates on strings, but main logic is numeric
    return [t.upper() if len(t) % 2 == 0 else t.lower() for t in text_list]

def calculate_entropy(values):
    # Semi-relevant: computed but not used in final score
    from math import log
    total = sum(values)
    if total == 0:
        return 0.0
    probs = [v / total for v in values]
    entropy = -sum(p * log(p + 1e-8) for p in probs)
    return round(entropy, 4)

def evaluate_performance(metrics, weights):
    normalized = normalize(metrics)
    
    # Intermediate distractor variables
    temp_data = [x ** 2 for x in metrics if x > 0.3]
    avg_temp = sum(temp_data) / len(temp_data) if temp_data else 0.0
    
    # String processing side-path (distractor)
    labels = ['MetricA', 'metricB', 'MetricC', 'metricD']
    processed_labels = case_convert(labels)
    label_hash = sum(ord(processed_labels[i][0]) for i in range(len(processed_labels))) % 100
    
    # Actual weighted score computation
    weighted_sum = sum(n * w for n, w in zip(normalized, weights))
    
    # Dead code branch (misleading)
    if label_hash > 200:  # Never true
        weighted_sum *= 0.8
    elif label_hash < 50:  # Always true
        pass  # No effect

    # Red herring: entropy calculated but unused
    _ = calculate_entropy(metrics)
    
    # Final adjustment based on control flow
    adjustment_factor = 1.1 if weighted_sum >= 0.6 else 0.95
    final_score = weighted_sum * adjustment_factor
    
    # Extra slicing operation (partially relevant)
    history = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7]
    recent = history[-len(metrics):]  # Slicing with variable length
    if len(recent) > 3:
        final_score += 0.05  # Minor boost for longer metric lists
    
    return final_score

# Main execution
raw_metrics = [0.4, 0.6, 0.8, 0.5]
weights = [0.2, 0.3, 0.4, 0.1]

# Unused dictionary operations (distractor)
diagnostic_info = {
    'version': 'v2.1',
    'mode': 'eval',
    'flags': [True, False, True],
    'config': {'scale': 1.5, 'offset': 0.1}
}
diagnostic_info['timestamp'] = 1234567890
diagnostic_info['derived'] = sum(diagnostic_info['flags'])

final_score = evaluate_performance(raw_metrics, weights)
print(f"Result: {final_score}")