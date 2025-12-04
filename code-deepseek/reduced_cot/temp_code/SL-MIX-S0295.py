def compute_final_rating(base_points, cutoff):
    # Distractor calculation - misleading intermediate
    bonus_points = (base_points * 2) - 15
    temp_adjustment = bonus_points % 7
    
    # Real logic with conditional expressions
    multiplier = 3 if base_points > cutoff else 2
    adjusted_base = base_points * multiplier
    
    # Distractor operations that don't affect result
    unused_set = {base_points, cutoff, multiplier}
    dummy_calc = len(unused_set) * 10
    
    # Dead code path - never executed
    if base_points < 0:
        negative_bonus = abs(base_points) // 2
        # This path is never reached
        
    # Core calculation with bitwise operations
    mask = 0b1111
    masked_value = adjusted_base & mask
    
    # Final computation with nested conditional
    result = (adjusted_base - 8) if masked_value > 5 else (adjusted_base + 4)
    return result

def misleading_helper(x, y):
    # This function is called but result is discarded
    return (x ** 2) + (y // 3)

# Main execution
initial_points = 24
threshold = 20
redundant_var = misleading_helper(initial_points, threshold)

# Distractor assignment that looks important
intermediate_result = initial_points + threshold

final_score = compute_final_rating(initial_points, threshold)
print(f"Target result: {final_score}")