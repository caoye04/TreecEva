def calculate_final_score(points, deductions):
    base = sum(points)
    penalty_total = 0
    for entry in deductions:
        if 'minor' in entry:
            penalty_total += 1
        elif 'major' in entry:
            penalty_total += 3
    
    # Apply bonus if no major penalties
    if penalty_total < 5:
        base += 10
    
    return base - penalty_total

# Simulated input data from user submissions
timestamps = ['2023-08-01', '2023-08-02']
raw_points = [15, 20, 10]
penalties = ['minor_late', 'none', 'major_incomplete']

# Irrelevant string processing (minimal distraction)
date_parts = timestamps[0].split('-')
year = int(date_parts[0])

final_score = calculate_final_score(raw_points, penalties)
print(f"Result: {final_score}")