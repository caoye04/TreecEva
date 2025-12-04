def process_team_performance(initial_score, bonus_points, penalty_reduction):
    # Calculate raw performance score
    raw_score = initial_score * 2 - penalty_reduction
    
    # Apply bonus calculation (distractor - not used in final result)
    bonus_calc = bonus_points * 3 + 10
    
    # Process data with conditional string evaluation
    data_status = "approved" if raw_score > 50 else "pending"
    processed_data = raw_score + (15 if data_status.upper().startswith("A") else 5)
    
    # Adjustment factor calculation with bitwise operations
    temp_value = 12 | 5  # Binary OR operation
    adjustment_factor = temp_value ^ 3  # Binary XOR operation
    
    # Final score calculation
    final_score = processed_data + adjustment_factor
    print(f"Result: {final_score}")
    return final_score

# Execute the function
process_team_performance(40, 8, 15)