import itertools

def analyze_system_health(metrics, config):
    # Irrelevant transformation (red herring)
    shadow_copy = [m ** 0.5 for m in metrics if m > 0]
    temp_adjusted = list(map(lambda x: x * 1.05 + 2, shadow_copy))

    # Distractor computation with unused result
    decoy_aggregate = sum(temp_adjusted) / len(temp_adjusted) if temp_adjusted else 0
    normalization_factor = max(metrics) / 100.0

    scaled = [m / normalization_factor for m in metrics]
    filtered = [s for s in scaled if s >= config.get('min_signal', 10)]

    # Real signal begins here
    trend = 0
    for i in range(1, len(scaled)):
        if scaled[i] > scaled[i-1]:
            trend += 1
        elif scaled[i] < scaled[i-1]:
            trend -= 1

    return {'trend': trend, 'count': len(filtered), 'raw': metrics}

def evaluate_stability(readings):
    baseline = sum(readings) / len(readings)
    variance = sum((r - baseline) ** 2 for r in readings) / len(readings)
    stability_score = 1 / (1 + variance)  # Invert variance

    # Dead code path (never executed due to condition)
    if False:
        for _ in range(10):
            stability_score *= 0.95

    return stability_score

def process_metrics(entries, thresholds):
    # Extract time-series values using zip and enumerate (idiomatic Python)
    timestamps, values, types = zip(*[(e['ts'], e['val'], e['type']) for e in entries])

    # Group by type using itertools.groupby (needs sorting first)
    sorted_entries = sorted(entries, key=lambda e: e['type'])
    grouped = {k: list(g) for k, g in itertools.groupby(sorted_entries, key=lambda e: e['type'])}

    # Irrelevant preprocessing branch
    if 'debug' in thresholds:
        debug_snapshot = [v * 2 for v in values if v < thresholds['debug']]
        debug_snapshot = debug_snapshot[::-1]  # Reverse

    # Real processing starts
    avg_by_type = {}
    for t, group in grouped.items():
        raw_vals = [g['val'] for g in group]
        avg_by_type[t] = sum(raw_vals) / len(raw_vals)

    # Complex conditional logic with short-circuiting
    primary_avg = avg_by_type.get('primary', 0)
    secondary_avg = avg_by_type.get('secondary', 0)

    if primary_avg > thresholds['critical'] or (primary_avg > thresholds['warning'] and secondary_avg > 75):
        trigger_level = 3
    elif primary_avg > thresholds['warning']:
        trigger_level = 2
    elif secondary_avg > 80:
        trigger_level = 1
    else:
        trigger_level = 0

    # Decoy calculation with bitwise distraction
    checksum = 0
    for v in values:
        checksum ^= int(v)  # Bitwise XOR chain
    checksum = (checksum << 2) ^ 0xFF  # More bit manipulation (unused later)

    # Core logic: composite diagnostic index
    trend_vector = [values[i+1] - values[i] for i in range(len(values)-1)]
    positive_trends = len([t for t in trend_vector if t > 0.5])
    negative_trends = len([t for t in trend_vector if t < -0.5])

    trend_index = positive_trends - negative_trends

    # Final integration of multiple factors
    base_score = primary_avg * 0.6 + secondary_avg * 0.4
    adjustment = trend_index * 0.3

    if trigger_level >= 2:
        adjustment -= 5  # Penalty for instability

    final_diagnostic = int(base_score + adjustment + trigger_level * 2)

    # Print required output
    print(f"Result: {final_diagnostic}")
    return final_diagnostic

# Simulated input data
log_entries = [
    {'ts': t, 'val': v, 'type': tp}
    for t, v, tp in zip(
        range(1000, 1050, 1),
        [89, 92, 88, 95, 91, 87, 93, 90, 94, 96, 85, 97, 92, 89, 93, 91, 88, 94, 90, 92,
         87, 95, 89, 91, 93, 88, 90, 92, 94, 86, 91, 89, 93, 95, 87, 90, 92, 88, 94, 91,
         89, 93, 87, 95, 90, 92, 88, 91, 89, 93],
        ['primary'] * 25 + ['secondary'] * 25
    )
]

system_thresholds = {
    'warning': 88,
    'critical': 94,
    'min_signal': 10,
    'debug': 100  # Sets debug snapshot but doesn't affect main flow
}

# Call entry point
final_diagnostic = 0
final_diagnostic = process_metrics(log_entries, system_thresholds)
