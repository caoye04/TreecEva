def calculate_final_score(participants):
    scores = []
    bonus_applied = set()
    
    for idx, (name, base, perf) in enumerate(participants):
        adjusted = base + perf * 3
        if 'senior' in name.lower():
            adjusted += 5
        if idx % 2 == 0:
            adjusted = int(adjusted * 1.1)
        scores.append(adjusted)
    
    threshold = sum(scores) / len(scores)
    
    for i, s in enumerate(scores):
        if s > threshold:
            bonus_applied.add(i)
    
    final_score = sum(s * 1.05 for i, s in enumerate(scores) if i in bonus_applied)
    
    temp_var_ignore = "cleanup"  # irrelevant distractor
    unused_list = [1, 2, 3]       # irrelevant distractor
    return int(final_score)

# Main data
participants = [
    ('Alice_senior', 80, 7),
    ('Bob_junior', 75, 6),
    ('Charlie_senior', 88, 8),
    ('Diana_junior', 70, 5)
]

final_score = calculate_final_score(participants)
print(f"Result: {final_score}")