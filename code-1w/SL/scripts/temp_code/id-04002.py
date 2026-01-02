def calculate_final_score(raw_scores, thresholds):
    total_score = 0
    bonus_applied = False
    
    for i, score in enumerate(raw_scores):
        if score >= thresholds[i]:
            adjustment = 10
            total_score += adjustment
            
            # Irrelevant tracking variable (minimal distraction)
            status_log = f'Score {i} met threshold'
            
            if not bonus_applied and score > thresholds[i] + 5:
                total_score += 5
                bonus_applied = True
        else:
            adjustment = -5
            total_score += adjustment

    # Additional unrelated but harmless computation
    avg = sum(raw_scores) / len(raw_scores) if raw_scores else 0

    return total_score

# Input data
raw_scores = [78, 85, 90, 67]
thresholds = [75, 80, 88, 70]

result = calculate_final_score(raw_scores, thresholds)
print(f'Result: {result}')