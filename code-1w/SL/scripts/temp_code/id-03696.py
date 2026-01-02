def calculate_performance(base, data):
    adjusted = [val - base for val in data if val > base]
    outliers = {x for x in adjusted if x > 2 * sum(adjusted) / len(adjusted)}
    filtered = [x for x in adjusted if x not in outliers]
    return sum(filtered) if filtered else 0

baseline = 75
readings = [80, 92, 67, 88, 95, 74, 90]
initial_avg = sum(readings) / len(readings)
above_baseline_count = len([x for x in readings if x > baseline])
final_score = calculate_performance(baseline, readings)
print(f"Result: {final_score}")