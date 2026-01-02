def process_performance(data, limit):
    filtered = [x for x in data if x > limit]
    adjusted = list(map(lambda x: x * 0.9 + 5, filtered))
    return sum(adjusted) // len(adjusted) if adjusted else 0

# Irrelevant auxiliary variables (minor distraction)
baseline = [70, 75, 80]
dummy_text = "Performance review Q3"
dummy_set = {1, 2, 3}

metrics = [88, 92, 76, 85, 90, 83]
threshold = 84

# Key computation
final_score = process_performance(metrics, threshold)
print(f"Result: {final_score}")