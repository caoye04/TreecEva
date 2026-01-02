def calculate_performance(base, data):
    adjust = lambda x: x * 1.5 if x > base else x * 0.8
    processed = [adjust(val) for val in data]
    avg = sum(processed) / len(processed)
    return int(avg + (base / 10))

baseline = 72
readings = [68, 75, 70, 80, 65]

# Irrelevant auxiliary variable (minor distraction)
temp_log = [f'Read: {r}' for r in readings]

final_score = calculate_performance(baseline, readings)
print(f"Result: {final_score}")