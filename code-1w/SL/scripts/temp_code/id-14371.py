from itertools import compress

def evaluate_performance(hours_worked, defect_count):
    base_score = sum(hours_worked) * 10
    penalty = sum(defect_count) * 5
    
    # Filter days with above-average productivity
    avg_hours = sum(hours_worked) / len(hours_worked)
    high_productivity_days = list(compress(hours_worked, (h > avg_hours for h in hours_worked)))
    
    # Bonus for consecutive high-productivity days
    bonus = 0
    consecutive = 0
    for day_hours in hours_worked:
        if day_hours > avg_hours:
            consecutive += 1
            bonus += consecutive * 2  # increasing bonus for streaks
        else:
            consecutive = 0
    
    # Irrelevant distraction: count characters in a status message
    status = "Performance review completed"
    char_count = len(status.replace(" ", ""))
    
    final_score = base_score - penalty + bonus
    return final_score

# Work log for a 5-day week
productivity = [7, 9, 8, 10, 6]
errors = [2, 1, 3, 0, 4]

# Unused variable (minor distraction)
temp_report = {"version": "1.2", "author": "mgr"}

final_score = evaluate_performance(productivity, errors)
print(f"Target result: {final_score}")