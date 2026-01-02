def analyze_system_load(raw_data, config):
    # Irrelevant pre-processing: normalizing unused signal data
    normalized_signals = [round((x - min(raw_data)) / (max(raw_data) - min(raw_data)) * 100, 2) for x in raw_data]
    spike_count = sum(1 for x in raw_data if x > config.get('critical_level', 90))

    # Distractor: unused function
    def smooth_signal(data, factor=0.3):
        smoothed = [data[0]]
        for i in range(1, len(data)):
            smoothed.append(smoothed[-1] * factor + data[i] * (1 - factor))
        return smoothed

    # Real path: extract timestamps and magnitudes
    timestamps = [entry[0] for entry in raw_data if isinstance(entry, tuple)]
    magnitudes = [entry[1] for entry in raw_data if isinstance(entry, tuple)]

    # Bit manipulation decoy
    checksum = 0
    for val in magnitudes:
        checksum ^= int(val) << 1
        checksum &= 0xFFFF

    # Unused statistical distraction
    mean_mag = sum(magnitudes) / len(magnitudes) if magnitudes else 0
    variance = sum((x - mean_mag) ** 2 for x in magnitudes) / len(magnitudes) if magnitudes else 0
    stdev = variance ** 0.5

    # Real logic begins: categorize events
    event_categories = {}
    for ts, mag in zip(timestamps, magnitudes):
        category = 'high' if mag > 75 else 'medium' if mag > 50 else 'low'
        event_categories[ts] = category

    # Lambda-based transformation (real use)
    severity_score = lambda cat: {'high': 3, 'medium': 2, 'low': 1}[cat]
    scores = list(map(severity_score, event_categories.values()))

    # Destructuring assignment red herring
    (*_, last_few_scores) = scores[-10:] if len(scores) > 10 else ([0] * 3 + scores)

    # Decoy control flow with dead branch
    adjustment_factor = 1.0
    if len(timestamps) > 100:
        adjustment_factor = 0.85  # Never reached in this case
    elif checksum > 5000:
        adjustment_factor = 1.1  # Also unreachable due to data scale

    # Core calculation disguised among noise
    active_periods = 0
    for i in range(1, len(timestamps)):
        if event_categories[timestamps[i]] == 'high' and event_categories[timestamps[i-1]] != 'high':
            active_periods += 1

    # Multiple assignments distraction
    peak, avg_score, total_events = max(magnitudes), sum(scores) / len(scores), len(scores)

    # Real answer derivation hidden in dictionary transform
    diagnostics = {
        'peak_load': peak,
        'event_bursts': active_periods,
        'compliance_rate': (len([s for s in scores if s >= 2]) / len(scores)) if scores else 0
    }

    health_index = diagnostics['peak_load'] * diagnostics['event_bursts']
    health_index -= int(diagnostics['compliance_rate'] * 100)

    # Final decoy: unused nested structure
    system_snapshot = {
        'meta': {'version': '2.1', 'region': config.get('region', 'unknown')},
        'layers': [
            {'id': i, 'status': 'active' if i % 2 == 0 else 'idle', 'load': (i * health_index) % 77} 
            for i in range(1, 6)
        ]
    }

    # Critical line: this is where the real answer is set
    final_diagnostic = int(health_index + adjustment_factor * 10)  # adjustment_factor still 1.0
    return final_diagnostic


def process_metrics(entries, thresholds):
    # Wrapper that appears complex but just forwards
    cleaned = [(e['time'], e['value']) for e in entries if e['value'] > thresholds.get('noise_floor', 5)]
    return analyze_system_load(cleaned, thresholds)

# Simulated input data
log_entries = [
    {'time': t, 'value': v} for t, v in enumerate(
        [45, 52, 88, 91, 67, 41, 33, 76, 83, 95, 92, 68, 55, 77, 81, 89, 94, 73, 60, 58]
    )
]
system_thresholds = {
    'critical_level': 85,
    'noise_floor': 30,
    'region': 'us-west-2'
}

# Execution point
final_diagnostic = process_metrics(log_entries, system_thresholds)
print(f"Target result: {final_diagnostic}")