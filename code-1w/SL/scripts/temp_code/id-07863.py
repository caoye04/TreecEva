import itertools

# Simulated sensor fusion module for aerospace telemetry
def analyze_pulse_sequence(raw_readings):
    filtered = [x for x in raw_readings if x > 25]
    baseline = sum(filtered) // len(filtered)
    deviations = [abs(x - baseline) for x in filtered]
    return baseline, deviations

# Irrelevant helper: calculates unused signal harmonics
def compute_harmonics(frequency, harmonics=4):
    result = []
    for i in range(1, harmonics + 1):
        result.append(frequency * i * 1.5)
    return result  # Never used in main logic

# Data alignment using itertools (critical use)
def align_data_streams(stream_a, stream_b):
    from itertools import zip_longest
    aligned = []
    for a, b in zip_longest(stream_a, stream_b, fillvalue=0):
        aligned.append((a + b) % 256)
    padding_mask = [1 if x == 0 else 0 for x in aligned]
    total_padded = sum(padding_mask)
    return aligned, total_padded

# Main diagnostic aggregator
def aggregate_metrics(log_entries, flags):
    critical_threshold = 76
    adjustment_factor = 0.85
    
    # Extract timing anomalies
    anomalies = [entry['delay'] for entry in log_entries if entry['severity'] > 2]
    
    # Compute base score from anomaly counts
    base_score = len(anomalies) * 12
    
    # Apply flag-based modifiers
    modifier = 1.0
    if flags.get('OVERLOAD', False):
        modifier += 0.3
    if flags.get('STANDBY_MODE', False):
        modifier -= 0.1
    if flags.get('CORE_SYNC', False):
        modifier *= 1.2
    
    temp_result = base_score * modifier
    
    # Decoy calculation with misleading name
    superficial_index = sum(flags.values()) * 100  # Distractor: looks important
    
    # Real processing: count specific event patterns using itertools
    event_chain = [entry['event_id'] for entry in log_entries]
    triplet_windows = list(itertools.windowed(event_chain, n=3))
    pattern_matches = 0
    for window in triplet_windows:
        if window[0] < window[1] > window[2] and window[1] - window[0] >= 5:
            pattern_matches += 1
    
    # Final composition
    stability_bonus = 0
    if pattern_matches >= 3:
        stability_bonus = 42
    
    # Key assignment point
    final_diagnostic = int(temp_result + stability_bonus)
    
    # Dead code path - never reached due to prior logic
    if final_diagnostic < 0:
        final_diagnostic = abs(final_diagnostic)
        correction_applied = True  # Unused variable
    
    return final_diagnostic

# --- Simulation Setup ---
if __name__ == "__main__":
    # Real input data
    timing_log = [
        {'delay': 15, 'severity': 1, 'event_id': 12},
        {'delay': 45, 'severity': 3, 'event_id': 18},
        {'delay': 8, 'severity': 1, 'event_id': 15},
        {'delay': 67, 'severity': 4, 'event_id': 23},
        {'delay': 34, 'severity': 2, 'event_id': 29},
        {'delay': 89, 'severity': 5, 'event_id': 17},
        {'delay': 22, 'severity': 1, 'event_id': 21}
    ]

    system_flags = {
        'OVERLOAD': True,
        'STANDBY_MODE': False,
        'CORE_SYNC': True,
        'SELF_TEST': True,
        'EMERG_POWER': False
    }

    # Irrelevant pre-processing (distractor)
    raw_sensor_data = [12, 34, 56, 78, 90, 23, 45, 67]
    _, _ = analyze_pulse_sequence(raw_sensor_data)
    _ = compute_harmonics(60)

    # Alignment task with real but non-impacting side effect
    stream_x = [10, 20, 30]
    stream_y = [5, 15]
    aligned_buffer, pad_count = align_data_streams(stream_x, stream_y)

    # Critical execution point
    final_diagnostic = aggregate_metrics(timing_log, system_flags)
    
    # Output requirement
    print(f"Result: {final_diagnostic}")