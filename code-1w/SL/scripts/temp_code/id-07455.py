def analyze_response_time(base_time, load_factor):
    adjusted = base_time * (1 + load_factor / 100)
    penalty = 0.0
    if adjusted > 2.0:
        penalty = (adjusted - 2.0) * 1.5
    return adjusted - penalty

# Simulate user feedback processing in a performance evaluation system
task_loads = [12, 8, 15, 6, 10]
response_times = [1.8, 2.3, 1.9, 2.7, 2.1]
weights = [0.2, 0.3, 0.1, 0.25, 0.15]

feedback_list = []
for i in range(len(task_loads)):
    normalized_load = task_loads[i] / max(task_loads)
    efficiency = 1 - (normalized_load * 0.4)
    raw_time = response_times[i]
    corrected_time = analyze_response_time(raw_time, task_loads[i])
    score_component = (1 / corrected_time) * efficiency * 100
    temp_diagnostic = (raw_time + normalized_load) ** 0.5  # unused diagnostic metric
    category_label = 'optimal' if corrected_time <= 2.0 else 'delayed'
    feedback_list.append({
        'index': i,
        'score_val': score_component,
        'status': category_label,
        'time_adj': corrected_time
    })

# Extraneous helper: computes entropy but not used in final path
def compute_entropy(values):
    total = sum(values)
    probs = [v / total for v in values if v > 0]
    return -sum(p * __import__('math').log2(p) for p in probs)

entropy_distractor = compute_entropy([f['score_val'] for f in feedback_list])

# Core aggregation logic with lambda and list comprehension
aggregate_performance = lambda entries: round(sum(
    [e['score_val'] * weights[e['index']] for e in entries]
), 4)

baseline_shift = 5.0
shift_log = []
for _ in range(3):
    shift_log.append(baseline_shift)
    baseline_shift *= 0.9  # irrelevant decay simulation

final_score = aggregate_performance(feedback_list)
print(f"Result: {final_score}")