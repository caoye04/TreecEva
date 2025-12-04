import itertools

def calculate_bonus(level, streak):
    # Calculate bonus points based on level and streak
    multiplier = min(level * 0.5, 3)
    bonus = streak * multiplier
    return int(bonus)

# Player game data
raw_scores = [42, 18, 27, 35, 19, 30, 25]
score_weights = [1.0, 0.8, 1.2, 1.0, 0.9, 1.1, 1.0]

# Apply weights to raw scores
weighted_scores = [score * weight for score, weight in zip(raw_scores, score_weights)]

# Track player achievements
achievements = {
    'quests_completed': 12,
    'battles_won': 8,
    'items_collected': 25,
    'bosses_defeated': 3
}

# Calculate achievement points
achievement_points = achievements['quests_completed'] * 5
achievement_points += achievements['battles_won'] * 10
achievement_points += achievements['items_collected'] * 2

# Level progression system
player_level = 4
win_streak = 3
bonus_points = calculate_bonus(player_level, win_streak)

# Generate potential point combinations
point_combinations = list(itertools.product([5, 10, 15], repeat=2))
point_options = [sum(combo) for combo in point_combinations]

# Filter options based on player level
valid_options = [p for p in point_options if p <= player_level * 10]

# Calculate total points from weighted scores
base_points = int(sum(weighted_scores))

# Apply modular arithmetic to normalize points
modifier = base_points % 10
if modifier > 5:
    base_points += (10 - modifier)
else:
    base_points -= modifier

# Generate filtered points list
filtered_points = [base_points]
for option in valid_options:
    if option % player_level == 0:
        filtered_points.append(option)

# Apply bonus points to the first element
filtered_points[0] += bonus_points

# Calculate total points
total_points = sum(filtered_points)

print(f"Result: {total_points}")