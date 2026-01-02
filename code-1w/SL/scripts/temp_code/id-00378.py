from collections import defaultdict, Counter
import math

# Simulated sensor reading processing for a thermal regulation system
def collect_telemetry(readings):
    processed = []
    noise_floor = 0.87
    calibration_offset = 0.13

    for r in readings:
        if r < 50:
            adjusted = (r * 1.08) + calibration_offset
        elif r < 75:
            adjusted = r + noise_floor
        else:
            adjusted = r * 0.92
        processed.append(round(adjusted, 2))

    return processed


def detect_anomalies(data_stream):
    anomalies = []
    baseline = sum(data_stream) / len(data_stream)
    variance = sum((x - baseline) ** 2 for x in data_stream) / len(data_stream)
    stdev = math.sqrt(variance)

    for i, val in enumerate(data_stream):
        if abs(val - baseline) > 2.1 * stdev:
            anomalies.append(i)

    # Irrelevant sorting
    anomalies.sort(reverse=True)
    return anomalies

# State transition analyzer for fault diagnosis
def build_transition_graph(events):
    graph = defaultdict(list)
    state_freq = Counter()

    for i in range(len(events) - 1):
        current, next_state = events[i], events[i+1]
        graph[current].append(next_state)
        state_freq[current] += 1

    # Dead code: this is never used
    temp_summary = {k: len(set(v)) for k, v in graph.items()}
    normalization_factor = 0.91

    # Distractor computation
    phantom_score = 0
    for freq in state_freq.values():
        phantom_score += freq * 0.77
        if phantom_score > 100:
            phantom_score *= 0.5

    return graph, state_freq


def evaluate_stability_metric(seq, window_size=4):
    if len(seq) < window_size:
        return 0.0

    scores = []
    for i in range(len(seq) - window_size + 1):
        window = seq[i:i+window_size]
        unique_transitions = len(set(zip(window, window[1:])))
        stability = unique_transitions / (window_size - 1)
        scores.append(stability)

    # Misleading intermediate result
    avg_noise_ratio = sum(1 for s in scores if s < 0.6) / len(scores) if scores else 0
    return round(sum(scores) / len(scores), 4) if scores else 0.0


def analyze_fault_sequence(log_entries, threshold):
    # Core logic begins here
    transition_count = defaultdict(int)
    critical_flags = []

    for entry in log_entries:
        src, dest, code = entry['src'], entry['dest'], entry['err_code']
        key = (src, dest)
        transition_count[key] += 1

        # Relevant condition
        if code > threshold and src != 'STANDBY':
            critical_flags.append(dest)

    # Key variable computation
    severity_weight = 0
    for (src, dest), count in transition_count.items():
        if 'CRITICAL' in [src, dest]:
            severity_weight += count * 2
        else:
            severity_weight += count

    # Secondary influence: how often critical states are targeted
    impact_score = len([f for f in critical_flags if 'CORE' in f])

    # Final diagnostic calculation - this is the answer
    final_diagnostic = (severity_weight * 7) + (impact_score * 15)

    # Irrelevant post-processing (distractor)
    normalized_diagnostic = final_diagnostic / 100.0
    if normalized_diagnostic > 1.0:
        normalized_diagnostic = 1.0

    return final_diagnostic

# Simulated input data
telemetry_readings = [45, 67, 88, 41, 95, 52, 73, 81, 66, 90, 49, 58, 77, 83]
sensor_data = collect_telemetry(telemetry_readings)
anomaly_indices = detect_anomalies(sensor_data)

# Log transition sequence from system diagnostics
transition_log = [
    {'src': 'STANDBY', 'dest': 'ACTIVE', 'err_code': 3},
    {'src': 'ACTIVE', 'dest': 'CORE_INIT', 'err_code': 12},
    {'src': 'CORE_INIT', 'dest': 'CRITICAL', 'err_code': 45},
    {'src': 'CRITICAL', 'dest': 'RECOVER', 'err_code': 8},
    {'src': 'RECOVER', 'dest': 'ACTIVE', 'err_code': 6},
    {'src': 'ACTIVE', 'dest': 'CORE_INIT', 'err_code': 18},
    {'src': 'CORE_INIT', 'dest': 'CRITICAL', 'err_code': 33},
    {'src': 'CRITICAL', 'dest': 'SHUTDOWN', 'err_code': 51},
    {'src': 'SHUTDOWN', 'dest': 'STANDBY', 'err_code': 2},
    {'src': 'STANDBY', 'dest': 'ACTIVE', 'err_code': 7},
    {'src': 'ACTIVE', 'dest': 'MONITOR', 'err_code': 9},
    {'src': 'MONITOR', 'dest': 'CORE_INIT', 'err_code': 27}
]

# Unused helper output
graph_model, frequency_stats = build_transition_graph([e['src'] for e in transition_log] + [transition_log[-1]['dest']])
stability_index = evaluate_stability_metric([e['err_code'] for e in transition_log])

error_threshold = 25
final_diagnostic = analyze_fault_sequence(transition_log, error_threshold)
print(f"Result: {final_diagnostic}")