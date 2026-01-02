def calculate_final_score(points, deductions):
    base_score = sum(points)
    penalty_set = set(deductions)
    reduction = len(penalty_set) * 2.5
    if base_score > 100:
        base_score = 100  # cap at maximum
    adjusted_score = base_score - reduction
    return round(adjusted_score, 3)

raw_points = [85.5, 10, 0.5]
penalties = ['late', 'format', 'late', 'clarity']

# Irrelevant utility function (minor interference)
def format_report(name):
    return f"Report: {name.upper()}".replace(' ', '_')

report_name = "project alpha"
formatted = format_report(report_name)

final_score = calculate_final_score(raw_points, penalties)
print(f"Result: {final_score}")