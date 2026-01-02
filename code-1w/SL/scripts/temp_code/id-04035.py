def process_leaderboard(entries):
    # Irrelevant transformation: reverse usernames
    reversed_names = [name[::-1] for name in entries.keys()]
    
    # Track cumulative stats (some irrelevant)
    total_points = 0
    entry_count = 0
    max_streak = 0
    score_map = {}
    
    for user, data in entries.items():
        points = data['base_points']
        level = data['level']
        streak = data.get('streak', 0)
        
        # Real computation branch
        if level > 5:
            adjusted = points * 1.2
        else:
            adjusted = points * 0.8
        
        # Red herring: unused metric
        efficiency = (points / (level + 1)) if level != 0 else 0
        
        # Actual scoring contribution
        if streak > 7:
            adjusted += 15
        if streak > max_streak:
            max_streak = streak  # Used later
        
        score_map[user] = round(adjusted)
        total_points += adjusted
        entry_count += 1

    # Distractor: sorting but not used in final result
    sorted_users = sorted(score_map.items(), key=lambda x: x[1], reverse=True)
    rank_data = {user: idx + 1 for idx, (user, _) in enumerate(sorted_users)}

    return score_map, rank_data, total_points


def calculate_final_score(ranks, multiplier):
    base = 0
    position_bonus = 0
    
    # Conditional scoring based on rank
    for user, rank in ranks.items():
        if rank == 1:
            position_bonus += 50
        elif rank == 2:
            position_bonus += 30
        elif rank <= 5:
            position_bonus += 10
    
    # Irrelevant string processing distraction
    rank_strings = [f"User_{i}" for i in range(len(ranks))]
    concatenated = "".join(rank_strings)
    char_sum = sum(ord(c) for c in concatenated) % 100  # Unused
    
    base = sum(100 - 10 * (rank - 1) for rank in ranks.values())
    final = base + position_bonus + multiplier * 5
    return int(final)

# Main execution
player_data = {
    'alice': {'base_points': 85, 'level': 6, 'streak': 10},
    'bob': {'base_points': 90, 'level': 4, 'streak': 5},
    'carol': {'base_points': 78, 'level': 7, 'streak': 8},
    'dave': {'base_points': 95, 'level': 3, 'streak': 12},
    'eve': {'base_points': 88, 'level': 5, 'streak': 6}
}

# Extra irrelevant dictionary operation
metadata = {'created': '2023', 'version': '1.2'}
metadata['hash'] = sum(len(k) for k in player_data.keys())

_, ranks, _ = process_leaderboard(player_data)
bonus_multiplier = len([p for p in player_data.values() if p['level'] > 4])

final_score = calculate_final_score(ranks, bonus_multiplier)
print(f"Result: {final_score}")