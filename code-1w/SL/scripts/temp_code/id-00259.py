def calculate_performance(flags):
    base = 100
    multiplier = 1.0
    
    # Apply bonuses based on flag characteristics
    for flag in flags:
        if len(flag) > 5:
            multiplier += 0.1
        if flag.startswith('gold'):
            multiplier += 0.15
        if flag.endswith('special'):
            multiplier += 0.2
    
    return int(base * multiplier)

# Simulation data
event_tags = ['gold_medal_special', 'silver_badge', 'gold_bonus_special', 'trial']
bonus_flags = [tag.upper() for tag in event_tags]
bonus_flags = [tag.lower() for tag in bonus_flags]  # Normalize case

final_score = calculate_performance(bonus_flags)
print(f"Result: {final_score}")