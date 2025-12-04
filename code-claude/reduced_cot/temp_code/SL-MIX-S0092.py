# Player performance analysis comparing overlap between player and opponent statistics

# Player's statistics for the last 5 games (points, rebounds, assists, steals, blocks)
player_stats = [22, 7, 5, 2, 1]

# Opponent's statistics for the last 5 games (same categories)
opponent_stats = [18, 9, 6, 1, 3]

# Calculate performance metrics
total_player_stats = sum(player_stats)
max_category = max(enumerate(player_stats), key=lambda x: x[1])
best_category_index = max_category[0]

# Categories for reference (not used in calculation)
categories = ['points', 'rebounds', 'assists', 'steals', 'blocks']

# Calculate advantage in each category
advantages = [p - o for p, o in zip(player_stats, opponent_stats)]

# Calculate overlap score - sum of minimum values in each category
overlap_score = sum([min(a, b) for a, b in zip(player_stats, opponent_stats)])

# Calculate differential score
differential = sum(advantages)

# Slice the advantages to get only defensive categories (steals and blocks)
defensive_advantage = sum(advantages[3:])

print(f"Player total stats: {total_player_stats}")
print(f"Player's best category: {categories[best_category_index]}")
print(f"Overlap score: {overlap_score}")
print(f"Overall differential: {differential}")