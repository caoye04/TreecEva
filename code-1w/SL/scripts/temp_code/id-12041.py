def calculate_final_score(points, deductions):
    base = sum(points)
    penalty_total = len(deductions) * 2
    adjusted = base - penalty_total
    
    # Apply bonus for perfect round (no penalties)
    if not deductions:
        adjusted += 10
    
    # Check for consistency bonus (all scores above 7)
    if all(p > 7 for p in points):
        adjusted += 5
    
    return adjusted

# Simulation data
tournament_results = [8, 9, 7, 10, 8]
penalty_log = ['minor_delay', 'incorrect_timing']
raw_points = tuple(tournament_results)
penalties = set(penalty_log)

# Irrelevant string processing (minimal distraction)
description = "Final tournament results summary"
summary_tag = description.upper().replace(" ", "_")

final_score = calculate_final_score(raw_points, penalties)
print(f"Result: {final_score}")