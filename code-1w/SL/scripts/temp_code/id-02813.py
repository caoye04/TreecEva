def calculate_performance(times, limit):
    valid = list(filter(lambda t: t < limit, times))
    count = len(valid) if valid else 0
    avg = sum(valid) / count if count > 0 else 0.0
    return round(avg * count, 3) if count > 0 else 0

# System performance metrics
run_times = [120, 85, 95, 110, 75, 130, 60]
threshold = 100
sample_size = len(run_times)  # Irrelevant distractor variable
baseline = 90  # Unused reference value

efficiency_score = calculate_performance(run_times, threshold)

print(f"Target result: {efficiency_score}")