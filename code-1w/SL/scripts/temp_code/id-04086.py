from itertools import combinations

def analyze_trends(data):
    trends = {}
    for i in range(2, len(data) + 1):
        for group in combinations(data.keys(), i):
            avg = sum(data[k] for k in group) / len(group)
            trends[group] = round(avg, 3)
    return trends

def normalize_values(raw):
    total = sum(raw.values())
    return {k: v / total for k, v in raw.items()}

def calculate_risk_factor(values):
    risk = 0
    for val in values:
        if val > 0.15:
            risk += val ** 2
    return round(risk, 4)

def evaluate_performance(metrics, weights):
    weighted_sum = 0.0
    temp_buffer = []
    
    # Core computation
    for key in ['reliability', 'efficiency', 'scalability']:
        if key in metrics and key in weights:
            weighted_sum += metrics[key] * weights[key]
    
    # Distractor: irrelevant aggregation
    for key in metrics:
        temp_buffer.append(metrics[key] * 0.1)  # Not used later
    
    adjustment = 0
    if weighted_sum > 80:
        adjustment = 5
    elif weighted_sum > 60:
        adjustment = 2
    else:
        adjustment = -3
    
    # Another red herring: complex but unused structure
    aux_data = {f'item_{i}': i * weighted_sum for i in range(3)}
    
    final_score = int(weighted_sum + adjustment)
    
    # Dead code path (never executed due to prior logic)
    if len(aux_data) < 2:
        final_score *= 2
        
    return final_score

# Main execution
metrics = {
    'reliability': 90,
    'efficiency': 75,
    'scalability': 85,
    'usability': 65,
    'compatibility': 40
}

weights = {
    'reliability': 0.4,
    'efficiency': 0.3,
    'scalability': 0.3,
    'security': 0.1  # Unused weight
}

# Preprocessing steps with side effects on other variables
trend_analysis = analyze_trends(metrics)
normalized_metrics = normalize_values(metrics)
risk_level = calculate_risk_factor(normalized_metrics.values())

# Key statement
final_score = evaluate_performance(metrics, weights)

print(f"Result: {final_score}")