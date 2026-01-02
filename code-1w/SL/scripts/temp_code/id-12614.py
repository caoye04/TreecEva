def calculate_final_score(results):
    total = 0
    bonus_applied = False
    for subject, score_str in results.items():
        if 'math' in subject.lower():
            score = int(score_str.strip('%'))
            total += score
            if score > 85 and not bonus_applied:
                total += 10  # Bonus for high math performance
                bonus_applied = True
        elif 'science' in subject.lower():
            clean_val = score_str.replace('*', '').strip()
            score = float(clean_val)
            total += score
    return total

exam_results = {
    'Mathematics': '92%',
    'Physics': '88.5*',
    'Chemistry': '76',
    'Biology': '81',
    'Advanced_Math': '87%'
}

# Irrelevant tracking variable (minimal distraction)
processed_count = len(exam_results)

final_score = calculate_final_score(exam_results)
print(f"Result: {final_score}")