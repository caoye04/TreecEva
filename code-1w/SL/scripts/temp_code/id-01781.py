def analyze_performance(marks, thresholds):
    # Irrelevant statistics
    avg_mark = sum(marks) / len(marks)
    variance = sum((x - avg_mark) ** 2 for x in marks) / len(marks)
    high_performers = {i for i, m in enumerate(marks) if m > thresholds[1]}
    low_performers = {i for i, m in enumerate(marks) if m < thresholds[0]}

    # Distractor: unused helper
    def normalize(values):
        min_val, max_val = min(values), max(values)
        return [(v - min_val) / (max_val - min_val) for v in values]

    # Key computation with distraction
    adjusted_marks = []
    bonus_applied = 0
    for idx, mark in enumerate(marks):
        if mark >= thresholds[1]:
            adjusted = mark * 1.1
            if adjusted > 100:
                adjusted = 100
            adjusted_marks.append(adjusted)
            bonus_applied += 1
        elif mark < thresholds[0]:
            adjusted_marks.append(mark * 0.9)
        else:
            adjusted_marks.append(mark)

    # Use of zip and enumerate in semi-relevant context
    rank_map = {}
    sorted_marks = sorted(adjusted_marks, reverse=True)
    for rank, (orig_idx, mark) in enumerate(zip(range(len(adjusted_marks)), adjusted_marks)):
        rank_map[orig_idx] = rank + 1

    # Secondary distractor calculation
    median_mark = sorted_marks[len(sorted_marks) // 2]
    outlier_count = len([m for m in adjusted_marks if abs(m - avg_mark) > 2 * (variance ** 0.5)])

    # Core logic buried among distractions
    base_score = sum(adjusted_marks)
    penalty = len(low_performers) * 2.5
    reward = bonus_applied * 3.7
    final_score = base_score - penalty + reward

    # Red herring: dead code path
    if False:
        final_score = max(final_score, 50)

    return final_score

# Input data
student_marks = [85, 92, 78, 63, 96, 88, 54, 73]
cutoffs = [60, 85]

# Execute
result = analyze_performance(student_marks, cutoffs)
print(f"Result: {result}")