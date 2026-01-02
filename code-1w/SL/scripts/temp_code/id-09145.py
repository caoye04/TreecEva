from itertools import compress

def evaluate_performance(output, time_taken):
    base_score = output * 1.5
    penalty = 0.1 * time_taken
    if base_score >= 50:
        bonus = 10
    else:
        bonus = 2
    return base_score - penalty + bonus

def analyze_team_performance():
    # Simulated daily productivity (units completed)
    productivity = 45
    # Time spent in hours (normalized to standard workday)
    efficiency = 7.5

    # Irrelevant metric: number of breaks taken (not used in calculation)
    breaks_taken = 3

    # Core computation
    final_score = evaluate_performance(productivity, efficiency)
    
    # Additional unused list for mild distraction
    daily_targets = [40, 50, 60]
    target_met = list(compress(daily_targets, [t <= productivity for t in daily_targets]))

    return final_score

result = analyze_team_performance()
print(f"Result: {result}")