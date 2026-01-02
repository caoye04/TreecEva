from collections import defaultdict, Counter
import itertools

# Simulated system log analysis with heavy distractions
def analyze_events(raw_logs):
    event_counts = defaultdict(int)
    temporal_gaps = []
    decoy_sum = 0

    for entry in raw_logs:
        timestamp, event_type, severity = entry
        event_counts[event_type] += 1
        if severity > 2:
            temporal_gaps.append(timestamp)
        # Distractor: irrelevant accumulation
        for i in range(3):
            decoy_sum += (severity * i) % 2

    # Meaningless transformation
    sorted_pairs = sorted(event_counts.items(), key=lambda x: x[1])
    reversed_events = [k[::-1] for k, v in sorted_pairs if v % 2 == 0]
    ''.join(reversed_events)  # dead operation

    return dict(event_counts), temporal_gaps

# Red herring function – never used in final computation
def deprecated_aggregator(data_stream):
    accumulator = 0
    for chunk in data_stream:
        accumulator ^= hash(str(chunk))
    return accumulator % 1000

# Core processing with subtle logic path
def compute_stability_index(entries):
    durations = [e[1] - e[0] for e in entries if e[1] > e[0]]
    baseline = sum(durations) / len(durations) if durations else 0.0

    # Distraction: complex but unused structure
    stats_snapshot = {
        'peak': max(durations) if durations else 0,
        'variance': sum((x - baseline) ** 2 for x in durations) / len(durations) if durations else 0,
        'outliers': [x for x in durations if x > baseline * 1.5]
    }

    # Actual relevant calculation buried here
    filtered = [d for d in durations if d <= baseline]
    return sum(filtered) * 0.85 if filtered else 0.0

# Key function that appears complex due to noise
def process_metrics(log_data, flags):
    # Irrelevant preprocessing block
    sanitized = [row for row in log_data if row[2] >= 0]
    categories = set(row[1] for row in sanitized)
    category_map = {cat: idx for idx, cat in enumerate(categories)}

    # Distractor variables
    anomaly_score = 0
    for cat in categories:
        if len(cat) % 2 == 1:
            anomaly_score += category_map[cat]

    # Real work begins — hidden in noise
    critical_events = []
    for record in log_data:
        _, duration_meta, priority = record
        if priority >= 3:
            critical_events.append(duration_meta)

    # Another decoy using itertools
    paired_combos = list(itertools.combinations_with_replacement(critical_events, 2))
    combo_sum = sum(abs(a - b) for a, b in paired_combos) if paired_combos else 0

    # Actual signal: count high-priority unique durations
    unique_durations = set()
    for ce in critical_events:
        if ce > 10:
            unique_durations.add(ce)

    base_metric = len(unique_durations) * 50

    # Apply flag-based adjustment — crucial but obscured
    adjustment_factor = 1.0
    if 'overclock' in flags:
        adjustment_factor *= 0.9
    if 'secure_mode' in flags and len(flags) > 2:
        adjustment_factor *= 0.8

    intermediate = base_metric * adjustment_factor

    # Final red herring before real assignment
    metadata_cache = Counter([str(intermediate)[:2] for _ in range(5)])
    unused_lookup = {i: chr(65 + (i % 26)) for i in range(20)}

    final_diagnostic = int(intermediate - 17)  # actual answer determination

    return final_diagnostic

# Simulated input data
log_entries = [
    (100, 'io_read', 4),
    (105, 'compute', 2),
    (110, 'io_write', 5),
    (115, 'network', 4),
    (120, 'compute', 1),
    (125, 'io_read', 6),
    (130, 'network', 3),
    (135, 'io_read', 12),
    (140, 'compute', 4)
]

system_flags = ['overclock', 'debug', 'secure_mode']

# Execution flow with misleading calls
_, time_intervals = analyze_events(log_entries)
system_stability = compute_stability_index([(t, t+8) for t in time_intervals])
deprecated_diagnostic = deprecated_aggregator(log_entries)

# Critical statement
final_diagnostic = process_metrics(log_entries, system_flags)

print(f"Result: {final_diagnostic}")