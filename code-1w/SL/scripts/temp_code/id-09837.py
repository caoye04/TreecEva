def process_performance(data):
    weights = [0.2, 0.3, 0.5]
    weighted_components = [(val + 0.1) * w for val, w in zip(data, weights)]
    bonus = 5 if all(x > 0.4 for x in data) else 0
    base = sum(weighted_components)
    adjustment = (lambda x: x * 0.95 if x > 6 else x * 1.05)(base)
    return int(adjustment + bonus)

# Irrelevant auxiliary variable (minimal distraction)
initial_threshold = 0.35

metrics = [0.7, 0.5, 0.8]
final_score = process_performance(metrics)
print(f"Result: {final_score}")