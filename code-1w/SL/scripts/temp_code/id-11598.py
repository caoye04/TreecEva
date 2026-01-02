import itertools

# Simulated system metrics from a distributed task scheduler
task_durations = [12, 15, 10, 20, 8, 25]
completion_flags = [True, True, False, True, True, False]
resource_usage = [0.65, 0.72, 0.54, 0.83, 0.69, 0.91]
arrival_order = list(range(len(task_durations)))

# Irrelevant transformations (distractors)
decoy_transform = [x ** 2 for x in task_durations if x > 10]
shadow_map = {i: val for i, val in enumerate(resource_usage) if val < 0.8}
useless_pairs = list(itertools.combinations(arrival_order[:4], 2))
offset_correction = sum([i * 0.1 for i in range(5)])

# Weight configuration for performance evaluation (critical)
weights = {
    'time_efficiency': 0.4,
    'completeness': 0.3,
    'resource_balance': 0.2,
    'priority_adherence': 0.1
}

# Auxiliary function – looks important but only some parts are used
def calculate_time_efficiency(times):
    avg_duration = sum(times) / len(times)
    peak_duration = max(times)
    normalized_efficiency = (peak_duration - avg_duration) / peak_duration
    return 1 - normalized_efficiency

# Unused decoy function (red herring)
def analyze_fault_tolerance(flags):
    failed_count = flags.count(False)
    recovery_rate = (len(flags) - failed_count) / len(flags)
    risk_score = failed_count * 10
    return {'recovery_rate': recovery_rate, 'risk_score': risk_score}

# Core logic with distractors embedded
def evaluate_task_completion(flags):
    completed = flags.count(True)
    total = len(flags)
    return completed / total if total else 0

# Another irrelevant helper
def compute_pairwise_gaps(lst):
    if len(lst) < 2:
        return []
    return [abs(lst[i] - lst[i+1]) for i in range(len(lst)-1)]

# Key function combining multiple concepts
def evaluate_performance(metrics, w):
    durations, flags, resources = metrics['durations'], metrics['flags'], metrics['resources']
    
    # Real computation branches
    time_metric = calculate_time_efficiency(durations)
    completion_metric = evaluate_task_completion(flags)
    
    # Fake dependency (never actually affects result)
    _ = [x * 1.5 for x in resources if x > 0.7]  
    
    # Actual resource balance score
    balanced_resources = sum(1 for r in resources if 0.6 <= r <= 0.8)
    balance_ratio = balanced_resources / len(resources)
    
    # Simulated priority adherence via arrival and duration correlation
    sorted_indices = sorted(range(len(durations)), key=lambda i: durations[i])
    rank_correlation = 0
    for i, idx in enumerate(sorted_indices):
        if idx == i or idx == len(durations) - 1 - i:
            rank_correlation += 1
    priority_score = rank_correlation / len(durations)
    
    # Final weighted score — this is what matters
    score = (
        w['time_efficiency'] * time_metric +
        w['completeness'] * completion_metric +
        w['resource_balance'] * balance_ratio +
        w['priority_adherence'] * priority_score
    )
    
    # Dead code path — looks like post-processing
    if score > 1.0:
        score = 0.95  # Never reached
    elif score < 0.0:
        score = 0.1  # Also never reached
    
    return round(score * 100, 4)  # Scale to percentage-like value

# Construct input bundle
metrics_bundle = {
    'durations': task_durations,
    'flags': completion_flags,
    'resources': resource_usage
}

# Perform evaluation (key statement)
final_score = evaluate_performance(metrics_bundle, weights)

# Irrelevant aggregation
aggregate_gap_stats = list(itertools.starmap(lambda x, y: abs(x - y), zip(task_durations[:-1], task_durations[1:])))
baseline_shift = sum(decoy_transform) / 100 if decoy_transform else 0

# Output result as required
print(f"Result: {final_score}")