def calculate_performance(base, data):
    adjusted = [val - base for val in data if val > base]
    outliers = {x for x in adjusted if x > 2 * sum(adjusted) / len(adjusted)}
    filtered = [x for x in adjusted if x not in outliers]
    performance = sum(filtered) if filtered else 0
    return performance + (10 if len(outliers) < 2 else 0)

baseline = 75
readings = [80, 90, 70, 95, 85, 60, 100]
initial_analysis = [r - baseline for r in readings]
discard_threshold = 25
flagged = [v for v in initial_analysis if abs(v) > discard_threshold]
final_score = calculate_performance(baseline, readings)
print(f"Result: {final_score}")