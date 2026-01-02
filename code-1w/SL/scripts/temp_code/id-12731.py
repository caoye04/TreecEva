from itertools import combinations

def analyze_trends(data):
    trend_pairs = list(combinations(data, 2))
    valid_trends = [pair for pair in trend_pairs if pair[1] > pair[0]]
    return len(valid_trends)

def calculate_performance(base, values):
    adjusted = [v - base for v in values]
    positive_shifts = [val for val in adjusted if val > 0]
    trend_count = analyze_trends(positive_shifts)
    avg_improvement = sum(positive_shifts) / len(positive_shifts) if positive_shifts else 0
    final_score = int(avg_improvement * trend_count)
    return final_score

# Experimental sensor baseline and readings
baseline = 78
readings = [85, 92, 79, 88, 95, 81]

# Calculation entry point
final_score = calculate_performance(baseline, readings)
print(f"Result: {final_score}")