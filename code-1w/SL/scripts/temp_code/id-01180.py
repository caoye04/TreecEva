def analyze_data(records):
    totals = {}
    counts = {}
    for r in records:
        key = r['category']
        value = r['value']
        if key not in totals:
            totals[key] = 0
            counts[key] = 0
        totals[key] += value
        counts[key] += 1

    averages = {k: totals[k] / counts[k] for k in totals}
    return averages


def normalize_values(data_list):
    # Irrelevant normalization function (dead code path)
    max_val = max(data_list) if data_list else 1
    return [x / max_val for x in data_list] if max_val != 0 else data_list


def compute_rankings(items):
    # Another decoy function with misleading logic
    sorted_items = sorted(items, key=lambda x: x[1], reverse=True)
    ranking = {}
    for idx, (name, _) in enumerate(sorted_items):
        ranking[name] = idx + 1
    return ranking

# Misleading metrics and fake weights
temp_metrics = {'latency': 85, 'throughput': 120, 'error_rate': 0.04, 'jitter': 5.6}
decoys = [0.1, 0.3, 0.2, 0.4]
fake_weights = {k: v * 1.5 for k, v in zip(temp_metrics.keys(), decoys)}

# Actual performance metrics used in calculation
metrics = {
    'efficiency': 92,
    'stability': 97,
    'responsiveness': 88,
    'scalability': 94
}

# Distractor: unused intermediate calculations
intermediate_results = []
for i, (k, v) in enumerate(zip(metrics.keys(), metrics.values())):
    adjusted = v * (i + 1) ** 0.5
    intermediate_results.append(adjusted)

# Fake transformation using enumerate and zip (irrelevant)
dummy_labels = ['A', 'B', 'C', 'D']
for i, (label, metric) in enumerate(zip(dummy_labels, metrics)):
    _ = f"{label}_{i}_{metric}"

# Real weights for evaluation (aligned with actual keys)
weights = {
    'efficiency': 0.3,
    'stability': 0.35,
    'responsiveness': 0.2,
    'scalability': 0.15
}

# Secondary distractor: sorting unrelated data
log_entries = [
    {'level': 'INFO', 'code': 200},
    {'level': 'WARN', 'code': 400},
    {'level': 'ERROR', 'code': 500}
]
sorted_logs = sorted(log_entries, key=lambda x: x['code'])

# Conditional red herring
threshold = 90
boost_factor = 1.1
if metrics['stability'] > threshold:
    # This block runs but doesn't affect final_score
    boosted = {k: v * boost_factor for k, v in metrics.items()}

# Core computation buried among distractions
def evaluate_performance(metrs, wts):
    score = 0.0
    for key in metrs:
        if key in wts:
            score += metrs[key] * wts[key]
    return int(score)  # Final score is integer

# Unused recursive distraction
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

unused_seq = [fibonacci(i) for i in range(8)]

# Key execution point
final_score = evaluate_performance(metrics, weights)

# Output result as required
print(f"Target result: {final_score}")