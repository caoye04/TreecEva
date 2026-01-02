def analyze_efficiency(data_points):
    threshold = 75
    filtered = [x for x in data_points if x > threshold]
    return sum(filtered) // len(filtered) if filtered else 0

# Simulate system diagnostics with mixed metrics
data_stream = [68, 82, 91, 74, 85, 93, 67, 88]

diagnostic_mean = sum(data_stream) / len(data_stream)

outlier_count = 0
for val in data_stream:
    if abs(val - diagnostic_mean) > 15:
        outlier_count += 1

# Secondary validation pass (distractor: not used later)
validations = []
for i in range(len(data_stream)):
    if i % 2 == 0 and data_stream[i] > 80:
        validations.append(True)

# Core logic for performance evaluation
def evaluate_performance(weights, outcomes):
    weighted_sum = 0
    for i in range(min(len(weights), len(outcomes))):
        weighted_sum += weights[i] * outcomes[i]
    return int(weighted_sum)

# Irrelevant transformation chain (distractor)
transform = lambda x: x ** 0.5
interim_values = list(map(transform, [x * 2 for x in data_stream[:4]]))
adjusted_interim = [round(v) for v in interim_values]

# Actual metric computation path
efficiency_baseline = analyze_efficiency(data_stream)
consistency_ratio = (len(data_stream) - outlier_count) / len(data_stream)

raw_outcomes = [
    efficiency_baseline,
    diagnostic_mean,
    consistency_ratio * 100,
    len(validations) * 5
]

metric_weights = [0.4, 0.3, 0.2, 0.1]

# Key statement
final_score = evaluate_performance(metric_weights, raw_outcomes)

# Print result
print(f"Result: {final_score}")