def calculate_player_score():
    base_points = 120
    rank = 3
    games_won = 7
    games_played = 10
    
    # Irrelevant statistic (minimal interference)
    win_rate = games_won / games_played if games_played > 0 else 0
    
    is_eligible = win_rate >= 0.6
    base_bonus = 25 if is_eligible else 10
    extra_award = 15 if games_won >= 8 else 0
    
    # Key computation with conditional expression
    final_bonus = base_bonus + extra_award
    total_score = final_bonus + base_points * (is_eligible if rank < 5 else 0)
    
    # Print result for clarity
    print(f"Result: {total_score}")

calculate_player_score()