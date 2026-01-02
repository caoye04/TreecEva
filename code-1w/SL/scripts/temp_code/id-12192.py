def analyze_productivity(records):
    base_multiplier = 1.5
    bonus_factor = 0.7
    temp_offset = 3
    total_hours = 0
    night_shift_penalty = 0.9
    adjusted_scores = []
    
    for entry in records:
        hours = entry['hours_worked']
        shift_type = entry['shift']
        complexity = entry['complexity']
        
        raw_score = hours * complexity
        if shift_type == 'night':
            raw_score *= night_shift_penalty
        
        # Distractor: irrelevant transformation
        transformed = (raw_score + temp_offset) ** bonus_factor
        adjusted_scores.append(raw_score * base_multiplier)

    return adjusted_scores


def calculate_rating(contributions, impact_levels):
    base_ratings = [0.8, 1.2, 0.9, 1.5]
    scaling_factor = 2.1
    cumulative_weight = 0
    total_impact = 0
    
    # Real logic starts here
    indexed_pairs = list(enumerate(zip(contributions, impact_levels)))
    intermediate_results = {}
    
    for idx, (contrib, impact) in indexed_pairs:
        if impact < 2:
            continue  # Skip low impact
        weight = contrib * scaling_factor
        if idx % 2 == 0:
            weight *= base_ratings[idx % len(base_ratings)]
        
        # Irrelevant caching attempt
        intermediate_results[f'entry_{idx}'] = weight * 0.95
        
        cumulative_weight += weight
        total_impact += impact

    # Distractor: unused computation
    avg_base_rating = sum(base_ratings) / len(base_ratings)
    penalty_adjustment = avg_base_rating * 0.3

    if total_impact > 10:
        cumulative_weight *= 1.1

    # Final rating calculation
    final_rating = cumulative_weight / (total_impact + 1e-8)
    return round(final_rating, 4)

# Main execution
employee_data = [
    {'hours_worked': 8, 'shift': 'day', 'complexity': 3},
    {'hours_worked': 6, 'shift': 'night', 'complexity': 4},
    {'hours_worked': 5, 'shift': 'day', 'complexity': 2}
]

productivity_scores = analyze_productivity(employee_data)

contributions = [12, 18, 9, 21, 14]
impact_levels = [3, 1, 4, 5, 2]

# Key statement
final_score = calculate_rating(contributions, impact_levels)

print(f"Result: {final_score}")