def calculate_performance(base, data):
    adjusted = [val - base for val in data]
    positives = [x for x in adjusted if x > 0]
    normalized = sum(positives) / len(data) if data else 0
    return int(normalized * 100) // 10 if normalized > 0.5 else int(normalized * 10)

baseline = 75
readings = [80, 88, 72, 90, 68, 85]
dummy_flag = True
temp_offset = 5

# Key computation
final_score = calculate_performance(baseline, readings)
print(f"Target result: {final_score}")