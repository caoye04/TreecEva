def analyze_frequency(text):
    freq = {}
    for char in text.lower():
        if char.isalpha():
            freq[char] = freq.get(char, 0) + 1
    return freq

raw_data = 'ProgrammingLanguagesAreFunToWorkWith'
char_freq = analyze_frequency(raw_data)

total_chars = sum(char_freq.values())
distinct_chars = len(char_freq)
redundancy_factor = (total_chars - distinct_chars) / total_chars if total_chars else 0

# Dummy metrics for various subsystems
system_load = [0.45, 0.67, 0.89, 0.34, 0.78]
response_times = [120, 230, 180, 95, 310]
error_rates = [0.01, 0.03, 0.02, 0.05, 0.01]

# Irrelevant aggregation (distractor)
avg_response = sum(response_times) / len(response_times)
peak_load = max(system_load)
min_error = min(error_rates)

# Simulate normalization of error rates via lambda
normalized_errors = list(map(lambda x: round(1 - x, 2), error_rates))

# Key data structure: performance metrics dictionary
metrics = {
    'latency': sum(response_times) / len(response_times),
    'stability': 100 * (1 - sum(error_rates) / len(error_rates)),
    'throughput': len(raw_data) / (sum(response_times) / 100),
    'consistency': distinct_chars / 26.0
}

# Weighting scheme using dictionary and lambda
weight_fn = lambda base: {k: v * base for k, v in {'latency': 0.2, 'stability': 0.4, 'throughput': 0.25, 'consistency': 0.15}.items()}
weights = weight_fn(1.0)

# Misleading alternate weights (dead path)
alt_weights = weight_fn(0.85)
shadow_value = sum(alt_weights.values()) * redundancy_factor  # unused

# Core evaluation logic
weighted_sum = 0.0
max_possible = 0.0
for key in metrics:
    norm_metric = min(metrics[key] / 100.0, 1.0)  # normalize to 0-1 scale
    weighted_sum += norm_metric * weights[key]
    max_possible += weights[key]

# Final computation
final_score = round(weighted_sum * 100 / max_possible, 2) if max_possible > 0 else 0

# Output result
print(f"Result: {final_score}")