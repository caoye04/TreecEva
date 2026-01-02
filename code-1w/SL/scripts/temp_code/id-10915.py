from itertools import combinations

def evaluate_metric(x, y):
    return (x + y) * 0.5 if x > 0 and y > 0 else 0

def calculate_performance(base, data):
    smoothed = list(map(lambda z: z * 0.9, data))
    pairs = list(combinations(smoothed[:4], 2))
    scores = [evaluate_metric(a, b) for a, b in pairs]
    aggregate = sum(scores)
    final_score = base + aggregate
    return final_score

baseline = 15
metrics = [4, 6, 8, 2, 10]
final_score = calculate_performance(baseline, metrics)
print(f"Result: {final_score}")