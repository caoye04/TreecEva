def evaluate_performance(records, importance):
    base = sum([r['value'] for r in records])
    adjustment = 0
    
    # Irrelevant pre-processing: counting record types (distractor)
    type_count = {'A': 0, 'B': 0, 'C': 0}
    for r in records:
        if r['type'] in type_count:
            type_count[r['type']] += 1
    
    temp_factor = 0
    for i, record in enumerate(records):
        if i % 2 == 0:
            temp_factor += record['value'] * 0.1
        else:
            temp_factor -= record['value'] * 0.05
    
    # Real logic begins: weighted scoring with lambda-based normalization
    normalized_weights = list(map(lambda w: w / sum(importance), importance))
    
    weighted_sum = 0
    for idx, rec in enumerate(records):
        weighted_sum += rec['value'] * normalized_weights[idx]
    
    # Conditional adjustment based on data pattern (slicing used here)
    mid_section = records[1:-1]
    if len(mid_section) > 1 and mid_section[0]['value'] < mid_section[-1]['value']:
        adjustment = 10
    else:
        adjustment = -5
    
    # Dummy state tracking (dead code path - distractor)
    processing_log = []
    for step in ['init', 'norm', 'weight', 'adjust']:
        processing_log.append(f'{step}_done')
    
    # Final score computation - only this matters
    final_score = weighted_sum + adjustment
    return final_score

# Main execution
raw_data = [
    {'type': 'A', 'value': 20},
    {'type': 'B', 'value': 35},
    {'type': 'C', 'value': 50},
    {'type': 'A', 'value': 45}
]

weights = [1, 3, 2, 4]
data_slice = raw_data[:]

# Key statement
final_score = evaluate_performance(data_slice, weights)
print(f"Result: {final_score}")