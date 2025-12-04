def calculate_player_score(health, coins, level):
    base_score = (health * 3) + (coins // 2)
    bonus_multiplier = 1 if level > 5 else 0
    
    # Distractor calculations that don't affect final result
    temp_calc = health + coins - level
    unused_value = temp_calc * 2
    
    score_adjustment = base_score + (level * 10) if bonus_multiplier else base_score
    player_status = health > 0 and coins >= 10
    
    # Red herring variable
    fake_adjustment = score_adjustment - 5 if level % 2 == 0 else score_adjustment + 3
    
    final_score = score_adjustment if player_status else base_score
    print(f"Result: {final_score}")

# Main execution
calculate_player_score(25, 15, 6)