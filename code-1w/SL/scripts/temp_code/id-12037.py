def calculate_final_score(records):
    base_scores = [rec['value'] for rec in records if rec['active']]
    adjustments = {i: (base_scores[i] * 0.1) for i in range(len(base_scores)) if base_scores[i] > 50}
    
    total_adjustment = sum(adjustments.values())
    raw_sum = sum(base_scores)
    
    outlier_filter = [v for v in base_scores if v < 100]
    filtered_mean = sum(outlier_filter) / len(outlier_filter) if outlier_filter else 0
    
    penalty = 0
    if raw_sum > 200:
        penalty = int(filtered_mean * 0.05)
    
    final_score = raw_sum + total_adjustment - penalty
    return final_score

# Simulated dataset
data = [
    {'value': 45, 'active': True},
    {'value': 75, 'active': True},
    {'value': 30, 'active': False},
    {'value': 85, 'active': True},
    {'value': 95, 'active': True},
    {'value': 60, 'active': True}
]

result = calculate_final_score(data)
print(f"Result: {result}")