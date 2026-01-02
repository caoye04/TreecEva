from collections import defaultdict

# Player performance tracking system
def calculate_final_score(stats, bonuses):
    base = sum(stats.values())
    multiplier = 1.0
    
    # Apply bonus multipliers based on achievement thresholds
    for key in bonuses:
        if stats[key] >= 10:
            multiplier += bonuses[key]
    
    return int(base * multiplier)

# Initialize player statistics
department_stats = defaultdict(int)
dept_data = [('engineering', 12), ('marketing', 8), ('sales', 15), ('support', 11)]

for dept, score in dept_data:
    department_stats[dept] = score

# Define performance bonus structure
bonus_rules = {
    'engineering': 0.2,
    'sales': 0.3,
    'support': 0.1
}

# Irrelevant utility variable (minor distraction)
temp_buffer = [0] * 5

# Core computation
final_score = calculate_final_score(department_stats, bonus_rules)

print(f"Result: {final_score}")