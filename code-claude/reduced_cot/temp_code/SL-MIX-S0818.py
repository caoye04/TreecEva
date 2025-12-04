from itertools import chain

def calculate_weighted_score(stats, weights):
    # Apply weights to player statistics and calculate final score
    base_points = sum(stat * weight for stat, weight in zip(stats.values(), weights.values()))
    
    # Bonus calculation based on statistical thresholds
    bonus_factor = 0
    penalty_factor = 0
    
    # Check if player meets certain thresholds for bonus
    if stats['accuracy'] > 75:
        bonus_factor += 1.5
    if stats['speed'] > 85:
        bonus_factor += 2.0
    
    # Calculate penalty for low endurance (not used in final calculation)
    if stats['endurance'] < 70:
        penalty_factor = 0.8
    
    # Apply bitwise operation to determine multiplier tier
    tier_code = stats['accuracy'] & stats['consistency']
    tier_multiplier = 1.0 + (tier_code % 10) / 100
    
    # Calculate alternate score (not used in final result)
    alternate_score = lambda s: sum(s.values()) / len(s)
    alt_result = alternate_score(stats) * 1.25
    
    # Track potential scores in a dictionary (distraction)
    potential_scores = {
        'standard': base_points,
        'aggressive': base_points * 1.2,
        'defensive': base_points * 0.9
    }
    
    # Extract values for processing (only some are used)
    score_values = list(chain(potential_scores.values(), [alt_result]))
    
    # Final calculation with bonus and tier multiplier
    return int(base_points * tier_multiplier + bonus_factor * 10)

# Player statistics
player_stats = {
    'accuracy': 82,     # Shooting accuracy percentage
    'speed': 88,        # Movement speed rating
    'strength': 75,     # Physical strength rating
    'consistency': 78,  # Consistency rating
    'endurance': 65     # Stamina rating
}

# Importance weights for each stat
weights = {
    'accuracy': 2.5,
    'speed': 1.8,
    'strength': 1.2,
    'consistency': 1.5,
    'endurance': 1.0
}

# Calculate player's weighted performance score
final_score = calculate_weighted_score(player_stats, weights)
print(f"Result: {final_score}")
