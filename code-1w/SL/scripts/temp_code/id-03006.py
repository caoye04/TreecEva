def calculate_performance(bonuses, weights):
    base_points = 450
    adjustment = 0
    
    # Apply conditional bonuses using dictionary and lambda
    multiplier = lambda x: 1.2 if x > 5 else 1.0
    for key in bonuses:
        if key in weights:
            adjustment += bonuses[key] * weights[key]
    
    # Linear search through performance tiers
    performance_tier = "basic"
    thresholds = [100, 250, 400]
    if adjustment >= thresholds[2]:
        performance_tier = "elite"
    elif adjustment >= thresholds[1]:
        performance_tier = "advanced"
    elif adjustment >= thresholds[0]:
        performance_tier = "intermediate"
    
    # Irrelevant tracking variable (minimal distraction)
    last_processed = None
    for k in bonuses:
        last_processed = k
    
    # Final score computation
    final_score = base_points + adjustment
    if performance_tier == "elite":
        final_score = int(final_score * multiplier(adjustment))
    
    return final_score

# Data setup
bonus_map = {'speed': 8, 'accuracy': 6, 'consistency': 7}
level_weights = {'speed': 15, 'accuracy': 20, 'consistency': 10}

# Key execution point
final_score = calculate_performance(bonus_map, level_weights)
print(f"Result: {final_score}")