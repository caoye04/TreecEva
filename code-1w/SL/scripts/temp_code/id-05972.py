def calculate_final_score(results):
    total_score = 0
    bonus_applied = False
    for i, (subject, score) in enumerate(results):
        if score >= 85:
            total_score += score * 1.1 if not bonus_applied else score
            bonus_applied = True
        elif score >= 70:
            total_score += score + 5
        else:
            total_score += score
    return int(total_score)

exam_results = [
    ('Math', 90),
    ('Physics', 78),
    ('Chemistry', 88),
    ('Biology', 65)
]

# Irrelevant helper (minor distraction)
def format_subject(s):
    return s.upper().replace(' ', '_')

# Key computation
final_list = [format_subject(sub) for sub, _ in exam_results]
total_score = calculate_final_score(exam_results)

print(f"Result: {total_score}")