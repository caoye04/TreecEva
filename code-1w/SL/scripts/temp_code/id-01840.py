from collections import defaultdict

def calculate_final_score(raw_scores, deductions):
    total_score = 0
    penalty_map = defaultdict(int)
    
    for idx, penalty in enumerate(deductions):
        penalty_map[idx] = penalty * 0.5
    
    for i, score in enumerate(raw_scores):
        if i % 2 == 0:
            total_score += score * 1.1
        else:
            total_score += score
    
    for val in penalty_map.values():
        total_score -= val

    return int(total_score)

# Irrelevant auxiliary variable (mild distraction)
config = {'version': '2.1', 'debug': False}

scores = [85, 90, 78, 92]
penalties = [10, 5, 8, 3]
total_score = calculate_final_score(scores, penalties)
print(f"Result: {total_score}")