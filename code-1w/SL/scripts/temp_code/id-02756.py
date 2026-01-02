def analyze_performance(records):
    base_multiplier = 1.5
    bonus_factor = 0.0
    total_points = 0
    penalty_offset = 0
    temp_result = 0
    
    for record in records:
        raw_score = record['score']
        category = record['category']
        
        # Irrelevant preprocessing (distractor)
        normalized = raw_score / 100.0
        if normalized > 0.8:
            bonus_factor += 0.1
        
        # Core logic
        if category == 'technical':
            weight = 3
        elif category == 'behavioral':
            weight = 1
        else:
            weight = 2
            
        contribution = raw_score * weight
        total_points += contribution
        
        # Dead code path (misleading)
        if raw_score < 0:
            temp_result -= 999

    # Another distraction: unused transformation
    transformed_records = [r['score']**0.5 for r in records if r['score'] > 0]
    avg_transformed = sum(transformed_records) / len(transformed_records) if transformed_records else 0

    return total_points


def compute_aggregate(data):
    raw_total = analyze_performance(data)
    adjustment = 0
    
    # String-based case conversion distractor
    status_flags = ['ACTIVE', 'PENDING', 'COMPLETED']
    flag_summary = ''.join([f[0].lower() for f in status_flags])
    
    # Dictionary operations with semi-relevant data
    modifiers = {k: v for k, v in zip(['base', 'extra'], [1.2, 0.8])}
    base_modifier = modifiers.get('base')
    
    # Conditional expression (required feature)
    adjustment = 10 if 'technical' in [d['category'] for d in data] else 5
    
    # Core computation
    intermediate = raw_total * base_modifier
    final_score = int(intermediate + adjustment)
    
    # Print required output format
    print(f"Result: {final_score}")
    return final_score

# Input data
evaluation_data = [
    {'score': 85, 'category': 'technical'},
    {'score': 70, 'category': 'behavioral'},
    {'score': 90, 'category': 'technical'},
    {'score': 75, 'category': 'hybrid'}
]

# Entry point
final_score = compute_aggregate(evaluation_data)