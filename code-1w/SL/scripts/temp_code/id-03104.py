import itertools

# Realistic domain: System performance evaluation with multiple metrics
def analyze_throughput(data):
    total = 0
    count = 0
    for item in data:
        if item < 0:
            continue
        total += item * 1.1
        count += 1
    return int(total // max(count, 1)) if count else 0

def compute_resilience_score(events):
    critical_failures = 0
    for e in events:
        if 'failure' in e and 'critical' in e:
            critical_failures += 1
    return 100 - critical_failures * 10

def filter_anomalies(logs):
    # Irrelevant helper - dead code path
    anomalies = set()
    for log in logs:
        if 'err' in log.lower():
            anomalies.add(log.strip())
    return sorted(anomalies)

def normalize_metrics(raw):
    # Distractor function: looks important but unused in final calculation
    cleaned = []
    for x in raw:
        if isinstance(x, float):
            cleaned.append(round(x, 2))
        else:
            cleaned.append(x)
    return cleaned

def detect_patterns(sequence):
    # Another red herring: uses itertools but not connected to main logic
    groups = []
    for k, g in itertools.groupby(sequence):
        groups.append((k, len(list(g))))
    pattern_count = sum(1 for _, length in groups if length > 2)
    return pattern_count

def evaluate_stability(values):
    if len(values) < 2:
        return 0
    diffs = [abs(values[i] - values[i+1]) for i in range(len(values)-1)]
    avg_diff = sum(diffs) / len(diffs)
    return int(100 - avg_diff)

def evaluate_performance(metrics, dataset):
    # Core logic embedded within noise
    base = metrics.get('throughput', [])
    events = metrics.get('event_log', [])
    
    # Key computation step 1
    throughput_rating = analyze_throughput(base)
    
    # Key computation step 2
    resilience_rating = compute_resilience_score(events)
    
    # Key computation step 3
    stability_rating = evaluate_stability(dataset)
    
    # Irrelevant intermediate variables (distractors)
    temp_analysis = {"raw": dataset, "size": len(dataset), "version": "2.1"}
    debug_info = f"Processing {len(dataset)} entries..."
    buffer_cache = [x * 0.95 for x in dataset if x > 5]  # Unused
    
    # Misleading transformation chain
    transformed = list(map(lambda x: x ** 0.5, dataset))
    filtered_transformed = [t for t in transformed if t > 3]
    derived_metric = sum(filtered_transformed) / len(filtered_transformed) if filtered_transformed else 0
    
    # Decoy conditional with early exit that never triggers in this case
    emergency_override = False
    if sum(dataset) < 0:
        return -999  # Dead path
    
    # Actual core formula
    raw_score = throughput_rating * 0.4 + resilience_rating * 0.3 + stability_rating * 0.3
    
    # Final adjustment using string-based key from unrelated operation
    key_tag = 'perf_' + ''.join([str(len(e)) for e in events if 'warning' in e])
    adjustment_factor = len(key_tag) % 7
    
    # Final score calculation
    final_score = int(raw_score + adjustment_factor)
    
    # Print required output
    print(f"Result: {final_score}")
    return final_score

# Simulated input data
metric_set = {
    'throughput': [85, 90, 92, 87, 88],
    'event_log': ['normal', 'warning_critical', 'normal', 'failure_critical', 'warning_minor']
}

benchmark_data = [88, 91, 89, 90, 87, 85, 88, 92]  # Stability sequence

# Trigger execution
final_score = evaluate_performance(metric_set, benchmark_data)