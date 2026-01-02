def analyze_metrics(raw_values):
    # Irrelevant transformation (distractor)
    normalized = [round(x * 0.95 + 2.1, 2) for x in raw_values]
    filtered = [val for val in raw_values if val > 50]
    return sum(filtered) // len(filtered) if filtered else 0

# Simulated system health indicators (misleading data)
system_load = [85, 90, 78, 92, 88]
response_times = [120, 150, 110, 130, 145]

def track_activity(events):
    log_summary = {}
    for e in events:
        log_summary[e] = log_summary.get(e, 0) + 1
    # Complex but unused structure (dead code path)
    if len(log_summary) > 10:
        return {k: v for k, v in log_summary.items() if v > 1}
    return log_summary

event_stream = ['login', 'fetch', 'login', 'update', 'fetch', 'logout']
activity_log = track_activity(event_stream)

# Core benchmark data (relevant)
benchmark_data = {
    'round_a': [65, 70, 80, 75],
    'round_b': [85, 90],
    'round_c': [55, 60, 68]
}

# Auxiliary calculation with red herring variables
baseline_offset = 5
scaling_factor = 1.05  # Not actually used

# Misleading intermediate computation
efficiency_ratio = (len(system_load) * 10) / (sum(response_times) / 100)

# Real logic begins here — compute average of high-performing rounds
high_performers = []
for round_name, scores in benchmark_data.items():
    avg_score = sum(scores) / len(scores)
    if avg_score >= 70:
        high_performers.append(avg_score)

aggregate = 0
if high_performers:
    weighted_sum = 0
    for i, score in enumerate(high_performers):
        weight = 1 + (i * 0.1)
        weighted_sum += score * weight
    aggregate = weighted_sum / len(high_performers)

# Final adjustment using auxiliary function (but only on relevant data)
base_metric = analyze_metrics([int(x) for x in high_performers])

# Final performance score calculation
final_score = int(aggregate) + (base_metric // 10)

# Output result as required
print(f"Result: {final_score}")