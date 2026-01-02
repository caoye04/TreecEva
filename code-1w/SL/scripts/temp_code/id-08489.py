def calculate_performance(base, data):
    adjusted = list(map(lambda x: (x - base) ** 2, data))
    avg_adjusted = sum(adjusted) / len(adjusted)
    threshold = 50
    tolerance = 3
    if avg_adjusted > threshold:
        penalty = tolerance * 2
    else:
        penalty = tolerance
    return int(avg_adjusted // 2 - penalty)

baseline = 23
readings = [25, 20, 27, 22, 24]
extra_data = "irrelevant string that does nothing"
placeholder_value = len(extra_data)
final_score = calculate_performance(baseline, readings)
print(f"Result: {final_score}")