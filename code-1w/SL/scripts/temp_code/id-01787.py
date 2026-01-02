def evaluate_performance(records, limits):
    # Irrelevant transformation (distractor)
    processed = list(map(lambda x: (x[0], x[1] ** 0.5), records))
    
    # Semi-relevant pre-filtering
    filtered = [r for r in records if r[1] > 50]
    
    # Misleading aggregation (not used in final result)
    avg_raw = sum(r[1] for r in records) / len(records)
    high_performers = len([r for r in filtered if r[2] == 'A'])

    # Core logic begins: analyze pass/fail based on multiple criteria
    passing = 0
    bonuses = []
    for name, score, grade in records:
        met_threshold = score >= limits['score'] and grade in limits['grades']
        if met_threshold:
            passing += 1
            # Bonus calculated using bitwise manipulation (relevant)
            bonus_flag = (score & 7) == 1  # True only if score mod 8 == 1
            if bonus_flag:
                bonuses.append(len(name) % 5)
    
    # Secondary mechanism: string-based rule
    names_set = {r[0] for r in records}
    duplicates_removed = len(names_set) < len(records)
    
    # Distractor: unused set operation
    extra_names = {'X', 'Y', 'Z'}
    overlap = names_set & extra_names
    
    # Conditional expression with combinatorics
    combo_factor = 1
    if passing >= 2:
        # Simple combinatorics: C(passing, 2)
        combo_factor = (passing * (passing - 1)) // 2
    
    base_score = passing * 10 + sum(bonuses)
    adjustment = 0
    if duplicates_removed:
        adjustment = len(overlap) - 1  # Always zero or negative due to fixed set
    
    # Final computation (only this matters)
    final_score = base_score * combo_factor + adjustment
    
    # Print result as required
    return final_score

# Input data
student_data = [
    ('Alice', 85, 'A'),
    ('Bob', 60, 'B'),
    ('Charlie', 97, 'A'),  # 97 & 7 == 1 → True → bonus
    ('Diana', 72, 'A'),
    ('Eve', 45, 'F')
]

thresholds = {
    'score': 60,
    'grades': {'A', 'B'}
}

# Execute and print
final_score = evaluate_performance(student_data, thresholds)
print(f"Result: {final_score}")