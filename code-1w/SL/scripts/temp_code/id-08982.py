def calculate_performance(base, data):
    adjusted = [val - base for val in data if isinstance(val, (int, float))]
    positives = [x for x in adjusted if x > 0]
    if len(positives) == 0:
        return base // 2
    avg_positive = sum(positives) / len(positives)
    threshold = 5.0
    meets = [p for p in positives if p >= threshold]
    bonus = len(meets) * 1.5
    return avg_positive + bonus

baseline = 10
readings = [12, 15, 'N/A', 8, 18, None, 9, 20]
system_status = 'active'
version = '2.1.0'
final_score = calculate_performance(baseline, readings)
print(f"Result: {final_score}")