def evaluate_performance(records, limits):
    stats = {}
    anomalies = []
    total_valid = 0
    cumulative = 0
    
    for record in records:
        raw_value = record.get('value', 0)
        status = record.get('active', False)
        category = record.get('type', 'unknown')
        
        # Irrelevant preprocessing (distractor)
        normalized = abs(raw_value) % 1000 if raw_value else 0
        adjusted = normalized * 1.1
        
        if status and category in ['A', 'B']:
            if raw_value > 0:
                total_valid += 1
                cumulative += raw_value
                
                # Track high values (semi-relevant but not used in final score)
                if raw_value > limits['high']:
                    anomalies.append(raw_value)
            
            # Nested condition with distraction
            if raw_value > limits['medium']:
                bonus = 5 if category == 'A' else 3
                cumulative += bonus

    # Distractor computation: unused summary
    avg_anomaly = sum(anomalies) / len(anomalies) if anomalies else 0
    stats['avg_normalized'] = adjusted  # Dead code path

    base_score = cumulative // total_valid if total_valid else 0
    penalty = len([v for v in records if v.get('flagged', False)]) * 2
    
    # Key logic with slicing distraction
    history = list(range(1, 51))
    recent = history[-base_score:]  # slicing - relevant only to mislead
    decay_factor = 0.95 ** len(recent) if recent else 1.0
    
    # Final score calculation
    final_score = int((base_score - penalty) * decay_factor)
    
    return final_score

# Input data
threshold_config = {'low': 10, 'medium': 25, 'high': 50}
data_set = [
    {'value': 30, 'active': True, 'type': 'A', 'flagged': False},
    {'value': 40, 'active': True, 'type': 'B', 'flagged': False},
    {'value': 20, 'active': True, 'type': 'A', 'flagged': True},
    {'value': -5, 'active': True, 'type': 'B', 'flagged': False},
    {'value': 60, 'active': False, 'type': 'A', 'flagged': False},
    {'value': 35, 'active': True, 'type': 'C', 'flagged': False},
]

# Execution
final_score = evaluate_performance(data_set, threshold_config)
print(f"Result: {final_score}")