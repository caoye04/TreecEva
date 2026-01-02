def calculate_ranking(scores):
    ranked = sorted(scores.values(), reverse=True)
    return ranked[0] - ranked[-1]

# Player points from different rounds
temp_data = [12, 18, 22]
points_map = {
    'player_alpha': 45 + temp_data[0],
    'player_beta': 38 + temp_data[1],
    'player_gamma': 52 + temp_data[2]
}

# Irrelevant tracking variable (minimal distraction)
update_count = len(points_map)

# Key computation
final_score = calculate_ranking(points_map)

print(f"Result: {final_score}")