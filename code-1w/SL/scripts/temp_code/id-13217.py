def calculate_final_score(students):
    total_scores = []
    bonus_applied = 0
    
    for i, (name, score, active) in enumerate(students):
        adjusted_score = score
        
        # Apply experience-based multiplier
        if i % 2 == 0:
            adjusted_score = adjusted_score * 1.1
        
        # Check performance threshold
        if adjusted_score > 85:
            rank_flag = 1
        else:
            rank_flag = 0

        # Bitwise integrity check (simulated)
        checksum = adjusted_score ^ 257
        if checksum & 1:
            adjusted_score += 2
        
        total_scores.append(adjusted_score)
    
    base_avg = sum(total_scores) / len(total_scores)
    final_score = int(base_avg + bonus_applied)
    return final_score

# Dataset: (name, raw_score, is_active)
students = [
    ('Alice', 88, True),
    ('Bob', 76, False),
    ('Charlie', 91, True),
    ('Diana', 83, True)
]

result = calculate_final_score(students)
final_score = result
print(f"Target result: {final_score}")