from collections import defaultdict

# Simulate player stats and bonus multipliers
def calculate_final_score(base_stats, extra_bonuses):
    total = 0
    multipliers = defaultdict(int)
    
    for key, value in base_stats.items():
        if key in ['strength', 'agility', 'intelligence']:
            total += value * 2
            multipliers[key] = 2
    
    # Apply conditional bonus based on total
    if total > 50:
        total += 10
    
    # Bonus override for special condition
    temp_override = 0  # Irrelevant variable for minor distraction
    for k, v in extra_bonuses.items():
        if v > 0:
            total += v
    
    return total

# Initial data
stats = {'strength': 15, 'agility': 20, 'intelligence': 10, 'charisma': 5}
bonuses = {'extra_hp': 5, 'crit_chance': 0, 'loot_bonus': 3}

# Computation entry point
final_score = calculate_final_score(stats, bonuses)
print(f"Result: {final_score}")