from collections import defaultdict

# Simulate player stats and bonus multipliers
def calculate_final_score(player_stats, extra_bonuses):
    base_points = 0
    multiplier = 1.0
    
    # Accumulate base points from stat categories
    for category in player_stats:
        if category == 'attack':
            base_points += sum(player_stats[category]) * 2
        elif category == 'defense':
            base_points += sum(player_stats[category])
        elif category == 'speed':
            base_points += max(player_stats[category])

    # Apply bonus multipliers based on achievements
    for bonus_type in extra_bonuses:
        if bonus_type == 'streak':
            multiplier += 0.2
        elif bonus_type == 'perfect':
            multiplier += 0.5

    return int(base_points * multiplier)

# Irrelevant utility function (minimal interference)
def reverse_string(s):
    return s[::-1]

# Setup data
stats = defaultdict(list)
stats['attack'] = [8, 7, 9]
stats['defense'] = [6, 5]
stats['speed'] = [3, 4, 5, 7]

bonuses = ['streak', 'streak', 'perfect']

# Key computation
final_score = calculate_final_score(stats, bonuses)

print(f"Result: {final_score}")