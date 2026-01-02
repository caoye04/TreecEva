from collections import defaultdict

# Simulate student quiz scoring with bonus rules
def calculate_final_score(raw_scores, deductions):
    score_map = defaultdict(int)
    for i, score in enumerate(raw_scores):
        score_map[f'student_{i}'] = max(0, score)
    
    total = sum(score_map.values())
    penalty_sum = sum(abs(p) for p in deductions)
    
    # Apply bonus if average > 50 and no penalty exceeds 10
    avg = total / len(score_map) if score_map else 0
    has_large_penalty = any(p > 10 for p in deductions)
    bonus = 15 if avg > 50 and not has_large_penalty else 0
    
    result = total - penalty_sum + bonus
    return result

# Irrelevant utility function (minor distraction)
def normalize(value):
    return value / 100.0

scores = [85, 90, 78, -5, 92]
penalties = [3, 7, 12]
result = calculate_final_score(scores, penalties)
print(f"Result: {result}")