def analyze_trends(data, baseline):
    trend_map = {}
    adjustments = []
    for key, values in data.items():
        avg = sum(values) / len(values)
        delta = avg - baseline
        trend_map[key] = avg
        if delta > 5:
            adjustments.append((key, delta * 0.8))
        elif delta < -5:
            adjustments.append((key, delta * 0.3))
    return trend_map, adjustments

# Irrelevant helper (distractor)
def normalize(x):
    return x / (abs(x) + 1) if x != 0 else 0

# Data processing with red herrings
raw_data = {
    'temperature': [23, 25, 27, 29, 30],
    'humidity': [45, 50, 52, 51, 49],
    'pressure': [1013, 1012, 1015, 1016, 1014]
}

baseline_ref = 26
summary_stats, corrections = analyze_trends(raw_data, baseline_ref)

# Misleading intermediate calculations (dead computations)
total_fluctuation = 0
for readings in raw_data.values():
    total_fluctuation += max(readings) - min(readings)

scaling_factor = 1.2  # Unused in final logic
offset_buffer = tuple(x * 0.1 for x in (10, 20, 30))  # Dead code

# Core evaluation logic
metrics = {
    'stability': 85,
    'consistency': 76,
    'adaptability': 92,
    'efficiency': 68
}

weights = {
    'stability': 0.3,
    'consistency': 0.25,
    'adaptability': 0.35,
    'efficiency': 0.1
}

# Lambda-based weighted scorer (core concept)
evaluate_performance = lambda m, w: sum(m[k] * w[k] for k in m)

# Key statement
final_score = evaluate_performance(metrics, weights)

# Print result as required
print(f"Result: {final_score}")