def calculate_performance(entries, weights):
    base = list(map(lambda x: x ** 0.5, entries))
    weighted_vals = []
    for k in weights:
        if k < len(base):
            weighted_vals.append(base[k] * weights[k])
    return round(sum(weighted_vals), 3)

# Irrelevant auxiliary data (mild distraction)
user_preferences = {'theme': 'dark', 'notifications': True}
system_log = ["init", "load", "complete"]

# Core input data
scores = [16, 25, 36, 49, 64]
weight_map = {0: 0.5, 2: 1.5, 4: 2.0}

# Key computation
final_score = calculate_performance(scores, weight_map)

print(f"Result: {final_score}")