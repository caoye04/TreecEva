def calculate_player_stats():
    player_data = {
        'kills': 15,
        'assists': 8,
        'deaths': 6,
        'objectives': 4
    }
    
    # Base calculations
    kill_points = player_data['kills'] * 100
    assist_points = player_data['assists'] * 50
    objective_points = player_data['objectives'] * 75
    
    # Distractor calculations (not used in final result)
    kda_ratio = (player_data['kills'] + player_data['assists']) / max(1, player_data['deaths'])
    total_actions = player_data['kills'] + player_data['assists'] + player_data['deaths']
    
    # Core logic
    base_total = kill_points + assist_points + objective_points
    death_penalty = player_data['deaths'] * 25
    adjusted_total = base_total - death_penalty
    
    # Bonus system
    performance_tier = 'gold' if adjusted_total >= 2000 else 'silver'
    bonus_multipliers = {'silver': 1.1, 'gold': 1.25, 'platinum': 1.5}
    bonus_factor = bonus_multipliers[performance_tier]
    
    final_score = adjusted_total * bonus_factor
    print(f"Target result: {final_score}")

calculate_player_stats()