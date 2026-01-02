from collections import Counter

def calculate_final_score(log):
    team_a_events = []
    team_b_events = []
    
    for event in log:
        if event['team'] == 'A':
            team_a_events.append(event['type'])
        elif event['team'] == 'B':
            team_b_events.append(event['type'])
    
    count_a = Counter(team_a_events)
    count_b = Counter(team_b_events)
    
    goals_a = count_a.get('goal', 0)
    goals_b = count_b.get('goal', 0)
    
    yellow_a = count_a.get('yellow_card', 0)
    yellow_b = count_b.get('yellow_card', 0)
    
    # Bonus point for comeback if behind by at least one goal and then score more
    bonus = 0
    if (goals_a > goals_b and goals_a >= 2) or (goals_b > goals_a and goals_b >= 2):
        bonus = 1
    
    discipline_penalty = (yellow_a + yellow_b) // 3  # Penalty every 3 yellow cards
    
    result = abs(goals_a - goals_b) + bonus - discipline_penalty
    return result

# Match event log
events = [
    {'team': 'A', 'type': 'goal'},
    {'team': 'B', 'type': 'goal'},
    {'team': 'A', 'type': 'goal'},
    {'team': 'A', 'type': 'yellow_card'},
    {'team': 'B', 'type': 'yellow_card'},
    {'team': 'A', 'type': 'goal'},
    {'team': 'B', 'type': 'yellow_card'},
    {'team': 'B', 'type': 'goal'},
    {'team': 'B', 'type': 'goal'}
]

result = calculate_final_score(events)
print(f"Result: {result}")