def process_teams(team_data):
    team_scores = {}
    bonus_points = 15
    temporary_buffer = []
    
    for idx, (team_name, scores) in enumerate(team_data):
        team_total = sum(scores) + (idx * 2)
        adjusted_score = team_total - 5
        team_scores[team_name] = adjusted_score
        temporary_buffer.append(team_total)
    
    # Calculate some intermediate values that won't be used
    max_possible = max(temporary_buffer) if temporary_buffer else 0
    average_temp = sum(temporary_buffer) / len(temporary_buffer) if temporary_buffer else 0
    
    # Process rankings
    sorted_teams = sorted(team_scores.items(), key=lambda x: x[1], reverse=True)
    ranking_multiplier = [3, 2, 1, 0]
    
    total_score = 0
    for rank, (team_name, score) in enumerate(sorted_teams[:4]):
        multiplier = ranking_multiplier[rank] if rank < len(ranking_multiplier) else 0
        total_score += score * multiplier
    
    # Some unused calculations
    unused_calc = bonus_points * len(team_data)
    alternative_total = sum(team_scores.values())
    
    return total_score

team_data = [
    ("Alpha", [12, 8, 15]),
    ("Bravo", [10, 14, 9]),
    ("Charlie", [11, 13, 12]),
    ("Delta", [9, 16, 8])
]

result = process_teams(team_data)
print(f"Target result: {result}")