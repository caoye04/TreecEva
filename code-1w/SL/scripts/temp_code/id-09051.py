def calculate_final_score(points, deductions):
    base = sum(points)
    penalty_total = 0
    for entry in deductions:
        if 'minor' in entry['type']:
            penalty_total += entry['value']
        elif 'major' in entry['type']:
            penalty_total += entry['value'] * 2
    return base - penalty_total

# Raw performance points from assessment
raw_points = [85, 90, 78, 92]

# Penalty records with descriptive metadata
penalties = [
    {'type': 'minor', 'value': 3, 'reason': 'formatting'},
    {'type': 'major', 'value': 5, 'reason': 'logic_error'},
    {'type': 'minor', 'value': 2, 'reason': 'naming'}
]

# Irrelevant string processing (minimal distraction)
dummy_text = "assessment_complete"
status_flag = dummy_text.upper().replace("_", " ")

# Core computation
final_score = calculate_final_score(raw_points, penalties)
print(f"Result: {final_score}")