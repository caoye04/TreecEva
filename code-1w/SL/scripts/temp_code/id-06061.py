def analyze_performance(scores):
    bonus = 5
    penalties = 2
    adjusted_scores = [score + bonus for score in scores]
    filtered_performance = [score for score in adjusted_scores if score > 50]
    total_score = sum(filtered_performance)
    return total_score

result = analyze_performance([40, 48, 55, 60, 45])
print(f"Result: {result}")