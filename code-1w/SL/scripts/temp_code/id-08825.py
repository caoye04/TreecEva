from itertools import compress

def calculate_final_score(scores, importance):
    normalized = [score / 100 for score in scores]
    weighted = [n * w for n, w in zip(normalized, importance)]
    total = sum(weighted)
    bonus = 5 if total > 0.8 else 0
    return int(total * 100) + bonus

def analyze_performance(logs):
    counts = {}
    for event in logs:
        if event in counts:
            counts[event] += 1
        else:
            counts[event] = 1
    return counts

events = ['login', 'file_access', 'logout', 'login', 'settings_change']
raw_scores = [85, 90, 78, 92]
weights = [0.2, 0.3, 0.15, 0.35]

# Irrelevant utility function (minor distraction)
analysis_result = analyze_performance(events)

final_score = calculate_final_score(raw_scores, weights)
print(f"Result: {final_score}")