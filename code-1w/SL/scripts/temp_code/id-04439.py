from collections import defaultdict

def calculate_final_score(records, importance):
    base_scores = defaultdict(lambda: 0)
    
    for record in records:
        category = record['type']
        base_scores[category] += record['value']
    
    weighted_sum = 0
    total_weight = 0
    normalize = lambda x: (x + 1) / (sum(importance.values()) + 1)
    
    for key in base_scores:
        if key in importance:
            weighted_sum += base_scores[key] * importance[key]
            total_weight += importance[key]
    
    avg_weighted = weighted_sum / total_weight if total_weight > 0 else 0
    adjustment = len(base_scores) * 0.5
    final_score = avg_weighted + adjustment
    
    return int(final_score)

# Irrelevant auxiliary data (minor distraction)
user_preferences = {'theme': 'dark', 'notifications': True}
data_stream = [{'type': 'sensor_A', 'value': 12},
              {'type': 'sensor_B', 'value': 8},
              {'type': 'sensor_A', 'value': 4},
              {'type': 'sensor_C', 'value': 15}]

weights = {'sensor_A': 2, 'sensor_B': 3, 'sensor_C': 1}

# Key computation
threshold_score = calculate_final_score(data_stream, weights)

Result: threshold_score