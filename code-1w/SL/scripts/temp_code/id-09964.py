from collections import defaultdict

# Simulated benchmark results across test categories
test_categories = ['arithmetic', 'logic', 'assignment', 'control_flow']
raw_scores = [88, 74, 91, 65]
benchmark_results = defaultdict(int)

for i, cat in enumerate(test_categories):
    benchmark_results[cat] = raw_scores[i]

# Irrelevant distractor: unused tracking map
evaluation_flags = {'strict': True, 'skip_invalid': False}

# Weight mapping using lambda for dynamic adjustment
weight_func = lambda x: 0.5 + (x / 100) * 0.5  # Increases weight based on score
weights = {cat: weight_func(score) for cat, score in benchmark_results.items()}

# Calculate weighted performance
weighted_total = 0
for cat in benchmark_results:
    weighted_total += benchmark_results[cat] * weights[cat]

# Normalize by sum of weights
total_weight = sum(weights.values())
normalized_performance = weighted_total / total_weight

# Additional processing step: apply experience bonus if above threshold
experience_bonus = 0
if normalized_performance > 75:
    experience_bonus = 10

final_score = int(normalized_performance + experience_bonus)

print(f"Result: {final_score}")