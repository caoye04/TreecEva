def calculate_adjusted_score(points, multiplier, penalties):
    # Calculate base score with multiplier
    preliminary_score = points * multiplier
    
    # Apply penalties if they exceed threshold
    penalty_threshold = 5
    effective_penalties = penalties if penalties < penalty_threshold else penalty_threshold
    
    # Track statistics (not used in final calculation)
    stats = {
        "original_points": points,
        "multiplier_used": multiplier,
        "raw_penalties": penalties,
        "effective_penalties": effective_penalties
    }
    
    # Calculate adjusted score based on conditional logic
    adjustment_factor = 1.5 if preliminary_score > 100 else 1.0
    
    # These calculations don't affect the final result
    potential_bonus = (points // 10) * 2
    theoretical_max = points * multiplier * 2
    
    # Perform the actual calculation that matters
    result = preliminary_score * adjustment_factor - effective_penalties * 3
    
    # Return the result (rounded to 1 decimal place)
    return round(result, 1)

# Player performance data
base_points = 75
time_bonus = 12
accuracy_points = 8
bonus_multiplier = 1.8
raw_penalties = (3, 4, 2)

# Calculate total points (combining base and bonuses)
total_points = base_points + (time_bonus if time_bonus < 15 else 15) + accuracy_points

# Process penalties - convert tuple to single value
penalties = sum(penalty for penalty in raw_penalties if penalty > 0)

# Some intermediate calculations that don't affect the result
max_possible = total_points * 2.5
efficiency_ratio = total_points / base_points

# Calculate the final score
final_score = calculate_adjusted_score(total_points, bonus_multiplier, penalties)

print(f"Result: {final_score}")