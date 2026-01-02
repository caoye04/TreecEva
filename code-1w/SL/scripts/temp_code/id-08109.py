from collections import defaultdict, Counter

# Simulated system telemetry data
def collect_telemetry(samples):
    raw_data = []
    for s in samples:
        if s['status'] == 'active':
            raw_data.append((s['id'], s['timestamp'], s['power_draw']))
    return raw_data

# Irrelevant preprocessing function (dead path)
def normalize_signal(data, factor=1.0):
    return [x / factor for x in data if x > 0]

# Core diagnostic logic
def analyze_phases(telemetry):
    phase_map = defaultdict(list)
    for entry in telemetry:
        node_id, timestamp, power = entry
        phase = int(timestamp // 100) % 4
        phase_map[phase].append(power)
    
    stats = {}
    for p, readings in phase_map.items():
        stats[p] = {
            'count': len(readings),
            'avg': sum(readings) / len(readings),
            'peak': max(readings)
        }
    return stats

# Secondary validation (distractor)
def validate_timing_integrity(log_entries):
    gaps = []
    sorted_log = sorted(log_entries, key=lambda x: x[1])
    for i in range(1, len(sorted_log)):
        delta = sorted_log[i][1] - sorted_log[i-1][1]
        gaps.append(delta)
    return len([g for g in gaps if g > 50]) < 3

# Decoy function using enumerate/zip (misleading relevance)
def compute_efficiency_index(nodes, baselines):
    index_vals = []
    for i, (n, b) in enumerate(zip(nodes, baselines)):
        if i % 2 == 0:
            index_vals.append(n['perf'] / (b + 0.1))
    return sum(index_vals)

# Main aggregation with critical computation
def aggregate_metrics(timing_log, system_flags):
    # Real work starts here
    filtered_entries = [t for t in timing_log if t[2] > 15.0]
    
    cumulative = 0
    history = defaultdict(int)
    
    for idx, (node, ts, pd) in enumerate(filtered_entries):
        bucket = ts % 7
        history[bucket] += pd * 0.85
        
        if idx % 3 == 0:
            cumulative += history[bucket]
        elif idx % 5 == 0 and bucket in system_flags:
            cumulative -= 5
            
    # Red herring: unused complex structure
    summary_counter = Counter([ts % 4 for _, ts, _ in filtered_entries])
    temp_shift = sum(summary_counter.values()) * 0.1
    
    # Critical distractor variables
    calibration_offset = 99
    stability_ratio = 0.92
    debug_trace = [calibration_offset * stability_ratio for _ in range(3)]
    
    # Actual answer computation (non-obvious due to distractions)
    base_value = sum(history.values())
    adjustment = len(filtered_entries) // 2
    final_diagnostic = int(base_value - adjustment + 7)
    
    # This print must be present
    print(f"Result: {final_diagnostic}")
    return final_diagnostic

# Setup realistic input data
sample_inputs = [
    {'id': 'N1', 'status': 'active', 'timestamp': 105, 'power_draw': 18.2, 'perf': 42},
    {'id': 'N2', 'status': 'active', 'timestamp': 211, 'power_draw': 16.5, 'perf': 38},
    {'id': 'N3', 'status': 'idle',   'timestamp': 190, 'power_draw': 12.1, 'perf': 29},
    {'id': 'N4', 'status': 'active', 'timestamp': 303, 'power_draw': 22.0, 'perf': 55},
    {'id': 'N5', 'status': 'active', 'timestamp': 155, 'power_draw': 17.3, 'perf': 40},
    {'id': 'N6', 'status': 'active', 'timestamp': 250, 'power_draw': 19.8, 'perf': 47}
]

# Generate telemetry
telemetry_data = collect_telemetry(sample_inputs)

# Sort by timestamp for temporal consistency
sorted_telemetry = sorted(telemetry_data, key=lambda x: x[1])

# System flags (only some are relevant)
system_flags = {1, 3, 6}  # Used in conditional adjustment
baseline_perf = [40, 35, 50, 45]

# Validate log (distractor call - result unused)
valid_log = validate_timing_integrity(sorted_telemetry)

# Compute fake efficiency (never used)
efficiency_score = compute_efficiency_index(sample_inputs, baseline_perf)

# Execute main diagnostic
final_diagnostic = aggregate_metrics(sorted_telemetry, system_flags)