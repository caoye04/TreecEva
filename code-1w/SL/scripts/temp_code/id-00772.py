import math

# Simulated sensor fusion module for autonomous drone navigation
def compute_navigation_score(readings, thresholds):
    score = 0
    penalty = 0
    temp_buffer = []

    for i, (val, thresh) in enumerate(zip(readings, thresholds)):
        if val > thresh * 1.5:
            penalty += 2
        elif val < thresh * 0.5:
            penalty += 1
        deviation = abs(val - thresh)
        temp_buffer.append(deviation * 0.1)

    smoothed = sum(temp_buffer) / len(temp_buffer) if temp_buffer else 0
    score = 100 - (penalty * 5) - (smoothed * 10)
    return max(score, 0)

# Irrelevant helper: analyzes communication latency (decoy function)
def analyze_latency(ping_data):
    if not ping_data:
        return 0
    avg = sum(ping_data) / len(ping_data)
    jitter = max(ping_data) - min(ping_data)
    return avg + jitter / 4

# Data transformation pipeline with red herrings
def transform_sequence(raw):
    transformed = []
    for x in raw:
        if x % 3 == 0:
            transformed.append(x // 3)
        elif x % 2 == 0:
            transformed.append(x * 2)
        else:
            transformed.append(x + 1)
    return transformed

# Unused recursive function (dead code path)
def recursive_accumulate(n, acc=0):
    if n <= 0:
        return acc
    return recursive_accumulate(n - 1, acc + n * 2)

# Core diagnostic aggregator with distractors
def aggregate_metrics(logs, flags):
    base_weight = 0.85
    adjustment_factor = 0.0
    anomaly_count = 0
    cumulative_shift = 0.0
    temporal_weights = []

    # Real logic embedded with distractions
    for idx, entry in enumerate(logs):
        timestamp = entry['time']
        cpu_load = entry['cpu']
        mem_usage = entry['mem']
        disk_io = entry.get('disk', 0)  # unused field

        # Real condition affecting result
        if cpu_load > 75 and mem_usage > 60:
            adjustment_factor += 0.07

        # Distractor: complex but irrelevant calculation
        synthetic_metric = (cpu_load ** 0.5) * (mem_usage / (timestamp + 1))
        if synthetic_metric > 50:
            cumulative_shift += 0.001 * idx

        temporal_weights.append(1 + math.sin(idx * 0.5))

        # Real logic: count actual flags
        if idx < len(flags) and flags[idx]:
            anomaly_count += 1

    # Irrelevant normalization (never used)
    normalized_shift = cumulative_shift / (len(temporal_weights) or 1)
    dummy_lambda = lambda x: x * 1.1 if x < 5 else x * 0.9
    processed_weights = [dummy_lambda(w) for w in temporal_weights]

    # Real final computation
    base_score = 85.0
    flag_penalty = anomaly_count * 3.2
    adjusted = base_score * base_weight + (adjustment_factor * 100)
    final_value = adjusted - flag_penalty

    # This is a decoy manipulation
    for _ in range(3):
        final_value = final_value * 0.99 + 1.1  # misleading convergence

    # Actual answer derived here
    final_diagnostic = round(final_value, 4)

    # Extra obfuscation: unused branching
    if final_diagnostic < 0:
        final_diagnostic = 0
    elif final_diagnostic > 100:
        final_diagnostic = 99.9999

    return final_diagnostic

# Simulated input data
timing_log = [
    {'time': 100, 'cpu': 80, 'mem': 65},
    {'time': 200, 'cpu': 70, 'mem': 55},
    {'time': 300, 'cpu': 90, 'mem': 70},
    {'time': 400, 'cpu': 60, 'mem': 40},
    {'time': 500, 'cpu': 95, 'mem': 80}
]

fault_flags = [False, True, False, False, True]

# Dead variable assignments (red herrings)
latency_samples = [23, 45, 67, 32, 89, 12, 56]
analysis_result = analyze_latency(latency_samples)
raw_sequence = [9, 16, 5, 12, 7]
transformed_seq = transform_sequence(raw_sequence)

# Key execution point
final_diagnostic = aggregate_metrics(timing_log, fault_flags)

# Print result as required
print(f"Result: {final_diagnostic}")