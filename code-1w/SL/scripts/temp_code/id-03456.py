from collections import Counter
def calculate_final_score(scores, penalties):
    total_score = sum(scores)
    deductions = sum(penalties)
    freq = Counter(scores)
    bonus = freq.most_common(1)[0][1] * 2 if freq else 0
    final_adjustment = (total_score - deductions + bonus)
    result = final_adjustment if final_adjustment > 0 else 0
    return result

def analyze_performance(logs):
    # Irrelevant auxiliary function (distractor)
    return len(logs) > 0

scores = [85, 92, 78, 92, 88]
penalties = [10, 5]
logs = ['start', 'checkpoint', 'end']
analyze_performance(logs)
result = calculate_final_score(scores, penalties)
print(f"Result: {result}")