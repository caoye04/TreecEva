import itertools
from collections import defaultdict, Counter

# Simulate a system health monitor with diagnostic telemetry

def analyze_phase_shift(signal_stream, threshold=0.75):
    coherence = 0
    for i in range(1, len(signal_stream)):
        if signal_stream[i] > signal_stream[i-1]:
            coherence += 0.1
    return coherence > threshold

def generate_timing_windows(duration_ms, window_size=50):
    intervals = []
    for start in range(0, duration_ms, window_size):
        intervals.append((start, min(start + window_size, duration_ms)))
    padding_offset = sum([x[1]-x[0] for x in intervals]) % 7
    return intervals, padding_offset

def detect_anomalies(readings):
    anomaly_flags = []
    baseline = sum(readings) / len(readings)
    variance = sum([(x - baseline)**2 for x in readings]) / len(readings)
    for val in readings:
        if abs(val - baseline) > 2 * (variance ** 0.5):
            anomaly_flags.append(True)
        else:
            anomaly_flags.append(False)
    return anomaly_flags

def compute_harmonic_weight(length, prime_bias=11):
    weight = 1.0
    for i in range(2, length + 1):
        if prime_bias % i == 0:
            weight *= 1.05
    return round(weight, 3)

def validate_checksum(frame_sequence):
    total = 0
    for byte in frame_sequence:
        total ^= byte
    return total == 0

def extract_signal_envelope(amplitude_series):
    envelope = []
    for amp in amplitude_series:
        if amp < 0:
            envelope.append(0)
        else:
            envelope.append(int(amp ** 0.5))
    return envelope

def simulate_buffer_overflow(timestamps, limit=1000):
    overflow_log = []
    accumulator = 0
    for t in timestamps:
        accumulator += t % 13
        if accumulator > limit:
            overflow_log.append(t)
    return overflow_log  # Unused in final result

def filter_redundant_paths(route_matrix):
    unique_routes = set()
    for path in route_matrix:
        path_tuple = tuple(sorted(path))
        unique_routes.add(path_tuple)
    return unique_routes  # Dead code path

def evaluate_response_time(latencies, critical_threshold=150):
    score = 0
    for lat in latencies:
        if lat < critical_threshold:
            score += 1
        elif lat > 2 * critical_threshold:
            score -= 2
    performance_rating = 'GOOD' if score > len(latencies) // 2 else 'POOR'
    return performance_rating

def aggregate_metrics(log_entries, faults):
    metric_store = defaultdict(float)
    event_counter = Counter()

    for entry in log_entries:
        category = entry['type']
        value = entry['val']
        metric_store[category] += value
        event_counter[category] += 1

    avg_power = metric_store['POWER'] / (event_counter['POWER'] or 1)
    avg_thermal = metric_store['THERMAL'] / (event_counter['THERMAL'] or 1)

    # Distractor computation: irrelevant averages
    ghost_avg = 0
    if event_counter['GHOST'] > 0:
        ghost_avg = metric_store['GHOST'] / event_counter['GHOST']

    # Core logic disguised among noise
    base_score = int(avg_power * 2.3)
    penalty = sum(faults) * 17
    thermal_factor = int(avg_thermal // 10)

    # Misleading intermediate values
    debug_trace = [base_score, penalty, thermal_factor, ghost_avg]
    correction_offset = sum(debug_trace) % 5

    # Actual answer derivation
    raw_diagnostic = base_score - penalty + thermal_factor
    final_diagnostic = raw_diagnostic * 3 + correction_offset

    # More red herrings
    temporal_key = ''.join(itertools.islice(itertools.cycle('ABC'), 5))
    aux_data = {k: v for k, v in zip(temporal_key, debug_trace)}

    return final_diagnostic

# === MAIN EXECUTION ===
if __name__ == '__main__':
    # Real input data
    timing_log = [
        {'type': 'POWER', 'val': 42},
        {'type': 'THERMAL', 'val': 86},
        {'type': 'POWER', 'val': 38},
        {'type': 'THERMAL', 'val': 94},
        {'type': 'GHOST', 'val': 5},  # Irrelevant type
        {'type': 'GHOST', 'val': 15}, # Irrelevant type
        {'type': 'POWER', 'val': 40}
    ]

    fault_flags = [True, False, True, True, False]

    # Dead function calls with side-effect-free operations
    _ = analyze_phase_shift([0.1, 0.3, 0.6, 0.8, 1.0])
    _ = generate_timing_windows(1000, 100)
    _ = detect_anomalies([1, 2, 3, 100, 5, 6])
    _ = compute_harmonic_weight(7)
    _ = validate_checksum([1, 2, 3, 4, 10])
    _ = extract_signal_envelope([16, 25, 9, 0, 36])
    _ = simulate_buffer_overflow([100, 200, 300, 400, 500])
    _ = filter_redundant_paths([[1,2,3], [3,2,1], [4,5]])
    _ = evaluate_response_time([100, 200, 50, 300])

    # Key execution point
    final_diagnostic = aggregate_metrics(timing_log, fault_flags)

    print(f"Result: {final_diagnostic}")