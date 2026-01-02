from collections import Counter

def process_results(scores, threshold):
    count_freq = Counter(scores)
    above_threshold = list(filter(lambda x: x > threshold, scores))
    bonus = len(above_threshold) // 2
    base_score = sum(above_threshold)
    adjustment = base_score % 7 if base_score > 0 else 0
    final_score = base_score + bonus - adjustment
    return final_score

scores = [85, 90, 78, 92, 88, 76, 94, 87]
threshold = 85
initial_avg = sum(scores) / len(scores)
deviation = max(scores) - min(scores)
final_score = process_results(scores, threshold)
print(f"Result: {final_score}")