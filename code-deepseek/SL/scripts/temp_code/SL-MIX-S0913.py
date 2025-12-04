def analyze_team_performance(players):
    scores = [p['performance'] for p in players if p['active']]
    primary_scores = {s for s in scores if s >= 50}
    
    # Distractor operations that don't affect final result
    temp_max = max(scores) if scores else 0
    temp_min = min(scores) if scores else 0
    range_calc = temp_max - temp_min
    
    core_set = {score * 2 for score in primary_scores}
    adjustment = len([s for s in scores if s % 2 == 0])
    
    # Another distractor calculation
    average_performance = sum(scores) / len(scores) if scores else 0
    performance_variance = sum((s - average_performance) ** 2 for s in scores) if scores else 0
    
    final_score = max(core_set) - min(core_set) + adjustment
    print(f"Result: {final_score}")

players_data = [
    {'name': 'Alice', 'performance': 85, 'active': True},
    {'name': 'Bob', 'performance': 92, 'active': True},
    {'name': 'Charlie', 'performance': 78, 'active': True},
    {'name': 'Diana', 'performance': 45, 'active': True},
    {'name': 'Eve', 'performance': 88, 'active': True}
]

analyze_team_performance(players_data)