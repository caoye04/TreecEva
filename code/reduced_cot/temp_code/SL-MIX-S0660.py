def calculate_player_score(accuracy, reaction_time, combo_count):
    base_score = accuracy * 100
    time_bonus = 500 - reaction_time if reaction_time < 500 else 0
    combo_multiplier = combo_count // 5 + 1
    
    # Distractor calculations that don't affect final result
    max_possible = base_score * 2 + time_bonus
    average_metrics = (accuracy + reaction_time / 100 + combo_count) / 3
    
    raw_total = base_score + time_bonus
    adjusted_total = raw_total * combo_multiplier
    
    # Conditional expression for multiplier
    multiplier = 1.5 if accuracy > 0.8 else 1.2 if accuracy > 0.6 else 1.0
    bonus_points = 50 if combo_count > 10 else 25 if combo_count > 5 else 0
    
    final_score = adjusted_total * multiplier + bonus_points
    
    # More distractor operations
    score_variance = final_score - raw_total
    performance_ratio = accuracy * multiplier
    
    print(f"Final result: {final_score}")
    return final_score

# Test case execution
player_accuracy = 0.85
player_reaction = 420
player_combos = 12

result = calculate_player_score(player_accuracy, player_reaction, player_combos)
print(f"Target result: {result}")