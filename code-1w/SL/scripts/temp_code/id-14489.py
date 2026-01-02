def calculate_final_score(ranks, metrics):
    # Irrelevant transformation: normalize ranks (not used in final logic)
    normalized_ranks = {k: v / max(ranks.values()) for k, v in ranks.items()}
    
    # Distractor: complex dictionary comprehension with unused result
    rank_squares = {k: v**2 for k, v in ranks.items() if v > 1}
    
    # Semi-relevant data restructuring
    ordered_teams = sorted(ranks.keys(), key=lambda x: ranks[x])
    
    # Key logic begins: filter top performers based on metrics
    high_performers = set()
    for team, data in metrics.items():
        if data['efficiency'] >= 85 and data['consistency'] > 70:
            high_performers.add(team)
    
    # Secondary filtering: must be in top 3 ranks
    top_three = set(ordered_teams[:3])
    elite_teams = high_performers & top_three  # Intersection: set operation
    
    # Compute base score using selected teams
    base_score = 0
    for team in elite_teams:
        raw_value = metrics[team]['efficiency'] * 0.6 + metrics[team]['consistency'] * 0.4
        rounded_value = int(round(raw_value / 5)) * 5  # Round to nearest 5
        base_score += rounded_value
    
    # Distractor: unused loop over normalized ranks
    adjustment_factor = 0
    for team in normalized_ranks:
        temp_val = normalized_ranks[team] * 100
        if temp_val > 50:
            adjustment_factor += 1  # This is tracked but not used
    
    # Final computation with red herring variables
    multiplier = len(elite_teams) if elite_teams else 1
    final_score = base_score * multiplier + 10  # Add arbitrary offset
    
    # Dead code path: never executed due to logic above
    if len(elite_teams) == 0 and False:
        final_score += 100
    
    return final_score

# Main execution context
rankings = {
    'Alpha': 1,
    'Bravo': 3,
    'Charlie': 2,
    'Delta': 4,
    'Echo': 5
}

performance_metrics = {
    'Alpha': {'efficiency': 92, 'consistency': 76},
    'Bravo': {'efficiency': 88, 'consistency': 68},
    'Charlie': {'efficiency': 84, 'consistency': 72},
    'Delta': {'efficiency': 90, 'consistency': 74},
    'Echo': {'efficiency': 86, 'consistency': 70}
}

# Execute main logic
final_score = calculate_final_score(rankings, performance_metrics)
print(f"Target result: {final_score}")