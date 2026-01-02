def calculate_performance(base, data):
    adjustment = lambda x: x * 1.5 if x > base else x * 0.8
    processed = [adjustment(val) for val in data]
    return sum(processed) // len(processed)

baseline = 75
metrics = [60, 80, 70, 95]

# Some auxiliary computation (minimal distraction)
temp_offset = 5
baseline_with_offset = baseline + temp_offset  # Not used in main logic

final_score = calculate_performance(baseline, metrics)
print(f"Result: {final_score}")