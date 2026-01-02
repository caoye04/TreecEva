def calculate_final_score(points, deductions):
    base = sum([p for p in points if p > 0])
    multiplier = 2 if base > 100 else 1
    adjusted = base * multiplier
    
    # Apply penalty adjustments using bitwise logic
    for d in deductions:
        if d & 1:  # odd penalty
            adjusted -= d ^ 3
        else:       # even penalty
            adjusted += d & 7
    
    return adjusted

# Simulation data
raw_points = [25, -10, 45, 60, 0, 30]
penalties = [4, 7, 2, 9]
temp_buffer = [x**2 for x in range(5)]  # irrelevant distractor list

final_score = calculate_final_score(raw_points, penalties)
print(f"Target result: {final_score}")