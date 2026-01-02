def calculate_final_score(results, bonus_enabled):
    base_score = 0
    multiplier = 1
    
    # Aggregate exam scores with weighting
    for subject, score in results.items():
        if score >= 75:
            base_score += score * 0.8
        else:
            base_score += score * 0.5
    
    # Apply logical bonus condition
    high_performers = sum(1 for s in results.values() if s >= 80)
    if high_performers >= 2 and bonus_enabled:
        multiplier = 1.2
    
    temp_adjustment = 5  # Irrelevant distraction (minimal interference)
    unused_flag = False   # Distractor variable

    return int(base_score * multiplier)

# Main data setup
exam_results = {
    'math': 88,
    'physics': 76,
    'chemistry': 81,
    'biology': 69
}
bonus_active = True

initial_total = sum(exam_results.values())  # Slight distraction, not used in final logic

final_score = calculate_final_score(exam_results, bonus_active)
print(f"Result: {final_score}")