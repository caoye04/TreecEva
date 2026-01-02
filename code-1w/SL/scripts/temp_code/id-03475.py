def calculate_final_score(entries, importance_weights):
    base_score = 0
    penalty_adjustment = 0
    bonus_tracker = []
    
    # Preprocess entries: filter valid records and normalize values
    valid_records = [e for e in entries if e['status'] == 'active']
    normalized_values = {k: v / 10.0 for k, v in importance_weights.items()}
    
    # Misleading computation: this tracks bonuses but isn't used in final score
    for record in valid_records:
        if record['performance'] > 80:
            bonus_tracker.append(record['id'])

    # Actual scoring logic
    for record in valid_records:
        weighted_value = record['performance'] * normalized_values.get(record['category'], 1.0)
        base_score += weighted_value
        
        # Apply tiered penalties based on delay factor
        if record['latency'] > 200:
            penalty_adjustment -= 3
        elif record['latency'] > 100:
            penalty_adjustment -= 1
    
    # Auxiliary distraction: compute unused stats
    avg_latency = sum(r['latency'] for r in valid_records) / len(valid_records) if valid_records else 0
    max_performance = max((r['performance'] for r in valid_records), default=0)
    
    # Final aggregation
    raw_total = base_score + penalty_adjustment * len(valid_records)
    scaling_factor = 1.5 if len(bonus_tracker) > 2 else 1.0
    final_score = int(raw_total * scaling_factor)  # deterministic integer result
    
    return final_score

# Input data setup
data = [
    {'id': 1, 'category': 'A', 'performance': 85, 'latency': 150, 'status': 'active'},
    {'id': 2, 'category': 'B', 'performance': 90, 'latency': 50,  'status': 'active'},
    {'id': 3, 'category': 'A', 'performance': 78, 'latency': 300, 'status': 'inactive'},
    {'id': 4, 'category': 'C', 'performance': 92, 'latency': 80,  'status': 'active'},
    {'id': 5, 'category': 'B', 'performance': 88, 'latency': 120, 'status': 'active'}
]

weights = {'A': 15, 'B': 20, 'C': 25}

# Execute main logic
final_score = calculate_final_score(data, weights)
print(f"Result: {final_score}")