import math

# Simulated system telemetry and diagnostic processing pipeline
def collect_diagnostics():
    # Core sensor readings (relevant)
    timing_log = [
        {'cycle': 1, 'delta': 0.05, 'power_draw': 120},
        {'cycle': 2, 'delta': 0.03, 'power_draw': 125},
        {'cycle': 3, 'delta': 0.08, 'power_draw': 118},
        {'cycle': 4, 'delta': 0.04, 'power_draw': 122}
    ]

    # Irrelevant environmental sensors (distractors)
    env_sensors = {
        'humidity': [45, 46, 44, 47],
        'pressure': [1013, 1012, 1015, 1014],
        'ambient_temp': [22.1, 22.3, 21.9, 22.0]
    }

    # Decoy function that computes unrelated stats (dead code path)
    def compute_env_trend(data):
        avg_humid = sum(data['humidity']) / len(data['humidity'])
        trend = 'stable' if abs(data['pressure'][-1] - data['pressure'][0]) < 5 else 'volatile'
        return {'average_humidity': avg_humid, 'atmospheric_trend': trend}

    # Unused transformation (red herring)
    processed_env = {k: [round(x * 1.01, 2) for x in v] for k, v in env_sensors.items()}

    # System flags with mixed relevance
    system_flags = {
        'overclock': True,
        'safe_mode': False,
        'legacy_protocol': True,
        'debug_trace': None
    }

    # Diagnostic thresholds (some are used, others are decoys)
    thresholds = {
        'latency_cap': 0.07,
        'min_cycles': 3,
        'max_power': 130,
        'version_check': '2.1.0',
        'retry_limit': 5
    }

    # Misleading intermediate calculation (looks important but unused)
    projected_load = sum(s['power_draw'] * 1.05 for s in timing_log) / len(timing_log)

    # Redundant list copy (distractor)
    log_backup = [dict(entry) for entry in timing_log]

    # Real-time anomaly detection (unused branch)
    anomalies = []
    for i, entry in enumerate(timing_log):
        if entry['delta'] > thresholds['latency_cap']:
            anomalies.append(i)

    # Unused lambda (misdirection)
    scale_reading = lambda x: round(x * 1000)

    # Actual signal processor using relevant subset
    def extract_timing_series(log):
        return [entry['delta'] for entry in log if entry['cycle'] >= 2]  # ignore first cycle

    # Key data transformation chain
    raw_deltas = extract_timing_series(timing_log)
    filtered_deltas = list(filter(lambda x: x < 0.07, raw_deltas))  # only stable cycles

    # Weighted jitter score computation (core logic)
    weights = [0.4, 0.6] if len(filtered_deltas) > 1 else [1.0]
    weighted_jitter = sum(w * d for w, d in zip(weights, sorted(filtered_deltas)))

    # Power fluctuation index (partially relevant)
    power_vals = [s['power_draw'] for s in timing_log]
    fluctuation_index = max(power_vals) - min(power_vals)

    # Phantom correlation attempt (irrelevant)
    correlated_drift = 0
    for i, val in enumerate(env_sensors['humidity']):
        correlated_drift += val * (0.01 * i)

    # Conditional flag modifier (actually used)
    multiplier = 2 if system_flags['overclock'] and not system_flags['safe_mode'] else 1

    # Hidden accumulator logic with enumerate (key step)
    adjustment_sum = 0
    for idx, delta in enumerate(filtered_deltas):
        adjustment_sum += delta * (idx + 1)  # position-weighted adjustment

    # Final aggregation function
    def aggregate_metrics(deltas, flags):
        base = sum(deltas)
        adj = adjustment_sum * 0.5
        boost = 10 if flags['legacy_protocol'] else 0
        return int((base + adj + boost) * multiplier)

    # Critical execution point
    final_diagnostic = aggregate_metrics(timing_log, system_flags)

    # Dead code: alternate computation path never taken
    if system_flags['debug_trace'] == 'full':
        fallback = math.fsum([d['delta']**2 for d in timing_log])
        final_diagnostic = int(fallback * 100)

    return final_diagnostic

# Execute and print result
def main():
    result = collect_diagnostics()
    print(f"Result: {result}")

main()