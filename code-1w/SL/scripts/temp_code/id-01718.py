def analyze_trends(data, threshold=5):
    high_impact = [x for x in data if x > threshold]
    low_impact = [x for x in data if x <= threshold]
    return len(high_impact) - len(low_impact)

weights = [0.8, 1.2, 0.9, 1.5, 1.1]
def compute_baseline(values):
    base = sum(values) / len(values)
    adjusted = [v * weights[i % len(weights)] for i, v in enumerate(values)]
    return sum(adjusted) / len(adjusted)

def evaluate_stability(readings):
    diffs = [abs(readings[i] - readings[i-1]) for i in range(1, len(readings))]
    return all(d < 3 for d in diffs)

readings_data = [4, 7, 6, 5, 8]
baseline_metric = compute_baseline(readings_data)

stability_flag = evaluate_stability(readings_data)

feedback_raw = [5, 3, 8, 2, 9, 4, 7]
feedback_filtered = list(filter(lambda x: x % 2 == 1, feedback_raw))
feedback_set = set(feedback_filtered)

# Irrelevant transformation
transformed = {x: x**2 for x in feedback_set}
duplicate_check = len(feedback_raw) != len(set(feedback_raw))

# Unused accumulator
running_total = 0
for val in feedback_set:
    running_total += val * 0.1

# Core logic with distractors
aggregate_performance = lambda s: sum(s) + analyze_trends(list(s), threshold=4)

final_score = aggregate_performance(feedback_set)
print(f"Result: {final_score}")