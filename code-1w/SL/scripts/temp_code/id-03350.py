def analyze_performance(entries):
    total_entries = len(entries)
    if total_entries == 0:
        return 0
    
    weighted_sum = 0
    temp_factor = 0
    debug_trace = []
    
    for i, entry in enumerate(entries):
        raw_value = entry.get('value', 0)
        multiplier = entry.get('multiplier', 1)
        category = entry.get('category', 'default')
        
        # Irrelevant computation (distractor)
        temp_factor += (i + 1) * raw_value % 7
        
        if category == 'critical':
            raw_value *= 1.5
        elif category == 'minor':
            raw_value *= 0.5
            
        weighted_sum += raw_value * multiplier
        
        # Dead code path (misleading)
        if raw_value > 1000:
            debug_trace.append(f'High value at {i}')

    average = weighted_sum / total_entries if total_entries else 0
    adjustment = 1.0 + (temp_factor % 5) / 100
    
    return average * adjustment


def calculate_rating(contributions, impact_levels):
    base_rating = 0
    level_map = {k: v for k, v in zip(['low', 'medium', 'high'], [1, 2, 3])}
    
    # Misleading dictionary operations
    stats_summary = {
        'count': len(contributions),
        'max_impact': max(impact_levels) if impact_levels else 0,
        'dummy_metric': sum([x**2 for x in impact_levels]) // len(impact_levels) if impact_levels else 0
    }
    
    contribution_scores = []
    
    for idx, contrib in enumerate(contributions):
        score = contrib['hours'] * 10
        
        # Conditional expression with distractor logic
        bonus = 50 if contrib['hours'] > 40 and impact_levels[idx] >= 2 else 20
        
        # Nested conditionals (2 levels)
        if impact_levels[idx] > 1:
            if level_map.get(contrib['priority'], 0) >= 2:
                score *= 1.8
            else:
                score *= 1.2
        else:
            score *= 0.7
            
        score += bonus
        contribution_scores.append(score)
        
        # Early break that rarely triggers (edge case red herring)
        if idx == 5 and contrib['hours'] < 5:
            break

    # Real computation
    base_rating = sum(contribution_scores) / len(contribution_scores) if contribution_scores else 0
    
    # Final adjustment using analysis function
    aux_data = [{'value': s, 'multiplier': 1, 'category': 'default'} for s in contribution_scores[:3]]
    auxiliary_boost = analyze_performance(aux_data)
    
    final_rating = base_rating + (auxiliary_boost * 0.3)
    
    # Key assignment point
    final_score = int(round(final_rating))
    
    return final_score

# Input data
contributions_list = [
    {'hours': 35, 'priority': 'medium'},
    {'hours': 45, 'priority': 'high'},
    {'hours': 50, 'priority': 'high'},
    {'hours': 20, 'priority': 'low'},
    {'hours': 60, 'priority': 'medium'}
]

impact_values = [2, 3, 3, 1, 2]

# Execution
final_score = calculate_rating(contributions_list, impact_values)
print(f"Result: {final_score}")