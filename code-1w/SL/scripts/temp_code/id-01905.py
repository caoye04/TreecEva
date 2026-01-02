def calculate_final_score(entries):
    base_values = [e['value'] for e in entries if e['active']]
    adjustments = []
    temp_sum = 0
    
    for i, v in enumerate(base_values):
        if i % 2 == 0:
            adjusted = v * 1.1
        else:
            adjusted = v * 0.95
        adjustments.append(round(adjusted, 2))
        temp_sum += adjusted

    # Irrelevant tracking variables (distractors)
    max_adjustment = max(adjustments) if adjustments else 0
    avg_base = sum(base_values) / len(base_values) if base_values else 0
    fluctuation_index = (max_adjustment - avg_base) / avg_base if avg_base else 0

    # Simulate redundant validation pass
    valid_count = 0
    for val in adjustments:
        if val > 0:
            valid_count += 1  # Not used in final logic

    # Secondary processing with dictionary aggregation (semi-relevant)
    detail_log = {f'entry_{i}': round(v, 2) for i, v in enumerate(adjustments)}
    total_from_log = sum(detail_log.values())
    
    # Core computation obscured by prior noise
    penalty = len([x for x in base_values if x < 10]) * 1.5
    bonus = len([x for x in base_values if x > 50]) * 2.0
    
    final_score = total_from_log + bonus - penalty
    
    # Dead code path (never executed under current logic)
    if False:
        final_score *= 0.9
        final_score += 100
    
    return round(final_score, 2)

# Input data setup
raw_data = [
    {'value': 5, 'active': True},
    {'value': 12, 'active': True},
    {'value': 8, 'active': True},
    {'value': 55, 'active': True},
    {'value': 3, 'active': True},
    {'value': 61, 'active': True},
    {'value': 40, 'active': False},  # Inactive, should be filtered
    {'value': 70, 'active': True}
]

# Additional irrelevant preprocessing
filtered_out = [x for x in raw_data if not x['active']]
dummy_transform = [str(x['value']) + '_processed' for x in raw_data]

# Main execution point
final_score = calculate_final_score(raw_data)
print(f"Target result: {final_score}")