def calculate_final_score(points, deductions):
    base = sum(points)
    penalty_total = 0
    for entry in deductions:
        if 'minor' in entry:
            penalty_total += 1
        elif 'major' in entry:
            penalty_total += 3
    
    adjusted = base - penalty_total
    
    # Apply bonus if no major penalties
    if 'major' not in ''.join(deductions):
        adjusted += 5
    
    return adjusted

# Simulated input data
event_logs = ['start', 'checkpoint', 'finish']
raw_points = [10, 15, 20, 12]
penalties = ['minor_slow_start', 'clean_run', 'minor_late_finish']

initial_check = len(event_logs) >= 3
bonus_awarded = False

if initial_check:
    final_score = calculate_final_score(raw_points, penalties)
else:
    final_score = sum(raw_points)

print(f"Result: {final_score}")