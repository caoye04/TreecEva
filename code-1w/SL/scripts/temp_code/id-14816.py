def calculate_final_score(ranks, multiplier):
    base_points = 10
    rank_scores = {}
    
    # Process each rank and assign preliminary scores
    for rank in ranks:
        if rank == 'S':
            rank_scores[rank] = base_points * 5
        elif rank == 'A':
            rank_scores[rank] = base_points * 3
        elif rank == 'B':
            rank_scores[rank] = base_points * 2
        else:
            rank_scores[rank] = base_points
    
    # Irrelevant string processing - distraction
    status_message = "Processing complete"
    padded_msg = status_message.center(30, '*')
    char_count = len([c for c in padded_msg if c.isalpha()])  # Not used later

    # Aggregate total from rank values
    raw_total = sum(rank_scores.values())
    
    # Simulate level progression bonuses (only some affect outcome)
    level_modifiers = [1.0, 1.1, 1.2, 1.3]
    applicable_modifier = level_modifiers[len(ranks) % 4]  # Depends on number of ranks
    
    # Extra computation with dead-end variables
    temp_buffer = [x * 0.1 for x in range(len(level_modifiers))]  # Unused list comprehension
    average_buffer = sum(temp_buffer) / len(temp_buffer) if temp_buffer else 0  # Distractor

    # Apply only the selected modifier and bonus multiplier
    scaled_total = raw_total * applicable_modifier * multiplier
    
    # Additional filtering: cap score if too high (not triggered in this case)
    capped_total = min(scaled_total, 500)  # Red herring - not actually needed
    
    # Final adjustment based on unique rank count
    unique_bonus = len(set(ranks)) * 2
    final_score = int(capped_total + unique_bonus)  # Final result as integer
    
    return final_score

# Main execution context
rank_data = ['S', 'A', 'S', 'B']
bonus_multiplier = 1.5

# Misleading pre-computations
placeholder_value = 999
intermediate_flag = False
tracking_log = {f"step_{i}": False for i in range(1, 6)}  # Dictionary distractor

final_score = calculate_final_score(rank_data, bonus_multiplier)
print(f"Result: {final_score}")