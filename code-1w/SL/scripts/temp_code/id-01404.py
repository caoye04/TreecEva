from collections import Counter

def process_performance(metrics, threshold):
    count_stats = Counter(metrics)
    above_threshold = list(filter(lambda x: x > threshold, metrics))
    bonus = len(above_threshold) * 1.5 if above_threshold else 0.0
    base_score = sum(count_stats.values())
    adjustment = 0
    for val in count_stats:
        if val % 2 == 0:
            adjustment += count_stats[val]
    final_score = base_score + bonus - adjustment
    return final_score

# Irrelevant auxiliary variable (minimal distraction)
ignore_data = [0, 2, 4]

data_stream = [3, 5, 6, 7, 5, 9, 6]
threshold = 4
final_score = process_performance(data_stream, threshold)
print(f"Target result: {final_score}")