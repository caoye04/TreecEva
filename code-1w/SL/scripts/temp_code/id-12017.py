def analyze_trends(data, threshold=5.0):
    trend_scores = {}
    temp_buffer = []
    for key, values in data.items():
        avg = sum(values) / len(values)
        if avg > threshold:
            trend_scores[key] = avg * 1.2
        else:
            trend_scores[key] = avg * 0.8
        temp_buffer.append(avg * 0.1)
    
    # Irrelevant normalization pass
    normalized = {k: v / max(trend_scores.values()) * 10 for k, v in trend_scores.items()}
    scaling_factor = sum(normalized.values()) / len(normalized)

    # Dead code path - never accessed in this execution
    if False:
        return None

    return trend_scores


def calculate_risk(weights, scores):
    risk = 0
    for w, s in zip(weights, scores):
        risk += w * (s ** 0.5)
    return risk if risk > 0 else 0.0


def process_performance(metrics, adjustments):
    base_values = [v['value'] for v in metrics.values()]
    categories = list(metrics.keys())
    
    adjusted_metrics = {}
    intermediate_log = []
    
    for i, cat in enumerate(categories):
        raw = metrics[cat]['value']
        adj = adjustments.get(cat, 1.0)
        seasonality = metrics[cat].get('seasonal', 1.0)
        
        # Core transformation
        adjusted = raw * adj * seasonality
        adjusted_metrics[cat] = adjusted
        
        # Tracking irrelevant intermediate
        if adjusted > 50:
            intermediate_log.append(f"High: {adjusted:.2f}")
        
    # Secondary processing with distraction
    aggregated = sum(adjusted_metrics.values())
    count_valid = len([v for v in adjusted_metrics.values() if v > 40])
    
    # Fake correction factor - not actually used
    correction = aggregated * 0.05 if count_valid > 2 else 0
    
    # Real computation path
    multiplier = 1.5 if count_valid >= 3 else 0.9
    preliminary = aggregated * multiplier
    
    # Conditional offset based on dictionary keys
    if 'growth' in adjusted_metrics and 'stability' in adjusted_metrics:
        preliminary += 10
    
    # Final adjustment using auxiliary function
    aux_data = {'baseline': [preliminary / 4] * 4}
    trends = analyze_trends(aux_data)
    trend_boost = trends['baseline'][0] * 0.2
    
    final_score = int(preliminary + trend_boost)
    
    # Print required at end
    print(f"Result: {final_score}")
    return final_score

# Input setup
metrics = {
    'growth': {'value': 25, 'seasonal': 1.4},
    'efficiency': {'value': 30, 'seasonal': 0.9},
    'stability': {'value': 45, 'seasonal': 1.1},
    'scalability': {'value': 35, 'seasonal': 1.0}
}

adjustments = {
    'growth': 1.3,
    'efficiency': 0.95,
    'stability': 1.05,
    'scalability': 1.2
}

final_score = process_performance(metrics, adjustments)