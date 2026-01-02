def analyze_productivity(hours, efficiency_map):
    base_output = 0
    peak_hours = 0
    for hour in hours:
        if hour > 6:
            peak_hours += 1
        base_output += hour * 1.5
    
    bonus = 0
    for level, multiplier in efficiency_map.items():
        if level < 3:
            bonus += multiplier * 2
    
    adjustment = len(hours) - peak_hours
    raw_performance = base_output + bonus - adjustment
    
    # Irrelevant distraction: tracking unused metric
    idle_periods = 0
    for h in hours:
        if h < 2:
            idle_periods += 1
    
    return int(raw_performance)

hours_worked = [5, 8, 6, 9, 4]
efficiency_ratings = {1: 2.1, 2: 1.8, 4: 0.9}  # Level 3 missing

initial_estimate = sum(hours_worked) * 2.0
final_score = analyze_productivity(hours_worked, efficiency_ratings)

Result: final_score