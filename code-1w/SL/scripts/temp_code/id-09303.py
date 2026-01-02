def analyze_system_metrics(log_entries, threshold=0.75):
    # Irrelevant preprocessing: normalize timestamps (not used later)
    normalized_times = [entry['timestamp'] % 3600 for entry in log_entries if 'timestamp' in entry]
    temp_offsets = [abs(t - 1800) for t in normalized_times]

    # Core data extraction
    severity_levels = []
    active_components = set()
    debug_flags = []

    for entry in log_entries:
        if 'component' in entry:
            active_components.add(entry['component'])
        if 'severity' in entry:
            severity_levels.append(entry['severity'])
            if entry.get('debug', False):
                debug_flags.append(entry['id'])

    # Distractor: complex unused transformation chain
    shifted_severities = [s * 1.5 + 2 for s in severity_levels]
    filtered_shifted = [s for s in shifted_severities if s > 3.0]
    derived_metric = sum(filtered_shifted) / len(filtered_shifted) if filtered_shifted else 0

    # Real computation begins: categorize alerts
    high_risk_ids = []
    medium_risk_ids = []
    total_volume = 0

    for entry in log_entries:
        total_volume += 1
        if entry['severity'] > threshold:
            high_risk_ids.append(entry['id'])
        elif entry['severity'] > threshold - 0.2:
            medium_risk_ids.append(entry['id'])

    # Simulate conditional suppression of alerts
    suppressed = set()
    for entry in log_entries:
        if entry.get('suppressed', False):
            suppressed.add(entry['id'])

    # Actual risk score calculation (uses only part of the data)
    base_score = len(high_risk_ids) * 3 + len(medium_risk_ids) * 1
    penalty = 0
    for entry in log_entries:
        if entry['component'] == 'power' and entry['severity'] > 0.6:
            penalty += 2

    aggregate_score = base_score - penalty

    # Critical distractor block: fake correction algorithm
    correction_factor = 0
    if len(debug_flags) > 5:
        correction_factor = 1
    elif len(active_components) > 4:
        correction_factor = -1
    synthetic_adjustment = derived_metric * correction_factor  # Never actually used

    # Determine remaining active alerts after filtering
    all_alert_ids = {e['id'] for e in log_entries}
    resolved_ids = {e['id'] for e in log_entries if e.get('resolved')}
    remaining_alerts = all_alert_ids - resolved_ids - suppressed

    # Key statement containing the answer
    final_diagnostic = aggregate_score + len(remaining_alerts)

    # Dead code path: looks important but unused
    def compute_stability_index():
        return len(normalized_times) / (1 + len(suppressed))

    # Print result as required
    print(f"Target result: {final_diagnostic}")

    return final_diagnostic

# Input data
log_data = [
    {'id': 1, 'component': 'sensor', 'severity': 0.8, 'timestamp': 3500},
    {'id': 2, 'component': 'network', 'severity': 0.72, 'timestamp': 3520, 'suppressed': True},
    {'id': 3, 'component': 'power', 'severity': 0.85, 'timestamp': 3540, 'debug': True},
    {'id': 4, 'component': 'sensor', 'severity': 0.65, 'timestamp': 3560},
    {'id': 5, 'component': 'storage', 'severity': 0.9, 'timestamp': 3580, 'resolved': True},
    {'id': 6, 'component': 'power', 'severity': 0.68, 'timestamp': 3600, 'debug': True},
    {'id': 7, 'component': 'display', 'severity': 0.71, 'timestamp': 3620},
    {'id': 8, 'component': 'sensor', 'severity': 0.5, 'timestamp': 3640, 'resolved': True},
    {'id': 9, 'component': 'network', 'severity': 0.81, 'timestamp': 3660},
    {'id': 10, 'component': 'power', 'severity': 0.59, 'timestamp': 3680}
]

# Execute function
analyze_system_metrics(log_data)