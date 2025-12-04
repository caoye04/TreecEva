# Inventory point calculation system
# Each item in the inventory has a point value

points_dict = {
    'apple': 5,
    'banana': 3,
    'cherry': 7,
    'date': 2,
    'elderberry': 9
}

# Items collected during the game
collected_items = ['apple', 'cherry', 'banana', 'fig', 'cherry', 'apple']

# Some game statistics
game_level = 3
player_health = 85
time_remaining = 120

# Calculate the total points from collected items
# Items not in the points_dict are worth 0 points
total_points = sum([points_dict.get(item, 0) for item in collected_items])

# Apply level bonus (not affecting the total_points calculation)
level_bonus = total_points * 0.1 * game_level

# Final score would include the level bonus
final_score = total_points + level_bonus

print(f"Result: {total_points}")