def calculate_final_score(ranks, multiplier):
    base_points = 100
    penalty = 0
    
    # Irrelevant tracking variables (distractors)
    historical_max = max(ranks) if ranks else 0
    temp_offsets = [abs(r - base_points) for r in ranks]
    adjustment_factor = sum(temp_offsets) / len(temp_offsets) if temp_offsets else 0

    # Real logic begins: filter top performers
    qualified = {r for r in ranks if r <= 10}  # Set operation: top 10
    
    # Additional distraction: unused transformation
    normalized = [(r / max(ranks)) * base_points for r in ranks if max(ranks) > 0]
    average_normalized = sum(normalized) / len(normalized) if normalized else 0

    # Core scoring logic
    raw_score = sum(15 - rank for rank in qualified if rank < 15)
    
    # Conditional expression with logical condition
    bonus = 25 if len(qualified) >= 3 and all(rank % 2 == 1 for rank in qualified) else 10
    
    # Apply multiplier only if conditions met
    multiplier_effect = multiplier if sum(ranks) < 50 else 1.0
    
    # Final computation
    final = raw_score + bonus
    final *= multiplier_effect
    
    # More red herring: unused state tracking
    status_log = []
    for idx, r in enumerate(ranks):
        if r < 5:
            status_log.append(f"Elite at {idx}")
        elif r < 15:
            status_log.append(f"Good at {idx}")
    
    return int(final)

# Main execution
rankings = [3, 7, 1, 12, 18, 9]
bonus_multiplier = 1.5

# Unused but plausible calculations (distractors)
shadow_rankings = [r ** 0.5 for r in rankings]
total_spread = max(rankings) - min(rankings)
consistency_metric = len([r for r in rankings if r <= 10]) / len(rankings)

# Key statement
final_score = calculate_final_score(rankings, bonus_multiplier)

print(f"Result: {final_score}")