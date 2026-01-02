from collections import defaultdict

# Simulate player stats and bonus multipliers
def calculate_base_performance(values):
    return sum(v ** 0.5 for v in values if v > 0)

def apply_multiplier(base, mult):
    return int(base * mult)

def calculate_final_score(player_stats, extra_bonuses):
    total = 0
    for category, values in player_stats.items():
        base_perf = calculate_base_performance(values)
        if category in extra_bonuses:
            total += apply_multiplier(base_perf, extra_bonuses[category])
    return total

# Irrelevant distraction: unused function
def analyze_trend(data):
    return [data[i+1] - data[i] for i in range(len(data)-1)]

# Player performance data
player_stats = {
    'speed': [25, 36, 49],
    'accuracy': [81, 64],
    'reaction': [16, 9, 4]
}

# Bonus multipliers by category
bonuses = {
    'speed': 1.2,
    'accuracy': 1.5,
    'reaction': 1.1
}

# Unused variable (minor distraction)
baseline_metrics = defaultdict(int)

final_score = calculate_final_score(player_stats, bonuses)
print(f"Result: {final_score}")