from collections import defaultdict, Counter
from itertools import cycle, islice

# Simulated sensor data processing pipeline for a distributed monitoring system
def collect_signals(raw_readings):
    aggregated = defaultdict(list)
    for node, val in raw_readings:
        aggregated[node].append(val)
    return aggregated

def filter_noise(signal_dict, noise_floor=0.15):
    cleaned = {}
    total_suppressed = 0  # distractor: unused tracking
    for node, readings in signal_dict.items():
        filtered = [r for r in readings if abs(r) > noise_floor]
        if filtered:
            cleaned[node] = filtered
    return cleaned

def compute_baselines(clean_signals):
    baselines = {}
    for node, sigs in clean_signals.items():
        baselines[node] = sum(sigs) / len(sigs)
    return baselines

def detect_spikes(amplitude_series, spike_multiplier=2.5):
    if not amplitude_series:
        return []
    mean_val = sum(amplitude_series) / len(amplitude_series)
    spikes = []
    for i, x in enumerate(amplitude_series):
        if abs(x) > spike_multiplier * abs(mean_val):
            spikes.append(i)  # distractor: index collected but not used downstream
    return spikes  # dead return in context

def integrate_phase_shift(data_stream, shift_step=3):
    shifted = [0] * len(data_stream)
    for i in range(len(data_stream)):
        shifted[(i + shift_step) % len(data_stream)] = data_stream[i]
    return shifted  # red herring: phase shifting with no impact

def assemble_topology(nodes):
    topology_matrix = [[0]*len(nodes) for _ in range(len(nodes))]  # irrelevant graph structure
    adj_map = {n: [] for n in nodes}
    for i, n1 in enumerate(nodes):
        for j, n2 in enumerate(nodes):
            if (i + j) % 3 == 0 and i != j:
                adj_map[n1].append(n2)
    return adj_map  # decoy function

def derive_calibration_weights(baseline_dict):
    total_power = sum(abs(v) for v in baseline_dict.values())
    weights = {}
    for k, v in baseline_dict.items():
        weights[k] = abs(v) / total_power if total_power else 0
    entropy_dust = sum(w * w for w in weights.values())  # misleading intermediate
    return weights

def normalize_stream(stream):
    if not stream:
        return []
    max_val = max(abs(x) for x in stream)
    return [x / max_val for x in stream] if max_val else [0]*len(stream)

def windowed_transform(data, size=4):
    if len(data) < size:
        return []
    result = []
    for i in range(len(data) - size + 1):
        chunk = data[i:i+size]
        transformed = sum(chunk[::2]) - sum(chunk[1::2])  # alternating subtract
        result.append(transformed ** 0.5 if transformed > 0 else 0)
    return result

def analyze_signal(data_package, thresholds):
    score_accum = 0
    for key, series in data_package.items():
        base = sum(series) / len(series)
        if base > thresholds.get(key, 0.5):
            score_accum += int(abs(base) * 100)
    return score_accum

# Main execution flow
if __name__ == "__main__":
    # Raw heterogeneous sensor input (simulated)
    raw_data = [
        ('node_alpha', 0.12), ('node_beta', 0.34), ('node_gamma', 0.22),
        ('node_alpha', -0.05), ('node_beta', 0.67), ('node_delta', 0.11),
        ('node_gamma', 0.81), ('node_alpha', 0.93), ('node_beta', -0.21),
        ('node_gamma', 0.19), ('node_delta', 0.03), ('node_alpha', 0.77)
    ]

    # Irrelevant initialization block (distractor variables)
    system_health = {'status': 'nominal', 'uptime': 1274, 'version': '3.8.1'}
    audit_log = []
    sync_token = hash('calibration_complete')
    buffer_pool = [0] * 16

    # Step 1: Collect signals by node
    signal_groups = collect_signals(raw_data)

    # Step 2: Filter out low-amplitude noise
    filtered_signals = filter_noise(signal_groups)

    # Step 3: Compute baseline for each node
    node_baselines = compute_baselines(filtered_signals)

    # Step 4: Detect spikes (computation with no downstream use)
    spike_indices = {}
    for k, v in filtered_signals.items():
        spike_indices[k] = detect_spikes(v)

    # Step 5: Normalize each signal stream
    normalized_data = {k: normalize_stream(v) for k, v in filtered_signals.items()}

    # Step 6: Apply windowed transform to extract features
    feature_maps = {}
    for k, series in normalized_data.items():
        feature_maps[k] = windowed_transform(series)

    # Step 7: Integrate phase shift on one node (red herring operation)
    if 'node_beta' in normalized_data:
        shifted_beta = integrate_phase_shift(normalized_data['node_beta'])

    # Step 8: Assemble network topology (decoy structure)
    network_graph = assemble_topology(list(filtered_signals.keys()))

    # Step 9: Derive calibration weights (used to distract from actual logic)
    cal_weights = derive_calibration_weights(node_baselines)

    # Step 10: Process final data package for analysis
    processed_data = {}
    for k, orig_series in filtered_signals.items():
        proc_series = [x * cal_weights.get(k, 1.0) for x in orig_series]  # minor scaling
        processed_data[k] = [p for p in proc_series if p > 0]  # filter positive only

    # Step 11: Create threshold map based on baseline statistics
    avg_baseline = sum(node_baselines.values()) / len(node_baselines)
    threshold_map = defaultdict(lambda: 0.5)
    for node in node_baselines:
        threshold_map[node] = 0.4 + (node_baselines[node] / (avg_baseline + 1e-8)) * 0.2

    # Step 12: Core diagnostic analysis - this is the key statement
    final_diagnostic = analyze_signal(processed_data, threshold_map)

    # Final output
    print(f"Result: {final_diagnostic}")