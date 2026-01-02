def calculate_performance(base, data):
    adjustment = lambda x: x * 1.5 if x > base else x * 0.8
    filtered = [adjustment(val) for val in data if val != 0]
    avg = sum(filtered) / len(filtered) if filtered else 0
    return int(avg + base // 10)

baseline = 40
readings = [25, 0, 60, 30, 55]
initial_check = baseline * 2  # Irrelevant distractor
final_score = calculate_performance(baseline, readings)
print(f"Target result: {final_score}")