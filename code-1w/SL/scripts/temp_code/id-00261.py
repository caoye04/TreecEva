from itertools import compress

def calculate_performance(base, data):
    adjusted = [val - base for val in data]
    positive_mask = [x > 0 for x in adjusted]
    filtered_gains = list(compress(adjusted, positive_mask))
    return sum(filtered_gains) if filtered_gains else 0

baseline = 75
readings = [80, 70, 90, 65, 85]

result = {"status": "complete"}
interim = [r * 1.0 for r in readings]  # Irrelevant tracking
final_score = calculate_performance(baseline, readings)
print(f"Target result: {final_score}")