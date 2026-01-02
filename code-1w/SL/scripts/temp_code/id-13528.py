from collections import defaultdict, Counter

# Simulated system telemetry data
timing_log = [
    (100, 'fetch'), (150, 'parse'), (200, 'validate'),
    (120, 'fetch'), (180, 'parse'), (210, 'validate'),
    (110, 'fetch'), (160, 'parse'), (195, 'validate')
]

errors = [
    {'code': 404, 'stage': 'fetch', 'retry': True},
    {'code': 200, 'stage': 'parse', 'retry': False},
    {'code': 400, 'stage': 'validate', 'retry': True},
    {'code': 404, 'stage': 'fetch', 'retry': True}
]

# Irrelevant helper function (dead code path)
def legacy_transform(data):
    return [x * 1.5 for x in data if x > 100]

# Unused statistical counter
counter_snapshot = Counter([x[1] for x in timing_log])

# Misleading intermediate calculation (not used in final result)
avg_duration_misleading = sum(x[0] for x in timing_log) / len(timing_log)

# Distractor: fake error classifier (never called)
def classify_error(code):
    if code < 300:
        return 'info'
    elif code < 500:
        return 'client'
    else:
        return 'server'

# Real processing begins here
def extract_critical_path(log):
    stages = {}
    for duration, stage in log:
        if stage not in stages:
            stages[stage] = []
        stages[stage].append(duration)
    return {s: min(durations) for s, durations in stages.items()}

# Another distractor: computes total retries but unused
total_retries = sum(1 for e in errors if e['retry'])

# Decoy transformation using enumerate and zip (no effect on result)
indexed_errors = list(enumerate([e['code'] for e in errors]))
zipped_data = list(zip([x[0] for x in timing_log], [x[1] for x in timing_log]))

# Function that looks important but is only partially used
def compute_efficiency(log):
    totals = defaultdict(int)
    counts = defaultdict(int)
    for duration, stage in log:
        totals[stage] += duration
        counts[stage] += 1
    return {s: totals[s] / counts[s] for s, _ in totals.items()}

# Core logic disguised among noise
def aggregate_metrics(log, err_list):
    # Extract fastest execution per stage
    critical_path = extract_critical_path(log)
    
    # Compute frequency of each error type
    error_freq = Counter(e['code'] for e in err_list)
    
    # Real computation: weighted diagnostic score
    fetch_time = critical_path.get('fetch', 0)
    parse_time = critical_path.get('parse', 0)
    validate_time = critical_path.get('validate', 0)
    
    # Weighted combination: lower is better
    base_score = fetch_time * 1.2 + parse_time * 0.8 + validate_time * 1.5
    
    # Penalty factor based on 404 frequency
    not_found_penalty = error_freq.get(404, 0) * 25.5
    
    # Final diagnostic combines performance and reliability
    result = base_score + not_found_penalty
    
    # Irrelevant rounding (but kept to look meaningful)
    return round(result, 4)

# Red herring: a variable that seems important but isn't used
system_health = sum(counter_snapshot.values()) * 0.75

# Key execution point
final_diagnostic = aggregate_metrics(timing_log, errors)

# Print required output
print(f"Result: {final_diagnostic}")