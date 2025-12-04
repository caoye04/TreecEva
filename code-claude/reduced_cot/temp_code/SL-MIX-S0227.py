def calculate_bitwise_rating(level, gear_score):
    # Calculate player rating based on level and gear score
    base_rating = (level << 2) | (gear_score >> 3)
    modifier = ~(level & 31) & 63
    return (base_rating + modifier) % 100

def apply_achievement_bonus(stats, achievements):
    # Apply bonuses based on achievements
    potential_bonus = sum(a['points'] for a in achievements if a['unlocked'])
    actual_bonus = min(potential_bonus, 50)
    
    # This is unused but looks important
    legendary_bonus = 0
    for a in achievements:
        if a.get('legendary', False) and a['unlocked']:
            legendary_bonus += a['points'] * 2
    
    return {k: v + (v * actual_bonus / 500) for k, v in stats.items()}

def calculate_normalized_score(stats):
    # Core scoring algorithm with misleading calculations
    strength_factor = stats.get('strength', 0) * 0.7
    agility_factor = stats.get('agility', 0) * 0.9
    intelligence_factor = stats.get('intelligence', 0) * 1.2
    
    # Misleading calculation that isn't used
    endurance_score = stats.get('endurance', 0) * 1.5
    charisma_score = stats.get('charisma', 0) * 0.8
    luck_modifier = stats.get('luck', 0) / 10
    
    # This calculation is actually used
    base_score = (strength_factor + agility_factor + intelligence_factor) / 3
    
    # Dict comprehension with zip to create a misleading mapping
    stat_modifiers = {name: idx for idx, name in enumerate(stats.keys())}
    
    # More misleading calculations
    weighted_sum = 0
    total_weight = 0
    for stat, value in stats.items():
        if stat in ['vitality', 'wisdom', 'dexterity']:
            weight = stat_modifiers.get(stat, 1) + 1
            weighted_sum += value * weight
            total_weight += weight
    
    # This branch is never taken because of the condition
    if 'legendary_factor' in stats and stats['legendary_factor'] > 100:
        return base_score * 1.5
    
    # The actual calculation that matters
    normalized = base_score
    if total_weight > 0:
        normalized = (base_score * 0.8) + (weighted_sum / total_weight * 0.2)
    
    # Modular arithmetic to cap the score
    return round(normalized) % 1000

# Player character data
player_level = 42
player_gear_score = 78

# These achievements look important but don't affect the final calculation
achievements = [
    {'name': 'Dungeon Master', 'points': 30, 'unlocked': True},
    {'name': 'Legendary Warrior', 'points': 50, 'unlocked': False, 'legendary': True},
    {'name': 'Speed Runner', 'points': 15, 'unlocked': True}
]

# Calculate the bitwise rating (distraction)
rating = calculate_bitwise_rating(player_level, player_gear_score)

# Base player statistics
base_stats = {
    'strength': 65,
    'agility': 48,
    'intelligence': 72,
    'endurance': 55,
    'charisma': 40,
    'vitality': 60,
    'wisdom': 30,
    'dexterity': 45,
    'luck': 25
}

# Apply achievement bonuses
player_stats = apply_achievement_bonus(base_stats, achievements)

# Calculate alternative scores (distractions)
special_score = (player_level * player_gear_score) % 100
enchantment_level = (special_score + rating) // 2

# Track stats with enumerate (distraction)
stat_progression = []
for i, (stat, value) in enumerate(player_stats.items()):
    if i % 2 == 0:  # Only even indexed stats
        stat_progression.append(value * (i + 1))

# Final calculation
final_score = calculate_normalized_score(player_stats)
print(f"Result: {final_score}")