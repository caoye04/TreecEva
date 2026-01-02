from collections import defaultdict, Counter
import itertools

# Simulate system telemetry processing with red herrings and distractions
def collect_diagnostics():
    # Core data structures
    timing_log = [0.12, 0.34, 0.23, 0.56, 0.18, 0.41, 0.29]
    event_sequence = ['start', 'init', 'load', 'compute', 'compute', 'save', 'end']
    system_flags = { 'overload': False, 'throttled': True, 'debug_mode': False }

    # Irrelevant statistical counters (distractor)
    stats_counter = Counter()
    for val in timing_log:
        if val > 0.3:
            stats_counter['high'] += 1
        else:
            stats_counter['low'] += 1

    # Fake transformation pipeline (dead code path)
    def transform_readings(data):
        return [round(x ** 0.5, 4) for x in data]  # unused

    # Misleading intermediate calculation (red herring)
    avg_latency = sum(timing_log) / len(timing_log)
    peak_noise = max([abs(x - 0.25) for x in timing_log]) * 1000
    diagnostic_weight = 0  # intentionally misleading, not used later

    # Complex but irrelevant string analysis (distractor)
    log_labels = [f"event_{i:02d}_{name}" for i, name in enumerate(event_sequence)]
    label_lengths = list(map(len, log_labels))
    total_chars = sum(label_lengths)

    # Use of itertools for distraction (irrelevant grouping)
    grouped_events = [list(g) for k, g in itertools.groupby(event_sequence, lambda x: x == 'compute')]

    # Unused nested structure (decoy)
    metadata_tree = {
        'version': {'major': 2, 'minor': 4},
        'nodes': [
            {'id': 'A', 'status': 'active', 'metrics': [0.1, 0.2]},
            {'id': 'B', 'status': 'idle',   'metrics': []}
        ]
    }

    # Key function buried in noise
    def aggregate_metrics(log_data, flags):
        base_score = sum(log_data) * 100
        if flags['throttled']:
            base_score *= 0.7
        if flags['overload']:
            base_score *= 0.5
        
        # Hidden conditional logic step
        adjustment = 1.0
        if len(log_data) > 5:
            adjustment += 0.1
        if 'debug_mode' in flags and not flags['debug_mode']:
            adjustment += 0.05
        
        # Additional computation with decoy variables
        temp_bias = total_chars % 10  # uses distractor variable
        final_value = int(base_score * adjustment + temp_bias)
        
        # Dead branch with misleading comment
        # NOTE: This would adjust for legacy mode, but it's obsolete
        if False:  # never executed
            final_value -= 50

        return final_value

    # Another red herring: fake optimization pass
    optimized = list(itertools.filterfalse(lambda x: x < 0.2, timing_log))
    smoothed = []
    for i in range(len(optimized)):
        window = optimized[max(0, i-1):i+2]
        smoothed.append(sum(window) / len(window))

    # Critical execution point buried in distractions
    final_diagnostic = aggregate_metrics(timing_log, system_flags)

    # Superfluous post-processing (not affecting answer)
    report_summary = defaultdict(int)
    for event in event_sequence:
        report_summary[event] += 1

    # Output the required result
    print(f"Result: {final_diagnostic}")
    return final_diagnostic

# Execute and capture result
collect_diagnostics()