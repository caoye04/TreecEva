from collections import defaultdict

# Simulate player stats and penalty tracking
def calculate_final_score(player_stats, infractions):
    base_score = 0
    deduction = 0
    
    # Accumulate points from different actions
    for action, count in player_stats.items():
        if action == 'goal':
            base_score += count * 10
        elif action == 'assist':
            base_score += count * 7
        elif action == 'save':
            base_score += count * 3
    
    # Use defaultdict to count penalty types (irrelevant to final result but adds minor distraction)
    penalty_count = defaultdict(int)
    for p in infractions:
        penalty_count[p] += 1
    
    # Deduct points for serious infractions
    for infraction in infractions:
        if infraction == 'yellow_card':
            deduction += 5
        elif infraction == 'red_card':
            deduction += 15
    
    final_score = base_score - deduction
    return final_score

# Player performance data
stats = {
    'goal': 3,
    'assist': 2,
    'save': 5
}

penalties = ['yellow_card', 'yellow_card', 'red_card']

# Irrelevant helper variable (minor distraction - intervention level 5)
temp_multiplier = 1.0

final_score = calculate_final_score(stats, penalties)
print(f"Result: {final_score}")