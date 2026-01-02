def analyze_performance(marks, thresholds):
    # Irrelevant transformation (distractor)
    normalized = [round((m - min(marks)) / (max(marks) - min(marks)) * 100) for m in marks]
    
    # Semi-relevant filtering (some distraction)
    passing = list(filter(lambda x: x >= thresholds['pass'], marks))
    distinction = list(filter(lambda x: x >= thresholds['distinction'], marks))

    # Unused computation path (dead code - mild red herring)
    if len(passing) > len(distinction) * 2:
        adjustment_factor = 1.1
    else:
        adjustment_factor = 0.9  # Not actually used later

    # Core logic: compute score using set operations and conditions
    unique_marks = set(marks)
    high_performers = {m for m in unique_marks if m >= thresholds['distinction']}
    mid_performers = {m for m in unique_marks if thresholds['pass'] <= m < thresholds['distinction']}

    # Additional distraction: unused helper
    def smooth_data(data):
        return [data[i] for i in range(0, len(data), 2)]

    bonus_points = 0
    if len(high_performers) >= 3:
        bonus_points += 10
    elif len(mid_performers) >= 5:
        bonus_points += 5

    base_score = len(passing) * 2 + len(high_performers) * 3

    # Conditional expression with logical checks
    penalty = 0
    has_improvement = any(marks[i] < marks[i+1] for i in range(len(marks)-1))
    trend_consistent = all(marks[i] <= marks[i+1] for i in range(len(marks)-1))

    if has_improvement and not trend_consistent:
        penalty = 3

    # Final score calculation (key point)
    final_score = base_score + bonus_points - penalty

    # Distractor: irrelevant tuple unpacking
    _, _, *leftover = sorted(unique_marks)

    # Print result as required
    print(f"Result: {final_score}")
    return final_score

# Input data
exam_marks = [68, 72, 79, 85, 62, 91, 88, 75, 85]
cutoffs = {'pass': 70, 'distinction': 85}

# Execution entry point
final_score = analyze_performance(exam_marks, cutoffs)