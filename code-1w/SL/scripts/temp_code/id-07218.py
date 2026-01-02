def calculate_ranking(points, penalties):
    base_score = sum(points)
    deduction = len(penalties) * 2
    adjusted_score = base_score - deduction
    
    # Apply bonus for perfect category completion
    category_map = {'A': 3, 'B': 2, 'C': 1}
    bonus = 0
    for cat, count in penalties.items():
        if count == 0 and cat in category_map:
            bonus += category_map[cat]
    
    final_score = adjusted_score + bonus
    return final_score

# Simulation data
points = [85, 92, 78, 88]
penalties = {'A': 0, 'B': 1, 'C': 0}

# Execution
final_score = calculate_ranking(points, penalties)
print(f"Result: {final_score}")