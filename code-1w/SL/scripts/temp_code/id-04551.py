def calculate_performance(base, data):
    adjustment = lambda x: x * 1.5 if x > base else x * 0.8
    processed = [adjustment(val) for val in data]
    return round(max(processed) - min(processed), 3)

baseline = 42
metrics = [30, 45, 50, 38]

# Irrelevant auxiliary variable (minor distraction, intervention=4)
temp_log = [f'val_{i}' for i in range(len(metrics))]

final_score = calculate_performance(baseline, metrics)
print(f"Result: {final_score}")