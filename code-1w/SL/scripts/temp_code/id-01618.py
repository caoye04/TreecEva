def process_results(data, limits):
    filtered = {k: v for k, v in data.items() if v >= limits['min_val']}
    values = list(filtered.values())
    adjusted = [v * 1.5 for v in values if v % 2 == 0]
    aggregate = sum(adjusted) + len(values)
    return int(aggregate // 1.7)

# Irrelevant auxiliary variables (minimal distraction)
user_preferences = {'theme': 'dark', 'notifications': True}
temp_buffer = [0] * 5

raw_data = {
    'metric_A': 8,
    'metric_B': 3,
    'metric_C': 12,
    'metric_D': 7,
    'metric_E': 16
}

thresholds = {'min_val': 5}

final_score = process_results(raw_data, thresholds)
print(f"Result: {final_score}")