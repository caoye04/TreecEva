from collections import Counter

def process_performance(data, limit):
    counts = Counter(data)
    above_threshold = [k for k, v in counts.items() if v >= limit]
    scaled_values = [val * 1.5 for val in above_threshold]
    adjusted = sum(scaled_values) - len(above_threshold) * 0.5
    return int(adjusted)

# Irrelevant auxiliary variable (distractor)
baseline = [1, 2, 3]
recent_events = (4, 5)

metrics = [10, 10, 7, 7, 7, 5, 4]
threshold = 3

final_score = process_performance(metrics, threshold)
print(f"Result: {final_score}")