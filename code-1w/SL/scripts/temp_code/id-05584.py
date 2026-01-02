def analyze_productivity(logs):
    total_entries = len(logs)
    idle_count = 0
    active_segments = []
    temp_buffer = []

    for i, entry in enumerate(logs):
        if 'idle' in entry:
            idle_count += 1
            if len(temp_buffer) > 0:
                active_segments.append(temp_buffer)
                temp_buffer = []
        else:
            temp_buffer.append(entry.strip().upper())

    if temp_buffer:
        active_segments.append(temp_buffer)

    # Distractor: irrelevant transformation
    reversed_logs = [log[::-1] for log in logs if 'error' not in log]
    checksum = sum(len(r) for r in reversed_logs) % 7

    # Real computation begins here
    durations = [len(segment) for segment in active_segments]
    avg_duration = sum(durations) / len(durations) if durations else 0

    outlier_count = sum(1 for d in durations if d > avg_duration * 1.5)
    normalized_outliers = outlier_count / len(durations) if durations else 0

    # Another decoy: unused statistical measure
    variance_proxy = sum((d - avg_duration) ** 2 for d in durations) / len(durations) if durations else 0
    peak_load = max(durations) if durations else 0

    return avg_duration, normalized_outliers, peak_load


def evaluate_workload(events):
    event_types = set(event.split()[0] for event in events)
    critical_events = [e for e in events if 'CRITICAL' in e]
    backup_copy = list(events)

    # Fake aggregation path
    summary_stats = {}
    for t in event_types:
        summary_stats[t] = len([e for e in events if e.startswith(t)])

    # Meaningless string manipulation chain
    combined = ''.join(events)
    char_freq = {c: combined.count(c) for c in set(combined) if c.isalpha()}
    rare_chars = [c for c, f in char_freq.items() if f < 3]

    # Actual signal extraction
    timestamps = [int(e.split()[-1]) for e in events if e.split()[-1].isdigit()]
    if not timestamps:
        return 0, 0

    time_gaps = [timestamps[i+1] - timestamps[i] for i in range(len(timestamps)-1)]
    consistency_metric = sum(1 for gap in time_gaps if gap <= 5)

    urgency_index = len(critical_events) * 2.5

    return consistency_metric, urgency_index

# Main workflow
activity_log = [
    'task start 100',
    'processing data 102',
    'idle state 105',
    'batch complete 108',
    'task resume 110',
    'subroutine call 111',
    'idle state 115',
    'critical alert 116',
    'finalizing 120'
]

# Irrelevant preprocessing
cleaned_log = [line.lower() for line in activity_log if 'temp' not in line]
duplicate_check = dict.fromkeys(cleaned_log)

engagement, efficiency = analyze_productivity(activity_log)
consistency, urgency = evaluate_workload(activity_log)

# Fake fusion logic (never used)
theoretical_max = (consistency + urgency) * len(activity_log)
safety_margin = theoretical_max * 0.15

# Real final calculation
baseline = engagement * 3.2
boost = urgency * 0.8 if efficiency > 0.3 else 0
final_score = int(baseline + boost)

# Decoy output
interim_result = (efficiency * urgency) // (engagement + 1e-5)

# This print must be preserved
Result: {final_score}