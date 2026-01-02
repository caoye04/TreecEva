def analyze_system_load(perf_data, threshold_map):
    # Irrelevant transformation: converts timestamps but not used later
    timestamp_shift = lambda ts: (ts[0], ts[1] + 3600)  
    shifted_logs = [timestamp_shift(entry) for entry in perf_data if entry[2] > 50]

    # Distractor: complex-looking but unused data structure
    diagnostic_tree = {i: {'level': 'deep', 'flag': False} for i in range(len(perf_data))}

    # Real logic begins: extract critical entries
    critical_entries = [entry for entry in perf_data if entry[3] == 'ERROR']

    # Misleading aggregation: looks important but unused
    error_frequency = {}
    for entry in critical_entries:
        service = entry[1]
        error_frequency[service] = error_frequency.get(service, 0) + 1

    # Dead code path: function defined but never called
    def compute_health_score():
        return sum([len(d['children']) for d in diagnostic_tree.values()]) // 2

    # Actual relevant processing
    severity_scores = []
    for entry in critical_entries:
        time_sec, service_id, cpu, _, mem_usage, disk_io = entry
        score = 0
        if cpu > threshold_map['cpu']:
            score += 3
        if mem_usage > threshold_map['memory']:
            score += 2
        if disk_io > threshold_map['disk']:
            score += 1
        severity_scores.append(score)
    
    return severity_scores

# Auxiliary irrelevant function
def normalize_series(data):
    base = min(data)
    return [round((x - base) / base * 100, 2) for x in data]

# Another decoy: character frequency counter with no impact
def count_service_chars(entries):
    char_count = {}
    for entry in entries:
        for c in entry[1]:
            char_count[c] = char_count.get(c, 0) + 1
    return char_count

# Main data - realistic system log format: (timestamp, service, cpu%, status, memory, disk_io)
log_entries = [
    (1623456780, 'auth', 75, 'ERROR', 8192, 120),
    (1623456781, 'api', 45, 'OK', 4096, 60),
    (1623456782, 'db', 90, 'ERROR', 12288, 200),
    (1623456783, 'cache', 30, 'OK', 2048, 40),
    (1623456784, 'auth', 85, 'ERROR', 9216, 140),
    (1623456785, 'queue', 60, 'ERROR', 5120, 180)
]

# Threshold configuration (real)
system_thresholds = {
    'cpu': 70,
    'memory': 8000,
    'disk': 100
}

# Unused sorting operation - distractor
sorted_by_memory = sorted(log_entries, key=lambda x: x[4], reverse=True)

# Enumerate and zip usage (required feature): irrelevant index mapping
indexed_services = list(enumerate([e[1] for e in log_entries]))
service_time_pairs = list(zip([e[0] for e in log_entries], [e[1] for e in log_entries]))

# Decoy dictionary operations
snapshot = {svc: ts for ts, svc in service_time_pairs}
summary_stats = {s: {'count': 0, 'alerts': 0} for s in snapshot.values()}

# Real processing pipeline
raw_scores = analyze_system_load(log_entries, system_thresholds)

# Intermediate transformation: maps scores to categories (some distraction here)
category_map = {0: 'stable', 1: 'warning', 2: 'critical', 3: 'critical', 4: 'severe', 5: 'severe', 6: 'emergency'}

categorized = [category_map.get(s, 'unknown') for s in raw_scores]

diagnostic_codes = {i: (log_entries[i][1], raw_scores[i]) for i in range(len(raw_scores))}

# Final computation: actual answer path
aggregated_diagnostic = sum(raw_scores) * len([c for c in categorized if c == 'critical'])

# Additional red herring: floating point conversion with no effect
normalized_score = round(aggregated_diagnostic / 1.0, 4)

# Key statement - this is where final_diagnostic is set
final_diagnostic = process_metrics(log_entries, system_thresholds)

# Function that actually computes the real result (was referenced above)
def process_metrics(entries, thresholds):
    errors = [e for e in entries if e[3] == 'ERROR']
    total_severity = 0
    for e in errors:
        _, _, cpu, _, mem, disk = e
        weight = 0
        if cpu > thresholds['cpu']:
            weight += 3
        if mem > thresholds['memory']:
            weight += 2
        if disk > thresholds['disk']:
            weight += 1
        total_severity += weight
    critical_count = sum(1 for s in [3,4,5,6] if s in [3,4,5,6])  # always 4 - misleading!
    return total_severity * 4  # Note: critical_count replaced with literal 4 for clarity in logic

# Print final result as required
Result: {final_diagnostic}