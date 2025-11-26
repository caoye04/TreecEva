def calculate_player_score(base_points, level_multiplier):
    adjusted_base = base_points * level_multiplier
    temp_check = adjusted_base > 50
    bonus_points = 15 if temp_check else 5
    final_score = adjusted_base + bonus_points
    print(f"Result: {final_score}")

calculate_player_score(12, 4)