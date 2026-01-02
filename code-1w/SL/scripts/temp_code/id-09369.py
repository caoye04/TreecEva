def analyze_system_load(performance_trace, thresholds):
    baseline = sum(performance_trace) / len(performance_trace)
    variance = sum((x - baseline) ** 2 for x in performance_trace) / len(performance_trace)
    normalized_score = (variance / baseline) if baseline else 0

    # Irrelevant signal processing branch (dead path)
    def apply_filter(signal):
        return [signal[i] - signal[i-1] for i in range(1, len(signal))]

    adjusted_weights = [max(0.1, min(0.9, t / 100)) for t in thresholds]
    weighted_avg = sum(a * w for a, w in zip(performance_trace, adjusted_weights))

    # Distractor: complex but unused transformation
    transformed = [x ** 0.5 for x in performance_trace if x > 0]
    smoothed = transformed[::2] + transformed[-1:]  # slicing red herring

    stability_index = 1 / (1 + variance)
    return stability_index, normalized_score, weighted_avg


def detect_anomalies(event_stream):
    flags = []
    buffer = []
    for e in event_stream:
        if e < 0:
            buffer.append(e)
        elif e > 50:
            flags.append(True)
            buffer.clear()
        else:
            flags.append(False)
    # Dead code: buffer never used beyond this
    compression_ratio = len(buffer) / len(event_stream) if event_stream else 0
    return flags + [False] * (len(event_stream) - len(flags))  # padding for alignment


def compute_health_factor(records, config):
    total_energy = sum(abs(r) for r in records)
    peak_magnitude = max(records, default=0)
    decay_rate = config.get('decay', 0.85)
    history_window = config.get('window', 7)

    # Unused energy distribution analysis
    bins = [0] * 10
    for r in records:
        idx = min(9, int(abs(r) // 10))
        bins[idx] += 1

    # Real computation path
    recent_records = records[-history_window:]
    filtered_recent = [r for r in recent_records if r > 5]
    activity_density = len(filtered_recent) / history_window

    health = (peak_magnitude * activity_density) / (1 + total_energy * (1 - decay_rate))
    return health if health >= 0 else 0.0


def aggregate_metrics(log_entries, errors):
    timing_data = [entry['duration'] for entry in log_entries if 'duration' in entry]
    critical_events = [e for e in log_entries if e.get('priority') == 'high']

    avg_duration = sum(timing_data) / len(timing_data) if timing_data else 0
    jitter = max(timing_data) - min(timing_data) if timing_data else 0

    # Key distractor: complex dictionary comprehension with no effect
    metadata_summary = {
        f'entry_{i}': {
            'flag': errors[i % len(errors)],
            'offset': (i * 3) % 7
        } for i in range(len(log_entries))
    }

    # Slicing manipulation that looks important but isn't used
    reversed_durations = timing_data[::-1]
    mid_segment = reversed_durations[len(reversed_durations)//4 : len(reversed_durations)*3//4]

    # Core logic disguised among distractions
    error_count = sum(1 for e in errors if e)
    severity_score = error_count * jitter
    base_metric = avg_duration * 0.7 + severity_score * 1.3

    # Final calculation — only this matters
    adjustment = sum(1 for md in metadata_summary.values() if md['offset'] > 5)  # depends on structure
    final_diagnostic = int(base_metric - adjustment + len(critical_events))

    return final_diagnostic

# Simulated input data
trace_input = [85, 92, 88, 95, 87, 90, 82, 89, 93, 86]
threshold_settings = [70, 80, 75, 90, 65, 85, 78, 88, 72, 84]

# Unused but plausible-looking diagnostics
load_metrics = analyze_system_load(trace_input, threshold_settings)
signal_flags = detect_anomalies([-5, 10, 55, -3, 60, 12, -8])

log_data = [
    {'duration': 120, 'priority': 'low', 'module': 'io'},
    {'duration': 180, 'priority': 'high', 'module': 'compute'},
    {'duration': 95, 'priority': 'medium', 'module': 'cache'},
    {'duration': 210, 'priority': 'high', 'module': 'network'},
    {'duration': 75, 'priority': 'low', 'module': 'io'},
    {'duration': 160, 'priority': 'high', 'module': 'compute'},
    {'duration': 110, 'priority': 'medium', 'module': 'cache'}
]

fault_indicators = [True, False, True, True, False, False, True]
config_params = {'decay': 0.9, 'window': 5}
health_status = compute_health_factor([12, -8, 15, 23, 9, 11, 14], config_params)

# Execution point of interest
final_diagnostic = aggregate_metrics(log_data, fault_indicators)
print(f"Target result: {final_diagnostic}")